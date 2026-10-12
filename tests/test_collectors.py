from datetime import datetime, timezone
from pathlib import Path

import httpx

from akd.collectors.base import Collector, collect_all, strip_html
from akd.collectors.github import GitHubCollector
from akd.collectors.reddit import RedditCollector
from akd.collectors.web import WebCollector
from akd.config import load_config
from akd.models import Item

ROOT = Path(__file__).resolve().parent.parent
FIX = Path(__file__).resolve().parent / "fixtures"
NOW = datetime(2026, 10, 12, 14, 0, tzinfo=timezone.utc)


def cfg():
    return load_config(ROOT / "config.yaml")


def client_for(routes: dict[str, bytes]) -> httpx.Client:
    """Mock transport: first route whose key is a substring of the URL wins."""

    def handler(request: httpx.Request) -> httpx.Response:
        for key, body in routes.items():
            if key in str(request.url):
                return httpx.Response(200, content=body)
        return httpx.Response(404)

    return httpx.Client(transport=httpx.MockTransport(handler))


def test_github_maps_search_and_releases():
    client = client_for(
        {
            "search/repositories": (FIX / "github_search.json").read_bytes(),
            "/releases": (FIX / "github_releases.json").read_bytes(),
        }
    )
    items = GitHubCollector(cfg(), client, now=NOW).collect()
    urls = {i.url for i in items}
    assert "https://github.com/affaan-m/ECC" in urls
    assert "https://github.com/anthropics/claude-code/releases/tag/v2.1.296" in urls
    assert all(i.source == "github" for i in items)
    release = next(i for i in items if i.url.endswith("v2.1.296"))
    assert release.title.startswith("anthropics/claude-code")
    assert "autoCompactWindow" in release.text


def test_reddit_maps_atom_feed():
    client = client_for({"reddit.com/r/": (FIX / "reddit.xml").read_bytes()})
    items = RedditCollector(cfg(), client, sleep=lambda s: None).collect()
    assert items
    first = items[0]
    assert first.source == "reddit"
    assert first.title == "Opus 5.5 is INSANE at decompilation / ports"
    assert first.url.startswith("https://www.reddit.com/r/ClaudeAI/comments/")
    assert first.published_at.tzinfo is not None


def test_web_maps_rss_feed():
    client = client_for({"": (FIX / "web.xml").read_bytes()})
    items = WebCollector(cfg(), client).collect()
    assert items
    assert items[0].source == "web"
    assert items[0].title.startswith("I think I found a planet")


def test_html_in_text_is_stripped():
    assert strip_html('<p>hi <script>alert(1)</script><b>there</b></p>') == "hi there"
    assert strip_html("a &amp; b") == "a & b"


def test_collect_all_isolates_failures():
    class Boom:
        name = "boom"

        def collect(self) -> list[Item]:
            raise RuntimeError("down")

    class Ok:
        name = "ok"

        def collect(self) -> list[Item]:
            return [
                Item("1", "web", "t", "https://e.com", "x", NOW),
            ]

    items = collect_all([Boom(), Ok()])
    assert [i.id for i in items] == ["1"]


def test_collector_http_error_does_not_raise_through_collect_all():
    client = client_for({})  # every request 404s
    items = collect_all([RedditCollector(cfg(), client, sleep=lambda s: None), WebCollector(cfg(), client)])
    assert items == []


def test_reddit_retries_once_on_429_and_spaces_requests():
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] == 1:
            return httpx.Response(429, headers={"Retry-After": "7"})
        return httpx.Response(200, content=(FIX / "reddit.xml").read_bytes())

    sleeps = []
    c = cfg()
    client = httpx.Client(transport=httpx.MockTransport(handler))
    items = RedditCollector(c, client, sleep=sleeps.append).collect()
    assert items  # recovered after the 429
    assert 7 in sleeps  # honored Retry-After
    assert len([s for s in sleeps if s > 0]) >= len(c.subreddits)  # spaced between subs


def test_reddit_gives_up_after_one_retry():
    client = httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(429)))
    assert RedditCollector(cfg(), client, sleep=lambda s: None).collect() == []
