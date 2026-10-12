"""Weighted ranking and selection. Pure code: weights live in config.yaml, so changing
them never re-runs inference."""

from __future__ import annotations

from akd.config import Config
from akd.models import Scored, Selected


def rank(scored: list[Scored], cfg: Config) -> list[Scored]:
    for s in scored:
        base = sum(cfg.weights[dim] * s.scores[dim] for dim in cfg.weights)
        s.rank = base * (1 - cfg.hype_penalty * s.hype_p)
    return sorted(scored, key=lambda s: (-s.rank, s.item.id))


def select(ranked: list[Scored], cfg: Config) -> list[Selected]:
    # The rank floor applies to picks too: a slow news day shows fewer items rather than filler.
    eligible = [s for s in ranked if s.rank >= cfg.min_notable_rank]
    picks = [Selected(s, "pick") for s in eligible[: cfg.max_picks]]
    notable = [Selected(s, "notable") for s in eligible[cfg.max_picks :][: cfg.max_notable]]
    return picks + notable
