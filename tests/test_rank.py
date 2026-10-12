from datetime import datetime, timezone
from pathlib import Path

import pytest

from akd.config import Config, load_config
from akd.models import Item, Scored
from akd.rank import rank, select

ROOT = Path(__file__).resolve().parent.parent
NOW = datetime(2026, 10, 12, tzinfo=timezone.utc)


def cfg(**overrides) -> Config:
    base = load_config(ROOT / "config.yaml")
    return Config(**{**base.__dict__, **overrides})


def scored(n: int, sig=0.5, rel=0.5, act=0.5, nov=0.5, hype=0.0) -> Scored:
    item = Item(f"id{n:03d}", "web", f"T{n}", f"https://e.com/{n}", "x", NOW)
    return Scored(item, "other", {"significance": sig, "relevance": rel, "actionability": act, "novelty": nov}, hype, 0.9)


def test_rank_formula():
    [a] = rank([scored(1, 1, 1, 1, 1, hype=0.0)], cfg())
    assert a.rank == pytest.approx(1.0)
    [b] = rank([scored(2, 1, 1, 1, 1, hype=1.0)], cfg())
    assert b.rank == pytest.approx(0.5)


def test_rank_uses_spec_weights():
    [s] = rank([scored(1, sig=1.0, rel=0.0, act=0.0, nov=0.0)], cfg())
    assert s.rank == pytest.approx(0.45)


def test_weights_change_order_without_rescoring():
    a = scored(1, sig=1.0, rel=0.0)
    b = scored(2, sig=0.0, rel=1.0)
    default = rank([a, b], cfg())
    assert [s.item.id for s in default] == ["id001", "id002"]
    flipped = rank(
        [a, b],
        cfg(weights={"significance": 0.1, "relevance": 0.7, "actionability": 0.1, "novelty": 0.1}),
    )
    assert [s.item.id for s in flipped] == ["id002", "id001"]


def test_tiebreak_is_deterministic():
    items = [scored(3), scored(1), scored(2)]
    assert [s.item.id for s in rank(items, cfg())] == ["id001", "id002", "id003"]
    assert [s.item.id for s in rank(list(reversed(items)), cfg())] == ["id001", "id002", "id003"]


def test_select_caps_picks_at_five():
    ranked = rank([scored(i, sig=0.9, rel=0.9, act=0.9, nov=0.9) for i in range(1, 9)], cfg())
    sel = select(ranked, cfg())
    assert [s.tier for s in sel].count("pick") == 5
    assert [s.tier for s in sel].count("notable") == 3


def test_select_notable_respects_min_rank_and_cap():
    strong = [scored(i, sig=0.9, rel=0.9, act=0.9, nov=0.9) for i in range(1, 6)]
    weak = [scored(i, sig=0.1, rel=0.1, act=0.1, nov=0.1) for i in range(6, 9)]
    sel = select(rank(strong + weak, cfg()), cfg())
    assert len(sel) == 5  # weak ones fall below min_notable_rank
    many = [scored(i, sig=0.6, rel=0.6, act=0.6, nov=0.6) for i in range(1, 30)]
    sel = select(rank(many, cfg()), cfg())
    assert len(sel) == 5 + 10


def test_select_empty_returns_empty():
    assert select(rank([], cfg()), cfg()) == []


def test_slow_day_publishes_fewer_than_five_picks():
    weak = [scored(i, sig=0.1, rel=0.1, act=0.1, nov=0.1) for i in range(1, 4)]
    assert select(rank(weak, cfg()), cfg()) == []
