"""Same-story grouping with Jev.

Several sources often cover one announcement. After ranking, every pair among the top
`group_shortlist` items is put to Jev as a yes/no question ("do these report the same story?").
Each item then joins the highest-ranked earlier item it matches, or starts a group of its own.
Matching is against group heads only, never through other members, so a chain of loose matches
cannot drag unrelated stories together.

Only heads are selected for publishing; the members ride along as `also` links, so a wrong
match hides nothing. The raw probabilities are returned so the threshold can be re-tuned
without new Jev calls.
"""

from __future__ import annotations

import asyncio
import itertools

from typesafe_sdk import Noul

from akd.config import Config
from akd.models import Scored

DEFAULT_CONCURRENCY = 8
SUMMARY_CHARS = 400

QUESTIONS = {
    "same_story": Noul(
        instructions=(
            "Do `item_a` and `item_b` report the same specific news story: the same announcement, release, "
            "event or finding, even if they come from different outlets, in different wording? "
            "Two different stories about the same company, product or topic are NOT the same story."
        ),
        criteria={
            "true": "Both items cover one and the same underlying announcement, release, event or finding.",
            "false": "They cover different announcements, releases, events or findings, even if the topic overlaps.",
        },
    )
}

Pairs = dict[tuple[int, int], float]


def _view(s: Scored) -> dict:
    return {"source": s.item.source, "title": s.item.title, "summary": s.item.text[:SUMMARY_CHARS]}


async def pair_probabilities(shortlist: list[Scored], client, concurrency: int = DEFAULT_CONCURRENCY) -> Pairs:
    """P(same story) for every unordered pair, keyed by shortlist indices (i < j)."""
    sem = asyncio.Semaphore(concurrency)

    async def one(i: int, j: int) -> tuple[tuple[int, int], float]:
        async with sem:
            response = await client.system_one(
                state={"item_a": _view(shortlist[i]), "item_b": _view(shortlist[j])}, questions=QUESTIONS
            )
        return (i, j), response.nouls["same_story"].noul

    results = await asyncio.gather(*(one(i, j) for i, j in itertools.combinations(range(len(shortlist)), 2)))
    return dict(results)


def assign_groups(ranked: list[Scored], probs: Pairs, threshold: float, also_max: int) -> list[Scored]:
    """Return the group heads in rank order, each carrying its members in `also` (capped at `also_max`)."""
    for s in ranked:
        s.also = []
    heads: list[int] = []
    for j, s in enumerate(ranked):
        best, best_p = None, 0.0
        for i in heads:
            p = probs.get((i, j), 0.0)
            if p >= threshold and (best is None or p > best_p):
                best, best_p = i, p
        if best is None:
            heads.append(j)
        elif len(ranked[best].also) < also_max:
            ranked[best].also.append(s.item)
    return [ranked[i] for i in heads]


def pairs_report(shortlist: list[Scored], probs: Pairs, floor: float = 0.1) -> list[dict]:
    """The likely matches (p >= floor), best first, with titles: what to read when tuning `group_threshold`."""
    rows = [
        {"a": shortlist[i].item.title, "b": shortlist[j].item.title, "p": round(p, 4)}
        for (i, j), p in probs.items()
        if p >= floor
    ]
    return sorted(rows, key=lambda r: -r["p"])


async def group_stories(ranked: list[Scored], cfg: Config, client) -> tuple[list[Scored], Pairs]:
    """Group the top of `ranked`; the rest follows unchanged. Returns (items to select from, raw pair probabilities)."""
    if cfg.group_shortlist < 2 or len(ranked) < 2:
        return ranked, {}
    shortlist, rest = ranked[: cfg.group_shortlist], ranked[cfg.group_shortlist :]
    probs = await pair_probabilities(shortlist, client)
    return assign_groups(shortlist, probs, cfg.group_threshold, cfg.group_also_max) + rest, probs
