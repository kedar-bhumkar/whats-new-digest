from __future__ import annotations

import logging
import re
import time
from collections.abc import Callable
from html.parser import HTMLParser
from urllib.parse import urlsplit

import feedparser
import httpx

from akd.collectors.base import clip, entry_datetime, get_with_retry, strip_html
from akd.config import Config
from akd.dedupe import item_id
from akd.models import Item

log = logging.getLogger("akd.collectors.web")

MIN_FEED_TEXT = 200  # shorter feed text is a teaser ("PLUS: ..."), not the story, and scores as a bare headline
MAX_ARTICLE_FETCHES = 20  # article pages fetched per run, so a chatty feed cannot turn into a crawl


def _body(entry) -> str:
    """The richest text a feed entry offers: many feeds (Substack among them) put a short teaser in `summary`
    and the real article in `content`, and the scorer needs the article."""
    body = strip_html(entry.get("summary", ""))
    for block in entry.get("content") or []:
        full = strip_html(block.get("value", ""))
        if len(full) > len(body):
            body = full
    return body


class _ArticleExtractor(HTMLParser):
    """The page's og:description plus the text inside <article>, with script/style bodies skipped."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.description = ""
        self.parts: list[str] = []
        self._article = 0
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            attrs = dict(attrs)
            if attrs.get("property") == "og:description" and not self.description:
                self.description = attrs.get("content") or ""
        elif tag == "article":
            self._article += 1
        elif tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag == "article" and self._article:
            self._article -= 1
        elif tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._article and not self._skip:
            self.parts.append(data)


def _host(url: str) -> str:
    return (urlsplit(url).hostname or "").removeprefix("www.")


def _article_text(client: httpx.Client, url: str, sleep: Callable[[float], None]) -> str:
    """The article's own summary and body, or "" when the page cannot be fetched or has no usable text."""
    try:
        resp = get_with_retry(client, url, sleep)
    except httpx.HTTPError as exc:
        log.info("article fetch failed: %s (%s)", url, exc)
        return ""
    parser = _ArticleExtractor()
    parser.feed(resp.text)
    parser.close()
    body = re.sub(r"\s+", " ", "".join(parser.parts)).strip()
    return " ".join(part for part in (parser.description.strip(), body) if part)


class WebCollector:
    """Configured RSS/Atom feeds (vendor blogs, aggregators)."""

    name = "web"

    def __init__(self, cfg: Config, client: httpx.Client, sleep: Callable[[float], None] = time.sleep) -> None:
        self.cfg = cfg
        self.client = client
        self.sleep = sleep

    def collect(self) -> list[Item]:
        items: list[Item] = []
        fetches = 0
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
                text = _body(entry)
                # Teasers are replaced by the article itself, but only from the feed's own site: the aggregator
                # feeds (Hacker News) link anywhere, and fetching arbitrary pages is not this collector's job.
                if len(text) < MIN_FEED_TEXT and fetches < MAX_ARTICLE_FETCHES and _host(link) == _host(feed_url):
                    fetches += 1
                    text = _article_text(self.client, link, self.sleep) or text
                items.append(
                    Item(
                        id=item_id(link),
                        source="web",
                        title=strip_html(entry.get("title", "")),
                        url=link,
                        text=clip(text),
                        published_at=published,
                    )
                )
        return items
