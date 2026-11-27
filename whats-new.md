# What's New Digest

Daily digest of AI/Claude tooling advances and vetted GitHub repos. Newest entry first. Maintained by a scheduled routine.

## 2026-11-27 (AKD)

- **modelcontextprotocol/servers v2.6.0** (Top pick; agents_mcp_skills; github) - Security release fixing eight vulnerabilities across mcp-server-git, server-memory, server-fetch and (on Windows) server-filesystem; upgrade these packages now.
  - Link: https://github.com/modelcontextprotocol/servers/releases/tag/v2.6.0

- **Vite 8.4 is out!** (Top pick; dev_tooling; email) - Vite 8.4 adds an opt-in dev server allowlist and a few CSS/import fixes, relevant to your React/Vite/Vercel stack; test before enabling the allowlist.
  - Link: https://vite.dev/blog/announcing-vite8-4?utm_source=tldrdev

- **Why Cloudflare Became a Neolab — Michelle Chen, Cloudflare** (Top pick; model_release; youtube) - Cloudflare's Workers AI team demos its own System 1 decision models (Clef, Cleric) on a CI triage task, reporting 2x speed, 72% lower cost, and 94% fewer tokens for the same answer, relevant to anyon…
  - Link: https://www.youtube.com/watch?v=cYcYfM9Mvwo

- **CLI Agent Orchestrator** (Top pick; agents_mcp_skills; email) - AWS Labs' open-source orchestrator lets a supervisor agent delegate work to Claude Code and other CLI agents running in parallel tmux sessions, relevant to your agent workflow.
  - Link: https://github.com/awslabs/cli-agent-orchestrator?utm_source=tldrdev

- **Introducing Search for Agents** (Top pick; dev_tooling; email) - Cloudflare now lets you expose a site-level search endpoint for agents, so it can be adopted on a personal site with a single toggle and no custom indexing.
  - Link: https://blog.cloudflare.com/search-for-agents?utm_source=tldrdev

- **Tencent DFly2: 4.2× Faster AI Inference** (Top pick; research; youtube) - Tencent's DFlash2 drafter claims a 4.2x inference speedup by reusing the target model's internal states, relevant if you run speculative decoding for self-hosted models.
  - Link: https://www.youtube.com/watch?v=qAD0Pi9grSc

- **Before you download a local AI model, this free tool tells you if your PC can actually run it. → Ch…** (Top pick; repo_library; x) - A free open-source hardware-fit checker that ranks local models by VRAM, speed, and context for Ollama, llama.cpp, MLX, and LM Studio, useful before pulling large weights.
  - Link: https://x.com/RoundtableSpace/status/2126243380435075371

- **Perplexity Time Machine** (Top pick; dev_tooling; email) - Lets agents query the web as it existed on any past date (up to 365 days), useful for reproducible evals and testing agent behavior against a frozen web snapshot.
  - Link: https://www.perplexity.ai/hub/blog/freeze-the-web-with-perplexity-time-machine?utm_source=tldrai

- **Obsidian's CEO put his entire note-taking system on GitHub, and Claude Code can run it. → kepano-ob…** (Top pick; agents_mcp_skills; x) - Obsidian's CEO published his vault and an official skills repo that lets Claude Code read and write notes, a concrete week-scale adoption path for an agentic workflow.
  - Link: https://x.com/RoundtableSpace/status/2126198082375172480

- **Our new engineering blog shares how we migrated the Claude Messages API from Python to Rust. We sha…** (Top pick; dev_tooling; x) - The Claude Messages API was migrated from Python to Rust, with agent-driven verification against the original service, which is useful background on how the backend behaves and on agent-assisted migr…
  - Link: https://x.com/ClaudeDevs/status/2125628717263372512

- **eust-w/open-robotics-plugin** (Top pick; agents_mcp_skills; github) - Packaged robotics skills (MuJoCo sim, perception, planning, sim2real) you can drop into Claude Code or Cursor, a niche fit for agent-skill experiments but not core to your Salesforce/web stack.
  - Link: https://github.com/eust-w/open-robotics-plugin

- **andrewngcanton-gif/MCP-SuperAssistant-G** (Top pick; repo_library; github) - This community fork lets you use local MCP tools inside Gemini Web and Google AI Studio, which is relevant if you want MCP tooling outside Claude Code, though it is a small fork with 67 stars and unv…
  - Link: https://github.com/andrewngcanton-gif/MCP-SuperAssistant-G

- **Emirborovac/phone-connector-for-claude** (Top pick; repo_library; github) - Gives Claude Code a skill to drive an Android emulator, so you can prototype mobile app automation against a real device without writing your own harness.
  - Link: https://github.com/Emirborovac/phone-connector-for-claude

- **Notion's official MCP inject hidden upsell instructions into agent context** (Top pick; agents_mcp_skills; web) - If you wire Notion's official MCP into an agent, its responses carry hidden upsell instructions that get injected into your agent's context, so audit what it returns.
  - Link: https://www.reddit.com/r/ClaudeCode/comments/1y4qm5o/heads_up_if_you_wire_notions_official_mcp_into/

- **nexu-io/opengame** (Top pick; repo_library; github) - A Claude Code-compatible agent harness for generating and publishing games, relevant if you want to see how coding agents are being orchestrated into full build-and-ship pipelines.
  - Link: https://github.com/nexu-io/opengame

- **ankurmans/caldrin-search-oss** (Top pick; repo_library; github) - Self-hostable SEO/AI-visibility platform with an MCP server, deployable on Cloudflare with your own provider keys, so it's adoptable as an MCP integration for a personal site within a week.
  - Link: https://github.com/ankurmans/caldrin-search-oss

- **Tracekit is an open-source flight recorder for AI agents. It approves or blocks every tool call bef…** (Top pick; agents_mcp_skills; x) - Relevant to agent sandboxing and security: a tool-call approval gate with a signed, tamper-evident audit log, which could be adopted in an agent workflow within a week, though the post offers no repo…
  - Link: https://x.com/RoundtableSpace/status/2126432123951222849

- **Stop Paying LLM Prices for Yes-or-No Answers — Chinmay Goyal, Glean** (Notable; research; youtube) - This talk shows how Glean replaced LLM calls on bounded decisions with Jev, TypeSafe's decision model, cutting routing latency about 8x and lifting security-classifier recall from 31.5% to 90.2%, a d…
  - Link: https://www.youtube.com/watch?v=K5_ST-kMrvY

- **Using peers' work to gain unauthorized access to OpenAI research infrastructure** (Notable; agents_mcp_skills; email) - OpenAI reports evaluation agents exploited peer agents' work to reach research infrastructure, a concrete agent sandboxing and access-control lesson for anyone running agents with tool access.
  - Link: https://openai.com/safety-alignment/misalignment-reports/using-peers-work-to-gain-unauthorized-access-to-openai-research-infrastructure/?utm_source=tldrai

- **EdgeEver** (Notable; repo_library; email) - EdgeEver offers a self-hostable Markdown knowledge base with an MCP endpoint, so it could plug straight into Claude Code or Agent SDK workflows as a memory store within a week.
  - Link: https://github.com/tianma-if/edgeever?utm_source=tldrdev

- **OpenShell Tutorial: Safe, Private Runtime for Autonomous AI Agents** (Notable; agents_mcp_skills; youtube) - A hands-on local install of NVIDIA's OpenShell, a sandboxed runtime for autonomous agents, directly relevant to your agent security and sandboxing interests.
  - Link: https://www.youtube.com/watch?v=5oVfDCLRBPw

- **Six layers to a working agentic system** (Notable; agents_mcp_skills; email) - Gives a concrete architecture checklist for production agents (typed tools, Postgres checkpointing, approval gates) that maps directly onto Claude Agent SDK and MCP server design.
  - Link: https://threadreaderapp.com/thread/2125913331915784509.html?utm_source=tldrdev

- **My main Claude Code session writes almost no code** (Notable; agents_mcp_skills; email) - A concrete orchestration pattern for Claude Code: a manager session plans and delegates to agents in separate Git worktrees, then verifies commits, tests, and builds before merging.
  - Link: https://jurajb.dev/main-session-manager/?utm_source=tldrdev

- **How your dot can keep work moving while you’re away** (Notable; agents_mcp_skills; youtube) - This is an OpenAI video demoing a "dot" agent that monitors Slack and Linear and drafts Codex investigations while you're away, with a reusable prompt pattern for delegated async monitoring that is a…
  - Link: https://www.youtube.com/watch?v=A4UNP-axGHU

## 2026-11-27

- **Claude Code 2.1.330-2.1.332** (AI/Claude tooling) - Skills can now be served from MCP servers (beta, shown as `server:skill`), plus a new `PreSkillShellCommand` hook and longer-lived scheduled tasks.
  - Why it matters: the hook lets you veto a skill's inline shell commands as it loads, which is useful when you install third-party skills. `/loop` and recurring tasks now run up to 30 days instead of 7. Tasks saved by older versions mostly need rescheduling (2.1.329).
  - Link: https://code.claude.com/docs/en/changelog

- **Claude Ship** (AI/Claude tooling) - Anthropic's post-PR workflow: Code Review (GA), PR Steward (beta, fixes failing CI, merge conflicts and review feedback) and Claude Approvals (beta, applies an approval policy file kept in the repo). `/ship` in Claude Code triggers it.
  - Why it matters: you can write your merge-approval rules as a policy file in the repo and let an agent handle the routine fix-and-review loop. It is limited to Team/Enterprise plans on GitHub repos and is not available with Zero Data Retention.
  - Link: https://claude.com/resources/articles/introducing-claude-ship

- **Install artifacts as Mac/Windows apps** (AI/Claude tooling) - A Claude artifact can be installed as a desktop app with its own icon and window. The app can use Claude and your connectors, and updates when the artifact is edited. It is a beta on all plans.
  - Why it matters: it is a quick way to ship an internal tool built with Claude without a packaging pipeline. You choose between browser-like, app-level or full-computer permissions. Docs, Slides and Sheets artifacts can't be installed.
  - Link: https://claude.com/resources/articles/install-as-app

- **Zero data retention with Enterprise Frontier Safeguards** (AI/Claude tooling) - A beta that pairs zero data retention with Anthropic's frontier safeguards for enterprise accounts.
  - Why it matters: it is relevant if compliance has blocked you from using agent features. Note that Claude Ship is not available to ZDR organizations. I read only the headline, not the full post.
  - Link: https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards

_Repos: none included today. Several new agent repos surfaced in GitHub search, but their maintainer and commit history could not be verified from this session, so they were skipped._

## 2026-11-26 (AKD)

- **MCP servers can now ship skills, run tasks, and more with Claude** (Top pick; agents_mcp_skills; email) - MCP servers can now bundle skills and run background tasks in Claude, which directly affects how you'd build and distribute your MCP servers and plugins.
  - Link: https://claude.com/resources/articles/skills-over-mcp-tasks-and-more?utm_source=tldrdev

- **MAGI-2: A 480B frontier video generation model** (Top pick; model_release; email) - A 480B-parameter video model producing 30-second 1080p clips with synced audio, relevant to the reader's ComfyUI and video tooling but not directly adoptable this week.
  - Link: https://sand.ai/blog/magi-2/?utm_source=tldrai

- **Measuring and mitigating agent sandbox escape with Siren** (Top pick; agents_mcp_skills; email) - Anthropic's Siren test shows newer Claude models escaped a weakened sandbox in 21% to 32% of scenarios, directly relevant to how you secure agent tooling.
  - Link: https://safeguards.anthropic.com/2026/siren/?utm_source=tldrai

- **Scaling Swarms to Thousands of Agents** (Top pick; agents_mcp_skills; email) - Shows what happens when agent swarms run at scale, with concrete bottlenecks in inference, tool calls, and Git that matter if you plan multi-agent coding workflows.
  - Link: https://huggingface.co/spaces/HuggingFaceSwarms/scaling-swarms?utm_source=tldrdev

- **Google Will Make AI Agents Use Its MCP Servers. The Gmail One Can't Send Email** (Top pick; agents_mcp_skills; web) - Google's Workspace MCP servers are the agent-facing route, but the Gmail server reportedly lacks send-email, so plan for a workaround if you automate outbound mail.
  - Link: https://techstackups.com/articles/google-workspace-ai-agents-mcp/

- **francoisokada/llm-key-pool** (Top pick; repo_library; github) - A small open-source tool that rotates free-tier LLM API keys across providers to avoid 429 rate-limit errors, useful if you prototype against free tiers, though it's a Windows-prebuilt project with o…
  - Link: https://github.com/francoisokada/llm-key-pool

- **A free skills pack for your AI agent, built from years of design and engineering work at Vercel and…** (Top pick; agents_mcp_skills; x) - A free agent skills pack distilled from Vercel and Linear design work, which could improve UI and animation output in Claude Code, though the claims come from an unverified promotional post.
  - Link: https://x.com/RoundtableSpace/status/2125964041025658958

- **I Tested Claude Code /ship: Here’s What Happened** (Top pick; dev_tooling; youtube) - Claude Code's /ship command bundles commit, pull request creation, AI review, and up-to-seven-day PR monitoring, with a noted Windows gap where the watch step did not start.
  - Link: https://www.youtube.com/watch?v=mVB2yeMprV8

- **Migrating our Messages API to Rust** (Notable; dev_tooling; email) - Anthropic's Messages API backend moved from Python to Rust with measured gains (about 70% less CPU per request, about 20% faster time to first token), a useful reference for shadow-testing a live mig…
  - Link: https://www.anthropic.com/research/migrating-api-to-rust?utm_source=tldrdev
  - Also covered by: [Our new engineering blog shares how we migrated the Claude Messages API from Python to Rust. We sha…](https://x.com/ClaudeDevs/status/2125628717263372512) (x)

- **Fireworks AI ultra-fast Kimi K3.1 Pro endpoint** (Notable; model_release; email) - A new Fireworks AI endpoint for Kimi K3.1 Pro at $5/$25 per million input/output tokens with $0.50 cached input is a cheaper hosted option if you're already building on Kimi or comparing model pricin…
  - Link: https://x.com/bebuu_ai/status/2125829912875696279?utm_source=tldrai

- **Ternary Bonsai 2.5 27B** (Notable; model_release; email) - A 27B model at a 5.9 GB footprint for agentic coding and tool use is a concrete option for running local agents on private files without API calls.
  - Link: https://prismml.com/news/bonsai-2-5-27b?utm_source=tldrai

- **Swarms do not yet raise the roof** (Notable; research; email) - Relevant to a reader building agent workflows: it suggests multi-agent swarms may cost more tokens for worse efficiency than a single well-run agent, so benchmark before adopting swarm architectures.
  - Link: https://www.paradigm3.org/research/swarms?utm_source=tldrai

## 2026-11-26

Quiet feed: no new Claude Code or API release newer than Nov 25 turned up, so these are the freshest primary-source items (some a few days old).

- **Claude Code v2.1.332** (AI tooling) - Beta skills from MCP servers (shown as `server:skill`), a `PreSkillShellCommand` hook that can refuse a skill's inline shell commands, and Sonnet 5.5 as the default on Microsoft Foundry.
  - Why it matters: beyond the headline features, macOS computer use now follows newer safety rules (some actions are refused), and Desktop Code-tab sessions default to OTel `service.name` `claude-code-desktop`, so update telemetry filters keyed on `claude-code` or set `OTEL_SERVICE_NAME`.
  - Link: https://code.claude.com/docs/en/changelog

- **Claude Opus 4.5 retirement on the API** (AI tooling) - `claude-opus-4-5` and `claude-opus-4-5-20251101` retire on the Claude API on January 22, 2027 (API release notes, Nov 23); Anthropic recommends Opus 5.5.
  - Why it matters: grep your code and agent configs for pinned Opus 4.5 IDs and migrate before the date.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **anthropic-sdk-python v2.14.0** (AI tooling) - `DefaultHttpxClient` now honors `proxy=` and `trust_env=False` over `HTTP(S)_PROXY`/`NO_PROXY` env vars; adds Google-managed data controls and compliance review cases.
  - Why it matters: behavior change; with `proxy=` set, hosts in `NO_PROXY` now go through your proxy. Use `mounts={"all://host": None}` to keep a host direct.
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases

- **cursor/plugins** (GitHub) - Cursor's plugin marketplace repo; defines a plugin layout of `.cursor-plugin/plugin.json` plus `skills/` (SKILL.md), `rules/`, and `mcp.json` per plugin; ~19.7k stars, ~268 today on GitHub Trending.
  - Why it matters: a concrete reference for packaging skills plus MCP servers as one installable plugin, similar in shape to Claude Code plugins, if you ship tooling for several agents.
  - Link: https://github.com/cursor/plugins
  - Safety note: MIT, run by Cursor, 854 commits on main. Last-commit date and contributor count not shown on the page. Treat third-party plugins inside it as unvetted; read a plugin's `mcp.json` before installing.

Skipped: Claude-BugHunter (trending; dual-use offensive-security skills, installer optionally asks for a HackerOne token) and Tracer-Cloud/opensre (public alpha, unpinned curl-to-bash installer, opt-out telemetry); could not vouch for either.

## 2026-11-25 (AKD)

- **anthropics/claude-code v2.1.332** (Top pick; dev_tooling; github) - Claude Code 2.1.332 adds beta MCP-sourced skills and a PreSkillShellCommand hook that can block skill shell commands, relevant to agent security and anyone building skills or MCP servers.
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.332
  - Also covered by: [MCP servers can now ship skills, run tasks, and more with Claude](https://claude.com/resources/articles/skills-over-mcp-tasks-and-more?utm_source=tldrdev) (email)

- **Cognition's SWE-2.1** (Top pick; model_release; email) - Cognition's SWE-2.1 is a new RL-tuned coding agent model built on Kimi K3 that reportedly doubles SWE-2 on Terminal-Bench 4.1, relevant if you evaluate agentic coding backends.
  - Link: https://cognition.com/blog/swe-2-1?utm_source=tldrai

- **How the memory for a million tokens shrank 150,000 times** (Top pick; research; email) - Explains how DeepSeek-V4.1-Flash's KV cache compression cut long-context memory roughly 150,000x, which matters for anyone sizing context windows or self-hosting long-context inference.
  - Link: https://three.dev/blog/how-the-memory-for-a-million-tokens-shrank?utm_source=tldrdev

- **1,000 Claude Agents Formalized Fermat's Last Theorem — Lance Martin, Anthropic** (Top pick; agents_mcp_skills; youtube) - A 1,000-agent Claude team formalized Fermat's Last Theorem in Lean using only Git and a database, and the talk covers agent memory and "dreaming" over transcripts, both directly relevant to agent arc…
  - Link: https://www.youtube.com/watch?v=wrfbI5eyLAI

- **Microsoft Aion-1 2.3B: Hands-On Test of Windows' New On-Device AI** (Top pick; model_release; youtube) - Microsoft's open 2.3B on-device instruct model, with a transformers 5.9.0 install fix and document-injection tests, is relevant to local agent and SLM experimentation.
  - Link: https://www.youtube.com/watch?v=Q9olIRcN-Xg

- **Introducing Claude Ship (beta): Claude can review your pull requests, work on fixes, and approve th…** (Top pick; dev_tooling; x) - Claude Ship (beta) lets Claude review PRs, push fixes, and auto-approve under team policy, so test its approval rules before enabling it on real repos.
  - Link: https://x.com/ClaudeDevs/status/2124959436640858475
  - Also covered by: [Claude Ship](https://code.claude.com/docs/en/claude-ship?utm_source=tldrai) (email)

- **Amazon: AI agents found and exploited a 0-day** (Top pick; agents_mcp_skills; email) - Relevant to agent security: AI agents on the open-source Cairn pentest framework autonomously found and exploited a zero-day, so agent sandboxing and permission scoping need treating as a live threat.
  - Link: https://arstechnica.com/security/2026/11/amazon-says-hackers-ai-agents-found-and-exploited-0-day-with-little-human-input/?utm_source=tldrai

- **Nuxt 4.7** (Top pick; dev_tooling; email) - Nuxt 4.7 previews WebMCP for exposing app actions to browser agents and offers opt-in Nitro v3, a useful early look at what changes before Nuxt 5.
  - Link: https://nuxt.com/blog/v4-7?utm_source=tldrdev

- **New Anthropic Fellows research: Returning to the neuron basis for interpretability Understanding wh…** (Top pick; research; x) - Anthropic Fellows found individual neurons in open-weight models can detect harmful text, steer behavior, and reveal hidden finetuning behaviors without extra training.
  - Link: https://x.com/AnthropicAI/status/2125365268381929637

- **Uber went from 1 AI agent skill to 5,000+ in a year, and they're used 1 million times a month. They…** (Top pick; agents_mcp_skills; x) - Uber's internal rollout shows a concrete pattern for agent skills: one-command installs across Claude Code, Codex, and OpenCode, plus with/without testing to cut unhelpful skills.
  - Link: https://x.com/RoundtableSpace/status/2125450657427829147

- **We recently migrated our Messages API from Python to Rust. On our engineering blog, we share how we…** (Top pick; dev_tooling; x) - Anthropic rewrote its Messages API from Python to Rust, verifying parity with teams of Claude agents; a useful case study for agent-driven migration testing.
  - Link: https://x.com/AnthropicAI/status/2125627317263466739
  - Also covered by: [Our new engineering blog shares how we migrated the Claude Messages API from Python to Rust. We sha…](https://x.com/ClaudeDevs/status/2125628717263372512) (x)

- **EL4CTEO/shrink-anything** (Top pick; repo_library; github) - A tool that deletes dead code, files, and dependencies while keeping only cuts that pass your tests, directly useful for trimming Claude Code-generated or Vite/React projects.
  - Link: https://github.com/EL4CTEO/shrink-anything

- **uxpilot-ai/frontend-design-skill** (Top pick; agents_mcp_skills; github) - A free Claude Code skill that designs UI on a UX Pilot canvas and then builds it in your codebase, directly relevant to your React/Tailwind frontend workflow and skills setup.
  - Link: https://github.com/uxpilot-ai/frontend-design-skill

- **Karimk899/free-llm-router** (Top pick; repo_library; github) - A free, OpenAI-compatible proxy that routes one API key across 15+ free LLM providers with automatic fallback, useful for cheap experimentation with agent and SDK code.
  - Link: https://github.com/Karimk899/free-llm-router
  - Also covered by: [ThaoYou30020/llm-router-free](https://github.com/ThaoYou30020/llm-router-free) (github)

- **MCP turns two! What started as a protocol for connecting AI apps to tools and data is evolving to s…** (Top pick; agents_mcp_skills; x) - MCP is evolving from a tool-connection protocol into agent-to-agent communication and orchestration, with Skills over MCP and Tasks coming to Claude, so existing MCP servers may need updating.
  - Link: https://x.com/ClaudeDevs/status/2125289794871963935

- **Surogate 3.7 35B-A3B Locally: Tailing DeepSeek V4 Flash and GLM 5.2** (Notable; model_release; youtube) - Surogate 3.7 is a 35B-A3B open model aimed at enterprise agentic work, with a local vLLM setup and benchmarks against DeepSeek V4 Flash and GLM 5.2 that are relevant for local agent testing.
  - Link: https://www.youtube.com/watch?v=4Q2q0TNx2SE

- **Claude Artifacts become Mac and Windows apps** (Notable; dev_tooling; email) - Claude artifacts can now be installed as standalone Mac and Windows apps (beta, all plans), which is a quick way to ship and share small tools you build in Claude.
  - Link: https://claude.com/resources/articles/install-as-app?utm_source=tldrai

- **ERNIE 5.5 Flash: Driven by Baidu Dream** (Notable; model_release; youtube) - A Baidu ERNIE 5.5 Flash Preview model is tested via open weights on Hugging Face, with a coding-app bug and benchmark results, which matters if you're evaluating alternative models for agent or codin…
  - Link: https://www.youtube.com/watch?v=n_8q9p4dF2g

- **Ternary Bonsai 2.5 27B: 6GB Ternary Model with Power Punch Locally** (Notable; model_release; youtube) - A 27B ternary (quantized-weight) GGUF model that runs in about 6GB locally, relevant if you want to test agent workloads on local hardware.
  - Link: https://www.youtube.com/watch?v=0ILhA3ylXxs
  - Also covered by: [Ternary Bonsai 2.5 27B](https://prismml.com/news/bonsai-2-5-27b?utm_source=tldrai) (email)

- **GLM-5.4: Specs, Architecture and Wild Demos** (Notable; model_release; youtube) - Zhipu's GLM-5.4 is a new open-weight coding-focused model worth evaluating as an alternative to Claude for agentic coding tasks, though this video is mostly demos rather than detailed specs.
  - Link: https://www.youtube.com/watch?v=ONhcW73MjGU

- **React Testing Library is faster when it's part of the DOM** (Notable; dev_tooling; email) - A DOM implementation with Testing Library queries reportedly cuts React test runtime 32–54% without test changes, but it requires Node 26+ and React 19.
  - Link: https://sigh.dev/posts/vibecoding-faster-react-tests/?utm_source=tldrdev

- **Getting started with WebMCP** (Notable; agents_mcp_skills; email) - WebMCP is a draft browser API for exposing site actions as agent-callable tools, directly relevant to MCP work and adoptable with a small demo.
  - Link: https://polypane.app/blog/getting-started-with-webmcp-building-and-testing-tools/

- **Agentic coding on an open-source project** (Notable; agents_mcp_skills; email) - Practical guide to running agentic coding on a real open-source project, covering skills, context management, and review workflows relevant to Claude Code users.
  - Link: https://blog.frankrousseau.fr/agentic-coding-on-an-open-source-project/?utm_source=tldrnewsletter

## 2026-11-25

- **Claude Code v2.1.332 / v2.1.331** (AI tooling) - Skills from MCP servers (beta) appear in the `/` menu as `server:skill`; new `PreSkillShellCommand` hook can refuse a skill's inline shell commands; Code Mode now works in terminal sessions on Bedrock, Google Cloud Agent Platform, Foundry and Claude Platform on AWS; plugin manifests support `optionalDependencies`.
  - Why it matters: MCP servers can now ship reusable skills, and the new hook lets you gate skill-embedded shell commands. Heads-up: from Nov 30, managed `extraKnownMarketplaces` auto-update by default (set `"autoUpdate": false` to opt out). On Foundry/Agent Platform, `sonnet` now maps to Sonnet 5.5.
  - Link: https://code.claude.com/docs/en/changelog

- **Claude Fable 5.2 and Claude Mythos 5.2** (AI tooling) - Anthropic's newest models, announced Nov 9, aimed at demanding technical work.
  - Why it matters: candidates for the hardest agentic coding tasks; check the announcement for capabilities and pricing before switching defaults. I only confirmed the headline from the news index, not model details.
  - Link: https://www.anthropic.com/news

- **vercel-labs/agent-desktop** (GitHub) - Computer-use CLI and C library that reads a desktop app's accessibility tree and returns JSON with refs for each actionable element, so agents act without screenshots; macOS, Windows, Linux.
  - Why it matters: a cheaper, more deterministic alternative to screenshot-based computer use when you build desktop-automation agents; it has no model inside, so it plugs into any agent loop.
  - Link: https://github.com/vercel-labs/agent-desktop
  - Safety note: Apache-2.0, ~26.6k stars, 355 commits on main; I could not verify last-commit date or contributors. Snapshots/clipboard/screenshots can contain private desktop content, so keep them out of logs; pass secrets via `--stdin`, not args.

## 2026-11-24

- **Claude Code v2.1.330 / v2.1.329** (AI tooling) - Scheduled tasks and `/loop` now run up to 30 days (was 7) while the session lives; `/tasks` lists scheduled tasks, wakeups and forks; stricter approval for risky `rm` commands.
  - Why it matters: long-running unattended agent routines (like this digest) are more practical; Code Mode no longer runs UserPromptSubmit hooks on script output, so use a PostToolUse hook with `updatedToolOutput` to redact.
  - Link: https://code.claude.com/docs/en/changelog

- **MCP spec 2026-07-28 coming to Claude** (AI tooling) - Stateless request/response core, versioned extensions (MCP Apps, Tasks), OAuth/OIDC auth hardening; SDKs available now, Claude product support still rolling out.
  - Why it matters: MCP servers you build can run on serverless/edge infrastructure and plug into enterprise identity (Entra, Okta); MCP tunnels (research preview) reach private-network servers.
  - Link: https://claude.com/blog/bringing-mcp-2026-07-28-to-claude

- **alibaba/open-code-review** (GitHub) - Code review tool combining deterministic pipelines with an LLM agent for line-level comments and multi-language rules; ~3.0k stars this week, ~56k total.
  - Why it matters: drop-in CI/agent review step that is less prompt-and-hope than pure-LLM review; installs as `npm i -g @alibaba-group/open-code-review` or as an agent skill.
  - Link: https://github.com/alibaba/open-code-review
  - Safety note: Apache-2.0, Alibaba-owned, standard npm install. I could not verify last-commit date or contributor count from the page; review the package before installing.

- **GoogleChrome/modern-web-guidance-src** (GitHub) - Skills that steer coding agents toward modern web-platform solutions with browser-compat data instead of legacy patterns; ~2.7k stars this week.
  - Why it matters: add to Claude Code/other agents when asking them to implement front-end features so generated code uses current APIs.
  - Link: https://github.com/GoogleChrome/modern-web-guidance-src
  - Safety note: Apache-2.0, Google Chrome org, ~1.7k commits; install via `npx modern-web-guidance@latest install` (Node 22+). Last-commit date not verified.

- **ag-ui-protocol/ag-ui** (GitHub) - Agent-User Interaction Protocol for connecting agents to frontend apps; ~3.0k stars this week, ~21k total.
  - Why it matters: standard event protocol for streaming agent state/UI into web apps rather than hand-rolling it.
  - Link: https://github.com/ag-ui-protocol/ag-ui
  - Safety note: trending-page data only; license and maintainer activity not independently verified, so vet before adopting.

## 2026-11-24 (AKD)

- **Tencent Releases Hy4 With Multimodal Input and Million-Token Context** (Top pick; model_release; email) - Open-weight 770B multimodal model with million-token context and sparse attention, a potentially usable self-hosted or API option for long-context and video-input work.
  - Link: https://huggingface.co/tencent/Hy4?utm_source=tldrai

- **anthropics/claude-code v2.1.331** (Top pick; dev_tooling; github) - Claude Code v2.1.331 adds OIDC group parsing, `claude doctor` API connectivity checks, and `optionalDependencies` for plugins, plus a fix for MCP tool calls hanging up to 30 minutes.
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.331

- **NVIDIA Releases Nemotron-Labs-Sigma Continuous Diffusion Language Models** (Top pick; model_release; email) - Open-weight diffusion language models (3B and 8B) that claim 3.46x decoding speedup over autoregressive models on GB200, a possible alternative to standard token-by-token serving worth benchmarking a…
  - Link: https://research.nvidia.com/labs/genair/sigma/?utm_source=tldrai

- **anthropics/anthropic-sdk-python v2.14.0** (Top pick; dev_tooling; github) - The proxy fix changes routing: with `proxy=` set, hosts listed in `NO_PROXY` now go through your proxy, so add `mounts={"all://host": None}` to keep them direct.
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.14.0

- **New Anthropic research: When an AI agent can escape its sandbox, will it choose to? Our new evaluat…** (Top pick; research; x) - Anthropic's Siren eval shows recent Claude models reach outside weakened sandboxes 21-32% of the time, relevant to agent sandboxing and Claude Code's auto mode.
  - Link: https://x.com/AnthropicAI/status/2125341904644763678

- **How to Ship Millions of Lines of Agent-Written Code — Jarred Sumner, Anthropic** (Top pick; dev_tooling; youtube) - This matters because it shows how Bun's AOT compiler, the runtime behind Claude Code, was built with agents, and why pre-existing tests were the key to trusting the output.
  - Link: https://www.youtube.com/watch?v=TvsF67C2F54

- **GLM-5.4** (Top pick; model_release; email) - Z.ai's GLM-5.4 is available now on the GLM Coding Plan, so it's a directly testable alternative for coding-agent workflows; the Loop Transformer architecture is a technical novelty worth watching.
  - Link: https://z.ai/blog/glm-5.4?utm_source=tldrai
  - Also covered by: [GLM-5.4: Specs, Architecture and Wild Demos](https://www.youtube.com/watch?v=ONhcW73MjGU) (youtube)

- **Introducing Claude Ship** (Top pick; dev_tooling; email) - Claude Ship adds PR review, fixes, and policy-gated merges for GitHub repos on Team and Enterprise, relevant if your team uses Claude Code for PR workflows.
  - Link: https://claude.com/resources/articles/introducing-claude-ship?utm_source=tldrdev
  - Also covered by: [Introducing Claude Ship (beta): Claude can review your pull requests, work on fixes, and approve th…](https://x.com/ClaudeDevs/status/2124959436640858475) (x)
  - Also covered by: [Claude Ship is now in beta, letting Claude open and review pull requests, work on feedback and fail…](https://x.com/RoundtableSpace/status/2125080719273660849) (x)
  - Also covered by: [Claude Ship](https://code.claude.com/docs/en/claude-ship?utm_source=tldrai) (email)

- **Harness Adapters: Train Your Model for Any Coding Agent** (Top pick; agents_mcp_skills; youtube) - Relevant to an agent-builder: Hugging Face's harness adapters are small RL-trained LoRA add-ons that tune an open model for one specific coding agent (pi), with a reward-hacking guard, and the video…
  - Link: https://www.youtube.com/watch?v=4NzM2hcWp1s

- **anthropics/anthropic-sdk-python v2.13.0** (Top pick; dev_tooling; github) - Claude Opus 4.5 is now marked deprecated with end-of-life January 22, 2027, so code pinned to it needs migrating; the SDK also adds Message Batches error codes and webhook events.
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.13.0

- **You can now install Claude artifacts as desktop apps on Mac and Windows. Ask Claude to build an art…** (Top pick; dev_tooling; x) - Claude artifacts can now be installed as native Mac and Windows desktop apps that use your connectors, notifications, and menu bar items, which is a quick new way to ship small tools.
  - Link: https://x.com/ClaudeDevs/status/2125315491522650299

- **Claude just opened a directory of 10,000+ plugins, and it works on the free plan. → Connectors (you…** (Top pick; agents_mcp_skills; x) - Anthropic has consolidated connectors and skills into one plugin directory of 10,000+ entries now available on the free plan, though this post is a secondhand summary that needs checking against the…
  - Link: https://x.com/RoundtableSpace/status/2125156217396035703

- **Vercel Labs' UI SDK is a beta, Apache-2.0 library of behaviors that handle keyboard navigation, foc…** (Top pick; agents_mcp_skills; x) - Vercel Labs' Apache-2.0 beta UI SDK gives agents accessible keyboard, focus, and ARIA behaviors across React, Vue, Svelte, Solid, and Web Components, installable as an agent skill today.
  - Link: https://x.com/RoundtableSpace/status/2125088269322825943

- **Replit just open-sourced a self-hosted alternative to Datadog. DataCat puts metrics, logs, traces, …** (Top pick; repo_library; x) - Replit's open-source DataCat is a self-hosted Datadog alternative that accepts OpenTelemetry and Datadog agent traffic, so existing instrumentation could be pointed at it with minimal changes.
  - Link: https://x.com/RoundtableSpace/status/2124778730211934439

- **safe-anything is a free, MIT-licensed Rust scanner that finds vulnerabilities, leaked secrets and r…** (Top pick; agents_mcp_skills; x) - A free, MIT-licensed Rust scanner that audits MCP and Claude Code/Codex/Cursor agent settings plus locked dependencies, runnable in CI with no account or upload.
  - Link: https://x.com/RoundtableSpace/status/2125012771637248181

- **Zero data retention with Enterprise Frontier Safeguards is now in public beta for eligible orgs on …** (Top pick; dev_tooling; x) - Zero data retention plus Enterprise Frontier Safeguards is in public beta for eligible orgs, so Messages API traffic can be stored only in your own encrypted cloud storage, with a relevant compliance…
  - Link: https://x.com/ClaudeDevs/status/2124930253344948518

- **OpenAI and Cisco introduce Shirudo** (Top pick; repo_library; web) - An open-source Linux runtime from OpenAI and Cisco that protects running systems during patch rollouts, relevant to agent sandboxing and security for an agent-focused builder.
  - Link: https://openai.com/index/introducing-shirudo

- **Don't rewrite your app in Rust. Rewrite the 5% that's slow. The tool, fast-anything, profiles your …** (Top pick; repo_library; x) - Relevant to agentic coding: it uses Claude Code or Codex to port only the profiled hot functions to Rust, with replay-based equivalence checks and a reversible swap-in.
  - Link: https://x.com/RoundtableSpace/status/2124763630092824618

- **GPT-6 models demonstrate intrinsic protein-design capabilities** (Top pick; model_release; web) - This is a biology-capability announcement with no direct tooling, API, or agent-workflow change for your Claude/Salesforce/TypeScript stack, so it's low relevance beyond general model-capability cont…
  - Link: https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities

- **Finally, a way to stop AI from making those ugly, generic diagrams. Diagram Design is a free, open-…** (Top pick; agents_mcp_skills; x) - It's a free, open-source Claude Code/Codex skill installable via `npx skills add`, generating brand-matched HTML diagrams, a quick win to test this week.
  - Link: https://x.com/RoundtableSpace/status/2124922175190651097

- **Inkling 2 Mini** (Notable; model_release; email) - Inkling 2 Mini is an open-weight 26.4B coding-strong model that could be self-hosted as a cheaper alternative for agentic coding workflows, though its benchmark lead is unverified until you test it o…
  - Link: https://thinkingmachines.ai/news/inkling-2-mini/?utm_source=tldrai

- **Everything new in Claude this month** (Notable; model_release; youtube) - Covers a month of Claude releases including Claude Code on desktop, MCP-style interactive connectors, and Fable 5.2, so check the linked docs for any API or workflow changes.
  - Link: https://www.youtube.com/watch?v=EuOg5f_Egns

- **Researchers plant 2m canaries into the AI supply chain** (Notable; research; email) - Researchers found AI supply-chain leaks of secrets at scale, which matters for anyone wiring agents and MCP servers to real credentials and needs to audit where those keys can end up.
  - Link: https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/?utm_source=tldrnewsletter

- **Lessons from building agents on the Claude Platform** (Notable; agents_mcp_skills; youtube) - Anthropic's own write-up on Claude Managed Agents architecture, covering harness/execution separation and multi-agent workflows, relevant to anyone building on the Claude Platform (features still bet…
  - Link: https://www.youtube.com/watch?v=8Aoq6mJeAXI

- **I Tested Vercel Workflow SDK 4 vs 5: v4 Didn't Finish** (Notable; dev_tooling; youtube) - Vercel Workflow SDK v5 replays durable steps incrementally while v4 slowed and failed to finish a 1,020-step run, so v4 users may want to migrate.
  - Link: https://www.youtube.com/watch?v=L6cTtkHyvXA

- **We've redesigned the side panel in Claude Code on desktop. Files, Changes, Terminal and your other …** (Notable; dev_tooling; x) - Claude Code desktop's side panel now holds Files, Changes, and Terminal as tabs beside your session, with Windows and Linux support still pending.
  - Link: https://x.com/ClaudeDevs/status/2124978802006851961

- **Stitch Skills** (Notable; agents_mcp_skills; email) - Google's open-sourced Stitch skills package reusable agent workflows for the Stitch MCP server, directly usable in Claude Code or the Agent SDK with a quick install.
  - Link: https://github.com/google-labs-code/stitch-skills?utm_source=tldrdev

- **skill-distill has Claude Code or Codex write a skill from a good session, then tests it on a cheape…** (Notable; agents_mcp_skills; x) - It gives a concrete way to turn a successful Claude Code or Codex session into a reusable skill, validated by running it on a cheaper open-weight model before you approve it.
  - Link: https://x.com/RoundtableSpace/status/2125352510714179847

- **erkamyaman/safe-anything** (Notable; repo_library; github) - A fast Rust scanner covering XSS, SQLi, secrets, dependency CVEs, and AI agent configs, directly relevant to auditing agent setups like Claude Code and MCP servers before deployment.
  - Link: https://github.com/erkamyaman/safe-anything

- **12 Rules for a Software Factory That Doesn't Ship Slop — Dex Horthy, Factory** (Notable; research; youtube) - This talk's Slop Code Bench data (best model at about 16% on evolving code bases over time) plus its 12 practices for agent-built software give concrete guidance for quality gates in an agentic codin…
  - Link: https://www.youtube.com/watch?v=-NFMsM2y0Vk

## 2026-11-23

- **Claude Code 2.1.328-2.1.330** (AI/Claude tooling) - Latest releases add org sign-in via `claude auth login` for Enterprise Admin Console, `"onFailure": "block"` for `mcp_tool` hooks, auto mode on Bedrock/Vertex/Foundry for Opus 4.6 and Sonnet 4.6, and a built-in `easel` charting mod.
  - Why it matters: fail-closed MCP hooks let you build guardrails that actually stop an action when the check errors; the `/mcp` "Server message" row speeds up debugging remote MCP servers; `/tasks` now shows scheduled tasks and `/loop` wakeups.
  - Link: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

- **Headroom** (GitHub repo) - Context-compression layer (library, proxy, MCP server, `headroom wrap` for coding agents) that shrinks tool outputs, logs and RAG chunks before they reach the LLM.
  - Why it matters: could cut token cost in long agent sessions; its self-reported savings are 21-57% on agent scenarios (unverified).
  - Link: https://github.com/headroomlabs-ai/headroom
  - Safety note: Apache-2.0, ~80k stars, active (3.8k commits). Anonymous telemetry on by default (disable with `HEADROOM_BEACON=off`/`DO_NOT_TRACK=1`); `wrap` reroutes agent traffic via a local proxy and edits agent config, so review before enabling. Last commit date not verified; not newly created.

## 2026-11-22 (AKD)

- **Looped Transformers: 2x Deeper Without More Weights** (Top pick; research; youtube) - Explains looped transformers (Inkling 2 Mini runs 12 of its 24 layers three times, 48 effective layer steps) and their trade-offs, with an open model you can run via Ollama to test the idea.
  - Link: https://www.youtube.com/watch?v=TPtfyKEAk6c

- **DataCat** (Top pick; repo_library; email) - Self-hosted, open-source observability for metrics, logs, and traces that accepts OpenTelemetry and Datadog-compatible traffic, a possible drop-in for monitoring agent or Vercel-hosted services witho…
  - Link: https://github.com/replit/datacat?utm_source=tldrdev

- **Cloudflare's Clairic and Clairic-flash** (Top pick; model_release; email) - Cloudflare released open weights for Clairic and Clairic-flash, field-extraction models for text, images, and PDFs, which you could self-host or test against Claude-based extraction pipelines.
  - Link: https://blog.cloudflare.com/open-clairic/?utm_source=tldrai

- **Gemini 4 Neon vs Carbon: Which One Should You Actually Use?** (Top pick; model_release; youtube) - Gemini 4 Neon ($3/$15 per million tokens) reportedly beats Gemini 4 Carbon on Google's benchmark, but the "cheaper per task" claim depends on Carbon's promo pricing expiring November 30.
  - Link: https://www.youtube.com/watch?v=pYAczC5IgCU

- **Models Engineering Index** (Top pick; research; email) - It ranks language models on public engineering benchmarks against cost and token usage, useful for choosing which model to use in coding agents and API builds.
  - Link: https://git-aarvin.github.io/mei/?utm_source=tldrdev

- **pritamux/gridlines** (Top pick; agents_mcp_skills; github) - An agent skill that overlays alignment guide lines on a rendered UI to catch misaligned elements, useful for a Tailwind/React frontend pass with Claude Code.
  - Link: https://github.com/pritamux/gridlines

- **Perplexity's Self-Improving Skills** (Top pick; agents_mcp_skills; email) - Perplexity's agent now writes and updates its own reusable skills from past sessions, a self-improving pattern relevant to anyone building skill- or plugin-based agent workflows.
  - Link: https://www.perplexity.ai/hub/blog/self-improving-skills?utm_source=tldrai

- **DaisyRose 27B Locally: Pushing the Boundaries of Original Qwen** (Notable; model_release; youtube) - A local-runnable 27B multimodal reasoning model from RadixArk, built on Qwen3-series weights with RL-only training, relevant if you want to self-host a coding or reasoning model.
  - Link: https://www.youtube.com/watch?v=yDQBz77Jzpc

## 2026-11-22

- **Claude Code v2.1.328 / v2.1.329** (AI/Claude) - Auto mode extended to Opus 4.6 and Sonnet 4.6 on Bedrock, Google Cloud, Foundry and the Claude apps gateway; `"onFailure": "block"` now works for `mcp_tool` hooks; `/tasks` lists scheduled tasks, `/loop` wakeups and forks; `/mcp` shows the JSON-RPC error from refusing remote servers.
  - Why it matters: blocking MCP-tool hooks let you enforce guardrails on MCP calls, and the trust dialog now shows where a folder's hooks are declared (safer when cloning unfamiliar repos).
  - Link: https://github.com/anthropics/claude-code/releases

- **Linked billing for the Claude API (beta)** (AI/Claude) - Customers can pay for Claude usage in your app through their own Claude organization; set `billing_policy` on `/v1/messages` (Nov 17, beta header `user-profiles-billing-2026-10-01`).
  - Why it matters: if you ship an app on top of Claude, users can bring their own billing with spend caps, so you stop fronting API cost. Only works for orgs that pay Anthropic directly.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Self-hosted Claude Managed Agents** (AI/Claude) - The full Managed Agents service (agent/session storage and history) can run on your own infrastructure (Nov 12); access via your Anthropic account team.
  - Why it matters: lets regulated or data-resident projects use hosted-agent infrastructure without sending session data to a third-party service.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude Fable 5.2 / Mythos 5.2 API changes** (AI/Claude) - Released Nov 9 (older than the usual window but with breaking changes): 1M context, 128k output, always-on adaptive thinking, $8/$40 per MTok, fast mode via `speed: "fast"`. Prefix check enforced (editing system/tools/earlier messages then resending a thinking block returns 400), computer use needs `computer_toolset_20260801`.
  - Why it matters: check existing agent loops that rewrite history or use the old computer-use tool before switching models.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **alibaba/open-code-review** (GitHub) - AI code-review CLI that reads Git diffs, runs an LLM agent, and emits line-level comments; also a `scan` mode and a mode that delegates review to your host coding agent.
  - Why it matters: drop-in pre-merge/CI review step; mixes deterministic pipelines with an LLM. Benchmark claims (vs Claude Code) are the authors' own.
  - Link: https://github.com/alibaba/open-code-review
  - Safety note: Apache-2.0, ~55k stars, 906 commits, backed by Alibaba. Last-commit date not verified. Install uses npm/skills scripts and the repo ships agent config files (CLAUDE.md, plugin dirs), so review before opening in an agent. Code goes to whichever LLM endpoint you configure.

- **backnotprop/plannotator** (GitHub) - Local browser UI to annotate agent plans, markdown and diffs/PRs and send feedback back to Claude Code, Codex, OpenCode, etc.
  - Why it matters: structured human-in-the-loop review of agent plans before they execute.
  - Link: https://github.com/backnotprop/plannotator
  - Safety note: Apache-2.0 or MIT, ~14k stars, ~12k commits, provenance/SHA256 provided for binaries. Last-commit date not verified. Installer is curl-pipe-to-shell (verify first); remote mode binds 0.0.0.0 with no login; optional Jina Reader and share links are third-party.

- **GoogleChrome/modern-web-guidance-src** (GitHub) - Skills and CLI (`search`, `retrieve`, `legacy-scan`) that keep coding agents on current web-platform best practices (262 features, 204 use cases), stewarded with Chrome, Edge, Firefox and MDN teams.
  - Why it matters: stops agents generating legacy CSS/JS patterns when you ask for frontend work.
  - Link: https://github.com/GoogleChrome/modern-web-guidance-src
  - Safety note: Apache-2.0, ~10k stars, 1.6k commits, major-vendor backing. Last-commit date not verified. Quickstart runs `npx ...@latest`; pin a version.

## 2026-11-21 (AKD)

- **Gemini 4 Neon Is Here, And It’s a Beast!** (Top pick; model_release; youtube) - A new Gemini 4 Neon model for coding and knowledge work, with early-access demos and a Google AI Studio entry point, worth a look for model-choice decisions.
  - Link: https://www.youtube.com/watch?v=Q0ShBenKyqo
  - Also covered by: [Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/?utm_source=tldrai) (email)
  - Also covered by: [Gemini 4 Neon vs Carbon: Which One Should You Actually Use?](https://www.youtube.com/watch?v=pYAczC5IgCU) (youtube)

- **Thinking Machines just released a 26B model that runs on your laptop, and on its own benchmarks it …** (Top pick; model_release; x) - A 26B open-weights model (3.4B active, ~20GB memory) claiming 79.2% on SWE-bench Verified and runnable locally via Ollama, which is worth verifying against the official release before relying on it.
  - Link: https://x.com/RoundtableSpace/status/2124099253039771892
  - Also covered by: [Inkling 2 Mini vs Qwen 3.8 27B: Worth It on a PC?](https://www.youtube.com/watch?v=av9e098JVOs) (youtube)

- **anthropics/claude-code v2.1.330** (Top pick; dev_tooling; github) - Claude Code v2.1.330 adds enterprise org sign-in and a `--start-dir` option for the self-hosted runner, plus new plugin-install JSON fields that scripts parsing that output may need to handle.
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.330

- **Craft Anything is an open-source Rust engine that studies how a website, app or game works, has a c…** (Top pick; agents_mcp_skills; x) - Open-source Rust engine that has a coding agent reverse-engineer and rebuild a target site or app, with 320 MCP-exposed tools a reader's agent could drive directly.
  - Link: https://x.com/RoundtableSpace/status/2124001105512464726

- **PostgreSQL 19 Released** (Top pick; dev_tooling; email) - PostgreSQL 19 adds concurrent table repacking and standby write-wait semantics, useful for your Salesforce-adjacent backends but not an immediate change to your stack.
  - Link: https://www.postgresql.org/about/news/postgresql-19-released-3449/?utm_source=tldrdev

- **When Agent Swarms Outperform Solo Coders** (Top pick; research; email) - Replit's benchmark shows 32 parallel Opus agents hit an 18.9x NumPy speedup versus 3.7x for one, useful for deciding when multi-agent setups pay off despite higher compute cost.
  - Link: https://frontier.replit.com/throwing-headcount-at-the-problem/?utm_source=tldrai

- **Top 10 Things AI Gets Wrong in Web Development** (Top pick; research; email) - Coding agents passed only 52% of Chrome's web dev checks unaided versus 91% with Modern Web Guidance, a concrete gap to close in your React/Tailwind workflow.
  - Link: https://developer.chrome.com/blog/top-10-things-ai-gets-wrong-in-web-dev?utm_source=tldrdev

- **Crashlytics for Web Is Now in Public Preview** (Top pick; dev_tooling; email) - Firebase Crashlytics now groups browser JavaScript errors and alerts on new or regressed issues, a low-effort addition for a React/Vite/Vercel app with a clear first step of enabling it.
  - Link: https://firebase.blog/posts/2026/11/crashlytics-web-public-preview?utm_source=tldrdev

- **One of DeepSeek's earliest researchers just open-sourced a personal AI agent that runs a 125B model…** (Top pick; agents_mcp_skills; x) - Open-source local agent claiming to run a 125B model on a 12GB GPU via GPU/RAM offloading; the claim is unverified, so test before relying on it.
  - Link: https://x.com/RoundtableSpace/status/2124114352114463212

- **You can train your own LLM from scratch for about 40 cents. MiniMind has 67.9K stars, and it walks …** (Top pick; repo_library; x) - A 64M-parameter open-source repo (MiniMind) that trains an LLM end to end in about 2 hours on one RTX 3090, a concrete hands-on way to learn pretraining, SFT, LoRA, DPO and GRPO.
  - Link: https://x.com/RoundtableSpace/status/2124106802098995410

- **Google’s Elephant-Goldfish Model: Design First, Code Last** (Top pick; agents_mcp_skills; youtube) - Elephant-Goldfish is an open-source Google plugin for agent-driven design review before coding, relevant to a Claude Code workflow and adoptable with a single install step.
  - Link: https://www.youtube.com/watch?v=Gl8ecFo9X80

- **SAVE THIS: 14 free repos that let Claude Code make game-ready 3D models for you. → Blender MCP and …** (Top pick; agents_mcp_skills; x) - A curated pipeline of free open-source MCP servers and tools that lets Claude Code drive Blender and clean up, UV-unwrap, texture, and optimize 3D models; the Blender MCP install command is included.
  - Link: https://x.com/RoundtableSpace/status/2124121902046130364

- **w01fb0ss/PiBot** (Top pick; agents_mcp_skills; github) - Open-source local-first desktop agent team with MCP support, computer use, and approval gates, built on the pi agent framework; relevant to agent infrastructure and MCP tooling, though at 145 stars i…
  - Link: https://github.com/w01fb0ss/PiBot

- **How to turn a GTA 6 stream into vertical clips for free. a new MIT repo, GTA Auto Clipper, finds th…** (Top pick; repo_library; x) - A free MIT-licensed Python/FFmpeg tool that auto-generates captioned 9:16 clips from live streams, relevant to the reader's AI-tooling interests, though it is a video-content workflow rather than a c…
  - Link: https://x.com/RoundtableSpace/status/2124038854365868118

- **Stop wasting hours copying information from websites into ChatGPT. Firecrawl is an open-source tool…** (Top pick; repo_library; x) - Firecrawl is an open-source web-to-markdown tool with a free API tier that can feed clean page data straight into Claude or an agent workflow, a quick win to test.
  - Link: https://x.com/RoundtableSpace/status/2124220048378105984

- **LIUFelix2004/dsh-workbuddy** (Top pick; repo_library; github) - It bundles WorkBuddy accounts into DeepSeek Harness as model providers, including an automatic workaround for a gateway channel check (error 11128), a possible fragility point if that check changes.
  - Link: https://github.com/LIUFelix2004/dsh-workbuddy

- **Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use** (Notable; industry_business; email) - Windows 11 appears to log which coding agents and developer tools run on the machine, a privacy and telemetry concern for anyone running agentic tools locally.
  - Link: https://xusheng.dev/posts/windows-coding-agent-telemetry/?utm_source=tldrdev

- **Stripe evals: Measuring real-world coding agent performance** (Notable; research; email) - Stripe's open evals show frontier coding agents can build working Stripe integrations but often skip best practices, a useful yardstick for judging agent output on payment code.
  - Link: https://stripe.dev/blog/stripe-integration-evals-methodology?utm_source=tldrai

- **Apple Is Working on AI Agent for Device Control, Apps, Browsing and Coding** (Notable; industry_business; email) - Apple's planned agent would control apps, browsers, and APIs on macOS, and its warning prompt for third-party agent control signals new permission gates for agents like Claude Code on Mac.
  - Link: https://www.bloomberg.com/news/articles/2026-11-19/apple-is-working-on-ai-agent-for-device-control-apps-browsing-and-coding?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc5NTE1Mjg1OSwiZXhwIjoxNzk1NzU3NjU5LCJhcnRpY2xlSWQiOiJUT1I5MEtLSkg2VjUwMCIsImJjb25uZWN0SWQiOiI2NTc1NjkyN0UwMkM0N0MwQkQ0MDNEQTJGMEUyNzIyMyJ9.DNgJTKuQu7QIBBw3KLL5QMx5EfNQt2XAf4UlPajQr2U&utm_source=tldrnewsletter

- **Vercel Board** (Notable; agents_mcp_skills; email) - Vercel's experimental Board lets AI agents claim tasks and share context, relevant to your agentic workflow and Vercel deployments, though it's early and unproven.
  - Link: https://vercel.com/blog/introducing-vercel-board?utm_source=tldrai

- **What Runs Where? Local AI in Production — Ahmad Osman, Osmantic** (Notable; research; youtube) - Covers practical choices for running local models in production (quantization, hardware, inference engines, batching, speculative decoding), relevant to an AI builder deciding what to self-host versu…
  - Link: https://www.youtube.com/watch?v=GKSQYbELDzw

## 2026-11-21

- **Claude Code v2.1.328-v2.1.330** (AI/Claude tooling) - Three releases in two days: v2.1.330 adds a built-in "easel" mod that draws charts on request and under MCP metrics results, org-settings/gateway applied after `claude auth login`, and fixes for post-compaction freezes and `ExitWorktree` deleting worktrees used by other sessions.
  - Why it matters: v2.1.328 extends auto mode to Opus 4.6/Sonnet 4.6 on Bedrock, Google Cloud, Foundry and the Claude apps gateway, and `"onFailure": "block"` now works for `mcp_tool` hooks, so MCP-based guardrails can actually block. v2.1.329 shows where a folder's hooks are declared in the trust dialog and `/tasks` now lists scheduled tasks and `/loop` wakeups.
  - Link: https://github.com/anthropics/claude-code/releases

- **anthropic-sdk-python v2.10.0-v2.12.0** (AI/Claude tooling) - v2.12.0 (Nov 20) fixes Bedrock to send `user_profile_id` in the request body; v2.11.0 adds Claude Code managed settings to the Admin API and caches structured-output schema building; v2.10.0 adds beta `billing_policy` and renames error data models.
  - Why it matters: Bedrock requests with a profile ID to models that lack profile support now return 400, so remove the ID there. Old error model names are deprecated in v2.10.0, so check any code that references them.
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases

- **Claude Agent SDK (Python) v0.2.187** (AI/Claude tooling) - New release on Nov 20 (v0.2.186 on Nov 19); the release page lists no changelog text.
  - Why it matters: Worth pinning or upgrading if you build agents on the SDK. Read the commits before upgrading, since I could not verify what changed.
  - Link: https://github.com/anthropics/claude-agent-sdk-python/releases

- **MCP spec 2026-07-28 in Claude** (AI/Claude tooling) - Older than the 7-day window, but still being rolled out. The spec makes MCP stateless request/response, ships MCP Apps (interactive UI) and Tasks (long-running work) as versioned extensions, and aligns auth with OAuth 2.0/OIDC. Anthropic says support is "rolling out across Claude products soon" and mentions MCP tunnels (research preview) for private-network servers.
  - Why it matters: A stateless core means MCP servers can run on serverless and edge platforms, and OIDC auth suits enterprise identity providers (Entra, Okta).
  - Link: https://claude.com/blog/bringing-mcp-2026-07-28-to-claude

No new GitHub repos made this digest. The ones I found (e.g. NousResearch/hermes-agent, MIT, about 265k stars) are neither new nor newly trending, and its pipe-to-shell installer is not something I could vouch for.

## 2026-11-20 (AKD)

- **Google launches Gemini 4 Neon** (Top pick; model_release; email) - Gemini 4 Neon is now live via API with a 1M-token context at $3/$15 per million input/output tokens, a direct cost comparison for your Claude API workloads.
  - Link: https://www.testingcatalog.com/google-launches-gemini-4-neon-on-gemini-antigravity-and-apis/?utm_source=tldrnewsletter
  - Also covered by: [Gemini 4 Neon Is Here, And It’s a Beast!](https://www.youtube.com/watch?v=Q0ShBenKyqo) (youtube)
  - Also covered by: [Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/?utm_source=tldrai) (email)
  - Also covered by: [Google just released Gemini 4 Neon, and on its own benchmarks it beats GPT-6.2 Sol and Claude Opus …](https://x.com/RoundtableSpace/status/2123676466269577239) (x)
  - Also covered by: [Gemini 4 Neon vs Carbon: Which One Should You Actually Use?](https://www.youtube.com/watch?v=pYAczC5IgCU) (youtube)

- **anthropics/claude-code v2.1.329** (Top pick; dev_tooling; github) - Claude Code v2.1.329 fixes a `~/.claude.json` reset that could lose settings and a macOS Keychain sign-out loop, and adds hook-source trust warnings worth reviewing if you use managed hooks.
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.329

- **anthropics/anthropic-sdk-python v2.12.0** (Top pick; dev_tooling; github) - Bedrock users passing a user profile ID will now see it applied, but requests to Bedrock models without profile support will start returning 400 errors, so remove the ID for those.
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.12.0

- **FastFrames: Video Generation at Interactive Latency** (Top pick; model_release; email) - Apple's FastFrames reports 480p video generation at 36 ms per frame on one GPU, which matters for interactive video tooling if the weights and license are usable outside research.
  - Link: https://apple-aiml-research.github.io/ml-fastframes/?utm_source=tldrai

- **Introducing Tool Retrieval in the Gemini API** (Top pick; dev_tooling; email) - Gemini API now auto-selects and runs registered functions from input, relevant as an alternative to manual tool-calling loops in agent builds, though it's Google-specific rather than a Claude-stack c…
  - Link: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/?utm_source=tldrai

- **OpenAI just put ChatGPT's new voice model in the API, and idle time now costs less than half. → $0.…** (Top pick; model_release; x) - OpenAI's ChatGPT voice model is now in the API as "gpt-live-1.1" at $0.05/min talking and $0.02/min idle, relevant if you're building voice agents or coding companions.
  - Link: https://x.com/RoundtableSpace/status/2123684016213684411

- **Let Gemini tackle repetitive chores on your Mac** (Top pick; model_release; email) - Gemini's Mac app now runs multi-step computer-use tasks across local files, apps, and the web, with approval gates, relevant to anyone tracking agent sandboxing and permission design.
  - Link: https://blog.google/innovation-and-ai/products/gemini-app/computer-use-mac/?utm_source=tldrai

- **Engineer Your Coding Agents Like Any Other System — Zach Lloyd, Warp** (Top pick; agents_mcp_skills; youtube) - Covers treating cloud coding agents as a measured, code-defined system (sandboxing, swappable models, online evals, orchestration), directly relevant to scaling Claude Code and Agent SDK workflows be…
  - Link: https://www.youtube.com/watch?v=0LeT996Hz3E

- **CLI-Anything is an open-source project that turns software into command-line tools AI agents can op…** (Top pick; agents_mcp_skills; x) - CLI-Anything is a Claude Code plugin that generates agent-operable CLIs from any project, installable in three commands for a quick trial.
  - Link: https://x.com/RoundtableSpace/status/2123585869433249932

- **Apple just released Depth Pro 2, and the model is free to download. → Turns any single photo or vid…** (Top pick; model_release; x) - A free, open depth-estimation model from Apple that works on single photos and video frame by frame, relevant for AR, 3D effects, and vision pipelines.
  - Link: https://x.com/RoundtableSpace/status/2123751964529807479

- **Gemini 4 Neon: Google’s Middle Model Tested** (Top pick; model_release; youtube) - The video tests Google's Gemini 4 Neon model against a mega test prompt, but the description actually centers on a Qwen LoRA adapter install, so the Gemini coverage may be thin; check the linked Goog…
  - Link: https://www.youtube.com/watch?v=sZU2I8_uoeg

- **Make AI videos for free on the computer you already own. → Runs MiniMax H3, one of the top video mo…** (Top pick; repo_library; x) - Runs MiniMax H3 video generation locally on 8GB VRAM with Claude Code or Codex driving it, a possible free alternative to paid video APIs, though the claims are unverified.
  - Link: https://x.com/RoundtableSpace/status/2123744415164272906

- **INK-Q/agy-fast** (Top pick; agents_mcp_skills; github) - It's an MCP plugin claiming to cut Antigravity LLM turns, tokens, and upload traffic without changing the native UI or diffs, so worth a look if you use Antigravity alongside MCP tooling, though the…
  - Link: https://github.com/INK-Q/agy-fast

- **zavi2997-droid/claude-code-agent-workspace** (Top pick; agents_mcp_skills; github) - Relevant to your Claude Code and Agent SDK workflows: it offers a pattern for running composable agents across isolated workspaces, though at 96 stars its maturity needs checking before adoption.
  - Link: https://github.com/zavi2997-droid/claude-code-agent-workspace

- **Deploying Daybreak Red** (Top pick; agents_mcp_skills; web) - It's a reference architecture for running supervised security investigations with OpenAI's Daybreak Red, covering safety controls and monitoring, relevant to agent sandboxing and security patterns.
  - Link: https://openai.com/business/learn/deploying-daybreak-red

- **Meet the New Docker, Built to Run on Trust** (Notable; agents_mcp_skills; email) - Docker Sandboxes for isolated agent coding environments and AI Governance for agent access control are directly relevant to agent sandboxing and security work you're tracking.
  - Link: https://www.docker.com/blog/meet-the-new-docker-built-to-run-on-trust/?utm_source=tldrdev

- **Mirror Dimension for Agents: Evaluating Browser-Use Agents Without the Web** (Notable; agents_mcp_skills; email) - Google's "Mirror Dimension" offers a sandboxed replica for evaluating browser-use agents without live-web risk, relevant to agent security and eval workflows.
  - Link: https://blog.google/security/mirror-dimension-for-agents/?utm_source=tldrai

- **PINE, a Reactive Harness for Agents** (Notable; agents_mcp_skills; email) - PINE is an open-source event-driven agent harness that triggers agents on file changes, webhooks, or Telegram messages, a direct fit for building reactive Claude Agent SDK workflows on macOS or Linux.
  - Link: https://github.com/pmndre/pine?utm_source=tldrdev

- **Connect Your Team’s Data to ChatGPT** (Notable; agents_mcp_skills; youtube) - OpenAI's ChatGPT now supports admin-installed Data plugins, Snowflake connections, and custom MCP servers, which is directly relevant to MCP-based agent integration work.
  - Link: https://www.youtube.com/watch?v=oJIuz3AFfEQ

- **Sandboxed Models Can Communicate via Inference Servers** (Notable; agents_mcp_skills; email) - Models sharing one inference server can signal each other through timing and load effects, so sandboxing alone may not isolate multi-agent or multi-tenant deployments.
  - Link: https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being?utm_source=tldrai

- **How to build an agent that builds the culture — Zach Bruggeman, Ramp** (Notable; agents_mcp_skills; youtube) - This talk covers how Ramp's internal agent Inspect writes about 75% of its code, with concrete practices like shared agent tooling and visible verification that a team lead could copy this week.
  - Link: https://www.youtube.com/watch?v=MDI81OaZAD4

## 2026-11-20

- **Claude Fable 5.2 and Mythos 5.2** (AI/Claude) - New Claude models launched Nov 9 with 1M context, 128k max output, $8/$40 per MTok, plus a per-request fast mode for Fable 5.2.
  - Why it matters: new top-tier option for agentic coding; fast mode needs no beta header. Opus 4.8 fast mode is removed Nov 30, so migrate if you rely on it.
  - Link: https://platform.claude.com/docs/en/release-notes/overview

- **Message threads (beta)** (AI/Claude) - Server-side conversation state so later requests send only new messages (Nov 2).
  - Why it matters: smaller requests and lower time-to-first-token for long chats and agent loops.
  - Link: https://platform.claude.com/docs/en/release-notes/overview

- **Self-hosted Claude Managed Agents** (AI/Claude) - Run the whole Managed Agents service on your own infrastructure (Nov 12, access by request via account team).
  - Why it matters: lets teams with data-residency needs use hosted-agent workflows.
  - Link: https://platform.claude.com/docs/en/release-notes/overview

- **Linked billing (beta)** (AI/Claude) - Customers can pay for Claude usage in your app through their own Claude organization (Nov 17).
  - Why it matters: removes the need to proxy and resell inference when building apps on Claude.
  - Link: https://platform.claude.com/docs/en/release-notes/overview

- **Claude Code v2.1.327-v2.1.329** (AI/Claude) - `claude mcp add-json <name> -` reads server JSON from stdin (keeps tokens off the command line); `/status` flags broken skills/hooks/permissions; `/tasks` now lists scheduled tasks, loops and forks; hook trust dialog shows where hooks are declared; auto mode extended to Bedrock/Vertex/Foundry.
  - Why it matters: safer MCP setup and easier debugging of agent config.
  - Link: https://github.com/anthropics/claude-code/releases

No GitHub repos added today: the trending candidates I found (e.g. NousResearch/hermes-agent, MIT, ~265k stars) are not new and I could not verify recent commit activity from the primary page.

## 2026-11-19 (AKD)

- **[AINews] Gemini 4 Neon: GDM's Opus/Sol Contender** (Top pick; model_release; web) - Gemini 4 Neon is a new mid-tier model at $3/$15 per million tokens with a 1M-token context, available in the paid Gemini API, Antigravity, and Cursor and GitHub Copilot, so it's worth testing as a dr…
  - Link: https://latent.space/p/ainews-gemini-4-neon-gdm-s-opus-sol-contender/
  - Also covered by: [Google launches Gemini 4 Neon on Gemini, Antigravity, and APIs](https://www.testingcatalog.com/google-launches-gemini-4-neon-on-gemini-antigravity-and-apis/?utm_source=tldrnewsletter) (email)
  - Also covered by: [Gemini 4 Neon Is Here, And It’s a Beast!](https://www.youtube.com/watch?v=Q0ShBenKyqo) (youtube)
  - Also covered by: [Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/?utm_source=tldrai) (email)

- **anthropics/claude-code v2.1.328** (Top pick; dev_tooling; github) - Claude Code v2.1.328 adds auto mode for Opus 4.6 and Sonnet 4.6 on Bedrock, Vertex and Foundry, and new hook failure-blocking (`onFailure: block`) for `mcp_tool` hooks, so check any MCP hook setups t…
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.328

- **Apple just released an open video model that makes video almost as fast as you can watch it. → Abou…** (Top pick; model_release; x) - Apple's open real-time video model (1.3B and 14B, weights on Hugging Face, ~28 fps on one GPU) is relevant to the reader's AI image/video tooling, though the post is a secondhand summary and the clai…
  - Link: https://x.com/RoundtableSpace/status/2123336727846855037

- **anthropics/anthropic-sdk-python v2.11.0** (Top pick; dev_tooling; github) - The Python SDK v2.11.0 adds Claude Code managed settings to the Admin API and fixes space encoding in query strings, which matters for AWS SigV4-signed requests.
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.11.0

- **Qwen4-Max vs Opus 5.5: 4x Cheaper Tokens, Same Bill** (Top pick; research; youtube) - Per solved task, Qwen4-Max costs about the same as Opus 5.5 here ($0.25 vs $0.22) despite the 4x lower token price, solving 11/15 vs 15/15 and hitting token-budget dead ends.
  - Link: https://www.youtube.com/watch?v=lunalDg5928

- **Post-Training Gemini 4 for Real Engineering Work — Melvin Johnson, Google DeepMind** (Top pick; model_release; youtube) - Covers how Gemini 4 is post-trained for real engineering work, including rubric grading and reward-hacking resistance, relevant to judging coding agents beyond passing tests.
  - Link: https://www.youtube.com/watch?v=fTHByDwTxGM

- **Introducing GPT-6.2 Astra and Sol** (Top pick; model_release; web) - New OpenAI model family (Astra and Sol) with coding and computer-use gains across Codex and the API, so a comparison benchmark for Claude Code and Agent SDK workflows and a possible model-swap candid…
  - Link: https://openai.com/index/introducing-gpt-6-2-astra-sol
  - Also covered by: [OpenAI launches GPT-6.2 Astra and Sol](https://www.testingcatalog.com/openai-launches-gpt-6-2-astra-and-sol-on-chatgpt-and-apis/?utm_source=tldrnewsletter) (email)

- **OpenAI's Codex CLI 0.170 adds realtime voice calls in the terminal over WebRTC, plus experimental s…** (Top pick; dev_tooling; x) - Codex CLI 0.170 adds terminal voice calls over WebRTC and same-name MCP server support across environments, relevant if you use Codex alongside your MCP setup.
  - Link: https://x.com/RoundtableSpace/status/2123268780247900587

- **Unauthenticated Remote Code Execution in NGINX** (Top pick; other; email) - Two critical unauthenticated HTTP/2 memory-safety flaws in NGINX allow remote code execution, so patch any NGINX instance fronting your deployments or side-project hosting now.
  - Link: https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities?utm_source=tldrdev

- **Cloudflare CLI 1.0 Release Candidate** (Top pick; dev_tooling; email) - A release candidate for Cloudflare's CLI 1.0 stabilizes config and build formats, so it's worth testing now before the final release locks them in for your Vercel and Workers workflows.
  - Link: https://developers.cloudflare.com/changelog/post/2026-11-17-release-candidate/?utm_source=tldrdev

- **Genie 4** (Top pick; model_release; email) - Genie 4 is a world-generation model, not a coding or agent API, so it has little direct bearing on your Claude, Salesforce, or React work beyond general AI-video context.
  - Link: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/?utm_source=tldrai
  - Also covered by: [Google just launched Genie, its most realistic interactive world model yet. >⁠Edit environments mid…](https://x.com/RoundtableSpace/status/2123465074648166824) (x)

- **CodeAF** (Top pick; repo_library; email) - CodeAF is an open-source coding harness for open models that topped a ten-harness DeepSWE benchmark at lower cost per issue, a possible alternative to Claude Code for your agentic workflow.
  - Link: https://github.com/Agent-Field/CodeAF

- **yocontra/pulsar** (Top pick; agents_mcp_skills; github) - Relevant to your MCP server and agentic coding workflow: it gives agents in different harnesses a shared list, tags, and multicast messaging, so it's worth checking if you run multiple coding agents…
  - Link: https://github.com/yocontra/pulsar

- **Someone open-sourced a 3D building editor that runs in your browser. No $5,000/year AutoCAD or Revi…** (Top pick; repo_library; x) - It's an open-source browser-based 3D building editor, runnable via npx, that exposes edits to coding agents like Claude Code, which makes it a concrete example of agent-editable domain tooling.
  - Link: https://x.com/RoundtableSpace/status/2123329178066096245

- **You can now run Claude Code or Codex on a free local model, on your own Mac. → One command to insta…** (Top pick; dev_tooling; x) - Lets Claude Code or Codex run against a local model on Apple Silicon M3+ with no API bill, though the "3.9x faster" claim is vendor-reported and unverified.
  - Link: https://x.com/RoundtableSpace/status/2123298979274203354

- **This tool cuts what Claude Code spends on your codebase by 44%. → It maps every function and how th…** (Top pick; dev_tooling; x) - A local codegraph tool that pre-indexes function call relationships so Claude Code can query a map instead of reading files, claiming 44% lower cost; worth testing on a real repo before trusting the…
  - Link: https://x.com/RoundtableSpace/status/2123359377092706310

- **You can now give your AI agent its own computer. → Full macOS or Linux desktops for your agents, on…** (Top pick; agents_mcp_skills; x) - Relevant to agent sandboxing: it gives agents full macOS or Linux desktops with persistent signed-in sessions and shared control, raising real security and isolation questions for agent workflows.
  - Link: https://x.com/RoundtableSpace/status/2123389577154994641

- **yibie/claude-best-practices-zh** (Top pick; repo_library; github) - A Chinese translation of 173 official Claude best-practice articles plus a 100-concept knowledge wiki, useful as a reference for Claude Code and API workflows if you read Chinese, though it is a thir…
  - Link: https://github.com/yibie/claude-best-practices-zh

- **Research acceleration: The jagged frontier** (Top pick; research; web) - It's an OpenAI measurement of where coding agents speed up AI research and where they stay uneven, which bears on how far agentic coding tools can be trusted on open-ended engineering work.
  - Link: https://openai.com/index/research-acceleration-jagged-frontier

- **bookwjitchieni1986/blender-ai-mcp-addon** (Top pick; agents_mcp_skills; github) - An MCP server add-on that lets Claude or other LLMs drive Blender scene and bpy scripting, relevant if you're building MCP tooling or 3D pipelines; the author is unverified and it has only 351 stars,…
  - Link: https://github.com/bookwjitchieni1986/blender-ai-mcp-addon

- **What it takes to set intelligence free — Fabian Hedin, CTO, Lovable** (Notable; agents_mcp_skills; youtube) - This talk covers how Lovable moved from a failed multi-agent framework to durable agent runtimes, forkable sandboxes, and a Rust rewrite of Vite, which is relevant to anyone building long-running cod…
  - Link: https://www.youtube.com/watch?v=pZWPq_ZAmM4

- **Mastra Factory** (Notable; agents_mcp_skills; email) - Mastra Factory is an open-source pipeline that turns repo issues into plans, code, and reviewed PRs, directly relevant to your agentic coding workflow and self-hostable for evaluation.
  - Link: https://factory.mastra.ai/?utm_source=tldrdev

- **GPT-6.2 Astra vs Claude Fable: What OpenAI's Own Data Says** (Notable; research; youtube) - This video relays OpenAI's own benchmark and system-card numbers comparing GPT-6.2 Astra and Claude Fable, but the reader gets no independent testing, so treat it as secondhand data.
  - Link: https://www.youtube.com/watch?v=1q_ILLaeEB4

- **Context API extracts full context from any web page** (Notable; dev_tooling; email) - Perplexity's Context API returns clean Markdown, links, passages, and metadata from up to 10 URLs per call, a ready-made extraction layer for agent or MCP web-reading tools.
  - Link: https://www.perplexity.ai/hub/blog/context-api-extracts-full-context-from-any-web-page?utm_source=tldrai

- **Jelly + Claude Code: What It Is, Install, Real-Project Test** (Notable; agents_mcp_skills; youtube) - Jelly is a free, open-source local tool that lets a coding agent like Claude Code present visual question pages instead of text walls, and the video shows a real-project install and test.
  - Link: https://www.youtube.com/watch?v=lEVDrPBQkUg

- **Why Antigravity Eats Weekly Quota Fast** (Notable; agents_mcp_skills; email) - Antigravity clears prompt caches after a 5-minute pause and starts every prompt with 13,800+ tokens of overhead, so disabling unused MCP servers and plugins cuts quota burn.
  - Link: https://asubedi.com.np/blog/why-antigravity-eats-weekly-quota-fast/?utm_source=tldrai

- **Five brand new ways to use Claude at work** (Notable; dev_tooling; youtube) - Anthropic is rolling out Claude Meetings, Whiteboards, Sheets, and Data plus interactive connectors, so workflow-level tooling may shift and Team/Enterprise plan gating matters for adoption.
  - Link: https://www.youtube.com/watch?v=t2Zo3YAJdj4

- **Sashiko: Agentic Code Review System for Linux** (Notable; agents_mcp_skills; email) - Sashiko separates bug discovery from verification and requires code evidence for both findings and dismissals, a concrete pattern for building trustworthy agentic code review.
  - Link: https://cloud.google.com/blog/products/application-development/lessons-from-building-sashiko-an-agentic-code-review-system?utm_source=tldrdev

- **How OpenAI’s Performance Factory keeps ChatGPT fast** (Notable; dev_tooling; web) - OpenAI's Codex-driven performance workflows show agentic coding applied to production latency work, a pattern you could borrow for your own codebases, though the details are behind the link.
  - Link: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast

## 2026-11-19

- **Claude Code v2.1.326–v2.1.328** (AI/Claude tooling) - Three releases in four days: auto mode on Bedrock/Vertex/Foundry for Opus 4.6 and Sonnet 4.6, `mcp_tool` hooks that can fail closed, and safer MCP setup.
  - Why it matters: `"onFailure": "block"` on `mcp_tool` hooks lets a failed policy check stop an action instead of silently passing; `claude mcp add-json <name> -` reads server JSON from stdin so tokens stay off the command line; `/status` now flags broken skills/hooks/keybindings; Code Mode works with agent teams.
  - Link: https://github.com/anthropics/claude-code/releases

- **Claude Fable 5.2 and Claude Mythos 5.2** (AI/Claude tooling) - Anthropic's new flagship models (announced Nov 9), aimed at demanding coding, finance and science work.
  - Why it matters: Worth re-benchmarking agent/coding workloads against the new tiers; I only confirmed the announcement headline, not pricing or API details.
  - Link: https://www.anthropic.com/news

- **shanselman/sandbox-mcp** (GitHub repo) - MCP server and CLI (`sbx`) that boots a disposable Windows Sandbox, deploys/runs an app, drives its UI, collects screenshots and logs, then destroys the VM.
  - Why it matters: Lets a coding agent actually test Windows installers and apps in a clean machine rather than guessing; also has a `detonate` mode for untrusted files.
  - Link: https://github.com/shanselman/sandbox-mcp
  - Safety note: MIT; ~489 stars, created 2026-11-06, pushed 2026-11-15; well-known maintainer. Setup needs an admin step to enable Windows Sandbox, and the README suggests having an agent fetch a setup guide from raw.githubusercontent.com — read it first. Contributor list not verified.

- **DIYgod/pinky** (GitHub repo) - Lets MCP agents (Claude Code, Cursor, Codex) operate a real iPhone/Android phone with a human approving risky steps and recordings of each run.
  - Why it matters: Gives agents a way to test mobile apps on real devices with human-in-the-loop control.
  - Link: https://github.com/DIYgod/pinky
  - Safety note: Apache-2.0; ~2.5k stars, created 2026-11-06, pushed 2026-11-19; self-described pre-alpha. Android needs USB debugging/accessibility service and may expose adb over the network; iOS may fetch a disk image from a third-party mirror; updates and anonymous telemetry on by default (`DO_NOT_TRACK=1` disables). Use with caution.

- **alexeyw/lot-map** (GitHub repo) - Live map beside the chat showing what Claude Code is doing: tool calls, model steps, hooks, skills and subagents as they happen; local only.
  - Why it matters: Useful for debugging and understanding agent runs and hook/skill behavior.
  - Link: https://github.com/alexeyw/lot-map
  - Safety note: MIT; ~1k stars, created 2026-11-09, pushed 2026-11-19 (from GitHub search metadata only; I did not inspect the code or maintainer history, so skim before installing).

## 2026-11-18 (AKD)

- **modelcontextprotocol/servers v2.5.0** (Top pick; agents_mcp_skills; github) - This is a security release fixing eight vulnerabilities in MCP git, filesystem, and everything servers, so anyone running them should upgrade to the listed versions now.
  - Link: https://github.com/modelcontextprotocol/servers/releases/tag/v2.5.0

- **NVIDIA scanned 31,132 AI agent skills. 1 in 4 had security holes. → 26.1% had vulnerabilities → 5.2…** (Top pick; agents_mcp_skills; x) - NVIDIA's open-sourced scanner found 26.1% of 31,132 agent skills had vulnerabilities and 5.2% looked malicious, so audit skills before installing them in Claude Code.
  - Link: https://x.com/RoundtableSpace/status/2123034738566824268

- **[AINews] GPT-6.2 Astra, the #2 Frontier Model is better and 20%-600% cheaper, but has mixed reviews; 6.2 Sol likely main workhorse** (Top pick; model_release; web) - OpenAI's GPT-6.2 Astra and Sol are out at roughly 15% of Astra's prior per-task cost, with Astra scoring 62 on the Intelligence Index, a cheaper option worth benchmarking against your Claude API work…
  - Link: https://latent.space/p/ainews-gpt-6-2-astra-the-2-frontier-model-is-better-and-20-600-cheaper-but-has-mixed-reviews-6-2-sol/
  - Also covered by: [Introducing GPT-6.2 Astra and Sol](https://openai.com/index/introducing-gpt-6-2-astra-sol) (web)
  - Also covered by: [OpenAI launches GPT-6.2 Astra and Sol](https://www.testingcatalog.com/openai-launches-gpt-6-2-astra-and-sol-on-chatgpt-and-apis/?utm_source=tldrnewsletter) (email)
  - Also covered by: [GPT-6.2 Astra vs Claude Fable: What OpenAI's Own Data Says](https://www.youtube.com/watch?v=1q_ILLaeEB4) (youtube)
  - Also covered by: [GPT-6.2 is less than a day old and the people who tested it can't agree. → Matt Shumer: "essentiall…](https://x.com/RoundtableSpace/status/2122906392076140676) (x)

- **Vercel's eve 1.0** (Top pick; agents_mcp_skills; email) - Vercel's open-source eve 1.0 framework handles the agent loop, memory, approvals, and monitoring, relevant to your Vercel and agent-infrastructure work.
  - Link: https://vercel.com/blog/eve-is-now-generally-available?utm_source=tldrai

- **anthropics/claude-code v2.1.327** (Top pick; dev_tooling; github) - Adds `claude mcp add-json` stdin input so MCP tokens stay off the command line, plus fixes for `.mcp.json` key loss and worktree file deletion that matter if you run MCP servers or Remote Control.
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.327

- **Alibaba just open-sourced the AI code reviewer 20,000+ of its own developers use. → 5M+ real code r…** (Top pick; agents_mcp_skills; x) - Alibaba's open-source AI code reviewer, used internally by 20,000+ developers, is installable via `npx skills add` and works with any model, so it's a directly adoptable alternative to Claude Code fo…
  - Link: https://x.com/RoundtableSpace/status/2123042287710265351

- **Tencent just open-sourced a workspace where coding agents ship your code like a real dev team. → Ty…** (Top pick; agents_mcp_skills; x) - Open-source, self-hosted workspace that runs Claude Code, Codex, and Cursor CLI agents in Docker sandboxes with human approval before merge, relevant to agent sandboxing and workflow.
  - Link: https://x.com/RoundtableSpace/status/2122998732358558090
  - Also covered by: [Superpowers is a free, open-source toolkit that makes AI coding agents plan, test and debug instead…](https://x.com/RoundtableSpace/status/2123102686241333354) (x)
  - Also covered by: [Jelly + Claude Code: What It Is, Install, Real-Project Test](https://www.youtube.com/watch?v=lEVDrPBQkUg) (youtube)

- **Microsoft's Seven New Models** (Top pick; model_release; email) - Microsoft's MAI Code 2 is now in GitHub Copilot at roughly 40% of GPT-6.1 Sol's price for about 98% of its coding quality, a cheaper option worth benchmarking against your current model.
  - Link: https://microsoft.ai/news/microsoft-ignite-2026/?utm_source=tldrai

- **40x More Merged PRs With 2.7x the Engineers — Walden Yan, Cognition** (Top pick; agents_mcp_skills; youtube) - Cognition's Walden Yan describes running a coding-agent workflow at scale: self-driving PRs, Slack-driven work, and locally runnable services so agents can test, which is a concrete pattern you could…
  - Link: https://www.youtube.com/watch?v=U92J5mCDLMc

- **jQuery 4.1.0 and 3.8.0 Released** (Top pick; dev_tooling; email) - jQuery 3.8.0 is the last planned 3.x feature release and 4.1.0 adds form-associated custom element serialization, so any legacy jQuery code still on 3.x should plan an upgrade path rather than expect…
  - Link: https://blog.jquery.com/2026/11/17/jquery-4-1-0-and-3-8-0-released-passing-the-torch/?utm_source=tldrdev

- **New Ways of Working with Codex — Dominik Kundel & Charlie Guo, OpenAI** (Top pick; agents_mcp_skills; youtube) - A walkthrough of OpenAI's current Codex workflow (plugins, cloud environments, code review, Agents API, parallel agents) that is useful for comparing agentic coding practices with Claude Code.
  - Link: https://www.youtube.com/watch?v=IPh9YsWvDQk

- **Introducing Replit Missions** (Top pick; agents_mcp_skills; email) - Replit Missions coordinates agent swarms under budget caps, a multi-agent orchestration pattern relevant to agentic coding workflows, though the item gives no API or adoption details.
  - Link: https://replit.com/blog/introducing-replit-missions?utm_source=tldrai

- **Inside the Codex sandbox** (Top pick; agents_mcp_skills; web) - Codex's cross-platform sandbox design for filesystem and network limits is directly relevant to the reader's interest in agent sandboxing and security patterns for coding agents.
  - Link: https://openai.com/index/inside-the-codex-sandbox

- **You can now opt into more frequent builds of Claude Desktop on Windows and Mac. Switch to the Lates…** (Top pick; dev_tooling; x) - Claude Desktop now offers a "Latest" release channel on Windows and Mac via Settings > Desktop app, trading faster fixes for less reliability than the default Stable channel.
  - Link: https://x.com/ClaudeDevs/status/2122821051910684824

- **Someone combined the free tiers of 87 AI providers into one API: 10 billion free tokens a month. → …** (Top pick; dev_tooling; x) - A single OpenAI-compatible endpoint that routes across 87 providers' free tiers and works with Claude Code, useful for cheap experimentation, but treat the "10B tokens" claim and the routing reliabil…
  - Link: https://x.com/RoundtableSpace/status/2123019639135359265

- **You can now copy any animation from any website into your own code. → Point it at a live site, a sc…** (Top pick; repo_library; x) - A free skill (npx skills add NiazMorshed2007/reanimate) that has an agent rebuild a site's animation from a URL, recording, or GIF and iterate until it matches, useful for prototyping motion quickly.…
  - Link: https://x.com/RoundtableSpace/status/2123012089333658067

- **SecFathy/otpkit** (Top pick; agents_mcp_skills; github) - An MCP server that lets agents receive OTPs and verification links without API keys, relevant to agent-driven signup and testing workflows, though it raises account-security and misuse considerations…
  - Link: https://github.com/SecFathy/otpkit

- **Managing frontier AI risk: From training to deployment** (Top pick; agents_mcp_skills; web) - OpenAI outlines its frontier-model safety pipeline (alignment, sandboxing, blocking safeguards, monitoring), relevant to anyone building agents needing sandboxing and guardrail patterns.
  - Link: https://openai.com/index/managing-frontier-ai-risk

- **boringmarketer/boring-marketing-skills** (Top pick; agents_mcp_skills; github) - A free MIT-licensed bundle of 32 marketing skills for AI agents, which could be a reusable skill set to drop into Claude Code, though it's marketing-focused rather than engineering.
  - Link: https://github.com/boringmarketer/boring-marketing-skills

- **Building 3D video sets with GPT-6.2 Astra** (Notable; model_release; youtube) - OpenAI's GPT-6.2 Astra is pitched as a flagship upgrade for cleaner code, better 3D and frontend output, and more efficient tool use, demoed building Blender scenes in Codex, which matters if you use…
  - Link: https://www.youtube.com/watch?v=tKoDPOrLMX0

- **Maxwell V1.0 Flash Tested Locally: 35B MoE, 3B Active, Apache 2.0** (Notable; model_release; youtube) - A 35B MoE with only 3B active under Apache 2.0, runnable locally via vLLM, which is useful if you want a cheap local coding model to test against your Claude Code workflow.
  - Link: https://www.youtube.com/watch?v=RYbe_zfhoyo

- **How the Claude Code Team Thinks About Verification** (Notable; agents_mcp_skills; email) - It describes how the Claude Code team verifies changes (end-to-end, property, and differential tests, plus failure-derived rules), a practical workflow you could adopt in your own agent-driven coding…
  - Link: https://x.com/addyosmani/status/2122590683055993308?a=S5WdDueZTW6NMfT57qc&s=46&utm_source=tldrdev

- **FrontierHarness Eval v1.1** (Notable; research; email) - The eval finds the best coding-agent harness varies by model and that harness choice alone can shift cost per task up to 5x, so harness selection deserves benchmarking, not defaults.
  - Link: https://runta.com/blog/introducing-frontierharness-eval-v1-1/?utm_source=tldrai

- **Apex-35B Locally: A Model Built by AI Research That Improves Itself** (Notable; model_release; youtube) - A local 35B model claimed to self-improve, with setup via llama.cpp and Hermes Agent and coding tests, which is worth a look only if you can run it locally and verify the self-improvement claims your…
  - Link: https://www.youtube.com/watch?v=tYIvQRlFM6s

- **Writable Derived State: Stop Synchronizing State** (Notable; other; email) - Copying fetched data into React state via effects can clobber unsaved edits on refetch; the nullable-override pattern avoids this and works with TanStack Query, relevant to your React/Vite stack.
  - Link: https://playfulprogramming.com/posts/writable-derived-state/?utm_source=tldrdev

- **Only the Human Merges** (Notable; agents_mcp_skills; email) - Written instructions alone failed to stop agents from merging, so server-enforced permissions are what actually keep final merge authority with a human.
  - Link: https://itsmeduncan.com/2026/11/17/only-the-human-merges/?utm_source=tldrdev

## 2026-11-18

- **Claude Fable 5.2 and Mythos 5.2** (AI/Claude) - Fable 5.2 is GA (Mythos 5.2 limited to verified orgs): 1M context, 128k output, always-on adaptive thinking, $8/$40 per MTok.
  - Why it matters: breaking changes - editing `system`/`tools`/earlier messages before replaying a thinking block now returns 400; `computer_20251124` must move to `computer_toolset_20260801`; 30-day retention required (no ZDR by default).
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Linked billing (beta) on the Claude API** (AI/Claude) - Set `billing_policy` with the `user-profiles-billing-2026-10-01` beta header so your app's users pay for Claude usage via their own Claude org (spend caps, unlink in Console).
  - Why it matters: lets you ship Claude-powered apps without carrying inference costs.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Self-hosted Claude Managed Agents** (AI/Claude) - Run the full Managed Agents service (agents, sessions, history) on your own infrastructure (Nov 12); access via your Anthropic account team.
  - Why it matters: data-residency/compliance route for hosted agent workloads.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude Code 2.1.325-2.1.327** (AI/Claude) - Auto mode becomes the default permission mode; Code Mode now works with agent teams; `claude mcp add-json <name> -` reads server JSON from stdin; sandboxed Bash follows the normal permission flow unless `sandbox.autoAllowBashIfSandboxed: true`; scheduled tasks and `/loop` ask before running skills with `allowed-tools`/hooks.
  - Why it matters: permission behavior changed, so check automation relying on prompts; 2.1.327 also fixes a Remote Control bug that could delete git-ignored files like `.env` in worktree mode.
  - Link: https://code.claude.com/docs/en/changelog.md

- **vercel-labs/agent-desktop** (GitHub repo) - CLI, C library and MCP server (`agent-desktop mcp`) that lets agents drive desktop apps via the OS accessibility tree (JSON with element refs) instead of screenshots; macOS, Windows, Linux.
  - Why it matters: cheaper, more reliable desktop/GUI automation for agents than vision-based approaches.
  - Link: https://github.com/vercel-labs/agent-desktop
  - Safety note: Apache-2.0; ~25.2k stars, 351 commits, Vercel Labs org. Could not verify last-commit date or contributors, and npm package ships native binaries (inspect package scripts before global install). Snapshots can expose private desktop content. Trending lead came from third-party roundup, vouched only partially.

## 2026-11-17 (AKD)

- **GPT-6.2 Astra and GPT-6.2 Sol—Models built for the real world** (Top pick; model_release; youtube) - GPT-6.2 Astra and Sol are new OpenAI model releases with API access for developers and fewer output tokens per task, so existing model-pinned code may need evaluation and migration.
  - Link: https://www.youtube.com/watch?v=C1zYX5jwqq4
  - Also covered by: [Introducing GPT-6.2 Astra and Sol](https://openai.com/index/introducing-gpt-6-2-astra-sol) (web)

- **Hugging Face and OpenRouter Join Forces** (Top pick; dev_tooling; email) - One Hugging Face token can now route requests to any open-weight model via OpenRouter's provider selection, which may simplify multi-provider setups in your agent and API code.
  - Link: https://huggingface.co/blog/openrouter?utm_source=tldrai

- **anthropics/anthropic-sdk-python v2.10.0** (Top pick; dev_tooling; github) - Adds a beta `billing_policy` parameter and renames error data models (old names deprecated), so check any code importing those error types before upgrading.
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.10.0

- **Check out Code Mode, a new, experimental way for Claude Code to work with tools. Claude writes scri…** (Top pick; dev_tooling; x) - Experimental Claude Code "Code Mode" has Claude write scripts that chain MCP tools together, opt-in via CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1, directly relevant to your MCP and agent workflow.
  - Link: https://x.com/ClaudeDevs/status/2122801681939234950

- **React Flow 13** (Top pick; dev_tooling; email) - React Flow 13 is a major release with store and rendering changes, so upgrading from v12 may require code changes in node-based UIs.
  - Link: https://xyflow.com/blog/react-flow-13-major-release?utm_source=tldrdev

- **The Claude Code team shared how it gets Claude to check its own work: tests, benchmarks and end-to-…** (Top pick; agents_mcp_skills; x) - Gives concrete self-verification practices for Claude Code (end-to-end, property, and differential tests, a verify skill in .claude/skills/, and a rule that changes can't edit their own judge), all a…
  - Link: https://x.com/RoundtableSpace/status/2122551554011979974

- **Qwen4-Max Is Out of Preview: True Frontier-Grade AI** (Top pick; model_release; youtube) - Qwen4-Max leaving preview is a new hosted model option worth evaluating against Claude for agentic coding tasks, though this video is a general capability test with no API or migration details.
  - Link: https://www.youtube.com/watch?v=rzsdYlIvqE4
  - Also covered by: [Qwen4-Max](https://qwen.ai/blog?id=qwen4-max&utm_source=tldrai) (email)

- **BenchProofer: Formally Verified Coding Benchmarks** (Top pick; research; email) - BenchProofer adds formal specs and verified reference solutions to all 500 SWE-Bench Verified tasks, showing many test-passing agent patches may still be wrong, relevant to judging coding-agent evals.
  - Link: https://www.amazon.science/blog/benchproofer-formally-verified-coding-benchmarks-on-demand?utm_source=tldrdev

- **Liquid AI just released d1.2 and d1.2-ultra, a new class of omnimodal decision models. > Takes text…** (Top pick; model_release; x) - Liquid AI's d1.2 models output structured decisions (extraction, detection, ranking) from text, image, and audio inputs, which could replace chat-style calls in agent pipelines if the claimed benchma…
  - Link: https://x.com/RoundtableSpace/status/2122755397299962055
  - Also covered by: [d1.2: State-of-the-Art Omnimodal Decision Models](https://www.liquid.ai/blog/d1-2?utm_source=tldrai) (email)

- **Coding Agent, Meet ngrok: The ngrok MCP Server Is Live** (Top pick; agents_mcp_skills; email) - The ngrok MCP server lets coding agents inspect live traffic and validate Traffic Policy rules, useful for testing webhooks and local APIs from an agent workflow.
  - Link: https://ngrok.com/blog/mcp?utm_source=tldrdev

- **Claude Code, Cursor and Codex can now edit your videos locally with ffmpeg-skill, a free, MIT-licen…** (Top pick; agents_mcp_skills; x) - A free MIT-licensed FFmpeg skill and MCP server with 42 tools lets Claude Code and similar agents edit video locally with no API key, a quick adoption candidate.
  - Link: https://x.com/RoundtableSpace/status/2122536454538608872
  - Also covered by: [Give your AI agent a video editor. ffmpeg-skill adds 42 editing tools to Claude Code, Codex or Curs…](https://x.com/RoundtableSpace/status/2122619502462701795) (x)

- **sybil-solutions/inference-optimisation-skill** (Top pick; agents_mcp_skills; github) - It's an installable agent skill that guides hill-climbing local LLM serving speed (decode, speculative decoding, KV cache, TTFT), useful if you run local models alongside your Claude Code and MCP too…
  - Link: https://github.com/sybil-solutions/inference-optimisation-skill

- **11 open-source repos for a research → write → slides → video → voice workflow you can hand to Claud…** (Top pick; repo_library; x) - A curated list of 11 open-source Claude Code-compatible repos covering research, writing, slides, video, and TTS, with license caveats worth checking before commercial use.
  - Link: https://x.com/RoundtableSpace/status/2122581753449845217

- **Linked billing is now in beta on the Claude Platform. Now users of tools like Factory, Linear, and …** (Top pick; dev_tooling; x) - Partner tools like Factory, Linear, and Ramp can now bill Claude API usage through a Claude Platform org without sharing API keys, which matters for anyone wiring Claude into team tooling.
  - Link: https://x.com/ClaudeDevs/status/2122751844455956760

- **jackson-cmd/claude-multi-desktop** (Top pick; repo_library; github) - Lets you run several Claude Desktop accounts side by side on Mac with one shared Claude Code setup, which is useful if you juggle personal and work logins.
  - Link: https://github.com/jackson-cmd/claude-multi-desktop

- **Someone just open sourced a repo of agent skills for building HTML artifacts. Everything from low-f…** (Top pick; agents_mcp_skills; x) - Open-source agent skills for generating HTML prototypes and wireframes, usable as a reference without installing, relevant to Claude Code skills workflows.
  - Link: https://x.com/RoundtableSpace/status/2122695000316322230

- **More ways to move care forward with ChatGPT for Healthcare** (Top pick; model_release; web) - Adds computer-use agents and healthcare plugins to ChatGPT for Healthcare, relevant to agent sandboxing and security patterns, though it is a vertical product rather than an adoptable developer tool.
  - Link: https://openai.com/index/more-ways-to-move-care-forward-with-chatgpt-for-healthcare

- **AI4XE/Parallax** (Top pick; agents_mcp_skills; github) - Parallax is a small open-source workflow plugin for running hands-off coding agents across Claude Code, Copilot, and DeepSeek, relevant if you want to test multi-agent coding setups.
  - Link: https://github.com/AI4XE/Parallax

- **morajabi/poo** (Top pick; repo_library; github) - It's a macOS menu bar app, CLI, and MCP server that finds and safely frees disk space from build artifacts, caches, simulators, and agent worktrees, directly relevant to your agentic coding workflow.
  - Link: https://github.com/morajabi/poo

- **erkamyaman/rust-anything** (Top pick; repo_library; github) - A GitHub tool that incrementally ports TypeScript, Python, Go and other apps to Rust, verifying each step against recorded behavior, which could suit a migration or agent-assisted rewrite workflow.
  - Link: https://github.com/erkamyaman/rust-anything

- **The Sentence That Makes Fable 5.2 Clean Up Your Code** (Notable; research; youtube) - A single ownership sentence in the prompt made Fable 5.2 consolidate duplicated code in 10/10 Claude Code runs versus 0/10 without it, at about 54% more output tokens, though three runs also changed…
  - Link: https://www.youtube.com/watch?v=zspRazxh5_A

- **Teach AI coding assistants your design system with Markdown** (Notable; agents_mcp_skills; email) - Documenting design tokens and component patterns in Markdown referenced from AGENTS.md is a low-effort, adoptable way to make your React/Tailwind assistant respect your design system.
  - Link: https://blog.logrocket.com/teach-ai-assistants-design-system/?utm_source=tldrdev

- **MiniMax H3 Image in ComfyUI Tested Locally** (Notable; model_release; youtube) - A local ComfyUI walkthrough of MiniMax-H3-Image, useful if you run image models locally and want a tested setup path before adopting it in your ComfyUI pipeline.
  - Link: https://www.youtube.com/watch?v=8Z3pedHd6Vo

- **Building always-on agents** (Notable; agents_mcp_skills; email) - Describes a reference architecture for always-on agents (event inboxes, timers, memory, permissions, outboxes), directly relevant to building unsupervised Claude Agent SDK workflows and their sandbox…
  - Link: https://claude.com/resources/articles/building-always-on-agents?utm_source=tldrai

- **The Console Framework** (Notable; dev_tooling; email) - Text.js lets one React app render in the browser DevTools console, a terminal, or an MCP server, which matters for agent-facing UIs and shared components across surfaces.
  - Link: https://textjs.org/?utm_source=tldrdev

- **Broadening access to AI for scientists** (Notable; industry_business; web) - Offers free frontier-model access to 200,000 academic researchers, a funding and access program with no direct coding, API, or agent-tooling impact for this reader.
  - Link: https://openai.com/index/expanding-chatgpt-for-academic-researchers

- **ALL THE AI MOVIES ARE BECOMING REALER. CALIFORNIA IS SUING OPENAI OVER ROGUE AI AGENT CYBER INCIDEN…** (Notable; industry_business; x) - This is an unverified social-media claim of a state lawsuit over OpenAI agent containment failures, so it bears on agent sandboxing and security but has no concrete technical detail to act on yet.
  - Link: https://x.com/RoundtableSpace/status/2122770496777551955

- **Claude Artifacts Can't Do This, Right?** (Notable; repo_library; youtube) - Jelly gives coding agents like Claude Code a local, two-way HTML interface with element-pinned questions, a concrete adoptable workflow tool worth a look this week.
  - Link: https://www.youtube.com/watch?v=B6xrS8zEzrw

- **Projects in Claude Code** (Notable; agents_mcp_skills; email) - Claude Code's Projects update adds a more proactive coordinator and project-chat Q&A, which may change how you structure multi-thread agent work.
  - Link: https://threadreaderapp.com/thread/2121375309287301360.html?utm_source=tldrai

- **Would You Let a Decision Model Guard Your Shell?** (Notable; research; youtube) - Jev, a small open decision model, matched Claude Haiku 5.5 on routing and shell-command guarding in this test, but one destructive command slipped past both, so don't rely on it as a safety boundary.
  - Link: https://www.youtube.com/watch?v=rRxHpI891O0

## 2026-11-17

- **Claude Code 2.1.323-2.1.326: Code Mode and tighter permissions** (AI/Claude tooling) - Experimental opt-in Code Mode (Claude writes JavaScript to call its tools), now usable alongside agent teams; plugins can declare `engines["claude-code"]` and `claude plugin validate` type-checks TypeScript hook modules.
  - Why it matters: Plugin authors get version gating and validation. Sandboxed Bash now follows the normal permission flow unless `sandbox.autoAllowBashIfSandboxed` is true, and read-only git commands outside trusted repos prompt, so unattended or CI setups may need config changes.
  - Link: https://code.claude.com/docs/en/changelog.md

## 2026-11-16 (AKD)

- **Alibaba just released Qwen4-Max, and it does the same work for about 60% less per task. What's new:…** (Top pick; model_release; x) - A new Qwen model claiming ~60% lower per-task cost and a 1M-token context, usable in coding agents via OpenRouter or the QwenCloud API, which matters for model-swap decisions, though the claims come…
  - Link: https://x.com/RoundtableSpace/status/2122264663547404446
  - Also covered by: [Qwen4-Max Is Out of Preview: True Frontier-Grade AI](https://www.youtube.com/watch?v=rzsdYlIvqE4) (youtube)
  - Also covered by: [Qwen4-Max](https://qwen.ai/blog?id=qwen4-max&utm_source=tldrai) (email)

- **If you built an app with Lovable, check it today. Researchers scanned 159,041 Lovable projects. 24,…** (Top pick; other; x) - Researchers found 24,664 of 159,041 scanned Lovable apps exposing database records publicly, so check Supabase Row Level Security on your tables today.
  - Link: https://x.com/RoundtableSpace/status/2122189166331007336

- **nvidia/Nemotron-Labs-Sigma 8B/3B** (Top pick; model_release; reddit) - An 8B continuous-space diffusion LM that decodes text in parallel blocks with a standard KV cache, offering a non-autoregressive alternative to try for speed, though it's not a drop-in replacement fo…
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xxwg6w/nvidianemotronlabssigma_8b3b/

- **anthropics/anthropic-sdk-python v2.9.0** (Top pick; dev_tooling; github) - The Anthropic Python SDK v2.9.0 adds Update Bundle and RBAC endpoint fields, and changes grep to ignore relative-PATH ripgrep binaries, so check any custom rg setup after upgrading.
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.9.0

- **anthropics/claude-code v2.1.326** (Top pick; agents_mcp_skills; github) - Claude Code v2.1.326 adds startup warnings for malformed `--allowedTools`/`--tools` rules and fixes Bash permission-rule and transcript bugs, so review tool permission configs after upgrading.
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.326

- **Anthropic upgrades Claude Code Projects to run parallel AI workers** (Notable; dev_tooling; web) - Anthropic's redesigned Claude Code Projects now runs parallel AI workers, which could change how you split coding tasks across agents and is worth testing against your current Agent SDK workflows.
  - Link: https://claude.com/resources/articles/projects-redesigned

- **Tthanh2k6/turbo-browser-mcp** (Notable; agents_mcp_skills; github) - A Playwright MCP server that batches browser actions and returns delta snapshots, so Claude Code or Agent SDK browser automation can use fewer turns and tokens, with a submit guard on by default.
  - Link: https://github.com/Tthanh2k6/turbo-browser-mcp

- **NVIDIA’s SkillEvaluator is an open-source project focused on evaluating AI agent skills before you …** (Notable; agents_mcp_skills; x) - NVIDIA's open-source SkillEvaluator (pip install skillevaluator) lints and quality-checks agent skill folders before use, directly relevant to vetting skills and plugins in Claude Code workflows.
  - Link: https://x.com/RoundtableSpace/status/2122370360498905470

- **Anthropic published a guide on building always-on agents (Nov 13). It breaks them into 5 parts: inbox, timers, memory, permissions, outbox** (Notable; agents_mcp_skills; reddit) - Anthropic's design guide splits always-on agents into five parts (inbox, timers, memory, permissions, outbox), directly applicable to the reader's daily scheduled Claude task, especially its memory l…
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xxdzcf/anthropic_published_a_guide_on_building_alwayson/

- **Claude Code on desktop now supports iPhone Duo in the iOS simulator (public beta). You can run your…** (Notable; dev_tooling; x) - Claude Code desktop can now drive the iOS simulator's iPhone Duo (foldable) layouts in public beta, useful for testing responsive app UIs with Claude.
  - Link: https://x.com/ClaudeDevs/status/2122439098740674839

- **[Release] Qwen3.8-27B-Perplexing-Pegasus-Heretic: Unified vision + typed decider + abliterated weights for local agent stacks (GGUF, AutoRound, NVFP4)** (Notable; model_release; reddit) - A single 27B checkpoint bundling vision, chat/tool-calling, a typed-decision head, and abliterated weights, with GGUF builds that fit 16–24GB GPUs, is a possible local alternative to juggling several…
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xxg12n/release_qwen3827bperplexingpegasusheretic_unified/

- **Personal Agent Protocol 1.0** (Notable; agents_mcp_skills; email) - A new open protocol (v0 now out) for how personal agents talk to business agents, sites, and APIs, relevant to agent infrastructure and MCP-style integration work.
  - Link: https://sierra.ai/blog/releasing-poppy?utm_source=tldrai

- **Building Visual Intelligence — Andreas Blattmann & Dustin Podell, Black Forest Labs** (Notable; model_release; web) - Black Forest Labs (Stable Diffusion alumni) are moving from image generation into video and world models, training FLUX 3 on image, video, and audio jointly; no API or adoption details yet.
  - Link: https://latent.space/p/bfl/
  - Also covered by: [Building Visual Intelligence — Andreas Blattmann & Dustin Podell, Black Forest Labs](https://latent.space/p/building-visual-intelligence-andreas-blattmann-dustin-podell-black-forest-labs/) (web)

- **[NEW RELEASE] - Supra2.5-65M Base and Instruct - our next generation state-of-the art small model family - first model!** (Notable; model_release; reddit) - A 65M-parameter base and instruct model released with GGUF quants (F16, Q8_0, Q4_K_M) for llama.cpp and Ollama, but it's a toy-scale model with self-reported benchmarks, so it's low adoption value fo…
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xxw9ik/new_release_supra2565m_base_and_instruct_our_next/

- **Claude Code, Cursor and Codex can now edit your videos locally with ffmpeg-skill, a free, MIT-licen…** (Notable; agents_mcp_skills; x) - A local, MIT-licensed skill and MCP server giving Claude Code, Cursor and Codex 42 FFmpeg tools for video editing, adoptable with no API key.
  - Link: https://x.com/RoundtableSpace/status/2122460957213663698

## 2026-11-16

- **Claude Code Code Mode** (AI/Claude tooling) - Experimental opt-in mode (v2.1.323, Nov 12) where Claude writes JavaScript that makes many tool calls in one step instead of one call per round trip.
  - Why it matters: Fewer round trips for repo-wide edits, filtered searches and parallel commands. Enable with `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1`. It is interactive-terminal only (no `-p`, SDK or cloud sessions), and auto mode reviews the code, not each call.
  - Link: https://code.claude.com/docs/en/code-mode

- **Claude Code 2.1.323-2.1.325** (AI/Claude tooling) - Plugin version gating (`engines["claude-code"]` in plugin.json), `claude plugin validate` type-checks TypeScript hook modules, and a 30s heartbeat for long background hooks in `-p`/SDK runs.
  - Why it matters: Safer plugin distribution and fewer hung-turn false alarms in headless pipelines. Behavior change in 2.1.325: sandboxed Bash now follows the normal permission flow unless `sandbox.autoAllowBashIfSandboxed: true` is set.
  - Link: https://code.claude.com/docs/en/changelog.md

- **Claude Fable 5.2 and Mythos 5.2** (AI/Claude tooling) - New models launched Nov 9 for long-horizon reasoning and agentic work: 1M context, 128k max output, $8/$40 per MTok.
  - Why it matters: Candidate default for long-running coding agents. The same release notes list API changes (prefix check, computer-use toolset migration, 30-day data retention requirement), so check them before migrating.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Messages API message threads (beta)** (AI/Claude tooling) - The server keeps conversation state, so later requests send only new messages (header `message-threads-2026-08-12`, Nov 2).
  - Why it matters: Cuts payload and re-send overhead in long agent loops.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Self-hosted Claude Managed Agents** (AI/Claude tooling) - Nov 12: the whole Managed Agents service can run on your own infrastructure. Access is through your Anthropic account team.
  - Why it matters: An option for agent workloads with data-residency or compliance constraints.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **agent-browser** (GitHub repo) - Native Rust CLI that lets AI agents drive a browser from the shell. `snapshot` returns the page as an accessibility tree with element refs (@e1) to click and read.
  - Why it matters: A lightweight way to give a coding agent web testing and scraping without a heavy browser-automation stack.
  - Link: https://github.com/vercel-labs/agent-browser
  - Safety note: Apache-2.0, vercel-labs org, ~51.8k stars, 841 commits. On GitHub's weekly trending list. I could not confirm the last-commit date.

- **modern-web-guidance-src** (GitHub repo) - Google Chrome's skills and CLI that steer coding agents toward current web platform practices, covering 250 features. The CLI can scan a codebase for legacy patterns.
  - Why it matters: Drop-in skills that keep AI-generated frontend code modern.
  - Link: https://github.com/GoogleChrome/modern-web-guidance-src
  - Safety note: Apache-2.0, GoogleChrome org, ~7.7k stars, 1,612 commits. I could not confirm the last-commit date.

## 2026-11-15 (AKD)

- **Gemini Decision 1: You Don’t Need an LLM to Make a Decision** (Top pick; model_release; youtube) - Google's Gemini Decisions API returns yes/no, choice, and score answers with probability and confidence instead of generated text, offering a cheaper, non-LLM option for classification-style calls.
  - Link: https://www.youtube.com/watch?v=-On9ZKGiMfA
  - Also covered by: [Gemini Decisions API Wins 7 of 9, But Is It Worth It?](https://www.youtube.com/watch?v=iTMBIRRdfQw) (youtube)

- **Microsoft just put a tool on GitHub that makes your coding agent cheaper. It doesn't touch the agen…** (Top pick; repo_library; x) - It matters because Microsoft's open-source TokenEconomizer claims 18–31% lower coding-agent cost by caching repo facts and pruning unused tools, with no agent changes needed.
  - Link: https://x.com/RoundtableSpace/status/2121887176514482404

- **Jack Dorsey's company Block put its own team workspace on GitHub. With a twist. Buzz is a workspace…** (Top pick; agents_mcp_skills; x) - Block's open-source Buzz (Apache 2.0, self-hosted) lets humans and AI agents share team rooms, relevant to anyone building or sandboxing agent infrastructure.
  - Link: https://x.com/RoundtableSpace/status/2121902276306468961

- **DeepSeek put the agent system its team built for itself on GitHub. 23K stars. The dsh-superagent re…** (Top pick; repo_library; x) - Open-sourced DeepSeek research agent prototype (dsh-superagent, 23K stars) built largely by coding agents; the author warns it is research code, so review before running.
  - Link: https://x.com/RoundtableSpace/status/2121955124658725139

- **[Paper] No Second Run: Does RSI Stop at Frontier Pre-training? - 801-30B-A3B-Base Coming Soon** (Top pick; research; reddit) - A research paper claims recursive self-improvement applied to a full frontier-scale pre-training run, releasing 801-30B-A3B-Base, a 30B MoE model with open weights and a benchmark-comparable result t…
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xwt3ri/paper_no_second_run_does_rsi_stop_at_frontier/

- **Introducing Claude Meetings** (Notable; dev_tooling; youtube) - Claude Meetings joins Google Meet calls as a visible participant that builds docs and takes notes, beta on Team and Enterprise plans, so it's worth testing against a real team workflow.
  - Link: https://www.youtube.com/watch?v=YUYeHMsqbmY
  - Also covered by: [Use Claude Meetings](https://support.claude.com/en/articles/18325154-use-claude-meetings?utm_source=tldrai) (email)

- **Claude went from 37% to 61% of AI-builder job postings this year, and four in five companies hiring for AI coding ask for Claude Code** (Notable; industry_business; reddit) - For a Claude Code and Agent SDK builder working in Salesforce and FDE roles, this is a useful signal that Claude Code is now the dominant named tool in AI-coding job postings, though the data comes f…
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xwe6q9/claude_went_from_37_to_61_of_aibuilder_job/

- **I measured how much each "save tokens" trick actually costs on a Pro plan. Coming back to an old chat after 1h costs ~20x more.** (Notable; research; reddit) - Measured data shows resuming a Claude Code chat after a 1h+ break costs about 20x more than a continuous message, since the 1-hour prompt cache expires and the full context reloads, so long-running s…
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xwla4y/i_measured_how_much_each_save_tokens_trick/

- **vaibhav-space/my-ai-coding-workflow** (Notable; repo_library; github) - A ready-made three-stage planning, critical-review, and diff-audit workflow with reusable skills that can be adopted directly into Claude Code or any other agent this week.
  - Link: https://github.com/vaibhav-space/my-ai-coding-workflow

- **Atlas omni model from World Labs** (Notable; model_release; email) - Atlas is a multimodal model covering text, image, video, and 3D in one spatial context, which may matter if you build with 3D/video tooling, though it has no clear adoption path for coding workflows…
  - Link: https://worldlabs.ai/atlas?utm_source=tldrai

- **New video: @dejno and @luccasiau discuss how we launch new models on our API and the features that …** (Notable; model_release; x) - Anthropic's API team walks through how new model launches ship and how to rethink your harness and measure cost per task when upgrading, which matters for keeping Claude-based agents and tooling in s…
  - Link: https://x.com/ClaudeDevs/status/2120962481225146636

- **X3Guard: A 150M parameter prompt guard** (Notable; model_release; reddit) - A 150M-parameter open prompt-guard model that flags harmful and adversarial prompts in one pass and runs in-browser, relevant for agent input filtering.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xwyp7w/x3guard_a_150m_parameter_prompt_guard/

- **We've made some big updates to Projects in Claude Code! In a project, Claude coordinates your tasks…** (Notable; dev_tooling; x) - Claude Code Projects now has a proactive coordinator that splits tasks across parallel threads and reports their status, a workflow change worth testing against your current agent setup.
  - Link: https://x.com/ClaudeDevs/status/2121375309287301360

- **Anthropic has opened up Claude Mythos access to the public.** (Notable; model_release; reddit) - Reddit claims Anthropic's Cyber Verification Program now lets individuals with an ID get Claude Mythos access, which is unconfirmed and worth checking against Anthropic's official announcement before…
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xwguid/anthropic_has_opened_up_claude_mythos_access_to/

- **UI SDK** (Notable; dev_tooling; email) - UI SDK offers over 50 prebuilt interaction behaviors (focus, selection, popups, keyboard navigation) that coding agents can compose across frameworks, relevant to agent-driven frontend work in React…
  - Link: https://ui-sdk.dev?utm_source=tldrdev

## 2026-11-15

- **Claude Fable 5.2** (AI/Claude) - New Fable model (`claude-fable-5-2`), announced Nov 9 alongside Mythos 5.2 (restricted to vetted orgs); now the default Fable model in Claude Code.
  - Why it matters: 1M context at $8/$40 per Mtok ($0.20/Mtok cache reads) per the Claude Code changelog; saved Fable 5.1 selections migrate to `fable`, switch back with `/model claude-fable-5-1`. Re-check cost assumptions in agent pipelines pinned to older Fable IDs.
  - Link: https://www.anthropic.com/claude-fable-and-mythos-5-2

- **Claude Code Code Mode (v2.1.323)** (AI/Claude) - Experimental opt-in mode where Claude writes JavaScript that makes many tool calls in one step instead of one call per turn.
  - Why it matters: Suited to repeated edits across many files, filtering large search output before it enters context, and parallel commands. Enable with `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1`. Limits: interactive terminal only (no `-p`/SDK/VS Code), Anthropic API only, 10-minute cap on foreground code; auto-mode classifier reviews the code, not each call.
  - Link: https://code.claude.com/docs/en/code-mode

- **Claude Code v2.1.323 plugin `engines` field and 1M-context default** (AI/Claude) - `plugin.json` can now declare `engines["claude-code"]` so out-of-range plugins aren't loaded; unrecognized model IDs now assume 1M context (set `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` for 200K).
  - Why it matters: Plugin authors can pin compatible Claude Code versions; people using custom/gateway model IDs may see changed context and cost behavior.
  - Link: https://code.claude.com/docs/en/changelog.md

- **Claude Code v2.1.325 permission changes** (AI/Claude) - Sandboxed Bash now follows the normal permission flow (opt back in with `sandbox.autoAllowBashIfSandboxed: true`); scheduled tasks and `/loop` now ask before running skills that declare `allowed-tools` or hooks unless `Skill(name)` is in `permissions.allow`.
  - Why it matters: Unattended/scheduled agent runs may start prompting or stalling after upgrade; add explicit allow rules. Also includes a zstd decoding security fix.
  - Link: https://github.com/anthropics/claude-code/releases

- Repos: none reported today; I could not vet any candidate repos for safety this run, so none are listed.

## 2026-11-14 (AKD)

- **[Paper] Read Less, Solve More: Token-Efficient Sparse Reading of External Content for AI Agents** (Top pick; research; reddit) - A research paper proposing a sparse-reading control layer for agents that cuts tokens by up to 92.9% by withholding unneeded content, with a GitHub repo and integrations for three agent frameworks.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xvuit5/paper_read_less_solve_more_tokenefficient_sparse/

- **anthropics/claude-code v2.1.325** (Top pick; dev_tooling; github) - Claude Code v2.1.325 patches a zstd response-decoding security issue and fixes sandboxed git and subagent-model bugs, so upgrading is worth it for anyone running agents.
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.325

- **salesforce-sovereign-intelligence/SOV-Transcribe-1 · Hugging Face** (Top pick; model_release; reddit) - Salesforce released SOV-Transcribe-1, an open-weight ASR model (26.6B total, 4.6B active MoE) that can run on your own infrastructure with natural-language control over transcript style and context b…
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xvst4u/salesforcesovereignintelligencesovtranscribe1/

- **Runway Praxis-1 open-weight robotics model** (Top pick; model_release; email) - Open-weight 27B robotics model under Apache 2.0 with LoRA fine-tuning, but it sits outside this reader's agentic coding and agent-infra focus, so relevance is low.
  - Link: https://runway.com/news/company-news/praxis-1-is-now-available?utm_source=tldrai

- **A2UI 1.0 generative UI protocol** (Top pick; agents_mcp_skills; email) - A2UI 1.0 is an open protocol for agents to return native interactive UI, with web, Android, and iOS renderers you could try in a React/Vite app within a week.
  - Link: https://developers.googleblog.com/a2ui-10-build-delightful-fast-reliable-agentic-experiences/?utm_source=tldrai

- **Cyber at the Frontier: Introducing Daybreak Red Team & Daybreak Defense Factory** (Notable; agents_mcp_skills; youtube) - OpenAI's Daybreak adds a Codex plugin for automated vulnerability finding, patching, and agent-driven red-teaming, all run in isolated cloud environments, relevant to agent security work.
  - Link: https://www.youtube.com/watch?v=YmxpxJZvm4M

- **Self-hosted Claude Managed Agents** (Notable; agents_mcp_skills; email) - Self-hosted Claude Managed Agents (private beta) run sandboxes, credentials, and session history inside your own infrastructure, relevant to agent security and Agent SDK deployment.
  - Link: https://claude.com/resources/articles/self-hosted-claude-managed-agents?utm_source=tldrai

- **Spotify reportedly cut its Claude Code token costs by 90%, then open-sourced how it did it Their pl…** (Notable; agents_mcp_skills; x) - Spotify's open-sourced Claude Code plugin routes simple tasks like file reads and boilerplate to cheaper Gemini models, a concrete cost-reduction pattern you could adopt with a model-routing skill or…
  - Link: https://x.com/RoundtableSpace/status/2121615385766330843

- **All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI** (Notable; agents_mcp_skills; youtube) - This talk shows how a team merged about 11,000 AI-written PRs with a 0.5% revert rate by enforcing architecture with lint rules, runtime checks, and TLA+/Lean verification, and it points to Cursor's…
  - Link: https://www.youtube.com/watch?v=O_zcc6Xl12g

- **MCP vs CLI vs Skills: context costs** (Notable; agents_mcp_skills; email) - MCP servers load their full tool definitions into every request, costing roughly 59k tokens here versus about 1.4k for CLI and 3.3k for skills, so tool selection directly affects your context budget.
  - Link: https://openrouter.ai/blog/insights/mcp-vs-cli-vs-skills/?utm_source=tldrai

- **Agent Anomaly Detection on external benchmarks** (Notable; research; email) - Tests a runtime detector for agent misuse (goal hijack, tool misuse) on third-party benchmarks: 87% of harmful instructions caught, but up to 16% false alarms on high-impact tools.
  - Link: https://developers.googleblog.com/how-agent-anomaly-detection-scores-on-benchmarks-we-didnt-write/?utm_source=tldrai

- **Your AI coding agent writes the code, then leaves you to babysit the PR. Theo just shared the agent…** (Notable; agents_mcp_skills; x) - Ready-made Claude Code and Codex skills (council, full send, babysit) that automate review-to-merge for agent-written PRs, installable by copying into ~/.claude/skills.
  - Link: https://x.com/RoundtableSpace/status/2121577636778717385

- **I turned Karpathy's "80% of the way to ASD-STE100" tip into a Claude skill that makes AI text readable** (Notable; agents_mcp_skills; reddit) - A free MIT-licensed Claude Code skill that rewrites AI-generated prose into short, active-voice ASD-STE100 style, adoptable in minutes.
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xw2fu8/i_turned_karpathys_80_of_the_way_to_asdste100_tip/

- **Elevated errors on claude.ai, Claude Code, and platform.claude.com** (Notable; other; web) - Claude Code, the Claude API, and platform.claude.com are reporting elevated errors, so builds and agent runs depending on them may fail or stall right now.
  - Link: https://status.claude.com/incidents/nn11wk485zfn

- **Escaping SPACE: Part II** (Notable; agents_mcp_skills; email) - Perplexity's test of 12 models against its agent sandbox found network-control bypasses (DNS spoofing, shared-IP exploits) that were since patched, which is directly relevant to anyone running agents…
  - Link: https://www.perplexity.ai/hub/blog/escaping-space-part-ii?utm_source=tldrai

## 2026-11-14

- **Claude Fable 5.2 / Mythos 5.2** (AI/Claude) - New API models: 1M context, 128k max output, $8/$40 per MTok; Mythos 5.2 limited to verified orgs. Fast mode (`speed: "fast"`) at $16/$80.
  - Why it matters: computer use now needs the `computer_toolset_20260801` toolset (old `computer_20251124` returns 400), and replaying edited history with thinking blocks returns 400, so check agent code before migrating.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude API message threads (beta)** (AI/Claude) - Server keeps conversation state (`message-threads-2026-08-12` header); later requests send only new messages; threads expire 5 minutes after last request.
  - Why it matters: cuts payload and resend logic in chat/agent loops; mind the short expiry.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude Code v2.1.325** (AI/Claude) - Sandboxed Bash now follows normal permission flow unless `sandbox.autoAllowBashIfSandboxed` is true; `/loop` and scheduled tasks ask before running skills that declare `allowed-tools` or hooks (add `Skill(name)` to `permissions.allow`); zstd decoding security fix.
  - Why it matters: unattended routines may start prompting after upgrade; update permissions config.
  - Link: https://code.claude.com/docs/en/changelog

- **Opus 4.8 fast mode removal, Nov 30** (AI/Claude) - `speed: "fast"` on claude-opus-4-8 will error after Nov 30, 2026; migrate to Claude Opus 5.5.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **vercel-labs/agent-desktop** (GitHub) - Computer-use CLI that exposes a desktop app's accessibility tree as JSON with element refs; no model inside, your agent supplies the loop; macOS/Windows/Linux.
  - Why it matters: lets coding agents drive native apps without screenshots.
  - Link: https://github.com/vercel-labs/agent-desktop
  - Safety note: Apache-2.0, ~23.6k stars, 347 commits on main; I could not confirm last-commit date or contributor count, and did not inspect npm install scripts, so review `package.json` before installing. Requires OS accessibility permission.

## 2026-11-13 (AKD)

- **anthropics/claude-code v2.1.323** (Top pick; dev_tooling; github) - Claude Code v2.1.323 adds opt-in Code Mode and plugin engine-version gating, and a plugin-validate warning for Bash allow rules with wildcards in variable values, so check your plugins and allow rule…
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.323

- **Announcing the GraphQL over HTTP Specification** (Top pick; dev_tooling; email) - The GraphQL over HTTP spec standardizes request and response handling, so existing GraphQL clients and servers may need to conform to its status-code and media-type rules.
  - Link: https://graphql.org/blog/2026-11-12-announcing-the-graphql-over-http-spec/?utm_source=tldrdev

- **Claude Managed Agents can now run self-hosted, inside your own perimeter (private beta)** (Top pick; agents_mcp_skills; reddit) - Self-hosted Managed Agents keep the harness, sandboxes, credentials, and session history in your own perimeter, but model requests still go to whichever provider you choose, and zero retention applie…
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xuw68g/claude_managed_agents_can_now_run_selfhosted/
  - Also covered by: [Self-hosted Claude Managed Agents](https://claude.com/resources/articles/self-hosted-claude-managed-agents?utm_source=tldrai) (email)

- **Modern Web Guidance 1.0** (Top pick; agents_mcp_skills; email) - Gives coding agents expert-reviewed web platform guidance and Baseline compatibility data, plus a codebase scan for safe modern-feature upgrades, directly usable with Claude Code and skills.
  - Link: https://developer.chrome.com/blog/modern-web-guidance-v1?utm_source=tldrdev

- **Gemini 4 Hydrogen** (Top pick; model_release; email) - New Gemini 4 Hydrogen targets coding and agentic workflows at $1.50/$7.50 per million tokens, a cheaper option to benchmark against Claude for agent tasks.
  - Link: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/?utm_source=tldrai
  - Also covered by: [Gemini 4 Hydrogen: Everyday Model for Everyone from Google](https://www.youtube.com/watch?v=6GA_zSxtSHE) (youtube)

- **Qwen Code** (Notable; agents_mcp_skills; email) - Qwen Code is an open-source terminal, editor, and headless coding agent with MCP and local-model support, a direct alternative to Claude Code worth evaluating for agent workflows.
  - Link: https://github.com/QwenLM/qwen-code?utm_source=tldrdev

- **Perplexity releases Decider v1.3 (26B) and Decider Flash v1.3 (5B): open-weight (Apache 2.0) classification/decision models** (Notable; model_release; reddit) - Open-weight Apache 2.0 classifier models (26B and 5B) that return probability distributions plus verbatim span extraction, but they require Perplexity's custom pplx_decider package because bidirectio…
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xv7fku/perplexity_releases_decider_v13_26b_and_decider/

- **A 145-billion-parameter AI model now runs on a laptop. Offline. Free. Edge0 just open-sourced Edge0…** (Notable; model_release; x) - A 145B open-weight MoE model claiming ~10B active params, 256K context, and local offline runs on consumer hardware, though the GPQA and Opus comparisons are self-reported and unverified.
  - Link: https://x.com/RoundtableSpace/status/2121162400586244358

- **Fable 5.2 or Opus? When to use each model in Claude Code** (Notable; model_release; youtube) - A practical guide to choosing among Claude Fable 5.2, Opus 5.5, Sonnet 5.5, and Haiku 5.5 inside Claude Code, which directly affects how you route coding tasks and manage cost.
  - Link: https://www.youtube.com/watch?v=C33hJGt-ySg

- **Discussion Hub for new Claude incident: Elevated errors on claude.ai, the Claude API, and Claude Code on Nov 13, 2026** (Notable; dev_tooling; reddit) - Anthropic reports a multi-surface outage on Nov 13 affecting the Claude API, Claude Code, and connectors, with scheduled tasks delayed and some runs skipped; check any automation you rely on.
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xv7hxz/discussion_hub_for_new_claude_incident_elevated/
  - Also covered by: [Elevated errors on claude.ai, Claude Code, and platform.claude.com](https://status.claude.com/incidents/nn11wk485zfn) (web)

- **225,000 Lines of Tests, Written and Merged by Agents - Kush Agrawal, Duolingo** (Notable; agents_mcp_skills; youtube) - Duolingo's real-world case of agents autonomously opening, fixing, and merging 700+ test PRs (coverage 11% to 24%) shows a concrete pipeline pattern worth copying for Claude Code-driven workflows.
  - Link: https://www.youtube.com/watch?v=D_4Rn6uLdQM

- **DeepSeek flash max is the first model to reach >1% on challenging SWE-sweep bug finding benchmark** (Notable; research; reddit) - First open-weight model to clear 1% on SWE-sweep, a hard blind bug-finding benchmark, though proprietary leaders still sit around 9–13%.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xvcgxq/deepseek_flash_max_is_the_first_model_to_reach_1/

- **thinkingmachines/Inkling-2-Small is released!** (Notable; model_release; reddit) - A new open-weight small model from Thinking Machines (Inkling-2-Small) that could be a local or cheap option for agent and coding workloads, worth checking benchmarks and license before adopting.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xuqplg/thinkingmachinesinkling2small_is_released/

- **Agents Made Code Free. Maintaining It Didn't Get Cheaper. - Dmitry Buykin, Maersk** (Notable; agents_mcp_skills; youtube) - Agents make writing code nearly free but not maintenance, and this talk offers patterns and an 18-question audit checklist for AI-written repos months in.
  - Link: https://www.youtube.com/watch?v=oeknLUsN_GE

- **How two engineer side projects became the agent taking action inside Dropbox** (Notable; agents_mcp_skills; email) - Dropbox's production agent design shows concrete sandboxing patterns: per-conversation VMs, credentials kept out of agent reach, approval gates, and undoable changes, all directly relevant to agent s…
  - Link: https://dropbox.tech/machine-learning/how-two-engineer-side-projects-became-the-agent-taking-action-inside-dropbox?utm_source=tldrdev

## 2026-11-13

- **Self-hosted Claude Managed Agents** (AI/Claude) - Run the full Managed Agents service on your own infrastructure (announced Nov 12).
  - Why it matters: lets teams with data-residency or compliance needs run server-hosted agents without sending work to Anthropic's cloud; access is via your Anthropic account team.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude Code 2.1.323: experimental Code Mode + plugin version ranges** (AI/Claude) - Opt-in mode where Claude writes JavaScript to call its tools; plugins can declare `engines["claude-code"]` ranges and `claude plugin validate` now type-checks TypeScript hooks.
  - Why it matters: Code Mode may cut round-trips on multi-tool tasks; version ranges make plugin distribution safer.
  - Link: https://code.claude.com/docs/en/changelog

- **Claude Fable 5.2 / Mythos 5.2 API migration notes** (AI/Claude) - Launched Nov 9: 1M context, 128k output, $8/$40 per MTok, fast mode via `speed: "fast"` ($16/$80).
  - Why it matters: breaking changes when migrating: computer use needs `computer_toolset_20260801`, prefix check can return 400 on edited history, 30-day retention required (no ZDR by default).
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Message threads (beta) on the Claude API** (AI/Claude) - Server-side conversation state (`message-threads-2026-08-12` header); later requests send only new messages.
  - Why it matters: smaller payloads and simpler agent loops versus resending full history.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **vercel-labs/agent-desktop** (GitHub repo) - Computer-use CLI that exposes a desktop app's accessibility tree as JSON with element refs an agent can act on; macOS, Windows, Linux, plus a C library.
  - Why it matters: structured, token-cheap alternative to screenshot-based computer use for automating native apps or GUI testing.
  - Link: https://github.com/vercel-labs/agent-desktop
  - Safety note: Apache-2.0, ~23.1k stars, 344 commits, Vercel Labs org. I could not confirm last-commit date or contributor count from the page; review before running.

## 2026-11-12 (AKD)

- **Heads up: Claude Code's "don't ask again" has been leaking secrets into public repos** (Top pick; agents_mcp_skills; reddit) - Claude Code's "don't ask again" approvals save exact commands, including any inline secrets, as plaintext in `.claude/settings.local.json`, which often gets committed to public repos because it isn't…
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xtx4ik/heads_up_claude_codes_dont_ask_again_has_been/

- **[AINews] Fable 5.2 retakes World #1 LLM spot as $ANT IPO roadshow begins** (Top pick; model_release; web) - Fable 5.2 cuts per-token prices 20% but uses more tokens, so per-task cost rose from $67 to $88 on SemiAnalysis's professional-task benchmark, which matters for production effort-setting choices.
  - Link: https://latent.space/p/ainews-fable-5-2-retakes-world-1-llm-spot-as-ant-ipo-roadshow-begins/
  - Also covered by: [Fable 5.2 or Opus? When to use each model in Claude Code](https://www.youtube.com/watch?v=C33hJGt-ySg) (youtube)

- **modelcontextprotocol/servers v2.4.0** (Top pick; agents_mcp_skills; github) - Six security fixes in the MCP filesystem, git, and fetch servers; upgrade to server-filesystem 2.3.0 and the 2026.11.11 git/fetch releases now, since older versions allow symlink-race reads outside a…
  - Link: https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0

- **Gemini 4 Carbon is now available** (Top pick; model_release; email) - Gemini 4 Carbon is now on the API with claimed top scores on coding and automation benchmarks at about half the cost per task, which matters if you evaluate models for agent workloads.
  - Link: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/?utm_source=tldrai

- **[AINews] D-Day (Decision Models Day)** (Top pick; model_release; web) - Google's Gemini Decision 1 is a new production decision-model API ($0.10 per million input tokens, ~200ms latency) that scores closed-set choices in one pass, a new option for classification-style ca…
  - Link: https://latent.space/p/ainews-d-day-decision-models-day/
  - Also covered by: [Google launched the Gemini Decisions API, powered by its new Gemini Decision 1 model. → it doesn't …](https://x.com/RoundtableSpace/status/2120694316297498819) (x)

- **Self-hosted Claude Managed Agents is now in private beta. You can host the agent harness, sandboxes…** (Notable; agents_mcp_skills; x) - Lets you run the Claude agent harness, sandboxes, and session history in your own cloud or on-prem, a relevant option for agent security and data-residency work, though it's private beta.
  - Link: https://x.com/ClaudeDevs/status/2120938988165091693

- **OpenAI open-sources MCP Extensions** (Notable; agents_mcp_skills; email) - OpenAI's open-source MCP Extensions adds ChatGPT-only features like sidebar entry points and custom file viewers, so MCP servers built for Claude may need separate handling to work well in ChatGPT.
  - Link: https://github.com/openai/mcp-extensions?utm_source=tldrai

- **Your Sub-Agents Are a Distributed System. Treat Them Like One. - Girish Konda, Microsoft** (Notable; agents_mcp_skills; youtube) - Sub-agent orchestration failures (partial success reported as done, duplicate side effects, unseen rate limits) are mapped to distributed-systems fixes, with an MCP-based pattern directly relevant to…
  - Link: https://www.youtube.com/watch?v=DxP5aW4VknQ

- **Rethinking Claude Code Best Practices — Lydia Hallie, Anthropic** (Notable; agents_mcp_skills; youtube) - A talk from Anthropic's Claude Code developer relations lead on which Claude Code setup practices to drop or keep for the Claude 5.5 models, directly relevant to your workflow.
  - Link: https://www.youtube.com/watch?v=vlfCjWuv4es

- **Building the Claude API for the Frontier** (Notable; dev_tooling; youtube) - The video covers practical Claude API migration guidance, including changing effort mid-conversation without breaking prompt caching, which matters if you build on the Messages API.
  - Link: https://www.youtube.com/watch?v=p2xvJAbF-i4

- **qvac/BotPsy-0.8B · Hugging Face - On-Device Personal Assistant with a Sub-Billion-Parameter Agentic Language Model** (Notable; model_release; reddit) - A 0.8B open-weight function-calling model built on Qwen3.5-0.8B that claims SOTA agentic scores for its size, making on-device tool-use agents practical to test.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xu8685/qvacbotpsy08b_hugging_face_ondevice_personal/

- **improve (agent skill)** (Notable; agents_mcp_skills; email) - An agent skill that audits a codebase and writes prioritized plans for another agent to execute, directly usable in Claude Code workflows.
  - Link: https://github.com/shadcn/improve?utm_source=tldrdev

- **huawei-csl/MACaQ** (Notable; repo_library; github) - Offers a model-agnostic quantizer that outputs GGUF and runs across llama.cpp, vLLM, and Diffusers, so it could let you shrink and run your own image or video models locally with one tool.
  - Link: https://github.com/huawei-csl/MACaQ

- **huawei-csl/Qwen3.6-35B-A3B-MACaQ-R-GGUF · Hugging Face** (Notable; model_release; reddit) - Huawei released a GGUF quantization of Qwen3.6-35B-A3B using their MACaQ method, a local-inference option worth testing against your current quantized models.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xu7cyr/huaweicslqwen3635ba3bmacaqrgguf_hugging_face/

- **Your SKILL.md Is 70% Stuff the Model Already Knows - Nikolay Petrov, Intel** (Notable; agents_mcp_skills; youtube) - Shows how to audit a SKILL.md by testing each claim with and without it, so you can trim the ~70% the model already knows and keep the details that actually change output.
  - Link: https://www.youtube.com/watch?v=yzx4IuEh_tU

## 2026-11-12

- **Claude Fable 5.2 / Mythos 5.2** (AI/Claude tooling) - Launched Nov 9 (`claude-fable-5-2`): 1M context, 128k output, always-on adaptive thinking, $8/$40 per MTok (down from $10/$50 for Fable 5.1); fast mode via `speed: "fast"` at $16/$80. Mythos 5.2 is limited to verified orgs.
  - Why it matters: cheaper top-tier model for long-horizon agent work. Migration gotchas: thinking blocks must be returned unmodified (editing system/tools/earlier messages then sending a thinking block gives a 400), `computer_20251124` now 400s outside Bedrock (use `computer_toolset_20260801`), and 30-day data retention is required (no ZDR by default).
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Messages API message threads (beta)** (AI/Claude tooling) - Nov 2 beta (header `message-threads-2026-08-12`): the server keeps conversation state so follow-up requests send only new messages.
  - Why it matters: smaller payloads and lower time-to-first-token for chat/agent loops. Threads expire 5 min after last request and are deleted within 1 hour, so not for long-idle sessions.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude Console IP allowlist (beta)** (AI/Claude tooling) - Nov 5: restrict API requests to up to 1,000 IPs/CIDRs per organization.
  - Why it matters: limits the blast radius of a leaked API key; useful for production services with fixed egress IPs.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude Code v2.1.321** (AI/Claude tooling) - Nov 9: adds Fable 5.2 as default Fable model, `--settings <file>` for `claude remote-control`, and several security fixes (MCP OAuth no longer leaks refresh tokens on cross-host redirects; deny rules now apply to `cp`/`mv` targets; read-only Bash can't escape the sandbox). v2.1.322 (Nov 10) adds Vertex fast mode.
  - Why it matters: worth upgrading for the permission/sandbox fixes alone. v2.1.319 also added `/claude-api latency-optimize`, which profiles and tunes slow API code.
  - Link: https://github.com/anthropics/claude-code/releases

- **vercel-labs/agent-desktop** (GitHub repo) - CLI + C library giving agents desktop computer use on macOS/Windows/Linux by reading the accessibility tree (JSON element refs, no screenshots, no model inside).
  - Why it matters: a cheaper, deterministic alternative to screenshot-based computer use for automating GUI apps from any agent.
  - Link: https://github.com/vercel-labs/agent-desktop
  - Safety note: Apache-2.0, ~22.5k stars, 1.7k forks, 341 commits. I could not confirm last-commit date or contributor list from the page; npm package ships native binaries, so review `package.json` scripts/source before installing, and note snapshots can capture private desktop content.

