from __future__ import annotations

import html
import logging
import re
import time
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


def struct_to_dt(parsed: time.struct_time | None, fallback: datetime) -> datetime:
    if not parsed:
        return fallback
    return datetime(*parsed[:6], tzinfo=timezone.utc)


def get(client: httpx.Client, url: str, **kwargs) -> httpx.Response:
    headers = {"User-Agent": USER_AGENT, **kwargs.pop("headers", {})}
    resp = client.get(url, headers=headers, timeout=20, follow_redirects=True, **kwargs)
    resp.raise_for_status()
    return resp


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
