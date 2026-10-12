# AKD (Automated Knowledge Discovery) and the "What's New" tab: Design

Date: 2026-10-11
Status: Draft for review

## 1. Goal

Build AKD, an unattended pipeline that collects the day's AI and coding news, classifies it, ranks it, and publishes the items that matter most to a new **What's New** tab on the personal site (kedarbhumkar.com).

Success: the user opens the tab and sees a short, ranked, categorized, current list without doing anything.

## 2. Decisions made during brainstorming

| Topic | Decision |
|---|---|
| Relationship to existing work | Evolve the existing `kedar-bhumkar/whats-new-digest` routine. It remains the source of truth. |
| What "matters" | Industry significance weighs most; relevance to the user's stack and actionability are secondary signals. |
| Phase 1 sources | Web, GitHub, Reddit. Email digests and X are later, pluggable collectors. |
| Site data delivery | The pipeline commits a JSON file into the site repo; Vercel deploys it. |
| Architecture | Staged pipeline: deterministic collectors, dedupe, LLM judgment, weighted rank, publish. |
| Scoring model | Jev (TypeSafe System One) for classification and scores; Claude only for the short "why it matters" text. |

## 3. Architecture

Runs daily in GitHub Actions in the `whats-new-digest` repo, plus manual trigger.

```
collectors (web, GitHub, Reddit)
  -> normalize + dedupe against already-published items
  -> Jev: category + dimension scores
  -> weighted rank, select Top picks / Also notable
  -> Claude: one-line "why it matters" for selected items
  -> publisher
       -> whats-new.md        (digest repo, existing format preserved)
       -> items.json          (site repo, validated against a schema)
```

### 3.1 Collectors
- One interface: `collect() -> list[Item]`.
- `Item`: `id`, `source`, `title`, `url`, `text`, `published_at`.
- A failing collector is logged and skipped. The run continues.
- Adding email or X later means adding one collector, with no changes to other stages.

### 3.2 Dedupe
- By canonical URL and title similarity, and against items already published.
- Deterministic code only.
- Semantic similarity, if used, must use embeddings, not term overlap. A simpler method must be flagged explicitly.

### 3.3 Judgment (Jev)
One request per item. State is `{item, profile}`. Questions run in parallel:

| Question | Type | Meaning |
|---|---|---|
| `category` | Choice | model/API release, dev tooling, agents/MCP/skills, research, repo/library, industry/business, other |
| `significance` | Score, 5 levels | "minor update or noise" to "shifts how the field works" |
| `relevance` | Score, 5 levels | "unrelated to the profile" to "directly changes something the profile depends on" |
| `actionability` | Score, 5 levels | "just news" to "adoptable this week with a clear first step" |
| `novelty` | Score, 5 levels | "rehash of known news" to "first report" |
| `is_hype` | Noul | marketing or speculation with no substance |

Level descriptions are written as concrete situations. Raw scores, probabilities and confidence are stored per item so re-weighting never re-runs inference.

`profile.yaml` holds the user's stack and interests (Claude Code and Agent SDK, Salesforce/Agentforce, React/Vite/Vercel, AI image and video tooling, TypeSafe) and is passed as state.

### 3.4 Ranking (code, in `config.yaml`)
Scores normalized to 0..1.

```
rank = 0.45*significance + 0.25*relevance + 0.20*actionability + 0.10*novelty
rank *= (1 - 0.5 * P(is_hype))
```

- **Top picks:** highest rank, capped at 5 per day.
- **Also notable:** next ~10 above a minimum rank.
- **Dropped:** stored with scores for debugging, not published.
- Items with low significance confidence are flagged in the data.

### 3.5 Summaries (Claude)
Only for selected items (about 15 per day): a one-line "why it matters". Jev does not generate text.

### 3.6 Publisher
- Appends to `whats-new.md` in the existing format.
- Writes `public/whats-new/items.json` in `ai-arch-showcase` after validating against a JSON schema. A bad run cannot break the page.
- Rolling window of 60 days in the JSON. Older days remain in the markdown history.

## 4. Site: What's New tab (`ai-arch-showcase`)

Follows the existing Daily Software Dose pattern (a route plus a page that fetches a static JSON file).

- Route `/whats-new` in `src/App.tsx`, above the catch-all.
- Page `src/pages/WhatsNew.tsx`, using the shared `Navigation` component, with loading and error states.
- A navigation entry for the tab. Placement needs confirming: the nav currently lists Home anchors and an external link.
- Data file `public/whats-new/items.json`.

Layout:
- Header with last-updated time and counts.
- Top picks band: larger cards with category badge, headline, one-line why, source, link.
- Feed below: reverse-chronological by day, old days collapsed.
- Controls: category filter, search, toggle "Top picks only" / "All notable".
- Optional "details" expander showing per-dimension scores. Hidden by default.

JSON shape: per day `date`, `picks[]`, `notable[]`. Per item `id`, `title`, `url`, `source`, `category`, `why`, `rank`, `scores{}`, `flags{}`.

## 5. Repository layout (`whats-new-digest/akd/`)

- `collectors/` (`web.py`, `github.py`, `reddit.py`)
- `dedupe.py`, `score.py`, `rank.py`, `summarize.py`, `publish.py`
- `profile.yaml`, `config.yaml`
- `tests/` with recorded fixtures

A thin Claude skill wraps it: `/akd run`, `/akd tune` (show the scored sample), `/akd add-source`.

## 6. Testing

- Unit tests: dedupe, ranking math, publisher schema validation.
- Recorded fixtures per collector. Tests never hit the network.
- Dry-run mode writes to a local folder instead of the repos.
- Tuning sample: the first real run prints the top and bottom 20 with scores for the user to review. Importance has no ground truth, so this is the quality check. Weights and level descriptions are tuned from it.

## 7. Operations

- Schedule: daily GitHub Actions cron plus manual trigger.
- Secrets in GitHub Actions: `TYPESAFE_API_KEY`, an Anthropic API key, and a fine-grained GitHub token scoped to the two repos. None in client code.
- If Jev is unavailable, the run fails loudly and publishes nothing, rather than publishing unranked items.
- Cost is expected to be small: Jev calls are cheap (the reranking cookbook cites about $0.06 for 1,200 calls); Claude is used for about 15 summaries a day.
- Git hygiene: files are staged by explicit path, with `git status` checked before each commit. The site repo is public, so published content is audited for secrets and sensitive content.

## 8. Rollout

1. Collectors, dedupe and Jev scoring in dry-run. The user reviews the scored sample and weights are tuned.
2. The site tab with real data, on a Vercel preview.
3. Enable the daily publish. The old routine runs in parallel for a week, then is retired or kept as a fallback.
4. Later phases: email digests via a dedicated inbox, then X.

## 9. Risks and open items

- Source rate limits or format changes (Reddit, web). Mitigated by per-collector isolation.
- Initial weights are a guess until reviewed against the sample.
- Re-ranking can only reorder what collectors gathered, so collector coverage limits quality.
- Navigation placement of the new tab is unconfirmed.
- Email (scheduled routines cannot use interactive connectors) and X (paid or fragile API access) are deferred and need their own designs.
- Jev model behavior should be validated on this domain; typed output guarantees the interface, not truth.
