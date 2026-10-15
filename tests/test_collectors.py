from datetime import datetime, timezone
from pathlib import Path

import httpx

from akd.collectors.base import Collector, collect_all, strip_html
from akd.collectors.github import GitHubCollector
from akd.collectors.reddit import RedditCollector
from akd.collectors.web import WebCollector
from akd.collectors.x import XCollector
from akd.collectors.youtube import YouTubeCollector
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


def test_reddit_retries_once_on_429():
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


def test_reddit_gives_up_after_one_retry():
    client = httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(429)))
    assert RedditCollector(cfg(), client, sleep=lambda s: None).collect() == []


def test_reddit_uses_a_single_multireddit_request():
    urls = []

    def handler(request: httpx.Request) -> httpx.Response:
        urls.append(str(request.url))
        return httpx.Response(200, content=(FIX / "reddit.xml").read_bytes())

    c = cfg()
    client = httpx.Client(transport=httpx.MockTransport(handler))
    RedditCollector(c, client, sleep=lambda s: None).collect()
    assert len(urls) == 1  # Reddit 429s a second request from the same client
    assert "r/" + "+".join(c.subreddits) + "/top/.rss" in urls[0]


UNDATED_RSS = b"""<?xml version="1.0"?><rss version="2.0"><channel><title>t</title>
<item><title>No date</title><link>https://e.com/nodate</link><description>x</description></item>
<item><title>Dated</title><link>https://e.com/dated</link><pubDate>Mon, 12 Oct 2026 10:00:00 +0000</pubDate></item>
</channel></rss>"""

UNDATED_ATOM = b"""<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom"><title>t</title>
<entry><title>No date</title><link href="https://www.reddit.com/r/x/comments/1/"/><id>1</id></entry>
<entry><title>Dated</title><link href="https://www.reddit.com/r/x/comments/2/"/><id>2</id><updated>2026-10-12T10:00:00+00:00</updated></entry>
</feed>"""


def test_web_skips_undated_entries():
    # An undated item can't be proven fresh; stamping it "now" would let stale items recirculate forever.
    items = WebCollector(cfg(), client_for({"": UNDATED_RSS})).collect()
    assert {i.title for i in items} == {"Dated"}


def test_reddit_skips_undated_entries():
    items = RedditCollector(cfg(), client_for({"reddit.com": UNDATED_ATOM}), sleep=lambda s: None).collect()
    assert {i.title for i in items} == {"Dated"}


def yt_cfg(*ids):
    from dataclasses import replace

    return replace(cfg(), youtube_channels=[{"id": i, "name": f"Chan {i}"} for i in ids])


def test_youtube_maps_channel_feed():
    client = client_for({"feeds/videos.xml?channel_id=UCa": (FIX / "youtube.xml").read_bytes()})
    items = YouTubeCollector(yt_cfg("UCa"), client, sleep=lambda s: None).collect()
    first = next(i for i in items if i.url.endswith("DdCEmlAydcw"))
    assert first.source == "youtube"
    assert first.title == "Inside Anthropic's molecular biology lab"
    assert first.url == "https://www.youtube.com/watch?v=DdCEmlAydcw"
    assert "molecular biology research group" in first.text
    assert "Chan UCa" in first.text  # the configured channel name is carried into the text
    assert first.published_at.tzinfo is not None


def test_youtube_disabled_when_no_channels_configured():
    called = []

    def handler(request: httpx.Request) -> httpx.Response:
        called.append(request)
        return httpx.Response(200)

    client = httpx.Client(transport=httpx.MockTransport(handler))
    assert YouTubeCollector(yt_cfg(), client, sleep=lambda s: None).collect() == []
    assert called == []


def test_youtube_retries_intermittent_404_then_recovers():
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] < 3:
            return httpx.Response(404)  # YouTube's feed host 404s intermittently
        return httpx.Response(200, content=(FIX / "youtube.xml").read_bytes())

    sleeps = []
    client = httpx.Client(transport=httpx.MockTransport(handler))
    items = YouTubeCollector(yt_cfg("UCa"), client, sleep=sleeps.append).collect()
    assert items
    assert calls["n"] == 3 and len(sleeps) == 2


def test_youtube_gives_up_on_persistent_404_without_raising():
    client = httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(404)))
    assert YouTubeCollector(yt_cfg("UCa"), client, sleep=lambda s: None).collect() == []


def test_youtube_one_failing_channel_does_not_stop_the_others():
    def handler(request: httpx.Request) -> httpx.Response:
        if "UCbad" in str(request.url):
            return httpx.Response(404)
        return httpx.Response(200, content=(FIX / "youtube.xml").read_bytes())

    client = httpx.Client(transport=httpx.MockTransport(handler))
    items = YouTubeCollector(yt_cfg("UCbad", "UCgood"), client, sleep=lambda s: None).collect()
    assert items and all("UCgood" in i.text for i in items)


def test_youtube_skips_undated_entries():
    undated = b"""<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom"><title>c</title>
<entry><title>No date</title><link href="https://www.youtube.com/watch?v=x1"/><id>x1</id></entry>
<entry><title>Dated</title><link href="https://www.youtube.com/watch?v=x2"/><id>x2</id><published>2026-10-12T10:00:00+00:00</published></entry>
</feed>"""
    items = YouTubeCollector(yt_cfg("UCa"), client_for({"": undated}), sleep=lambda s: None).collect()
    assert {i.title for i in items} == {"Dated"}


def x_cfg(handles=("AnthropicAI",), searches=()):
    from dataclasses import replace

    return replace(cfg(), x_handles=list(handles), x_searches=list(searches), x_min_likes=50, x_max_items=150)


def x_client(captured: list, body: bytes | None = None, status: int = 200) -> httpx.Client:
    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(status, content=body if body is not None else (FIX / "x.json").read_bytes())

    return httpx.Client(transport=httpx.MockTransport(handler))


def test_x_maps_posts_and_skips_retweets_replies_undated_and_placeholders():
    items = XCollector(x_cfg(), x_client([]), token="tok").collect()
    assert [i.url for i in items] == ["https://x.com/AnthropicAI/status/1845000000000000001"]
    post = items[0]
    assert post.source == "x"
    assert post.title.startswith("Claude Code now supports background tasks")
    assert "@AnthropicAI" in post.text and "4200" in post.text
    assert post.published_at == datetime(2026, 10, 12, 10, 0, tzinfo=timezone.utc)


def test_x_sends_confirmed_actor_inputs_and_keeps_token_out_of_the_url():
    captured = []
    XCollector(x_cfg(searches=("claude code",)), x_client(captured), token="s3cret").collect()
    req = captured[0]
    assert "apidojo~tweet-scraper" in str(req.url) and "run-sync-get-dataset-items" in str(req.url)
    assert "s3cret" not in str(req.url)
    assert req.headers["Authorization"] == "Bearer s3cret"
    import json

    body = json.loads(req.content)
    assert body["twitterHandles"] == ["AnthropicAI"]
    assert body["searchTerms"] and "claude code" in body["searchTerms"][0]
    assert body["maxItems"] == 150 and body["minimumFavorites"] == 50 and body["sort"] == "Latest"


def test_x_is_off_without_token_or_without_targets():
    captured = []
    assert XCollector(x_cfg(), x_client(captured), token=None).collect() == []
    assert XCollector(x_cfg(handles=(), searches=()), x_client(captured), token="tok").collect() == []
    assert captured == []


def test_x_http_error_returns_nothing_and_never_logs_the_token(caplog):
    with caplog.at_level("WARNING"):
        items = XCollector(x_cfg(), x_client([], body=b"{}", status=402), token="s3cret").collect()
    assert items == []
    assert "s3cret" not in caplog.text


def test_web_retries_transient_502_then_recovers():
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] == 1:
            return httpx.Response(502)
        return httpx.Response(200, content=(FIX / "web.xml").read_bytes())

    from dataclasses import replace

    sleeps = []
    one_feed = replace(cfg(), feeds=["https://example.com/feed"])
    client = httpx.Client(transport=httpx.MockTransport(handler))
    items = WebCollector(one_feed, client, sleep=sleeps.append).collect()
    assert items and calls["n"] == 2 and len(sleeps) == 1


def test_web_does_not_retry_a_404():
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        return httpx.Response(404)

    from dataclasses import replace

    one_feed = replace(cfg(), feeds=["https://example.com/feed"])
    client = httpx.Client(transport=httpx.MockTransport(handler))
    assert WebCollector(one_feed, client, sleep=lambda s: None).collect() == []
    assert calls["n"] == 1


def yt_apify_client(captured: list, rss_ok_for=(), status: int = 200):
    """RSS GETs 404 unless the channel is in rss_ok_for; Apify POSTs return the recorded dataset."""

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        if request.method == "POST":
            return httpx.Response(status, content=(FIX / "apify_youtube.json").read_bytes())
        if any(ch in str(request.url) for ch in rss_ok_for):
            return httpx.Response(200, content=(FIX / "youtube.xml").read_bytes())
        return httpx.Response(404)

    return httpx.Client(transport=httpx.MockTransport(handler))


def test_youtube_falls_back_to_apify_when_the_feed_is_down():
    captured = []
    items = YouTubeCollector(yt_cfg("UCa"), yt_apify_client(captured), sleep=lambda s: None, token="tok").collect()
    posts = [r for r in captured if r.method == "POST"]
    assert len(posts) == 1
    assert "apidojo~youtube-scraper" in str(posts[0].url) and "run-sync-get-dataset-items" in str(posts[0].url)
    assert posts[0].headers["Authorization"] == "Bearer tok" and "tok" not in str(posts[0].url)
    import json

    body = json.loads(posts[0].content)
    assert body["startUrls"] == ["https://www.youtube.com/channel/UCa"]
    assert body["includeShorts"] is False and body["maxItems"] == 10
    [video] = items  # the unparseable-date row is skipped
    assert video.source == "youtube" and video.url.endswith("abc123XYZ01")
    assert video.title == "Claude Code: a deep dive into hooks"
    assert "Chan UCa" in video.text and "hooks, skills and subagents" in video.text
    assert video.published_at == datetime(2026, 10, 12, tzinfo=timezone.utc)


def test_youtube_does_not_call_apify_when_the_feed_works():
    captured = []
    client = yt_apify_client(captured, rss_ok_for=("UCa",))
    items = YouTubeCollector(yt_cfg("UCa"), client, sleep=lambda s: None, token="tok").collect()
    assert items and not [r for r in captured if r.method == "POST"]


def test_youtube_batches_all_failed_channels_into_one_apify_run():
    captured = []
    client = yt_apify_client(captured, rss_ok_for=("UCok",))
    YouTubeCollector(yt_cfg("UCa", "UCok", "UCb"), client, sleep=lambda s: None, token="tok").collect()
    posts = [r for r in captured if r.method == "POST"]
    assert len(posts) == 1
    import json

    body = json.loads(posts[0].content)
    assert body["startUrls"] == ["https://www.youtube.com/channel/UCa", "https://www.youtube.com/channel/UCb"]
    assert body["maxItems"] == 20  # 10 per failed channel


def test_youtube_without_a_token_never_calls_apify():
    captured = []
    items = YouTubeCollector(yt_cfg("UCa"), yt_apify_client(captured), sleep=lambda s: None, token=None).collect()
    assert items == [] and not [r for r in captured if r.method == "POST"]


def test_youtube_apify_failure_returns_nothing_and_never_logs_the_token(caplog):
    with caplog.at_level("WARNING"):
        items = YouTubeCollector(
            yt_cfg("UCa"), yt_apify_client([], status=402), sleep=lambda s: None, token="s3cret"
        ).collect()
    assert items == [] and "s3cret" not in caplog.text

def test_youtube_apify_logs_rows_per_channel(caplog):
    with caplog.at_level("INFO", logger="akd.collectors.youtube"):
        YouTubeCollector(yt_cfg("UCa"), yt_apify_client([]), sleep=lambda s: None, token="tok").collect()
    assert "returned 2 rows: {'Chan UCa': 2}" in caplog.text


def test_x_logs_rows_per_author(caplog):
    with caplog.at_level("INFO", logger="akd.collectors.x"):
        XCollector(x_cfg(), x_client([]), token="tok").collect()
    assert "'AnthropicAI': 2" in caplog.text

def test_youtube_skips_obvious_shorts():
    feed = b"""<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom"><title>c</title>
<entry><title>Long video</title><link href="https://www.youtube.com/watch?v=v1"/><id>v1</id><published>2026-10-12T10:00:00+00:00</published></entry>
<entry><title>A short</title><link href="https://www.youtube.com/shorts/s1"/><id>s1</id><published>2026-10-12T10:00:00+00:00</published></entry>
<entry><title>Quick tip #Shorts</title><link href="https://www.youtube.com/watch?v=s2"/><id>s2</id><published>2026-10-12T10:00:00+00:00</published></entry>
</feed>"""
    items = YouTubeCollector(yt_cfg("UCa"), client_for({"": feed}), sleep=lambda s: None).collect()
    assert {i.title for i in items} == {"Long video"}


def test_youtube_apify_skips_obvious_shorts():
    from akd.collectors.youtube import is_short

    assert is_short("https://www.youtube.com/shorts/abc", "x")
    assert is_short("https://www.youtube.com/watch?v=abc", "Tip #shorts")
    assert not is_short("https://www.youtube.com/watch?v=abc", "A normal video about shorts of the year")


def test_shipped_config_caps_youtube_picks():
    caps = load_config(ROOT / "config.yaml").per_source_pick_cap
    assert caps.get("youtube") == 2 and caps.get("reddit") == 2

FULL_BODY_RSS = b"""<?xml version="1.0"?><rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/"><channel><title>t</title>
<item><title>Newsletter</title><link>https://e.com/n</link><pubDate>Mon, 12 Oct 2026 10:00:00 +0000</pubDate>
<description>Short teaser.</description>
<content:encoded><![CDATA[<p>Teaser.</p><p>The full body has the real detail about Gemini 4 and the benchmark results.</p>]]></content:encoded></item>
<item><title>Plain</title><link>https://e.com/p</link><pubDate>Mon, 12 Oct 2026 11:00:00 +0000</pubDate><description>Only a description here.</description></item>
</channel></rss>"""


def test_web_prefers_the_full_content_body_over_a_short_summary():
    items = WebCollector(cfg(), client_for({"": FULL_BODY_RSS})).collect()
    by_title = {i.title: i for i in items}
    assert "real detail about Gemini 4" in by_title["Newsletter"].text
    assert by_title["Plain"].text == "Only a description here."


def test_shipped_config_includes_latent_space():
    assert "https://www.latent.space/feed" in cfg().feeds



# --- web: short feed teasers are replaced by the article's own text ---

ARTICLE_HTML = """<html><head>
<meta property="og:description" content="Meta&#x27;s new model lands near the frontier. Here&#x27;s what it means.">
</head><body><nav>menu menu</nav>
<article><h1>Big headline</h1><p>Good morning. The full story about the model, with real detail.</p>
<script>var tracker = 1;</script></article><footer>footer links</footer></body></html>"""

FEED_URL = "https://news.example.com/feed"
TEASER = "PLUS: Put it to work"


def rss(*entries):
    body = "".join(
        f"<item><title>{t}</title><link>{link}</link><description>{d}</description>"
        f"<pubDate>Mon, 12 Oct 2026 10:00:00 GMT</pubDate></item>"
        for t, link, d in entries
    )
    return f'<?xml version="1.0"?><rss version="2.0"><channel><title>t</title>{body}</channel></rss>'.encode()


def web_with_pages(feed_xml, pages):
    """A web collector for one feed; `pages` maps URL -> (status, body). Returns (collector, fetched page URLs)."""
    from dataclasses import replace

    fetched: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        url = str(request.url)
        if url == FEED_URL:
            return httpx.Response(200, content=feed_xml)
        fetched.append(url)
        status, body = pages.get(url, (404, b""))
        return httpx.Response(status, content=body)

    client = httpx.Client(transport=httpx.MockTransport(handler))
    one_feed = replace(cfg(), feeds=[FEED_URL])
    return WebCollector(one_feed, client, sleep=lambda s: None), fetched


def test_web_short_teaser_is_replaced_with_the_article_text():
    link = "https://news.example.com/articles/meta"
    collector, fetched = web_with_pages(rss(("Meta ships", link, TEASER)), {link: (200, ARTICLE_HTML.encode())})
    (item,) = collector.collect()
    assert fetched == [link]
    assert "Meta's new model lands near the frontier" in item.text
    assert "full story about the model" in item.text
    assert "tracker" not in item.text and "menu menu" not in item.text and "footer links" not in item.text


def test_web_long_feed_text_does_not_trigger_a_page_fetch():
    link = "https://news.example.com/articles/long"
    long_text = "A full length summary. " * 20
    collector, fetched = web_with_pages(rss(("Long", link, long_text)), {link: (200, ARTICLE_HTML.encode())})
    (item,) = collector.collect()
    assert fetched == []
    assert item.text.startswith("A full length summary.")


def test_web_only_fetches_pages_on_the_feeds_own_host():
    link = "https://other.example.org/story"
    collector, fetched = web_with_pages(rss(("Elsewhere", link, TEASER)), {link: (200, ARTICLE_HTML.encode())})
    (item,) = collector.collect()
    assert fetched == []
    assert item.text == TEASER


def test_web_article_fetch_failure_keeps_the_teaser():
    link = "https://news.example.com/articles/blocked"
    collector, fetched = web_with_pages(rss(("Blocked", link, TEASER)), {link: (403, b"")})
    (item,) = collector.collect()
    assert fetched == [link]
    assert item.text == TEASER


def test_web_article_page_without_usable_text_keeps_the_teaser():
    link = "https://news.example.com/articles/empty"
    collector, _ = web_with_pages(rss(("Empty", link, TEASER)), {link: (200, b"<html><body>nothing here</body></html>")})
    (item,) = collector.collect()
    assert item.text == TEASER


def test_web_limits_article_fetches_per_run():
    from akd.collectors.web import MAX_ARTICLE_FETCHES

    links = [f"https://news.example.com/articles/{n}" for n in range(MAX_ARTICLE_FETCHES + 5)]
    pages = {u: (200, ARTICLE_HTML.encode()) for u in links}
    collector, fetched = web_with_pages(rss(*[(f"T{n}", u, TEASER) for n, u in enumerate(links)]), pages)
    items = collector.collect()
    assert len(items) == len(links)
    assert len(fetched) == MAX_ARTICLE_FETCHES
