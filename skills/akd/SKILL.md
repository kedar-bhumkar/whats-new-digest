---
name: akd
description: Automated Knowledge Discovery for the What's New tab. Use when the user says "akd", asks to run, tune, or extend the daily AI/coding news pipeline, re-rank what's new, add a news source, or check why an item was or wasn't surfaced.
---

# AKD: Automated Knowledge Discovery

A daily pipeline (repo `kedar-bhumkar/whats-new-digest`, package `akd/`) that collects AI and coding news from web feeds, GitHub and Reddit, scores each item with Jev (significance, relevance, actionability, novelty, hype, category), ranks it in code, and publishes the best to the site's What's New tab (`public/whats-new/items.json` in `kedar-bhumkar/ai-arch-showcase`) and to `whats-new.md`.

## Commands (run from the digest repo checkout, with the venv active)

- **Run manually (safe):** `gh workflow run akd.yml -R kedar-bhumkar/whats-new-digest -f dry_run=true`. Output is an Actions artifact; nothing is pushed.
- **Run for real:** same with `-f dry_run=false`. This pushes to both repos: confirm with the user first.
- **Tune weights:** `python -m akd.cli tune --top 20` scores a live sample (calls Jev) and caches raw scores in `out/scored.json`. Then edit `weights` in `config.yaml` and re-rank for free with `python -m akd.cli tune --from-cache`.
- **Local dry run:** `python -m akd.cli run --dry-run` writes to `out/` and touches neither repo.

## Where things live

- `config.yaml`: weights, caps (5 picks, ~10 notable), freshness window (`max_age_days`), subreddits, feeds, GitHub topics and watchlist.
- `profile.yaml`: the reader's stack and interests, passed to Jev so "relevance" is personal. Edit it when focus changes.
- `akd/levels.py`: the Jev question wording and level descriptions. Tune these from the sample, not by guesswork.

## Add a source

1. Create `akd/collectors/<name>.py` with a class that has `name` and `collect() -> list[Item]` (see `web.py`).
2. Test it against a recorded fixture in `tests/fixtures/`: tests never hit the network.
3. Register it in `_collectors()` in `akd/cli.py` and add its `source` value to the enum in `akd/schema/items.schema.json`.
Email and X are deliberately not built yet (email needs a non-interactive path; X needs paid or fragile access).

## Rules

- Jev scores; Claude only writes the one-line "why it matters". If Jev fails, the run fails and publishes nothing.
- Stage files by explicit path; the site repo is public.
