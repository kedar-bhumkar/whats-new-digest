"""Orchestration: collect -> dedupe -> score (Jev) -> rank -> select -> summarize -> publish.

Scoring and summarizing are injected callables so client lifecycles live in the CLI and
the pipeline stays testable. A scorer error propagates: nothing is published unranked.
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from akd.collectors.base import Collector, collect_all
from akd.config import Config
from akd.dedupe import dedupe
from akd.models import DIMENSIONS, Item, Scored, Selected
from akd.publish import write_outputs
from akd.rank import rank, select

log = logging.getLogger("akd.pipeline")

Scorer = Callable[[list[Item], str], list[Scored]]
Summarizer = Callable[[list[Selected], str], list[Selected]]


def published_ids_from(doc: dict, exclude_day: date) -> set[str]:
    """Ids already published on earlier days. The day being (re)run is excluded so a
    rerun recomputes that whole day instead of losing its earlier items."""
    ids: set[str] = set()
    for day in doc.get("days", []):
        if day["date"] == exclude_day.isoformat():
            continue
        ids.update(i["id"] for i in day.get("picks", []) + day.get("notable", []))
    return ids


def filter_fresh(items: list[Item], now: datetime, max_age_days: int) -> list[Item]:
    """Drop items older than the window. Some feeds return their whole archive."""
    cutoff = now - timedelta(days=max_age_days)
    return [i for i in items if i.published_at >= cutoff]


def rank_all(scored: list[Scored], cfg: Config) -> list[Scored]:
    return rank(scored, cfg)


def run(
    cfg: Config,
    profile: str,
    collectors: list[Collector],
    scorer: Scorer,
    summarizer: Summarizer,
    published_ids: set[str],
    day: date,
    digest_dir: Path,
    site_dir: Path,
    now: datetime | None = None,
) -> list[Selected]:
    now = now or datetime.now(timezone.utc)
    items = dedupe(filter_fresh(collect_all(collectors), now, cfg.max_age_days), published_ids)
    log.info("%d new items after freshness filter and dedupe", len(items))
    if not items:
        return []
    ranked = rank_all(scorer(items, profile), cfg)
    selected = select(ranked, cfg)
    if not selected:
        log.info("nothing above the rank floor; publishing nothing")
        return []
    selected = summarizer(selected, profile)
    write_outputs(selected, day, digest_dir, site_dir, cfg.window_days, now)
    return selected


def format_tune(ranked: list[Scored], n: int = 20) -> str:
    """Human-readable top/bottom sample for weight tuning."""

    def line(i: int, s: Scored) -> str:
        dims = " ".join(f"{d[:3]}={s.scores[d]:.2f}" for d in DIMENSIONS)
        flag = " LOWCONF" if s.low_confidence else ""
        return f"{i:>3}. {s.rank:.3f} [{s.category}] {s.item.title[:70]} ({s.item.source}) {dims} hype={s.hype_p:.2f}{flag}"

    top = ranked[:n]
    bottom = ranked[-n:] if len(ranked) > n else []
    out = [f"TOP {len(top)} of {len(ranked)}"]
    out += [line(i, s) for i, s in enumerate(top, 1)]
    if bottom:
        out += ["", f"BOTTOM {len(bottom)}"]
        out += [line(len(ranked) - len(bottom) + i, s) for i, s in enumerate(bottom, 1)]
    return "\n".join(out)
