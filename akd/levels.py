"""Jev question definitions. Level descriptions are concrete situations, per the
TypeSafe Score guidance; tune them from the `tune` sample, not by guesswork."""

from __future__ import annotations

from typesafe_sdk import Choice, Noul, Score

CATEGORIES = {
    "model_release": "A new or updated AI model, model version, pricing change or model-level capability announcement.",
    "dev_tooling": "A release or change of a developer tool, CLI, IDE integration, SDK, framework or API (not a model).",
    "agents_mcp_skills": "Agent frameworks, MCP servers, skills, plugins, orchestration or agent-safety/sandboxing tooling.",
    "research": "A paper, benchmark, evaluation, or technical analysis advancing understanding or capability.",
    "repo_library": "A new or trending open-source repository or library, mainly notable as something to adopt or study.",
    "industry_business": "Company, market, policy, funding, partnership or regulatory news.",
    "other": "None of the above fits.",
}

_ITEM = "`item` (a news item with title, source, url and text)"

QUESTIONS = {
    "category": Choice(
        instructions=f"Which kind of news is {_ITEM}?",
        criteria=CATEGORIES,
    ),
    "significance": Score(
        instructions=f"How significant is {_ITEM} for the AI and software-engineering field as a whole, regardless of who is reading?",
        criteria=[
            "Routine or trivial: a minor patch release, a small tutorial, an opinion post, or a rehash of known facts.",
            "Useful but narrow: a modest feature, a small library, or an incremental improvement that matters to a small group.",
            "Notable: a meaningful release or finding that many practitioners will want to know about this month.",
            "Major: a flagship model or tool launch, a widely applicable technique, or a change that many teams must respond to.",
            "Field-shifting: changes how the field works, such as a new model generation, a new standard, or a breakthrough that makes earlier approaches obsolete.",
        ],
    ),
    "relevance": Score(
        instructions="How relevant is `item` to this reader, given `profile` (their stack, interests and exclusions)?",
        criteria=[
            "Unrelated to anything in the profile, or squarely inside its not_interested list.",
            "Loosely related: same broad field but no tool, language or workflow the reader uses.",
            "Adjacent: concerns a technology the reader touches occasionally or a close alternative to what they use.",
            "Directly relevant: concerns a tool, platform or topic listed in the profile's stack or interests.",
            "Critical: changes, breaks or substantially improves something the profile depends on every day.",
        ],
    ),
    "actionability": Score(
        instructions="How actionable is `item` for the reader: could they use it, adopt it, or must they respond to it?",
        criteria=[
            "Pure news: nothing the reader can do with it.",
            "Awareness only: worth knowing, but no concrete step follows.",
            "Worth evaluating: a tool, repo or technique to try when time allows, with an unclear first step.",
            "Adoptable soon: has a clear install or usage path and a plausible benefit within weeks.",
            "Act now: can be adopted this week with an obvious first step, or requires action to avoid breakage.",
        ],
    ),
    "novelty": Score(
        instructions="How new is the information in `item` compared with what has been widely reported?",
        criteria=[
            "Rehash: restates earlier announcements or common knowledge.",
            "Follow-up: adds a little detail to something already widely covered.",
            "Fresh angle: a new analysis or data point on a known topic.",
            "New: reports something not previously covered by mainstream outlets.",
            "First report: the primary source of a new release, finding or announcement.",
        ],
    ),
    "is_hype": Noul(
        instructions=(
            "Is `item` mostly marketing, speculation or vague claims with no verifiable technical substance "
            "(no release, no data, no code, no concrete capability)?"
        ),
    ),
}
