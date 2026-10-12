from __future__ import annotations

import logging
from datetime import datetime, timezone

import feedparser
import httpx

from akd.collectors.base import clip, get, strip_html, struct_to_dt
from akd.config import Config
from akd.dedupe import item_id
from akd.models import Item

log = logging.getLogger("akd.collectors.reddit")


class RedditCollector:
    """Daily top posts per subreddit via the Atom feed.

    Flagged simplification: the anonymous JSON API returns 403 for unauthenticated
    clients, so this uses the Atom feed, which carries no upvote counts. Ranking
    therefore relies on Jev's judgment of the post text alone.
    """

    name = "reddit"

    def __init__(self, cfg: Config, client: httpx.Client) -> None:
        self.cfg = cfg
        self.client = client

    def collect(self) -> list[Item]:
        items: list[Item] = []
        now = datetime.now(timezone.utc)
        for sub in self.cfg.subreddits:
            url = f"https://www.reddit.com/r/{sub}/top/.rss?t=day&limit=15"
            try:
                parsed = feedparser.parse(get(self.client, url).content)
            except Exception:
                log.exception("reddit feed failed for r/%s", sub)
                continue
            for entry in parsed.entries:
                items.append(
                    Item(
                        id=item_id(entry.link),
                        source="reddit",
                        title=strip_html(entry.title),
                        url=entry.link,
                        text=clip(strip_html(entry.get("summary", ""))),
                        published_at=struct_to_dt(entry.get("published_parsed") or entry.get("updated_parsed"), now),
                    )
                )
        return items
