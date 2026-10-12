from __future__ import annotations

import logging
from datetime import datetime, timezone

import feedparser
import httpx

from akd.collectors.base import clip, get, strip_html, struct_to_dt
from akd.config import Config
from akd.dedupe import item_id
from akd.models import Item

log = logging.getLogger("akd.collectors.web")


class WebCollector:
    """Configured RSS/Atom feeds (vendor blogs, aggregators)."""

    name = "web"

    def __init__(self, cfg: Config, client: httpx.Client) -> None:
        self.cfg = cfg
        self.client = client

    def collect(self) -> list[Item]:
        items: list[Item] = []
        now = datetime.now(timezone.utc)
        for feed_url in self.cfg.feeds:
            try:
                parsed = feedparser.parse(get(self.client, feed_url).content)
            except Exception:
                log.exception("feed failed: %s", feed_url)
                continue
            for entry in parsed.entries:
                link = entry.get("link")
                if not link:
                    continue
                items.append(
                    Item(
                        id=item_id(link),
                        source="web",
                        title=strip_html(entry.get("title", "")),
                        url=link,
                        text=clip(strip_html(entry.get("summary", ""))),
                        published_at=struct_to_dt(entry.get("published_parsed") or entry.get("updated_parsed"), now),
                    )
                )
        return items
