# AKD "What's New" Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A daily unattended pipeline that collects AI/coding news from web, GitHub and Reddit, scores and ranks it with Jev, and publishes the top items to a new What's New tab on the personal site.

**Architecture:** A Python package `akd/` in `kedar-bhumkar/whats-new-digest` runs as a GitHub Actions cron: collectors, then dedupe, then Jev judgment, then weighted rank, then Claude summaries, then a publisher that writes `whats-new.md` (digest repo) and `public/whats-new/items.json` (site repo `kedar-bhumkar/ai-arch-showcase`). The site gets a `/whats-new` page modeled on `DailySoftwareDose.tsx`.

**Tech Stack:** Python 3.12, pytest, `typesafe-sdk` (Jev), `anthropic` SDK, `httpx`, `feedparser`, `jsonschema`, `pyyaml`, GitHub Actions; site side: Vite, React, TypeScript, Tailwind.

**Spec:** `docs/superpowers/specs/2026-10-11-akd-whats-new-design.md`

## Global Constraints

- Phase 1 sources are web, GitHub and Reddit only. Email and X are out of scope.
- Rank formula: `0.45*significance + 0.25*relevance + 0.20*actionability + 0.10*novelty`, scores normalized to 0..1, then `rank *= (1 - 0.5*P(is_hype))`. Weights live in `config.yaml`, never hardcoded.
- Top picks capped at 5/day; Also notable about 10 above a minimum rank; the rest are dropped (stored, not published).
- JSON window: rolling 60 days. `whats-new.md` existing format preserved; AKD only prepends a new dated section.
- Jev gives typed judgments only. Claude writes the one-line "why it matters", only for selected items (about 15/day). No text generation by Jev.
- If Jev is unavailable the run fails loudly and publishes nothing (never publish unranked items).
- Publisher validates `items.json` against a JSON schema before any commit.
- Secrets only in GitHub Actions: `TYPESAFE_API_KEY`, `ANTHROPIC_API_KEY`, and a fine-grained token scoped to the two repos. None in client code.
- Semantic dedupe, if used, must use embeddings. Any simpler method must be flagged explicitly in code and docs.
- Git hygiene: stage files by explicit path; run `git status` before each commit. The site repo is public: audit published content for secrets or sensitive content.
- Preserve each file's existing line endings (Windows, CRLF) when editing existing files.
- Tests never hit the network; collectors are tested against recorded fixtures.

## Review Focus

- Empty day (every collector returns zero items): publishes nothing, exits 0, existing JSON untouched.
- Two collectors return the same story under different URLs (tracking params, `www.`, trailing slash): collapse to one item.
- An item already published yesterday reappears today: not published again.
- A Jev response with low confidence or all-equal scores: still ranks deterministically (stable tiebreak), flagged `low_confidence`.
- Item text containing HTML or script markup: escaped or stripped before it reaches the site JSON; the page renders it as text.
- Re-running the same day twice: idempotent, no duplicate day block in JSON or markdown.

---

## File Structure

In `whats-new-digest` (new, under `akd/`):
- `akd/models.py`: `Item`, `Scored`, `Selected` dataclasses.
- `akd/config.py`: loads `config.yaml` and `profile.yaml`.
- `akd/collectors/base.py`, `github.py`, `reddit.py`, `web.py`: one source each.
- `akd/dedupe.py`: canonical URLs and filtering.
- `akd/score.py`: Jev judgment.
- `akd/rank.py`: weighted rank and selection.
- `akd/summarize.py`: Claude one-liners.
- `akd/publish.py`: JSON merge, schema validation, markdown prepend.
- `akd/schema/items.schema.json`
- `akd/pipeline.py` and `akd/cli.py`: orchestration, `--dry-run`, `tune`.
- `config.yaml`, `profile.yaml`, `.github/workflows/akd.yml`, `tests/`.

In `ai-arch-showcase`: `src/pages/WhatsNew.tsx`, `src/App.tsx` (route), nav entry, `public/whats-new/items.json` (seed).

---

### Task 1: Scaffold, models and config

**Files:**
- Create: `akd/__init__.py`, `akd/models.py`, `akd/config.py`, `config.yaml`, `profile.yaml`, `pyproject.toml`, `tests/test_config.py`

**Interfaces:**
- Produces:
  - `Item(id: str, source: str, title: str, url: str, text: str, published_at: datetime)`
  - `Scored(item: Item, category: str, scores: dict[str, float], hype_p: float, confidence: float, rank: float = 0.0, low_confidence: bool = False)` where `scores` keys are `significance|relevance|actionability|novelty`, each normalized 0..1
  - `Selected(scored: Scored, tier: Literal["pick","notable"], why: str = "")`
  - `load_config(path: Path) -> Config`, with `Config.weights: dict[str, float]`, `.max_picks: int`, `.max_notable: int`, `.min_notable_rank: float`, `.hype_penalty: float`, `.window_days: int`, `.subreddits: list[str]`, `.feeds: list[str]`, `.github_topics: list[str]`
  - `load_profile(path: Path) -> str` (the profile as text passed to Jev as state)

- [ ] **Step 1: Write the failing test** `test_load_config_defaults`: write a `config.yaml` with the spec's weights to `tmp_path`; assert `weights == {"significance":0.45,"relevance":0.25,"actionability":0.20,"novelty":0.10}`, `max_picks == 5`, `max_notable == 10`, `hype_penalty == 0.5`, `window_days == 60`. Add `test_weights_must_sum_to_one`: weights summing to 0.9 raise `ValueError`.
- [ ] **Step 2: Run** `pytest tests/test_config.py -v`. Expected: FAIL (module missing).
- [ ] **Step 3: Implement** models and config per the Interfaces block. Seed `profile.yaml` with: Claude Code and Agent SDK, Salesforce/Agentforce, React/Vite/Vercel, AI image and video tooling (ComfyUI, HyperFrames), TypeSafe/Jev. Seed `config.yaml` with the spec's values and an initial list of subreddits (`LocalLLaMA`, `ClaudeAI`, `MachineLearning`, `programming`), feeds, and GitHub topics.
- [ ] **Step 4: Run** the tests. Expected: PASS.
- [ ] **Step 5: Commit** with explicit paths.

### Task 2: Dedupe

**Files:**
- Create: `akd/dedupe.py`, `tests/test_dedupe.py`

**Interfaces:**
- Consumes: `Item`
- Produces:
  - `canonical_url(url: str) -> str`: lowercase host, strip `www.`, tracking params (`utm_*`, `ref`, `fbclid`), fragment, trailing slash
  - `dedupe(items: list[Item], published_ids: set[str]) -> list[Item]`: drops items whose canonical URL appears earlier in the list or whose id is in `published_ids`; keeps the first occurrence
  - `item_id(url: str) -> str`: stable hash of the canonical URL

- [ ] **Step 1: Write failing tests:** `test_canonical_url_strips_tracking` (`https://www.Example.com/a/?utm_source=x#frag` equals `https://example.com/a`); `test_dedupe_collapses_variants` (two items with variant URLs return one); `test_dedupe_skips_already_published`; `test_dedupe_empty_list_returns_empty`.
- [ ] **Step 2: Run** and expect FAIL. **Step 3: Implement.** Use URL-only dedupe in this task and mark in the module docstring that near-duplicate title matching is not implemented. If added later it must use embeddings. **Step 4: Run** and expect PASS. **Step 5: Commit.**

### Task 3: Collectors (GitHub, Reddit, web)

**Files:**
- Create: `akd/collectors/base.py`, `github.py`, `reddit.py`, `web.py`, `tests/fixtures/{github,reddit,web}.json|xml`, `tests/test_collectors.py`

**Interfaces:**
- Consumes: `Item`, `Config`, `item_id`
- Produces: `class Collector(Protocol): name: str; def collect(self) -> list[Item]`. Each collector takes an injected `httpx.Client` so tests can mock transport.
  - `GitHubCollector(cfg, client)`: GitHub search API for recently pushed repos by topic and star velocity, plus release feeds of a configured watchlist (e.g. `anthropics/claude-code`)
  - `RedditCollector(cfg, client)`: each subreddit's `top.json?t=day`
  - `WebCollector(cfg, client)`: configured RSS/Atom feeds via `feedparser`
  - `collect_all(collectors: list[Collector]) -> list[Item]`: runs each, catches and logs exceptions per collector, never raises

- [ ] **Step 1: Write failing tests** from recorded fixtures: each collector maps its fixture to the expected `Item` fields (assert count, first title, url, source name); `test_collect_all_isolates_failures` (one collector raising does not stop the others); `test_html_in_text_is_stripped` (a fixture with `<script>` in the body yields text without tags).
- [ ] **Step 2: Run** and expect FAIL. **Step 3: Implement** the collectors. Record the fixtures once from real responses, with secrets removed. Reddit requires a descriptive `User-Agent`. **Step 4: Run** and expect PASS. **Step 5: Commit.**

### Task 4: Jev scoring

**Files:**
- Create: `akd/score.py`, `akd/levels.py`, `tests/test_score.py`

**Interfaces:**
- Consumes: `Item`, profile text, a `TypeSafeClient` (injected)
- Produces: `score_items(items: list[Item], profile: str, client) -> list[Scored]`; `levels.py` holds the question definitions (`category` Choice with the 7 categories from the spec; `significance`, `relevance`, `actionability`, `novelty` as 5-level Scores with concrete-situation descriptions; `is_hype` as Noul).

- [ ] **Step 1: Write failing tests** with a fake client returning canned responses: `test_scores_normalized_to_unit_range` (Score 3.0 of 4 levels, normalized by `len(legend)-1`, equals 0.75); `test_category_taken_from_choice`; `test_hype_probability_read_from_noul`; `test_low_confidence_flag_when_significance_confidence_below_threshold`; `test_client_error_propagates` (the pipeline must fail loudly; assert the exception is not swallowed).
- [ ] **Step 2: Run** and expect FAIL.
- [ ] **Step 3: Implement.** One `client.system_one(state={"item":..., "profile":...}, questions=...)` call per item, run concurrently with `AsyncTypeSafeClient` and a semaphore. Verify the exact response shape (`response.scores[name].score`, `.confidence`, `response.choices[name].choice`, `response.nouls[name]`) against the live docs at https://docs.typesafe.ai/sdk/python.md and https://docs.typesafe.ai/primitives/noul.md before coding. In particular, confirm whether `.noul` is a probability. Write each level description as a concrete situation.
- [ ] **Step 4: Run** and expect PASS. **Step 5: Commit.**
- [ ] **Step 6 (manual, needs `TYPESAFE_API_KEY`):** run `score_items` on 5 real items and eyeball the output.

### Task 5: Ranking and selection

**Files:**
- Create: `akd/rank.py`, `tests/test_rank.py`

**Interfaces:**
- Consumes: `Scored`, `Config`
- Produces: `rank(scored: list[Scored], cfg: Config) -> list[Scored]` (sets `.rank`, sorted descending, stable tiebreak by `item.id`); `select(ranked: list[Scored], cfg: Config) -> list[Selected]` (first `max_picks` are `pick`; next `max_notable` with `rank >= min_notable_rank` are `notable`)

- [ ] **Step 1: Write failing tests:** `test_rank_formula` (scores 1,1,1,1 and hype 0 give 1.0; the same with hype 1 gives 0.5); `test_weights_change_order_without_rescoring`; `test_tiebreak_is_deterministic`; `test_select_caps_picks_at_five`; `test_select_notable_respects_min_rank`.
- [ ] **Step 2: Run** and expect FAIL. **Step 3: Implement** using the weights and hype penalty from config. **Step 4: Run** and expect PASS. **Step 5: Commit.**

### Task 6: Summaries (Claude)

**Files:**
- Create: `akd/summarize.py`, `tests/test_summarize.py`

**Interfaces:**
- Consumes: `Selected`, an Anthropic client (injected)
- Produces: `summarize(selected: list[Selected], client) -> list[Selected]` filling `.why` with one sentence of at most 200 characters

- [ ] **Step 1: Write failing tests** with a fake client: `test_fills_why_for_every_selected`; `test_why_truncated_to_200_chars`; `test_failure_leaves_why_empty_and_continues` (a failed call for one item must not drop the item; the page falls back to the title).
- [ ] **Step 2: Run** and expect FAIL. **Step 3: Implement.** Use a Haiku-class model (look up the current model ID with the claude-api skill before coding). The prompt gets the item text and the profile and asks for why it matters, without hype. **Step 4: Run** and expect PASS. **Step 5: Commit.**

### Task 7: Publisher and schema

**Files:**
- Create: `akd/publish.py`, `akd/schema/items.schema.json`, `tests/test_publish.py`

**Interfaces:**
- Consumes: `Selected`, `Config`
- Produces:
  - `merge_day(existing: dict, day: date, selected: list[Selected], window_days: int) -> dict`: replaces any existing block for `day` (idempotent), trims to the window, sorts newest first
  - `validate(doc: dict) -> None` (raises `jsonschema.ValidationError`)
  - `prepend_markdown(md: str, day: date, selected: list[Selected]) -> str`: inserts a `## YYYY-MM-DD` section directly under the intro, in the existing entry style (title, why, link)
  - `write_outputs(selected, day, digest_dir: Path, site_dir: Path, dry_run: bool)`: writes only if validation passes

JSON shape per spec: `{"lastUpdated", "days":[{"date","picks":[Item...],"notable":[Item...]}]}` with Item = `id,title,url,source,category,why,rank,scores,flags`.

- [ ] **Step 1: Write failing tests:** `test_merge_day_is_idempotent`; `test_merge_trims_to_60_days`; `test_invalid_doc_rejected_and_nothing_written`; `test_markdown_prepend_keeps_existing_entries`; `test_text_is_sanitized` (`<script>` in `why` or `title` is escaped in output); `test_empty_selection_writes_nothing`.
- [ ] **Step 2: Run** and expect FAIL. **Step 3: Implement.** Escape HTML in all string fields. **Step 4: Run** and expect PASS. **Step 5: Commit.**

### Task 8: Pipeline and CLI

**Files:**
- Create: `akd/pipeline.py`, `akd/cli.py`, `tests/test_pipeline.py`

**Interfaces:**
- Consumes: everything above
- Produces: `run(cfg, profile, collectors, jev, claude, published_ids, day, out) -> list[Selected]`; CLI `python -m akd.cli run [--dry-run] [--out DIR]` and `python -m akd.cli tune` (prints the top 20 and bottom 20 with per-dimension scores)

- [ ] **Step 1: Write failing tests** with fakes: `test_end_to_end_dry_run_writes_expected_files`; `test_empty_day_exits_cleanly_and_writes_nothing`; `test_jev_failure_aborts_and_writes_nothing`; `test_second_run_same_day_is_idempotent`.
- [ ] **Step 2: Run** and expect FAIL. **Step 3: Implement.** Published ids come from the existing `items.json`. `--dry-run` writes to a local folder. **Step 4: Run** and expect PASS. **Step 5: Commit.**

### Task 9: GitHub Actions workflow

**Files:**
- Create: `.github/workflows/akd.yml`

- [ ] **Step 1:** Define triggers: `schedule` daily and `workflow_dispatch`. Steps: checkout, set up Python, install, `pytest`, `python -m akd.cli run`. Secrets: `TYPESAFE_API_KEY`, `ANTHROPIC_API_KEY`, `SITE_REPO_TOKEN` (fine-grained, contents write on `ai-arch-showcase`).
- [ ] **Step 2: Commit** the workflow. **Step 3 (user action):** add the three secrets in the repo settings. **Step 4:** trigger `workflow_dispatch` with `--dry-run` first; expected: green run and artifacts uploaded, no pushes to either repo.
- [ ] **Step 5:** Before enabling the real push, confirm the push step stages only `whats-new.md` and `public/whats-new/items.json` by explicit path.

### Task 10: Site page (in `ai-arch-showcase`)

**Files:**
- Create: `src/pages/WhatsNew.tsx`, `public/whats-new/items.json` (seed with 2 hand-written items for the preview)
- Modify: `src/App.tsx` (add `<Route path="/whats-new" element={<WhatsNew />} />` above the catch-all), `src/components/Navigation.tsx` (add the entry)

**Interfaces:**
- Consumes: the `items.json` shape from Task 7
- Produces: a page at `/whats-new` with header (last updated, counts), Top picks band, day-grouped feed with old days collapsed, category filter, search box, "Top picks only / All notable" toggle, and a score-details expander. It shows loading and error states, and renders all strings as text (no `dangerouslySetInnerHTML`).

- [ ] **Step 1:** Read `DailySoftwareDose.tsx` and `Navigation.tsx` and follow their patterns. Check how the nav lists pages; this resolves the open placement item in the spec.
- [ ] **Step 2:** Implement the page and route. **Step 3:** `npm run build` (expect success) and `npm run lint`.
- [ ] **Step 4:** Run `npm run dev` and open `/whats-new` in a browser. Verify the seed items render, the filter and toggle work, an empty file shows an empty state, and a missing file shows the error state. Check at phone width too.
- [ ] **Step 5: Commit** by explicit paths. The preview deploy comes from the Vercel branch build.

### Task 11: Tuning, rollout and skill wrapper

**Files:**
- Create: `skills/akd/SKILL.md` (in the digest repo, installable to `~/.claude/skills/akd`)

- [ ] **Step 1:** Run `python -m akd.cli tune` on real data. Present the top and bottom 20 with scores to the user; record their agree/disagree marks. Adjust weights in `config.yaml` and level descriptions in `levels.py`, then re-run until the user is satisfied.
- [ ] **Step 2:** Write `SKILL.md` with `/akd run` (manual workflow dispatch), `/akd tune`, and `/akd add-source` (instructions for adding a collector). Keep it short.
- [ ] **Step 3:** Enable the real push. Watch the first scheduled run end to end, then check the live tab and Vercel deploy.
- [ ] **Step 4:** Run the old digest routine in parallel for one week, then retire it or keep it as a fallback (user decision).
- [ ] **Step 5:** Tell the user that a newly installed global skill requires restarting already-open sessions, and verify it in a fresh session.
