from __future__ import annotations

import logging
import time
from collections.abc import Callable

import feedparser
import httpx

from akd.collectors.base import clip, entry_datetime, get, strip_html
from akd.config import Config
from akd.dedupe import item_id
from akd.models import Item

log = logging.getLogger("akd.collectors.youtube")

FEED_URL = "https://www.youtube.com/feeds/videos.xml?channel_id={id}"
# YouTube's feed host answers 404 for hours at a time, then recovers; a short back-off catches the brief blips.
BACKOFF_SECONDS = (2, 6)


class YouTubeCollector:
    """Latest uploads from the configured channels, via each channel's public Atom feed (no API key)."""

    name = "youtube"

    def __init__(self, cfg: Config, client: httpx.Client, sleep: Callable[[float], None] = time.sleep) -> None:
        self.cfg = cfg
        self.client = client
        self.sleep = sleep

    def _fetch(self, url: str) -> bytes:
        for attempt in range(len(BACKOFF_SECONDS) + 1):
            try:
                return get(self.client, url).content
            except httpx.HTTPError:
                if attempt == len(BACKOFF_SECONDS):
                    raise
                self.sleep(BACKOFF_SECONDS[attempt])
        raise AssertionError("unreachable")

    def collect(self) -> list[Item]:
        items: list[Item] = []
        for channel in self.cfg.youtube_channels:
            try:
                parsed = feedparser.parse(self._fetch(FEED_URL.format(id=channel["id"])))
            except httpx.HTTPError as exc:
                log.warning("channel skipped: %s (%s): %s", channel.get("name"), channel["id"], exc)
                continue
            for entry in parsed.entries:
                link = entry.get("link")
                published = entry_datetime(entry)
                if not link or published is None:
                    continue
                description = clip(strip_html(entry.get("summary", "")))
                items.append(
                    Item(
                        id=item_id(link),
                        source="youtube",
                        title=strip_html(entry.get("title", "")),
                        url=link,
                        text=f"Video on the YouTube channel {channel.get('name', channel['id'])}. {description}".strip(),
                        published_at=published,
                    )
                )
        return items
