from __future__ import annotations

import logging
import time
from collections.abc import Callable
from datetime import datetime, timezone

import feedparser
import httpx

from akd.collectors.base import clip, get, strip_html, struct_to_dt
from akd.config import Config
from akd.dedupe import item_id
from akd.models import Item

log = logging.getLogger("akd.collectors.reddit")

LIMIT = 50
DEFAULT_RETRY_WAIT = 10.0
MAX_RETRY_WAIT = 30.0


class RedditCollector:
    """Daily top posts per subreddit via the Atom feed.

    Flagged simplification: the anonymous JSON API returns 403 for unauthenticated
    clients, so this uses the Atom feed, which carries no upvote counts. Ranking
    therefore relies on Jev's judgment of the post text alone. All subreddits are fetched
    as one multireddit (`r/a+b+c`) because Reddit rate-limits repeat requests.
    """

    name = "reddit"

    def __init__(self, cfg: Config, client: httpx.Client, sleep: Callable[[float], None] = time.sleep) -> None:
        self.cfg = cfg
        self.client = client
        self.sleep = sleep

    def _fetch(self, url: str) -> bytes:
        """Reddit 429s back-to-back requests: honor Retry-After once, then give up."""
        try:
            return get(self.client, url).content
        except httpx.HTTPStatusError as e:
            if e.response.status_code != 429:
                raise
            self.sleep(min(float(e.response.headers.get("Retry-After", DEFAULT_RETRY_WAIT)), MAX_RETRY_WAIT))
            return get(self.client, url).content

    def collect(self) -> list[Item]:
        if not self.cfg.subreddits:
            return []
        now = datetime.now(timezone.utc)
        # One multireddit request: Reddit 429s a second request from the same client.
        url = f"https://www.reddit.com/r/{'+'.join(self.cfg.subreddits)}/top/.rss?t=day&limit={LIMIT}"
        try:
            parsed = feedparser.parse(self._fetch(url))
        except Exception:
            log.exception("reddit feed failed")
            return []
        return [
            Item(
                id=item_id(entry.link),
                source="reddit",
                title=strip_html(entry.title),
                url=entry.link,
                text=clip(strip_html(entry.get("summary", ""))),
                published_at=struct_to_dt(entry.get("published_parsed") or entry.get("updated_parsed"), now),
            )
            for entry in parsed.entries
        ]
