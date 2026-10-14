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


def _limit_per_source(candidates: list[Scored], cap: int) -> list[Scored]:
    """Keep at most `cap` items per source (0 = unlimited). A source over its cap keeps the items most
    relevant to the reader's profile, not merely the highest ranked; the result stays in rank order."""
    if cap <= 0:
        return candidates
    by_source: dict[str, list[Scored]] = {}
    for s in candidates:
        by_source.setdefault(s.item.source, []).append(s)
    keep: set[int] = set()
    for group in by_source.values():
        # `group` is in rank order, so on equal relevance the better-ranked item wins (sort is stable).
        keep.update(id(s) for s in sorted(group, key=lambda s: -s.scores["relevance"])[:cap])
    return [s for s in candidates if id(s) in keep]


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
    rest = _limit_per_source([s for s in eligible if id(s) not in chosen], cfg.max_notable_per_source)[: cfg.max_notable]
    return [Selected(s, "pick") for s in picks] + [Selected(s, "notable") for s in rest]
