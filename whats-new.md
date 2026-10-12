# What's New Digest

Daily digest of AI/Claude tooling advances and vetted GitHub repos. Newest entry first. Maintained by a scheduled routine.

## 2026-10-12

- **Dynamic workflows for Claude Managed Agents (beta)** (AI/Claude tooling) - Oct 9 API release: an agent can write a workflow program that fans out many agents in phases and combines their results, run server-side in the background.
  - Why it matters: Lets you hand a task too big for one conversation (e.g. reviewing hundreds of documents) to a hosted agent without writing your own orchestrator. Enable with beta header `managed-agents-2026-04-01` and `"multiagent": {"type": "multiagent_20261001", "workflows": {"type": "enabled"}}`; follow progress via `workflow_run.*` events.
  - Link: https://platform.claude.com/docs/en/managed-agents/workflow-runs

- **Claude Code v2.1.296** (AI/Claude tooling) - Released Oct 9.
  - Why it matters: `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` pins all workflow agents to one model (cost control); `autoCompactWindow` in subagent frontmatter lets a subagent compact earlier; Read tool gains `allow_large`; MCP tool description/instruction limit raised from 2,048 to 4,096 chars; managed `PreToolUse` deny hooks with `"continue": false` no longer end the turn.
  - Link: https://github.com/anthropics/claude-code/releases

- **Sonnet 5.5 prompt-cache reads halved** (AI/Claude tooling) - Oct 7: cache reads now $0.10 per million tokens (was $0.20).
  - Why it matters: Long-context agent loops and repeated-prefix workloads get cheaper with no code change; worth re-checking cost estimates for caching-heavy designs.
  - Link: https://platform.claude.com/docs/en/release-notes/api

No GitHub repos made the cut today: the trending ones I checked either use a non-OSI license (mksglu/context-mode is ELv2) or had anomalous star growth I could not vouch for.

## 2026-10-11

- **Claude Haiku 5.5 (`claude-haiku-5-5`)** (AI/Claude tooling) - Launched Oct 7: 1M context, 128k max output, adaptive thinking.
  - Why it matters: Cheap/fast tier for subagents and high-volume steps. Migration gotcha: Haiku 4.5 patterns now return 400s (`budget_tokens`, `temperature`/`top_p`/`top_k`, assistant prefill, and the `computer_20250124` tool), so audit existing calls before swapping the model ID.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **SDK computer-use and browser-use classes (beta)** (AI/Claude tooling) - Oct 7 API release: Python and TypeScript SDKs let you subclass a computer or browser class and implement one method per tool against your own automation backend.
  - Why it matters: Less glue code for custom computer-use agents (e.g. driving your own Playwright or VM harness). Same release: Managed Agents `limited` networking now also restricts `web_search`/`web_fetch` via `allowed_hosts`, and `web_fetch` only fetches URLs already seen in the session.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude Code v2.1.295 / v2.1.294** (AI/Claude tooling) - Released Oct 8.
  - Why it matters: New `onFailure: "block"` for command and HTTP hooks makes a hook that fails to start, times out, or crashes block the action instead of letting it through (fail-closed guardrails). Also: `prompt`/`agent` hooks phrased as instructions no longer allow actions they should block, remote MCP servers back off up to 30s instead of reconnect-looping, and OSC 7501 lets terminals show working/waiting/done status.
  - Link: https://github.com/anthropics/claude-code/releases

- **strands-agents/box** (GitHub repo) - Rust sandbox for running AI agents with OS isolation, default-deny network/file/exec policies, and credential injection so secrets stay outside the agent. macOS on Apple silicon today; Linux planned.
  - Why it matters: A way to run coding agents or MCP tools with least privilege instead of trusting prompt-level rules; relevant to any agent that executes untrusted code or holds API keys.
  - Link: https://github.com/strands-agents/box
  - Safety note: Apache-2.0; created Oct 2, last push Oct 11; ~319 stars, 14 forks; under the `strands-agents` org. Young project (41 open issues), so review before relying on it for real isolation.

- **dzhng/jevgrep** (GitHub repo) - CLI for coding agents that finds code by describing what it does, using the Jev model to pick relevant files and source context.
  - Why it matters: Semantic code retrieval for Claude Code/Codex without hand-built embeddings pipelines; a concrete example of a typed/judgment model replacing grep-and-guess steps.
  - Link: https://github.com/dzhng/jevgrep
  - Safety note: MIT; created Sep 26, last push Oct 2; ~2.6k stars, 187 forks. I checked repo metadata only, not the code or install scripts, so inspect before installing.

## 2026-10-10

- **Dynamic workflows for Claude Managed Agents (beta)** (AI/Claude tooling) - Oct 9 API release notes: an agent can write a program that runs many agents in phases, executed server-side as a workflow run.
  - Why it matters: Fan-out/pipeline orchestration (review, research, migration jobs) without hosting your own orchestrator. Enable via the agent's `multiagent` field set to `{"type": "multiagent_20261001", "workflows": {"type": "enabled"}}` with the `managed-agents-2026-04-01` beta header; progress arrives as `workflow_run.*` events.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Sonnet 5.5 cheaper cache reads + Models API capability fields** (AI/Claude tooling) - Prompt cache reads on Claude Sonnet 5.5 dropped from $0.20 to $0.10 per million tokens (Oct 7). The Models API also gained `capabilities.server_tools` (Oct 6) and `capabilities.thinking.types.disabled` (Oct 5).
  - Why it matters: Halves the cost of cache-heavy agent loops; the capability fields let code check programmatically whether a model accepts web search/code execution tools or `thinking: {type: "disabled"}` instead of hardcoding per-model assumptions.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude Code v2.1.296** (AI/Claude tooling) - Released Oct 9.
  - Why it matters: Subagents (frontmatter and `--agents`) get `autoCompactWindow` to compact earlier than the main conversation; `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` pins one model for all workflow agents; Read tool gains `allow_large`; the MCP tool-description/instructions limit rises from 2,048 to 4,096 characters. Fixes: managed `PreToolUse` hooks that deny with `"continue": false` no longer end the turn, Edit/NotebookEdit refuse non-UTF-8 files instead of corrupting them, and Bash permission checks no longer auto-approve `BASH_ARGV0` assignment tricks.
  - Link: https://github.com/anthropics/claude-code/releases

- **mattpocock/skills** (GitHub repo) - Collection of agent skills from the author's own `.agents` directory: engineering skills (e.g. `tdd`, `grill-with-docs`, `to-spec`, `code-review`) and productivity skills (`grill-me`, `handoff`, `teach`), packaged as plugins for Claude Code, Codex, Copilot and Gemini CLI.
  - Why it matters: Ready-made, reusable workflows (spec grilling, TDD, handoff notes) you can install into your own agent setup rather than writing prompts from scratch.
  - Link: https://github.com/mattpocock/skills
  - Safety note: MIT; ~284k stars, 545 commits, trending today. Last-commit date and contributor list not visible to me. Install via one method per agent only (otherwise skills duplicate). Skills are prompt files that steer your agent, so skim them before enabling. I did not audit the source.

Not included: mksglu/context-mode (interesting context-window tool, but Elastic License 2.0 is not OSI-approved); other trending repos I did not vet (morluto/rea, AnyPS5, storytold/artcraft).

## 2026-10-09

- **Claude Code v2.1.295** (AI/Claude tooling) - Released Oct 8 (with v2.1.294 earlier that day).
  - Why it matters: New `onFailure: "block"` option for command and HTTP hooks, so a hook that fails to start, times out or exits unexpectedly blocks the action instead of letting it through (a fail-closed guardrail). Also adds `CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS` to cap unattended retry waits on 429/529, remote MCP servers now reconnect with backoff, and `claude -p` no longer drops earlier responses when background work starts another turn. v2.1.292 (Oct 6) added an `effort` parameter on the Agent tool for sub-agents.
  - Link: https://github.com/anthropics/claude-code/releases

- **Managed Agents web-tool restrictions and SDK browser/computer-use classes** (AI/Claude tooling) - API release notes for Oct 7: with `limited` networking, `allowed_hosts` now also governs `web_search`/`web_fetch`; `web_fetch` only fetches URLs already seen in the session; the Python/TypeScript SDKs add beta classes where you subclass and implement one method per browser/computer-use tool.
  - Why it matters: Safer egress control for agents that browse, and less boilerplate for custom browser or computer-use agents. Note `allowed_domains` outside `allowed_hosts` now fails with a 400. Max and Team plans also now include monthly API credits.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **alibaba/open-code-review** (GitHub repo) - `ocr` CLI that reviews Git diffs (or whole files via `ocr scan`) by pairing deterministic pipelines with a tool-using LLM agent, producing line-level comments with a model provider you configure.
  - Why it matters: A drop-in AI review step for CI or pre-merge checks that is provider-configurable rather than tied to one assistant.
  - Link: https://github.com/alibaba/open-code-review
  - Safety note: Apache-2.0; ~44.9k stars, 787 commits, listed on GitHub Trending today. I could not see last-commit or creation dates or contributor count on the page. The project's own benchmark (AACR-Bench) is self-reported and it says recall is lower than general-purpose agents like Claude Code. Install is via npm (`@alibaba-group/open-code-review`); an install script is also offered, so prefer npm. Needs your own LLM API key. I did not audit the source.

- **diagram-design** (GitHub repo, cathrynlavery) - Agent skill that generates editorial-style diagrams as self-contained HTML/SVG (42 diagram types), can match a site's brand, redraw draw.io/Mermaid/Excalidraw sources, and export PNG/SVG.
  - Why it matters: Gives Claude Code and similar agents a consistent way to produce architecture diagrams and docs visuals.
  - Link: https://github.com/cathrynlavery/diagram-design
  - Safety note: MIT; ~47.4k stars, 265 commits, trending today. Last-commit date and contributors not visible to me. Brand onboarding fetches your website and diagrams load Google Fonts (see its PRIVACY.md); PNG export needs Playwright/Chromium. README warns of unofficial copies under other names, so install only from this repo. I did not audit the source.

Not included: other trending repos I did not vet (morluto/rea, AnyPS5, storytold/artcraft, lingbot-map).

## 2026-10-08

- **Claude Haiku 5.5** (AI/Claude tooling) - New small/fast model, `claude-haiku-5-5`, released Oct 7 and now the default Haiku on the Anthropic API (also in Claude Code v2.1.293).
  - Why it matters: Per the API release notes: 1M-token context, 128k max output, adaptive thinking with the `effort` parameter, and availability on Bedrock, Google Cloud and Foundry. Good fit for high-volume sub-agents and routing steps. Migrating from Haiku 4.5: manual `budget_tokens` extended thinking now returns a 400, and thinking blocks appear by default (more tokens). The release notes page did not list prices; check the pricing page.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude API changes, Oct 5-8** (AI/Claude tooling) - Sonnet 5.5 cache reads cut from $0.20 to $0.10 per million tokens (cache writes unchanged); Python/TypeScript SDKs add beta classes for the browser-use and computer-use tools where the SDK runs the tool loop; Managed Agents `allowed_hosts` now also governs `web_search`/`web_fetch`; Models API gains `capabilities.server_tools` and `capabilities.thinking.types.disabled`.
  - Why it matters: Cheaper long-context agent loops, less hand-written tool-loop code, and programmatic capability checks when choosing a model. Note Sonnet 4.5 retires Nov 30, 2026.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude Code v2.1.293 / v2.1.294** (AI/Claude tooling) - Released Oct 7 and Oct 8.
  - Why it matters: 2.1.294 fixes `prompt`/`agent` hooks written as plain instructions (e.g. "Block commands that...") failing to block what they should, and improves Stop/SubagentStop hook judging. 2.1.293 fixes an HTTP MCP connection memory leak and Claude treating pre-compaction actions as done after compaction. Upgrade if you rely on hooks or long sessions.
  - Link: https://github.com/anthropics/claude-code/releases

- **HyperFrames** (GitHub repo, heygen-com) - Turns HTML/CSS/media and seekable animations (GSAP, Lottie, Three.js) into deterministic MP4s by seeking frames in headless Chrome and encoding with FFmpeg; ships a Claude Code plugin and standalone skills.
  - Why it matters: Lets an agent produce video by writing plain HTML, which it can already do well, with reproducible output. Useful for generated demos, changelog videos or social clips.
  - Link: https://github.com/heygen-com/hyperframes
  - Safety note: Apache-2.0; listed on GitHub Trending this week; page shows ~58.9k stars (I could not confirm creation or last-commit dates from the page). Installs run third-party packages via `npx` and a plugin marketplace, so review them like any dependency. I did not audit the source.

- **OpenRig** (GitHub repo, mvschwarz) - Local daemon, CLI, TUI and MCP server on tmux for defining teams of Claude Code, Codex and Pi agents in YAML, with roles, shared context and persistent sessions.
  - Why it matters: A concrete way to run multi-agent setups with durable roles instead of ad hoc terminals.
  - Link: https://github.com/mvschwarz/openrig
  - Safety note: Apache-2.0; ~6.0k stars, 3,673 commits, trending this week (creation/last-commit dates not visible to me). Invasive: it writes hooks, status-line commands and trust settings into `~/.claude` and `~/.codex/config.toml`, offers `curl | sh` and a postinstall check, and has optional permission-bypass modes. No credential requests seen. Try it in a disposable environment and prefer the npm route over `curl | sh`.

Not included: other trending repos I did not vet (claude-mem, mattpocock/skills, Agent-Reach, text-to-cad, cursor/plugins).

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

