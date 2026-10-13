from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone

import httpx

from akd.collectors.base import USER_AGENT, clip, strip_html
from akd.config import Config
from akd.dedupe import item_id
from akd.models import Item

log = logging.getLogger("akd.collectors.x")

ACTOR = "apidojo~tweet-scraper"
ENDPOINT = f"https://api.apify.com/v2/acts/{ACTOR}/run-sync-get-dataset-items"
TWITTER_TIME = "%a %b %d %H:%M:%S %z %Y"  # e.g. "Mon Oct 12 10:00:00 +0000 2026"


def _created_at(raw) -> datetime | None:
    if not isinstance(raw, str):
        return None
    for parse in (lambda s: datetime.strptime(s, TWITTER_TIME), datetime.fromisoformat):
        try:
            return parse(raw).astimezone(timezone.utc)
        except ValueError:
            continue
    return None


class XCollector:
    """Posts from configured X accounts and searches, fetched through an Apify actor (paid, token required).

    Off unless an Apify token and at least one handle or search term are configured.
    """

    name = "x"

    def __init__(self, cfg: Config, client: httpx.Client, token: str | None, now: datetime | None = None) -> None:
        self.cfg = cfg
        self.client = client
        self.token = token
        self.now = now or datetime.now(timezone.utc)

    def _payload(self) -> dict:
        since = (self.now - timedelta(days=self.cfg.max_age_days)).date().isoformat()
        payload: dict = {
            "maxItems": self.cfg.x_max_items,
            "minimumFavorites": self.cfg.x_min_likes,
            "sort": "Latest",
        }
        if self.cfg.x_handles:
            payload["twitterHandles"] = list(self.cfg.x_handles)
        if self.cfg.x_searches:
            payload["searchTerms"] = [f"{term} since:{since}" for term in self.cfg.x_searches]
        return payload

    def collect(self) -> list[Item]:
        if not self.token or not (self.cfg.x_handles or self.cfg.x_searches):
            return []
        try:
            resp = self.client.post(
                ENDPOINT,
                json=self._payload(),
                headers={"Authorization": f"Bearer {self.token}", "User-Agent": USER_AGENT},
                timeout=240,
            )
            resp.raise_for_status()
            rows = resp.json()
        except (httpx.HTTPError, ValueError) as exc:
            log.warning("X fetch failed: %s", exc)  # the exception text never contains the token (it is in a header)
            return []
        items: list[Item] = []
        for row in rows if isinstance(rows, list) else []:
            if row.get("type") != "tweet" or row.get("isRetweet") or row.get("isReply"):
                continue
            url, created = row.get("url"), _created_at(row.get("createdAt"))
            if not url or created is None:
                continue
            text = strip_html(row.get("text", ""))
            author = (row.get("author") or {}).get("userName", "unknown")
            items.append(
                Item(
                    id=item_id(url),
                    source="x",
                    title=clip(text, 100),
                    url=url,
                    text=clip(f"Post by @{author} ({row.get('likeCount', 0)} likes): {text}"),
                    published_at=created,
                )
            )
        return items
