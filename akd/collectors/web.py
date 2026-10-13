from __future__ import annotations

import logging
import time
from collections.abc import Callable

import feedparser
import httpx

from akd.collectors.base import clip, entry_datetime, get_with_retry, strip_html
from akd.config import Config
from akd.dedupe import item_id
from akd.models import Item

log = logging.getLogger("akd.collectors.web")


class WebCollector:
    """Configured RSS/Atom feeds (vendor blogs, aggregators)."""

    name = "web"

    def __init__(self, cfg: Config, client: httpx.Client, sleep: Callable[[float], None] = time.sleep) -> None:
        self.cfg = cfg
        self.client = client
        self.sleep = sleep

    def collect(self) -> list[Item]:
        items: list[Item] = []
        for feed_url in self.cfg.feeds:
            try:
                parsed = feedparser.parse(get_with_retry(self.client, feed_url, self.sleep).content)
            except Exception:
                log.exception("feed failed: %s", feed_url)
                continue
            for entry in parsed.entries:
                link = entry.get("link")
                published = entry_datetime(entry)
                if not link or published is None:
                    continue
                items.append(
                    Item(
                        id=item_id(link),
                        source="web",
                        title=strip_html(entry.get("title", "")),
                        url=link,
                        text=clip(strip_html(entry.get("summary", ""))),
                        published_at=published,
                    )
                )
        return items
