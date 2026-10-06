# What's New Digest

Daily digest of AI/Claude tooling advances and vetted GitHub repos. Newest entry first. Maintained by a scheduled routine.

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

