import asyncio
import json
from dataclasses import replace
from types import SimpleNamespace

import pytest

from akd.group import assign_groups, group_stories, pair_probabilities, pairs_report
from akd.models import Scored, Selected
from akd.publish import _item_dict, _md_section, validate
from akd.pipeline import run
from tests.test_pipeline import CFG, DAY, NOW, FakeCollector, dirs, good_scorer, load_doc, make_item, summarizer


def sc(n: int, source: str = "web") -> Scored:
    item = replace(make_item(n), source=source)
    return Scored(item, "other", {"significance": 0.5, "relevance": 0.5, "actionability": 0.5, "novelty": 0.5}, 0.0, 0.9, rank=1 - 0.01 * n)


def titles(scored: list[Scored]) -> list[str]:
    return [s.item.title for s in scored]


# --- pure head-based assignment --------------------------------------------------------------------------------------


def test_members_join_the_highest_ranked_matching_item_and_disappear_from_the_list():
    ranked = [sc(1), sc(2), sc(3)]
    out = assign_groups(ranked, {(0, 1): 0.8, (0, 2): 0.1, (1, 2): 0.1}, threshold=0.5, also_max=5)
    assert titles(out) == ["Story 1", "Story 3"]
    assert titles_of_also(out[0]) == ["Story 2"]


def titles_of_also(s: Scored) -> list[str]:
    return [i.title for i in s.also]


def test_no_chaining_through_a_member():
    # B matches A, C matches only B. C must NOT be pulled under A via B.
    ranked = [sc(1), sc(2), sc(3)]
    out = assign_groups(ranked, {(0, 1): 0.9, (1, 2): 0.95, (0, 2): 0.05}, threshold=0.5, also_max=5)
    assert titles(out) == ["Story 1", "Story 3"]
    assert titles_of_also(out[0]) == ["Story 2"] and out[1].also == []


def test_item_joins_the_best_matching_head_when_several_match():
    ranked = [sc(1), sc(2), sc(3)]
    out = assign_groups(ranked, {(0, 1): 0.01, (0, 2): 0.6, (1, 2): 0.9}, threshold=0.5, also_max=5)
    assert titles(out) == ["Story 1", "Story 2"]
    assert titles_of_also(out[1]) == ["Story 3"] and out[0].also == []


def test_threshold_is_inclusive_and_below_it_nothing_is_grouped():
    ranked = [sc(1), sc(2)]
    assert titles(assign_groups(ranked, {(0, 1): 0.5}, threshold=0.5, also_max=5)) == ["Story 1"]
    assert titles(assign_groups([sc(1), sc(2)], {(0, 1): 0.49}, threshold=0.5, also_max=5)) == ["Story 1", "Story 2"]


def test_also_is_capped_but_every_member_is_still_removed():
    ranked = [sc(i) for i in range(1, 6)]
    probs = {(0, j): 0.9 for j in range(1, 5)}
    [head] = assign_groups(ranked, probs, threshold=0.5, also_max=2)
    assert len(head.also) == 2 and head.item.title == "Story 1"


def test_missing_pairs_count_as_different():
    assert titles(assign_groups([sc(1), sc(2)], {}, threshold=0.5, also_max=5)) == ["Story 1", "Story 2"]


# --- the Jev call ----------------------------------------------------------------------------------------------------


class FakeJev:
    def __init__(self, same_titles=()):
        self.same = {frozenset(p) for p in same_titles}
        self.calls: list[dict] = []

    async def system_one(self, state, questions):
        self.calls.append({"state": state, "questions": questions})
        pair = frozenset((state["item_a"]["title"], state["item_b"]["title"]))
        return SimpleNamespace(nouls={"same_story": SimpleNamespace(noul=0.9 if pair in self.same else 0.02)})


def test_pair_probabilities_asks_one_question_per_unordered_pair():
    shortlist = [sc(i) for i in range(1, 5)]
    jev = FakeJev([("Story 1", "Story 3")])
    probs = asyncio.run(pair_probabilities(shortlist, jev))
    assert len(jev.calls) == 6 and set(probs) == {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}
    assert probs[(0, 2)] == 0.9 and probs[(0, 1)] == 0.02
    call = jev.calls[0]
    assert set(call["state"]) == {"item_a", "item_b"} and set(call["state"]["item_a"]) == {"source", "title", "summary"}
    assert list(call["questions"]) == ["same_story"]


def test_group_stories_compares_only_the_shortlist_and_keeps_the_rest_in_order():
    ranked = [sc(i) for i in range(1, 7)]
    cfg = replace(CFG, group_shortlist=3, group_threshold=0.5, group_also_max=5)
    jev = FakeJev([("Story 1", "Story 2"), ("Story 5", "Story 6")])
    out, probs = asyncio.run(group_stories(ranked, cfg, jev))
    assert len(jev.calls) == 3  # 3 choose 2: Story 4+ never compared, so Story 5/6 are not grouped
    assert titles(out) == ["Story 1", "Story 3", "Story 4", "Story 5", "Story 6"]
    assert titles_of_also(out[0]) == ["Story 2"]


def test_group_stories_is_off_when_shortlist_is_zero():
    ranked = [sc(1), sc(2)]
    jev = FakeJev()
    out, probs = asyncio.run(group_stories(ranked, replace(CFG, group_shortlist=0), jev))
    assert out == ranked and probs == {} and jev.calls == []


# --- pipeline wiring -------------------------------------------------------------------------------------------------


def run_with(tmp_path, grouper):
    digest, site = dirs(tmp_path)
    return run(CFG, "profile", [FakeCollector([make_item(n) for n in range(1, 9)])], good_scorer, summarizer, set(), DAY, digest, site, now=NOW, grouper=grouper)


def test_grouped_members_are_not_published_and_the_head_carries_them(tmp_path):
    def grouper(ranked):
        return assign_groups(ranked, {(0, 1): 0.9}, threshold=0.5, also_max=5)  # story 2 folds into story 1

    selected = run_with(tmp_path, grouper)
    published = [s.scored.item.title for s in selected]
    assert "Story 2" not in published and published[0] == "Story 1"
    first = load_doc(tmp_path)["days"][0]["picks"][0]
    assert first["title"] == "Story 1" and [a["title"] for a in first["also"]] == ["Story 2"]


def test_a_failing_grouper_never_blocks_publishing(tmp_path):
    def broken(ranked):
        raise RuntimeError("jev down")

    selected = run_with(tmp_path, broken)
    assert len(selected) == 8 and all("also" not in p for p in load_doc(tmp_path)["days"][0]["picks"])


def test_scored_json_hook_still_sees_every_item_before_grouping(tmp_path):
    seen = []
    digest, site = dirs(tmp_path)
    run(CFG, "p", [FakeCollector([make_item(n) for n in range(1, 4)])], good_scorer, summarizer, set(), DAY, digest, site, now=NOW,
        grouper=lambda r: assign_groups(r, {(0, 1): 0.9}, 0.5, 5), on_scored=lambda ranked: seen.extend(ranked))
    assert len(seen) == 3


# --- output format ---------------------------------------------------------------------------------------------------


def head_with_also() -> Selected:
    s = sc(1)
    s.also = [
        replace(make_item(2), source="email", title="<b>Second</b> take", url="https://example.org/second"),
        replace(make_item(3), source="x", title="Bad link", url="javascript:alert(1)"),
    ]
    return Selected(s, "pick", "why")


def test_item_dict_lists_related_coverage_safely_and_validates():
    d = _item_dict(head_with_also())
    assert d["also"] == [{"title": "Second take", "url": "https://example.org/second", "source": "email"}]  # html stripped, unsafe URL dropped
    validate({"lastUpdated": "x", "days": [{"date": "2026-10-12", "picks": [d], "notable": []}]})


def test_item_without_related_coverage_has_no_also_key():
    assert "also" not in _item_dict(Selected(sc(1), "pick", "why"))


def test_markdown_digest_mentions_related_coverage():
    md = _md_section(DAY, [head_with_also()])
    assert "Also covered by" in md and "https://example.org/second" in md


def test_config_defaults_for_grouping():
    assert (CFG.group_threshold, CFG.group_shortlist, CFG.group_also_max) == (0.5, 40, 5)

def test_pairs_report_lists_the_likely_matches_with_titles_for_tuning():
    shortlist = [sc(1), sc(2), sc(3)]
    report = pairs_report(shortlist, {(0, 1): 0.9, (0, 2): 0.02, (1, 2): 0.4})
    assert report == [
        {"a": "Story 1", "b": "Story 2", "p": 0.9},
        {"a": "Story 2", "b": "Story 3", "p": 0.4},
    ]  # near-zero pairs are omitted, highest probability first

