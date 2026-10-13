from datetime import datetime, timezone

from akd.dedupe import canonical_url, dedupe, item_id
from akd.models import Item


def make(url: str, title: str = "t") -> Item:
    return Item(
        id=item_id(url),
        source="web",
        title=title,
        url=url,
        text="body",
        published_at=datetime(2026, 10, 11, tzinfo=timezone.utc),
    )


def test_canonical_url_strips_tracking():
    assert canonical_url("https://www.Example.com/a/?utm_source=x#frag") == "https://example.com/a"


def test_canonical_url_keeps_meaningful_query():
    assert canonical_url("https://example.com/p?id=7&utm_medium=x") == "https://example.com/p?id=7"


def test_dedupe_collapses_variants():
    items = [make("https://example.com/a"), make("https://www.example.com/a/?utm_source=x")]
    assert len(dedupe(items, set())) == 1


def test_dedupe_keeps_first_occurrence():
    first = make("https://example.com/a", "first")
    out = dedupe([first, make("https://example.com/a/", "second")], set())
    assert out[0].title == "first"


def test_dedupe_skips_already_published():
    item = make("https://example.com/a")
    assert dedupe([item], {item.id}) == []


def test_dedupe_empty_list_returns_empty():
    assert dedupe([], set()) == []


def test_canonical_url_ignores_scheme_and_query_order():
    assert canonical_url("http://x.com/a?b=1&c=2") == canonical_url("https://x.com/a?c=2&b=1")


def test_dedupe_collapses_scheme_and_query_order_variants():
    items = [make("http://x.com/a?b=1&c=2"), make("https://x.com/a?c=2&b=1")]
    assert len(dedupe(items, set())) == 1
