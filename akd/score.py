"""Jev judgment: one System One request per item, all questions in parallel.

Raw judgments are normalized to 0..1 and kept on `Scored`; weighting happens later in
rank.py so changing weights never re-runs inference. Client errors propagate: the run
must fail loudly rather than publish unranked items.
"""

from __future__ import annotations

import asyncio

from akd.levels import QUESTIONS
from akd.models import DIMENSIONS, Item, Scored

DEFAULT_CONCURRENCY = 8


def _state(item: Item, profile: str) -> dict:
    return {
        "item": {
            "source": item.source,
            "title": item.title,
            "url": item.url,
            "text": item.text,
            "published_at": item.published_at.isoformat(),
        },
        "profile": profile,
    }


def _to_scored(item: Item, response, low_confidence_threshold: float) -> Scored:
    scores: dict[str, float] = {}
    for dim in DIMENSIONS:
        answer = response.scores[dim]
        top_level = len(answer.legend) - 1
        scores[dim] = answer.score / top_level
    significance_confidence = response.scores["significance"].confidence
    return Scored(
        item=item,
        category=response.choices["category"].choice,
        scores=scores,
        hype_p=response.nouls["is_hype"].noul,
        confidence=significance_confidence,
        low_confidence=significance_confidence < low_confidence_threshold,
    )


async def score_items_async(
    items: list[Item],
    profile: str,
    client,
    low_confidence_threshold: float = 0.4,
    concurrency: int = DEFAULT_CONCURRENCY,
) -> list[Scored]:
    sem = asyncio.Semaphore(concurrency)

    async def one(item: Item) -> Scored:
        async with sem:
            response = await client.system_one(state=_state(item, profile), questions=QUESTIONS)
        return _to_scored(item, response, low_confidence_threshold)

    return list(await asyncio.gather(*(one(i) for i in items)))


def score_items(
    items: list[Item],
    profile: str,
    client,
    low_confidence_threshold: float = 0.4,
    concurrency: int = DEFAULT_CONCURRENCY,
) -> list[Scored]:
    """Sync wrapper. `client` is an `AsyncTypeSafeClient` (or anything with an async `system_one`)."""
    return asyncio.run(score_items_async(items, profile, client, low_confidence_threshold, concurrency))
