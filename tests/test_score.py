from datetime import datetime, timezone
from types import SimpleNamespace

import pytest

from akd.levels import CATEGORIES, QUESTIONS
from akd.models import DIMENSIONS, Item
from akd.score import score_items

NOW = datetime(2026, 10, 12, tzinfo=timezone.utc)


def item(n: int = 1) -> Item:
    return Item(f"id{n}", "web", f"Title {n}", f"https://e.com/{n}", "body text", NOW)


def score_answer(score: float, confidence: float = 0.9, levels: int = 5):
    return SimpleNamespace(score=score, confidence=confidence, legend={i: f"L{i}" for i in range(levels)})


def response(sig=3.0, sig_conf=0.9, rel=2.0, act=1.0, nov=4.0, category="dev_tooling", hype=0.1):
    return SimpleNamespace(
        scores={
            "significance": score_answer(sig, sig_conf),
            "relevance": score_answer(rel),
            "actionability": score_answer(act),
            "novelty": score_answer(nov),
        },
        choices={"category": SimpleNamespace(choice=category, confidence=0.8)},
        nouls={"is_hype": SimpleNamespace(noul=hype)},
    )


class FakeClient:
    def __init__(self, responses=None, error=None):
        self.responses = responses or {}
        self.error = error
        self.calls = []

    async def system_one(self, state, questions):
        self.calls.append((state, questions))
        if self.error:
            raise self.error
        return self.responses.get(state["item"]["title"], response())


def test_scores_normalized_to_unit_range():
    [s] = score_items([item()], "profile", FakeClient())
    assert s.scores["significance"] == pytest.approx(0.75)  # 3.0 of 5 levels -> 3/4
    assert s.scores["relevance"] == pytest.approx(0.5)
    assert s.scores["actionability"] == pytest.approx(0.25)
    assert s.scores["novelty"] == pytest.approx(1.0)
    assert set(s.scores) == set(DIMENSIONS)


def test_category_taken_from_choice():
    [s] = score_items([item()], "profile", FakeClient({"Title 1": response(category="research")}))
    assert s.category == "research"


def test_hype_probability_read_from_noul():
    [s] = score_items([item()], "profile", FakeClient({"Title 1": response(hype=0.8)}))
    assert s.hype_p == pytest.approx(0.8)


def test_low_confidence_flag_when_significance_confidence_below_threshold():
    client = FakeClient({"Title 1": response(sig_conf=0.2), "Title 2": response(sig_conf=0.9)})
    a, b = score_items([item(1), item(2)], "profile", client, low_confidence_threshold=0.4)
    assert a.low_confidence is True
    assert b.low_confidence is False
    assert a.confidence == pytest.approx(0.2)


def test_state_carries_item_and_profile_and_all_questions_asked():
    client = FakeClient()
    score_items([item()], "MY PROFILE", client)
    state, questions = client.calls[0]
    assert state["profile"] == "MY PROFILE"
    assert state["item"]["title"] == "Title 1"
    assert set(questions) == {"category", "is_hype", *DIMENSIONS}


def test_results_keep_input_order():
    items = [item(i) for i in range(1, 6)]
    out = score_items(items, "p", FakeClient())
    assert [s.item.id for s in out] == [i.id for i in items]


def test_client_error_propagates():
    with pytest.raises(RuntimeError, match="jev down"):
        score_items([item()], "p", FakeClient(error=RuntimeError("jev down")))


def test_question_definitions_are_well_formed():
    assert len(CATEGORIES) == 7 and "other" in CATEGORIES
    for dim in DIMENSIONS:
        assert len(QUESTIONS[dim].criteria) == 5
    assert set(QUESTIONS["category"].criteria) == set(CATEGORIES)
