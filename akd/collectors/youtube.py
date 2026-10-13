from __future__ import annotations

import logging
import time
from collections import Counter
from collections.abc import Callable
from datetime import datetime, timezone

import feedparser
import httpx

from akd.collectors.base import apify_items, clip, entry_datetime, get_with_retry, strip_html
from akd.config import Config
from akd.dedupe import item_id
from akd.models import Item

log = logging.getLogger("akd.collectors.youtube")

FEED_URL = "https://www.youtube.com/feeds/videos.xml?channel_id={id}"
# YouTube's feed host answers 404 for hours at a time, then recovers; a short back-off catches the brief blips.
BACKOFF_SECONDS = (2, 6)
YOUTUBE_RETRY_STATUSES = frozenset({404, 429, 500, 502, 503, 504})

APIFY_ACTOR = "apidojo~youtube-scraper"
APIFY_MIN_PER_CHANNEL = 10  # the actor fetches at least 10 videos per start URL
DAY_FORMATS = ("%b %d, %Y", "%B %d, %Y")  # the actor reports e.g. "Jan 30, 2024": a day, with no time


def _day(raw) -> datetime | None:
    if not isinstance(raw, str):
        return None
    for fmt in DAY_FORMATS:
        try:
            return datetime.strptime(raw.strip(), fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(raw).astimezone(timezone.utc)
    except ValueError:
        return None


class YouTubeCollector:
    """Latest uploads from the configured channels.

    Each channel's public Atom feed is tried first (free, no key). YouTube's feed host is often down, so channels
    whose feed fails are fetched together through an Apify actor when a token is available (about $0.50 per
    1,000 videos), and skipped otherwise."""

    name = "youtube"

    def __init__(
        self,
        cfg: Config,
        client: httpx.Client,
        sleep: Callable[[float], None] = time.sleep,
        token: str | None = None,
    ) -> None:
        self.cfg = cfg
        self.client = client
        self.sleep = sleep
        self.token = token

    def _fetch(self, url: str) -> bytes:
        return get_with_retry(self.client, url, self.sleep, BACKOFF_SECONDS, YOUTUBE_RETRY_STATUSES).content

    def collect(self) -> list[Item]:
        items: list[Item] = []
        failed: list[dict] = []
        for channel in self.cfg.youtube_channels:
            try:
                parsed = feedparser.parse(self._fetch(FEED_URL.format(id=channel["id"])))
            except httpx.HTTPError as exc:
                log.warning("feed failed: %s (%s): %s", channel.get("name"), channel["id"], exc)
                failed.append(channel)
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
        return items + self._collect_via_apify(failed)

    def _collect_via_apify(self, channels: list[dict]) -> list[Item]:
        if not channels:
            return []
        if not self.token:
            log.warning("%d channel(s) skipped: feed down and no APIFY_TOKEN for the fallback", len(channels))
            return []
        names = {c["id"]: c.get("name", c["id"]) for c in channels}
        payload = {
            "startUrls": [f"https://www.youtube.com/channel/{c['id']}" for c in channels],
            "includeShorts": False,
            "maxItems": APIFY_MIN_PER_CHANNEL * len(channels),
        }
        try:
            rows = apify_items(self.client, APIFY_ACTOR, self.token, payload)
        except (httpx.HTTPError, ValueError) as exc:
            log.warning("YouTube Apify fallback failed: %s", exc)  # the token is in a header, not in this text
            return []
        per_channel = Counter(
            names.get((r.get("channel") or {}).get("id")) or (r.get("channel") or {}).get("name") or "unknown"
            for r in rows
        )
        log.info("YouTube Apify returned %d rows: %s", len(rows), dict(per_channel))
        items: list[Item] = []
        undated = 0
        for row in rows:
            url = row.get("url")
            if not url or row.get("type") not in (None, "video"):
                continue
            published = _day(row.get("publishDate") or row.get("uploadDate"))
            if published is None:
                undated += 1
                continue
            channel = row.get("channel") or {}
            name = names.get(channel.get("id")) or channel.get("name") or "unknown"
            description = clip(strip_html(row.get("description", "")))
            items.append(
                Item(
                    id=item_id(url),
                    source="youtube",
                    title=strip_html(row.get("title", "")),
                    url=url,
                    text=f"Video on the YouTube channel {name}. {description}".strip(),
                    published_at=published,
                )
            )
        if undated:
            log.warning("YouTube Apify fallback: %d video(s) skipped for an unreadable publish date", undated)
        return items
