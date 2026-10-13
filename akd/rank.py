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
    picks: list[Scored] = []
    per_source: dict[str, int] = {}
    for s in eligible:
        if len(picks) == cfg.max_picks:
            break
        source = s.item.source
        if per_source.get(source, 0) >= cfg.per_source_pick_cap.get(source, cfg.max_picks):
            continue  # this source already filled its share of Top picks; it can still be notable
        picks.append(s)
        per_source[source] = per_source.get(source, 0) + 1
    chosen = {id(s) for s in picks}
    rest = [s for s in eligible if id(s) not in chosen][: cfg.max_notable]
    return [Selected(s, "pick") for s in picks] + [Selected(s, "notable") for s in rest]
