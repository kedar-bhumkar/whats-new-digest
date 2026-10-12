import json
from datetime import date, datetime, timezone
from pathlib import Path

import jsonschema
import pytest

from akd.models import Item, Scored, Selected
from akd.publish import merge_day, prepend_markdown, validate, write_outputs

NOW = datetime(2026, 10, 12, 12, 0, tzinfo=timezone.utc)
DAY = date(2026, 10, 12)

MD = """# What's New Digest

Daily digest. Newest entry first.

## 2026-10-12

- **Routine entry** (AI/Claude tooling) - from the old routine.
  - Link: https://example.com/old

## 2026-10-11

- **Older entry** (GitHub repo) - older.
"""


def sel(n=1, tier="pick", title=None, why="Because it matters.", url=None) -> Selected:
    item = Item(
        f"id{n}", "github", title or f"Title {n}", url or f"https://e.com/{n}", "text", NOW
    )
    scored = Scored(
        item, "dev_tooling",
        {"significance": 0.8, "relevance": 0.7, "actionability": 0.6, "novelty": 0.5},
        0.1, 0.9, rank=0.7 - n / 100,
    )
    return Selected(scored, tier, why)


def test_merge_day_is_idempotent():
    selected = [sel(1), sel(2, "notable")]
    once = merge_day({}, DAY, selected, 60, now=NOW)
    twice = merge_day(once, DAY, selected, 60, now=NOW)
    assert once == twice
    assert len(twice["days"]) == 1
    assert [i["id"] for i in twice["days"][0]["picks"]] == ["id1"]
    assert [i["id"] for i in twice["days"][0]["notable"]] == ["id2"]


def test_merge_trims_to_60_days_and_sorts_newest_first():
    doc = {}
    for offset in (0, 30, 61, 90):
        d = date(2026, 10, 12).fromordinal(DAY.toordinal() - offset)
        doc = merge_day(doc, d, [sel(offset + 1)], 60, now=NOW)
    # merging an old day last must not resurrect days beyond the window of the newest day
    dates = [d["date"] for d in doc["days"]]
    assert dates == sorted(dates, reverse=True)
    assert "2026-10-12" in dates and "2026-09-12" in dates
    assert len(dates) == 2


def test_invalid_doc_rejected_and_nothing_written(tmp_path):
    bad = sel(1)
    bad.scored.item = Item("id1", "github", "T", "https://e.com/1", "x", NOW)
    bad.scored.scores = {"significance": 5.0}  # out of range / incomplete
    with pytest.raises(jsonschema.ValidationError):
        write_outputs([bad], DAY, tmp_path / "d", tmp_path / "s", now=NOW)
    assert not (tmp_path / "s").exists() or not any((tmp_path / "s").rglob("items.json"))
    assert not (tmp_path / "d" / "whats-new.md").exists()


def test_markdown_prepend_keeps_existing_entries():
    out = prepend_markdown(MD, DAY, [sel(1), sel(2, "notable")])
    assert "Routine entry" in out and "Older entry" in out
    assert out.index("## 2026-10-12 (AKD)") < out.index("## 2026-10-12\n")
    assert "https://e.com/1" in out


def test_markdown_prepend_is_idempotent():
    once = prepend_markdown(MD, DAY, [sel(1)])
    twice = prepend_markdown(once, DAY, [sel(1)])
    assert once == twice
    assert twice.count("## 2026-10-12 (AKD)") == 1


def test_markdown_preserves_crlf_line_endings():
    crlf = MD.replace("\n", "\r\n")
    out = prepend_markdown(crlf, DAY, [sel(1)])
    assert "\n" not in out.replace("\r\n", "")


def test_text_is_sanitized():
    evil = sel(1, title="<script>alert(1)</script>Hello <b>World</b>", why="<img src=x onerror=alert(1)>Safe")
    doc = merge_day({}, DAY, [evil], 60, now=NOW)
    item = doc["days"][0]["picks"][0]
    assert item["title"] == "Hello World"
    assert item["why"] == "Safe"
    assert "<" not in json.dumps(item["title"])


def test_non_http_urls_are_dropped():
    bad = sel(1, url="javascript:alert(1)")
    good = sel(2)
    doc = merge_day({}, DAY, [bad, good], 60, now=NOW)
    assert [i["id"] for i in doc["days"][0]["picks"]] == ["id2"]


def test_empty_selection_writes_nothing(tmp_path):
    write_outputs([], DAY, tmp_path / "d", tmp_path / "s", now=NOW)
    assert not (tmp_path / "d").exists() and not (tmp_path / "s").exists()


def test_write_outputs_writes_valid_json_and_markdown(tmp_path):
    digest, site = tmp_path / "digest", tmp_path / "site"
    digest.mkdir()
    (digest / "whats-new.md").write_text(MD, encoding="utf-8", newline="")
    write_outputs([sel(1), sel(2, "notable")], DAY, digest, site, now=NOW)
    doc = json.loads((site / "public" / "whats-new" / "items.json").read_text(encoding="utf-8"))
    validate(doc)
    assert doc["days"][0]["date"] == "2026-10-12"
    assert "## 2026-10-12 (AKD)" in (digest / "whats-new.md").read_text(encoding="utf-8")


def test_rerun_same_day_does_not_duplicate(tmp_path):
    digest, site = tmp_path / "digest", tmp_path / "site"
    digest.mkdir()
    (digest / "whats-new.md").write_text(MD, encoding="utf-8", newline="")
    for _ in range(2):
        write_outputs([sel(1)], DAY, digest, site, now=NOW)
    doc = json.loads((site / "public" / "whats-new" / "items.json").read_text(encoding="utf-8"))
    assert len(doc["days"]) == 1
    assert (digest / "whats-new.md").read_text(encoding="utf-8").count("(AKD)") == 1
