import imaplib
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path
from types import SimpleNamespace

import httpx

from akd.collectors.email import EmailCollector, HaikuExtractor, extract_links
from akd.config import load_config

ROOT = Path(__file__).resolve().parent.parent
NOW = datetime(2026, 10, 14, 12, 0, tzinfo=timezone.utc)


def cfg(**over):
    from dataclasses import replace

    base = load_config(ROOT / "config.yaml")
    return replace(base, email_senders=["tldr", "rundown"], email_max_messages=6, email_max_stories=15, **over)


def make_mail(sender: str, subject: str, html: str, date: str = "Tue, 14 Oct 2026 08:00:00 +0000") -> bytes:
    msg = EmailMessage()
    msg["From"], msg["To"], msg["Subject"], msg["Date"] = sender, "me@example.com", subject, date
    msg.set_content("plain fallback")
    msg.add_alternative(html, subtype="html")
    return msg.as_bytes()


TLDR_HTML = """<html><body><script>alert(1)</script>
<h2>Top stories</h2>
<p><a href="https://tracking.tldrnewsletter.com/c/AAA">Story One: a new model (5 minute read)</a></p>
<p>Story one blurb about a new model.</p>
<p><a href="https://tracking.tldrnewsletter.com/c/BBB">Story Two: a new framework (3 minute read)</a></p>
<p>Story two blurb.</p>
<p><a href="https://tldrnewsletter.com/unsubscribe?x=1">Unsubscribe</a> <a href="mailto:a@b.com">Contact</a></p>
</body></html>"""


class FakeImap:
    def __init__(self, messages: dict[bytes, bytes], fail_login: bool = False):
        self.messages = messages
        self.fail_login = fail_login
        self.calls: list[tuple] = []

    def login(self, user, password):
        self.calls.append(("login", user))
        if self.fail_login:
            raise imaplib.IMAP4.error("AUTHENTICATIONFAILED " + password)  # real servers can echo detail
        return "OK", [b"ok"]

    def select(self, mailbox, readonly=False):
        self.calls.append(("select", mailbox, readonly))
        return "OK", [b"1"]

    def search(self, charset, *criteria):
        self.calls.append(("search", criteria))
        return "OK", [b" ".join(self.messages)]

    def fetch(self, num, spec):
        self.calls.append(("fetch", num, spec))
        raw = self.messages[num]
        if "HEADER" in spec:
            head = raw.split(b"\n\n", 1)[0] + b"\n\n"
            return "OK", [(b"1 (BODY[HEADER.FIELDS] {n}", head), b")"]
        return "OK", [(b"1 (BODY[] {n}", raw), b")"]

    def logout(self):
        self.calls.append(("logout",))
        return "BYE", [b""]


def stub_extractor(stories):
    seen = {}

    def extract(sender, subject, text, links):
        seen.update(sender=sender, subject=subject, text=text, links=links)
        return stories

    extract.seen = seen
    return extract


def redirecting_client(table: dict[str, str]) -> httpx.Client:
    def handler(request: httpx.Request) -> httpx.Response:
        target = table.get(str(request.url))
        if target:
            return httpx.Response(302, headers={"Location": target})
        return httpx.Response(200, content=b"page")

    return httpx.Client(transport=httpx.MockTransport(handler))


def collector(imap, extractor, client=None, **kw):
    return EmailCollector(
        cfg(),
        client or redirecting_client({}),
        address="bot@example.com",
        password="app-pass",
        extractor=extractor,
        imap_factory=lambda: imap,
        now=NOW,
        **kw,
    )


def test_collects_stories_from_matching_newsletters_only():
    imap = FakeImap(
        {
            b"1": make_mail("TLDR AI <dan@tldrnewsletter.com>", "TLDR AI 2026-10-14", TLDR_HTML),
            b"2": make_mail("Shop Deals <promo@shop.com>", "50% off", "<p>buy</p>"),
        }
    )
    ext = stub_extractor([{"link": 1, "title": "Story One", "blurb": "A new model."}])
    items = collector(imap, ext, redirecting_client({"https://tracking.tldrnewsletter.com/c/AAA": "https://example.org/story-one?utm_source=tldr"})).collect()
    [item] = items
    assert item.source == "email"
    assert item.title == "Story One"
    assert item.url == "https://example.org/story-one?utm_source=tldr"  # tracking redirect resolved
    assert "TLDR AI" in item.text and "A new model." in item.text
    assert item.published_at == datetime(2026, 10, 14, 8, 0, tzinfo=timezone.utc)
    assert ext.seen["subject"] == "TLDR AI 2026-10-14"  # the shop mail never reached the extractor


def test_extractor_sees_clean_text_and_only_real_links():
    imap = FakeImap({b"1": make_mail("TLDR AI <dan@tldrnewsletter.com>", "s", TLDR_HTML)})
    ext = stub_extractor([])
    collector(imap, ext).collect()
    assert "alert(1)" not in ext.seen["text"] and "Story one blurb" in ext.seen["text"]
    urls = [u for _, _, u in ext.seen["links"]]
    assert urls == ["https://tracking.tldrnewsletter.com/c/AAA", "https://tracking.tldrnewsletter.com/c/BBB"]  # no unsubscribe/mailto
    assert [n for n, _, _ in ext.seen["links"]] == [1, 2]


def test_model_cannot_introduce_links_that_are_not_in_the_email():
    imap = FakeImap({b"1": make_mail("TLDR AI <dan@tldrnewsletter.com>", "s", TLDR_HTML)})
    stories = [
        {"link": 99, "title": "Out of range", "blurb": "x"},
        {"link": "javascript:alert(1)", "title": "Bad type", "blurb": "x"},
        {"link": 2, "title": "", "blurb": "no title"},
        {"link": 2, "title": "Good", "blurb": "ok"},
        {"link": 2, "title": "Duplicate link", "blurb": "again"},
        "not even a dict",
    ]
    items = collector(imap, stub_extractor(stories)).collect()
    assert [i.title for i in items] == ["Good"]


def test_story_whose_tracking_link_cannot_be_resolved_is_dropped_not_published():
    # An unresolved tracker URL carries a per-subscriber token; it must never reach a public page.
    def boom(request):
        raise httpx.ConnectError("down")

    imap = FakeImap({b"1": make_mail("TLDR AI <dan@tldrnewsletter.com>", "s", TLDR_HTML)})
    client = httpx.Client(transport=httpx.MockTransport(boom))
    assert collector(imap, stub_extractor([{"link": 1, "title": "T", "blurb": "b"}]), client).collect() == []


def test_bot_blocked_tracker_is_dropped_but_a_direct_article_link_is_kept():
    def handler(request: httpx.Request) -> httpx.Response:
        if "AAA" in str(request.url):
            return httpx.Response(403)  # e.g. beehiiv refuses automated requests
        return httpx.Response(200, content=b"article")  # a normal page, URL unchanged

    imap = FakeImap({b"1": make_mail("TLDR AI <dan@tldrnewsletter.com>", "s", TLDR_HTML)})
    stories = [{"link": 1, "title": "Blocked", "blurb": "b"}, {"link": 2, "title": "Direct", "blurb": "b"}]
    client = httpx.Client(transport=httpx.MockTransport(handler))
    items = collector(imap, stub_extractor(stories), client).collect()
    assert [i.title for i in items] == ["Direct"]


def test_reads_the_mailbox_without_changing_it():
    imap = FakeImap({b"1": make_mail("TLDR AI <dan@tldrnewsletter.com>", "s", TLDR_HTML)})
    collector(imap, stub_extractor([])).collect()
    selects = [c for c in imap.calls if c[0] == "select"]
    assert selects == [("select", "INBOX", True)]  # read-only
    assert all("PEEK" in c[2] for c in imap.calls if c[0] == "fetch")  # never marks mail as read
    assert imap.calls[-1] == ("logout",)


def test_is_off_without_credentials():
    made = []
    c = EmailCollector(cfg(), redirecting_client({}), address=None, password=None, extractor=stub_extractor([]), imap_factory=lambda: made.append(1) or FakeImap({}), now=NOW)
    assert c.collect() == [] and made == []


def test_login_failure_returns_nothing_and_never_logs_the_password(caplog):
    imap = FakeImap({}, fail_login=True)
    with caplog.at_level("WARNING"):
        items = collector(imap, stub_extractor([])).collect()
    assert items == []
    assert "app-pass" not in caplog.text


def test_logs_the_senders_it_saw_so_matching_can_be_tuned(caplog):
    imap = FakeImap(
        {
            b"1": make_mail("TLDR AI <dan@tldrnewsletter.com>", "s", TLDR_HTML),
            b"2": make_mail("Shop Deals <promo@shop.com>", "x", "<p>buy</p>"),
        }
    )
    with caplog.at_level("INFO", logger="akd.collectors.email"):
        collector(imap, stub_extractor([])).collect()
    assert "promo@shop.com" in caplog.text and "dan@tldrnewsletter.com" in caplog.text


def test_caps_how_many_messages_are_processed():
    msgs = {str(i).encode(): make_mail("TLDR AI <dan@tldrnewsletter.com>", f"s{i}", TLDR_HTML, f"Tue, 14 Oct 2026 0{i}:00:00 +0000") for i in range(1, 9)}
    ext_calls = []

    def ext(sender, subject, text, links):
        ext_calls.append(subject)
        return []

    collector(FakeImap(msgs), ext).collect()
    assert len(ext_calls) == 6  # email_max_messages


def test_message_without_a_date_is_skipped():
    imap = FakeImap({b"1": make_mail("TLDR AI <dan@tldrnewsletter.com>", "s", TLDR_HTML, date="")})
    assert collector(imap, stub_extractor([{"link": 1, "title": "T", "blurb": "b"}])).collect() == []


def test_extract_links_skips_unsubscribe_mailto_and_non_http():
    html = '<a href="https://a.com/x">Real story headline here</a><a href="mailto:x@y.com">mail</a><a href="https://a.com/unsubscribe">Unsubscribe</a><a href="javascript:void(0)">js</a><a href="https://a.com/x">Real story headline here</a>'
    assert extract_links(html) == [(1, "Real story headline here", "https://a.com/x")]


def haiku_client(text: str):
    return SimpleNamespace(messages=SimpleNamespace(create=lambda **kw: SimpleNamespace(content=[SimpleNamespace(type="text", text=text)], stop_reason="end_turn")))


def test_haiku_extractor_parses_fenced_json():
    reply = 'Here you go:\n```json\n[{"link": 2, "title": "T", "blurb": "B"}]\n```'
    got = HaikuExtractor(haiku_client(reply))("TLDR AI", "subj", "body", [(1, "a", "https://a.com"), (2, "b", "https://b.com")])
    assert got == [{"link": 2, "title": "T", "blurb": "B"}]


def test_haiku_extractor_returns_nothing_on_garbage_or_errors():
    assert HaikuExtractor(haiku_client("sorry, no"))("s", "s", "b", []) == []

    def raises(**kw):
        raise RuntimeError("api down")

    broken = SimpleNamespace(messages=SimpleNamespace(create=raises))
    assert HaikuExtractor(broken)("s", "s", "b", []) == []


def test_shipped_config_splits_newsletters_between_email_and_web_feeds():
    conf = load_config(ROOT / "config.yaml")
    senders = [s.lower() for s in conf.email_senders]
    assert "tldr" in senders
    # AINews arrives via the Latent Space feed and The Rundown via its public feed (its email links are unresolvable trackers).
    assert not any(x in s for s in senders for x in ("ainews", "latent", "rundown"))
    assert "https://www.therundown.ai/feed" in conf.feeds
