from __future__ import annotations

import html
import logging
import re
import time
from collections.abc import Callable
from datetime import datetime, timezone
from html.parser import HTMLParser
from typing import Protocol

import httpx

from akd.models import Item

log = logging.getLogger("akd.collectors")

USER_AGENT = "akd-whats-new/0.1 (personal digest)"
MAX_TEXT = 1500


class Collector(Protocol):
    name: str

    def collect(self) -> list[Item]: ...


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)


def strip_html(text: str) -> str:
    """Drop tags and script/style bodies, unescape entities, collapse whitespace."""
    parser = _TextExtractor()
    parser.feed(text or "")
    parser.close()
    return re.sub(r"\s+", " ", html.unescape("".join(parser.parts))).strip()


def clip(text: str, limit: int = MAX_TEXT) -> str:
    return text if len(text) <= limit else text[: limit - 1] + "…"


def entry_datetime(entry) -> datetime | None:
    """A feed entry's own date, or None. Undated entries must be skipped, not stamped "now":
    a fresh timestamp every day would let stale items bypass the freshness filter forever."""
    parsed: time.struct_time | None = entry.get("published_parsed") or entry.get("updated_parsed")
    return datetime(*parsed[:6], tzinfo=timezone.utc) if parsed else None


def get(client: httpx.Client, url: str, **kwargs) -> httpx.Response:
    headers = {"User-Agent": USER_AGENT, **kwargs.pop("headers", {})}
    resp = client.get(url, headers=headers, timeout=20, follow_redirects=True, **kwargs)
    resp.raise_for_status()
    return resp


def get_with_retry(
    client: httpx.Client,
    url: str,
    sleep: Callable[[float], None] = time.sleep,
    backoff: tuple[float, ...] = (2, 6),
    retry_statuses: frozenset[int] = frozenset({429, 500, 502, 503, 504}),
) -> httpx.Response:
    """GET with a short back-off on transient failures; anything else (and the last failure) raises."""
    for attempt in range(len(backoff) + 1):
        try:
            return get(client, url)
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code not in retry_statuses or attempt == len(backoff):
                raise
        except httpx.TransportError:
            if attempt == len(backoff):
                raise
        sleep(backoff[attempt])
    raise AssertionError("unreachable")


def apify_items(client: httpx.Client, actor: str, token: str, payload: dict) -> list:
    """Run an Apify actor synchronously and return its dataset rows. The token goes in a header, never the URL,
    so it cannot leak through logged request URLs or exception text. Raises httpx.HTTPError / ValueError."""
    resp = client.post(
        f"https://api.apify.com/v2/acts/{actor}/run-sync-get-dataset-items",
        json=payload,
        headers={"Authorization": f"Bearer {token}", "User-Agent": USER_AGENT},
        timeout=240,
    )
    resp.raise_for_status()
    rows = resp.json()
    return rows if isinstance(rows, list) else []


def collect_all(collectors: list[Collector]) -> list[Item]:
    """Run every collector; one failing never stops the others."""
    items: list[Item] = []
    for collector in collectors:
        try:
            got = collector.collect()
            log.info("collector %s returned %d items", collector.name, len(got))
            items.extend(got)
        except Exception:
            log.exception("collector %s failed; skipping", collector.name)
    return items
