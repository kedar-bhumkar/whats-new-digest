import json
from datetime import date, datetime, timezone
from pathlib import Path

import pytest

from akd.config import load_config
from akd.dedupe import item_id
from akd.models import Item, Scored, Selected
from akd.pipeline import format_tune, published_ids_from, rank_all, run

ROOT = Path(__file__).resolve().parent.parent
NOW = datetime(2026, 10, 12, 12, tzinfo=timezone.utc)
DAY = date(2026, 10, 12)
CFG = load_config(ROOT / "config.yaml")


def make_item(n: int) -> Item:
    url = f"https://example.com/story-{n}"
    return Item(item_id(url), "web", f"Story {n}", url, f"text {n}", NOW)


class FakeCollector:
    name = "fake"

    def __init__(self, items):
        self.items = items

    def collect(self):
        return list(self.items)


class BoomCollector:
    name = "boom"

    def collect(self):
        raise RuntimeError("down")


def good_scorer(items, profile):
    out = []
    for i, item in enumerate(items):
        v = max(0.0, 0.95 - 0.05 * i)
        out.append(
            Scored(item, "dev_tooling", {"significance": v, "relevance": v, "actionability": v, "novelty": v}, 0.0, 0.9)
        )
    return out


def summarizer(selected, profile):
    for s in selected:
        s.why = f"why {s.scored.item.title}"
    return selected


def dirs(tmp_path):
    digest, site = tmp_path / "digest", tmp_path / "site"
    digest.mkdir(exist_ok=True)
    return digest, site


def do_run(tmp_path, collectors, scorer=good_scorer, published=frozenset()):
    digest, site = dirs(tmp_path)
    return run(CFG, "profile", collectors, scorer, summarizer, set(published), DAY, digest, site, now=NOW)


def load_doc(tmp_path):
    return json.loads((tmp_path / "site" / "public" / "whats-new" / "items.json").read_text(encoding="utf-8"))


def test_end_to_end_dry_run_writes_expected_files(tmp_path):
    selected = do_run(tmp_path, [FakeCollector([make_item(n) for n in range(1, 9)])])
    doc = load_doc(tmp_path)
    assert [s.tier for s in selected].count("pick") == 5
    assert len(doc["days"][0]["picks"]) == 5
    assert doc["days"][0]["picks"][0]["why"].startswith("why Story")
    assert "(AKD)" in (tmp_path / "digest" / "whats-new.md").read_text(encoding="utf-8")


def test_empty_day_exits_cleanly_and_writes_nothing(tmp_path):
    assert do_run(tmp_path, [FakeCollector([])]) == []
    assert not (tmp_path / "site").exists()
    assert not (tmp_path / "digest" / "whats-new.md").exists()


def test_all_collectors_failing_is_an_empty_day(tmp_path):
    assert do_run(tmp_path, [BoomCollector()]) == []
    assert not (tmp_path / "site").exists()


def test_jev_failure_aborts_and_writes_nothing(tmp_path):
    def broken(items, profile):
        raise RuntimeError("jev down")

    with pytest.raises(RuntimeError, match="jev down"):
        do_run(tmp_path, [FakeCollector([make_item(1)])], scorer=broken)
    assert not (tmp_path / "site").exists()


def test_second_run_same_day_is_idempotent(tmp_path):
    items = [make_item(n) for n in range(1, 4)]
    do_run(tmp_path, [FakeCollector(items)])
    first = load_doc(tmp_path)
    md1 = (tmp_path / "digest" / "whats-new.md").read_text(encoding="utf-8")
    do_run(tmp_path, [FakeCollector(items)], published=published_ids_from(first, exclude_day=DAY))
    assert load_doc(tmp_path) == first
    assert (tmp_path / "digest" / "whats-new.md").read_text(encoding="utf-8") == md1


def test_item_published_yesterday_is_not_published_again(tmp_path):
    prior = {"lastUpdated": "x", "days": [{"date": "2026-10-11", "picks": [{"id": make_item(1).id}], "notable": []}]}
    assert published_ids_from(prior, exclude_day=DAY) == {make_item(1).id}
    assert do_run(tmp_path, [FakeCollector([make_item(1)])], published=published_ids_from(prior, DAY)) == []


def test_same_day_ids_are_not_treated_as_published():
    doc = {"days": [{"date": "2026-10-12", "picks": [{"id": "a"}], "notable": [{"id": "b"}]}]}
    assert published_ids_from(doc, exclude_day=DAY) == set()
    assert published_ids_from(doc, exclude_day=date(2026, 10, 13)) == {"a", "b"}


def test_published_ids_from_empty_doc():
    assert published_ids_from({}, exclude_day=DAY) == set()


def test_rank_all_orders_and_format_tune_shows_top_and_bottom():
    scored = good_scorer([make_item(n) for n in range(1, 8)], "p")
    ranked = rank_all(scored, CFG)
    text = format_tune(ranked, n=2)
    assert "TOP 2" in text and "BOTTOM 2" in text
    assert "Story 1" in text and "Story 7" in text
    assert "Story 4" not in text
    assert "sig=" in text and "rel=" in text
