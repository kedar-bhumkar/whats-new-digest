# What's New Digest

Daily digest of AI/Claude tooling advances and vetted GitHub repos. Newest entry first. Maintained by a scheduled routine.

## 2026-10-07

- **Claude Code v2.1.292** (AI/Claude tooling) - Released Oct 6 (also v2.1.290 Oct 5, v2.1.291 Oct 6 regression fixes, per the GitHub release page).
  - Why it matters: Adds an `effort` parameter on the Agent tool so you can set sub-agent effort per call (cheap sub-agents for search, heavier for design), `claude plugin install --marketplace <source>`, a `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` retry knob, and security fixes for file-read access and permission prompts. 2.1.290 added `claude attach <name>` / `claude logs <name>` for background sessions.
  - Link: https://github.com/anthropics/claude-code/releases

- **Leviathan** (GitHub repo) - Single static Rust binary that turns JSONL/JSON/CSV/SQLite records into a ranked BM25 full-text index, with MCP and Claude skill integration, so agents query large datasets without grepping them.
  - Why it matters: A token-saving retrieval step for agents working over big logs or exports. README claims median ~436 tokens per query vs 107K+ with grep (vendor claim, not verified).
  - Link: https://github.com/elstongun/leviathan
  - Safety note: Apache-2.0; created Oct 5, ~650 stars, only 5 commits and very new; described as read-only, offline and `unsafe`-free; install via `cargo install leviathan-index` or release binaries. I read the README only, not the source. Review before use.

- **mesh-avatar-studio** (GitHub repo) - Turns one illustration into an animated 2D mesh avatar using a coding agent plus a local editor, with camera face tracking, lip-sync and OBS output.
  - Why it matters: A concrete pattern of an agent producing an asset that a human then refines in a purpose-built local editor. Useful reference if you build agent-plus-editor workflows.
  - Link: https://github.com/shinshin86/mesh-avatar-studio
  - Safety note: MIT for code (the bundled sample character has separate usage terms); 47 commits; created Oct 4, ~440 stars; plain `npm install && npm run dev` on Node 22.17+. I did not audit the source or check last-commit date beyond the Oct 7 repo update.

Not included: repos whose primary pages I did not vet (e.g. several skill-pack repos trending with 600-1900 stars), and universal-modder / jevgrep, already covered Oct 6.

## 2026-10-06

- **Claude Code v2.1.290 / v2.1.291** (AI/Claude tooling) - Latest releases (Oct 5-6 per the GitHub release page).
  - Why it matters: 2.1.290 adds `claude attach <name>` / `claude logs <name>` for background sessions, an `agentId` on plugin-hook `tool.check` events, org-level approval `ceiling` for permission prompts, and fixes WebFetch silently dropping page text past 100k chars and plan-mode approving non-read-only connector tools. 2.1.291 fixes regressions that could drop cloud-session permission answers and lose final messages on quit. Upgrade if you run cloud sessions.
  - Link: https://github.com/anthropics/claude-code/releases

- **Jev by TypeSafe AI** (AI/Claude tooling) - "System One" decision model: takes text plus typed questions and returns yes/no probabilities, one option from a fixed list, or a scale position, never free text.
  - Why it matters: Could replace prompt-and-parse LLM steps for routing, classification, ranking and guardrails. Output is schema-bound by construction. Vendor-claimed pricing is $0.042 per 1M input tokens with free output and 70-500 ms latency (not independently verified). Reported to be served via OpenRouter, Vercel AI Gateway and Cloudflare AI Gateway; TypeSafe reportedly paused direct signups on Sep 22. Endpoint: `POST https://api.typesafe.ai/v1/systemone`.
  - Link: https://typesafe.ai (docs; secondary coverage: https://openrouter.ai/docs/guides/community/jev.md)

- **jevgrep** (GitHub repo) - CLI that lets coding agents find code by describing what it does, using Jev to pick relevant files.
  - Why it matters: A drop-in context-retrieval step for Claude Code / Codex that is cheaper than an LLM grep loop. Created Sep 26, about 2.3k stars.
  - Link: https://github.com/dzhng/jevgrep
  - Safety note: MIT license; 212 commits; repo updated Oct 6 (per GitHub search). `npm install -g @dzhng/jevgrep`, then `jg auth` stores your provider key in an owner-only config file; it needs your own API key. I read the README only, not the source, and could not check contributor history. Review before use.

- **universal-modder** (GitHub repo) - Claude Code plugin/skills plus a fal MCP for having an agent reverse-engineer and mod PC games you own.
  - Why it matters: A worked example of a long-horizon agent workflow (recon, code reading, asset generation, in-game testing, video) packaged as portable skills for several agent CLIs.
  - Link: https://github.com/rehan-remade/universal-modder
  - Safety note: MIT license; 78 commits; created Sep 30, about 4.2k stars, updated Oct 6. Install paths are `npx skills add` or `uv tool install git+...`; it needs a fal API key. Very new, with 21 open issues. I did not audit the source. Read it before installing, and note that reverse engineering has legal limits.

Not included: feder-cr/dots (stealth "does not get blocked" browser agent) and the AIHOT clone-style aggregator, since I could not vouch for them.

