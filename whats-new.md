# What's New Digest

Daily digest of AI/Claude tooling advances and vetted GitHub repos. Newest entry first. Maintained by a scheduled routine.

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

## 2026-11-11

- **Claude Code v2.1.319 / v2.1.322** (AI/Claude tooling) - Recent releases add MCP task support (background tasks that report back), `permissions.denyInsteadOfPrompting`, `CLAUDE_CODE_DISABLE_FEATURE_FLAGS`, and fast mode on Vertex (v2.1.322, Nov 10).
  - Why it matters: `denyInsteadOfPrompting` makes unattended/CI agent runs deterministic (denied calls don't stall), and MCP background tasks suit long-running tool servers. Note v2.1.319 changed auto mode behind LLM gateways or with telemetry off (set `CLAUDE_CODE_AUTO_MODE_SERVER=0` to keep the classifier).
  - Link: https://github.com/anthropics/claude-code/releases

- **Claude Agent SDK (Python) v0.2.177-0.2.180** (AI/Claude tooling) - Nov 3-9 releases; v0.2.177 added an `on_failure` option to `HookMatcher`, v0.2.178 bundles Claude CLI 2.1.318.
  - Why it matters: hooks that can react to failures help build safer, self-correcting agent pipelines. Release notes for 0.2.179/0.2.180 were not shown, so check before upgrading.
  - Link: https://github.com/anthropics/claude-agent-sdk-python/releases

- **MCP spec revision 2026-07-28 (stable)** (AI/Claude tooling) - Latest stable Model Context Protocol spec; SDKs adopt it at their own pace.
  - Why it matters: check that your MCP servers/clients target the current revision. I did not read the changelog itself.
  - Link: https://github.com/modelcontextprotocol/modelcontextprotocol/releases

- **Prime Agent (PrimeIntellect-ai)** (GitHub repo) - Self-improving RLM coding/long-running agent harness, open-sourced Aug 2026 (older than 7 days, included as the one repo I could verify).
  - Why it matters: reference design for long-horizon autonomous coding agents.
  - Link: https://github.com/PrimeIntellect-ai/prime-agent
  - Safety note: MIT license; ~22.7k stars, 5,269 commits; last commit date not verified. Unix installer is `curl | sh`, so read it first; README warns it is not a sandbox and runs model-generated code with your permissions.

## 2026-11-10 (AKD)

- **anthropics/claude-code v2.1.321** (Top pick; dev_tooling; github) - Claude Code v2.1.321 adds the Fable 5.2 default model and fixes several sandbox, MCP OAuth token-leak, and permission-check bugs, so review the upgrade and update any pinned model IDs.
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.321
  - Also covered by: [[AINews] Fable 5.2 retakes World #1 LLM spot as $ANT IPO roadshow begins](https://latent.space/p/ainews-fable-5-2-retakes-world-1-llm-spot-as-ant-ipo-roadshow-begins/) (web)
  - Also covered by: [Claude Fable 5.2 is cheaper than the last Fable: $8 per million input tokens and $40 per million ou…](https://x.com/RoundtableSpace/status/2119999739777491426) (x)
  - Also covered by: [Fable 5.2 is now available in the Claude Platform and Claude Code. It’s up to 30% faster than Fable…](https://x.com/ClaudeDevs/status/2119868698613956992) (x)
  - Also covered by: [Introducing Claude Fable 5.2](https://www.youtube.com/watch?v=6a1QSJlsYpU) (youtube)

- **Claude Code's "Don't Ask Again" exposes passwords in 1,122 public GitHub files** (Top pick; agents_mcp_skills; web) - Claude Code's "Don't Ask Again" permission option is linked to credentials committed in 1,122 public GitHub files, so review those approvals and rotate any exposed secrets.
  - Link: https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again

- **Gemini 4 Carbon: The Most Capable Model from Google** (Top pick; model_release; youtube) - Google's Gemini 4 Carbon is aimed at long unattended engineering tasks, and this video shows real outputs (including a 100+ pass 3D engine build) plus four prompting rules, though the creator has ear…
  - Link: https://www.youtube.com/watch?v=lQ6wwLHqDAg

- **By default, Claude Code can read files anywhere on your computer. Your SSH keys, your .env files, y…** (Top pick; agents_mcp_skills; x) - Claude Code's new settings block file reads and writes outside the working directory (even in bypass mode) and deny SSH, AWS, and .env access, which matters for agent security; the write block needs…
  - Link: https://x.com/RoundtableSpace/status/2120045855109509406

- **Amazon just replaced Claude in one of the world's biggest internal ticketing systems. With a 2B mod…** (Top pick; repo_library; x) - A small 2B open model replaced Claude Sonnet for ticket labeling at Amazon, with reported cost and latency drops and a pip-installable CLI to try the same pattern, which is a concrete option for rout…
  - Link: https://x.com/RoundtableSpace/status/2120112986274881756

- **anthropics/anthropic-sdk-python v2.8.0** (Notable; dev_tooling; github) - Bedrock and Vertex model-ID and path-handling fixes change how `;` and empty IDs are treated, so check any custom Bedrock/Vertex model strings or base URLs before upgrading.
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.8.0

- **Safely scaling multi-agent teams with Claude Fable 5.2** (Notable; agents_mcp_skills; email) - A 1,000-agent team reproducing a Fermat's Last Theorem formal proof with sandboxed agents, shared Git, and SQL coordination is a concrete multi-agent architecture pattern worth studying.
  - Link: https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/?utm_source=tldrdev
  - Also covered by: [Claude Fable 5.2 and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) (web)

- **MiniMax H3-Image Released, an Open-Weight Image Model built on H3** (Notable; model_release; reddit) - An open-weight image model from MiniMax, relevant as a locally runnable option for the ComfyUI and image tooling workflow you already use.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xso1ie/minimax_h3image_released_an_openweight_image/
  - Also covered by: [MiniMaxAI/MiniMax-H3-Image · Hugging Face](https://www.reddit.com/r/LocalLLaMA/comments/1xsp3xt/minimaxaiminimaxh3image_hugging_face/) (reddit)

- **NaiveAI Promises 2,100 Tokens per Second. How Well Does It Code?** (Notable; model_release; web) - Naive-N0.5-Flash is an open-weights coding model claiming about 2,100 tokens/sec, built by fine-tuning Xiaomi's MiMo-V2.5 with DeepSeek Sparse Attention and a 1M context, so the throughput and real c…
  - Link: https://latent.space/p/naiveai/

- **Claude Fable 5.2 Release vs Opus 5.5: Don't Pay for Max Effort** (Notable; model_release; youtube) - It's a model-choice guide for Claude Code users: Fable 5.2 at High effort matches Opus 5.5 on FrontierCode at about half the cost, so it changes which model and effort level to default to.
  - Link: https://www.youtube.com/watch?v=7cx2unMXBYY

- **anthropics/claude-code v2.1.322** (Notable; dev_tooling; github) - Claude Code v2.1.322 adds fast mode on Vertex (global, US, EU regions) with automatic fallback to standard speed, relevant if you run Claude Code through Vertex.
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.322

- **Your Agent Hates Your CLI - Ayush Bhardwaj, Allos AI** (Notable; agents_mcp_skills; youtube) - Analysis of about 20,000 agent tool calls shows where CLI output hides failures or forces repeated queries, with concrete fixes and a replay-test method for agent-facing tools.
  - Link: https://www.youtube.com/watch?v=rS36lYuvXQ8

- **You Can't Tell What an Agent Skill Will Do by Reading It - Roey Ben Chaim, Zenity** (Notable; agents_mcp_skills; youtube) - Reading a skill's SKILL.md can't reveal what it does at runtime, since it can chain-install packages and fetch remote prompts, so treat skills as dependencies and sandbox them.
  - Link: https://www.youtube.com/watch?v=_7P580m4kPY

- **speakleash/Bielik-11B-v3.1-Instruct · Hugging Face** (Notable; model_release; reddit) - Bielik-11B-v3.1-Instruct is a new open-weight 11B model with GGUF builds, useful if you want a local option for Polish or other European-language work with tool use.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xsrg0l/speakleashbielik11bv31instruct_hugging_face/

- **How Anthropic Builds Agent Memory** (Notable; research; email) - Anthropic's research on agent memory, including a "dreaming" consolidation step during idle time, bears directly on how you'd design persistent memory for Claude Agent SDK agents and MCP-based workfl…
  - Link: https://www.anthropic.com/research/components-of-agent-memory?utm_source=tldrai

## 2026-11-10

- **Claude Code v2.1.322 / v2.1.321 / v2.1.319** (AI/Claude tooling) - Fast mode on Vertex (global/US/EU) in v2.1.322; Fable 5.2 (`claude-fable-5-2`, 1M context, $8/$40 per Mtok) becomes the default Fable model in v2.1.321.
  - Why it matters: v2.1.321 fixes security issues (MCP OAuth no longer leaks refresh tokens on cross-host redirects; read-only Bash no longer escapes the sandbox; deny rules now cover `cp`/`mv` into directories). v2.1.319 adds MCP tasks in the terminal (background long-running MCP calls) and `permissions.denyInsteadOfPrompting` for unattended/headless agent runs.
  - Link: https://github.com/anthropics/claude-code/releases

- **anthropic-sdk-python v2.7.0** (AI/Claude tooling) - Adds `claude-fable-5-2` and `claude-mythos-5-2` model IDs; structured-output schemas now keep `const`; Bedrock/Vertex clients honor `ANTHROPIC_CUSTOM_HEADERS`.
  - Why it matters: v2.5.0 made `OverloadedError`/`ServiceUnavailableError` subclasses of `InternalServerError`, so existing `except InternalServerError` blocks now catch them. Review retry logic when upgrading.
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases

- **MCP spec revision 2026-07-28 (stable)** (AI/Claude tooling) - Latest stable Model Context Protocol revision, following the 2025-11-25 one.
  - Why it matters: check that MCP servers/clients you build or depend on target the current revision. Details are in the linked changelog on the release page.
  - Link: https://github.com/modelcontextprotocol/modelcontextprotocol/releases

_No GitHub repos included today: searches surfaced only older or unverifiable trending lists, and nothing could be vouched for._

## 2026-11-09 (AKD)

- **Fable 5.2 REVIEW Here is what's actually different and what to try first (cheaper, faster, way fewer blocks)** (Top pick; model_release; reddit) - A Reddit early-access review of a new model "Fable 5.2" (claude-fable-5-2) reporting lower API prices ($8/$40 per million tokens), faster output, and a changed model string relevant to an agent/API b…
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xs2wdl/fable_52_review_here_is_whats_actually_different/
  - Also covered by: [anthropics/claude-code v2.1.321](https://github.com/anthropics/claude-code/releases/tag/v2.1.321) (github)
  - Also covered by: [Fable 5.2 is now available in the Claude Platform and Claude Code. It’s up to 30% faster than Fable…](https://x.com/ClaudeDevs/status/2119868698613956992) (x)
  - Also covered by: [Introducing Claude Fable 5.2](https://www.youtube.com/watch?v=6a1QSJlsYpU) (youtube)
  - Also covered by: [Claude Fable 5.2 vs Opus 5.5: Don't Pay for Max Effort](https://www.youtube.com/watch?v=7cx2unMXBYY) (youtube)
  - Also covered by: [Fable 5.2 just landed.](https://www.reddit.com/r/ClaudeAI/comments/1xs0dct/fable_52_just_landed/) (reddit)

- **Hackers now have AI agents searching GitHub for your API keys, 24/7. Microsoft just warned that att…** (Top pick; industry_business; x) - Attackers are using AI agents to scan public GitHub repos for leaked cloud and AI API keys, so any key that ever touched a public repo should be rotated and treated as compromised.
  - Link: https://x.com/RoundtableSpace/status/2119675100911804878

- **anthropics/anthropic-sdk-python v2.7.0** (Top pick; dev_tooling; github) - Adds claude-fable-5-2 and claude-mythos-5-2 model IDs plus Bedrock/Vertex and structured-output fixes, so check any pinned model names and schema handling after upgrading.
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.7.0

- **Anthropic open-sourced a way to prove which model actually answered your request (and it targets exactly the "is my provider serving a quantized model?" problem)** (Top pick; repo_library; reddit) - Anthropic's FlashProve (Apache 2.0, unmaintained research prototype) lets you verify which model served a reply, but current limits (1,024-token context, one-token checks, ~19 MB proofs) make it a wa…
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xrydq5/anthropic_opensourced_a_way_to_prove_which_model/

- **The One Thing Every AI Agent Framework Agrees On - Mislav Ivanda, Daytona** (Top pick; agents_mcp_skills; youtube) - Argues that where agent-generated code runs (a separate sandboxed computer versus allow lists or embedded runtimes) is the hard-to-swap decision, and that CrewAI, AG2 and the OpenAI Agents SDK are al…
  - Link: https://www.youtube.com/watch?v=WWIFiQi9U4w

- **Claude Code can now use your phone. And it has to ask you before anything risky. Pinky lets any AI …** (Notable; agents_mcp_skills; x) - Pinky is an open-source MCP server that lets Claude Code or Codex drive a real iPhone or Android, with confirmation gates on payments and sends, a sandboxed setup for banking and password apps, and s…
  - Link: https://x.com/RoundtableSpace/status/2119750598480343348

- **Spec Kit** (Notable; agents_mcp_skills; email) - Spec Kit gives agentic coding tools reusable spec-driven workflows and templates, a concrete process you could adopt in Claude Code within a week.
  - Link: https://github.com/github/spec-kit?utm_source=tldrdev

- **meituan-longcat/LongCat-2.5 · Hugging Face** (Notable; model_release; reddit) - A 1.6T-parameter open-weights multimodal model from Meituan, relevant to local-inference users only if it's runnable at quantized sizes; the Reddit post itself gives no benchmarks, license, or hardwa…
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xrsptp/meituanlongcatlongcat25_hugging_face/

- **Anthropic just made the skills behind Claude's Word, Excel, PowerPoint and PDF files fully open sou…** (Notable; agents_mcp_skills; x) - Anthropic's document skills for Word, Excel, PowerPoint, and PDF are now open source, so they can be reused in your own agents, subject to the license terms.
  - Link: https://x.com/RoundtableSpace/status/2119780797674832359

- **Which Claude model should you build with? Our new guide breaks down when to use Fable 5.2, Opus 5.5…** (Notable; model_release; x) - It's an official Claude model-selection guide covering Fable 5.2, Opus 5.5, Sonnet, and Haiku, including effort tuning and routing subagents to cheaper models, directly relevant to Claude API and Age…
  - Link: https://x.com/ClaudeDevs/status/2119898687803621427

- **Nanoutrolley/roblox-studio-mcp** (Notable; agents_mcp_skills; github) - An MCP server that lets Claude or Cursor read Roblox Studio object trees and run Lua scripts and playtests, a concrete adoptable pattern for agent-driven game dev tooling.
  - Link: https://github.com/Nanoutrolley/roblox-studio-mcp

- **Securing AI Agents: Lessons From Real-World Deployment** (Notable; agents_mcp_skills; email) - Uber's production approach to agent security (scoped intents, runtime behavioral checks, prompt provenance) gives a concrete pattern for adding guardrails to your own agent tooling, beyond traditiona…
  - Link: https://x.com/UberEng/status/2118769501332463762?utm_source=tldrdev

- **PI-Desktop** (Notable; agents_mcp_skills; email) - PI-Desktop is an Electron and Rust workspace that unifies coding agents, models, and MCP-based plugins, which overlaps directly with your Claude Code and MCP setup and is worth testing for local-mode…
  - Link: https://github.com/vastsa/PI-Desktop?utm_source=tldrdev

- **M4 Pro vs M5 Pro (24GB): Qwen 3.8 Flash Next IQ3 with MoEShift at 374 tok/s prefill, 14.7 tok/s decode, 8.5GB peak memory** (Notable; research; reddit) - Shows a 125B MoE model running on a 24GB Apple Silicon Mac via SSD offloading (MoEShift) at 14.7 tok/s decode and 374 tok/s prefill, an adoptable local-inference option for an agent setup, though bas…
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xrq2fv/m4_pro_vs_m5_pro_24gb_qwen_38_flash_next_iq3_with/

- **How One Founder Manages 20 AI Coding Agents at Once - Ryan Carson, Untangle** (Notable; agents_mcp_skills; youtube) - One founder's workflow of a manager agent supervising up to 20 cloud builder agents, with automated review, QA, and a merge queue, is a concrete pattern to borrow for Claude Code and Agent SDK setups.
  - Link: https://www.youtube.com/watch?v=BTtyguoPvBU

## 2026-11-09

- **Claude Code v2.1.317-2.1.319** (AI/Claude tooling) - Three releases in Nov 3-6 adding safer unattended runs and background MCP handling.
  - Why it matters: `permissions.denyInsteadOfPrompting` lets headless/scheduled runs deny a blocked tool call and continue instead of stalling; long-running MCP tool calls now go to the background with the result reported on completion; `claude -p` exits 1 when auto mode refuses actions or a full disk loses transcript writes (easier CI/automation checks); a new check asks before a tool call sends your account email to the network; `/claude-api latency-optimize` reviews Claude API code for slow spots; Agent SDK hook callbacks support `onFailure: "block"`.
  - Link: https://github.com/anthropics/claude-code/releases

## 2026-11-08 (AKD)

- **If you ever clicked “Yes, and don’t ask again” in Claude Code, check one file before your next push** (Top pick; agents_mcp_skills; reddit) - Claude Code saves "always allow" commands verbatim to .claude/settings.local.json, so any secret in an approved command can leak via git; check the file and rotate anything exposed.
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xqxx5b/if_you_ever_clicked_yes_and_dont_ask_again_in/
  - Also covered by: [Claude Code's "Don't Ask Again" exposes passwords in 1,122 public GitHub files](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) (web)

- **Meta open-sourced Astryx, a design system built for people and the AI agents working with them. → F…** (Top pick; repo_library; x) - Meta's MIT-licensed Astryx is a React 19 and StyleX design system (in beta) that gives coding agents a fixed component set to build from, which fits the React and Tailwind stack.
  - Link: https://x.com/RoundtableSpace/status/2119395759745384863

- **The web scraper your AI agent has been missing. 99K stars. Scrapling covers the whole job: → Fast r…** (Top pick; repo_library; x) - Scrapling is an open-source scraper with an MCP server and agent skill that Claude Code can drive directly, adoptable in an afternoon for web-data tasks.
  - Link: https://x.com/RoundtableSpace/status/2119403309656310231

- **Claude can now read your bank accounts. Not move money, just read. Personal Finance is rolling out …** (Top pick; model_release; x) - Read-only Plaid connection to bank accounts with up to two years of transactions, rolling out in US beta on paid tiers; a personal-finance data-access surface, not a developer API, so it's of limited…
  - Link: https://x.com/RoundtableSpace/status/2119312712740278669
  - Also covered by: [Personal Finance in Claude](https://claude.com/resources/articles/introducing-personal-finance-in-claude?utm_source=tldrai) (email)

- **Gemini Omni 1.2 Flash** (Top pick; model_release; email) - Gemini Omni 1.2 Flash offers faster, cheaper, longer video generation via API, relevant to your AI video tooling alongside HyperFrames and Remotion.
  - Link: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/?utm_source=tldrai

- **HeyGen's HyperFrames can now rebuild any video as an editable project, so Claude can recreate a cli…** (Notable; dev_tooling; x) - HyperFrames' new reverse-engineering feature lets Claude rebuild a video as an editable HTML project, directly relevant to your HyperFrames and Claude Code workflow, though it's a Pro-only feature.
  - Link: https://x.com/RoundtableSpace/status/2119433508670132372

- **Your Coding Agent Can't Undo Its Own Mistakes - Tanmay Sah & Dolly Sah** (Notable; research; youtube) - Relevant to agent sandboxing and safety: it shows Git rollback misses external API calls, runtime config, and notifications, and that about 42% of capability-improving changes also broke recovery.
  - Link: https://www.youtube.com/watch?v=BT1Mo-fD-g0

- **GG Coder desktop coding agent** (Notable; agents_mcp_skills; email) - GG Coder is a desktop coding agent that runs on existing subscriptions, API keys, or local models, and its reusable agent packages are AGPL-3.0 licensed, which matters for embedding it in your own pr…
  - Link: https://github.com/KenKaiii/gg-framework?utm_source=tldrdev

- **Build live apps in Cursor and share them** (Notable; dev_tooling; email) - Cursor can now go from a description to a deployed, shareable app with database and security checks, a quick way to test agentic full-stack builds.
  - Link: https://x.com/cursor_ai/status/2118458629091426304?utm_source=tldrai

- **[AINews] Inkling 2 Small: 17A-594B trained in 68 hours on 12T tokens, beating Muse Spark** (Notable; model_release; web) - Inkling 2 Small is a new open-weight model trained natively in NVFP4 on under 12T tokens, competitive with same-size Chinese models and highlighting customizability for fine-tuning.
  - Link: https://latent.space/p/ainews-inkling-2-small-17a-594b-trained-in-68-hours-on-12t-tokens-beating-muse-spark/
  - Also covered by: [Thinking Machine's Inkling 2 Small is Here](https://www.youtube.com/watch?v=3fmkbkkhxQ8) (youtube)

- **We've made it easier to get your repo running in Claude Code cloud sessions on Pro, Max, and Ultra.…** (Notable; dev_tooling; x) - Claude Code cloud sessions on Pro, Max, and Ultra now auto-detect a repo's dependencies, network needs, and API keys, then cache the environment, which lowers setup friction for agentic coding.
  - Link: https://x.com/ClaudeDevs/status/2118795192090386454

- **React.lazy, Suspense and the hidden 300 ms delay** (Notable; research; email) - Relevant to React/Vite work: a 300 ms Suspense reveal throttle can dominate perceived startup even when lazy-loaded chunks arrive quickly, so measure before shrinking bundles.
  - Link: https://tabwidgets.com/blog/react-lazy-suspense-delay?utm_source=tldrdev

- **Artificial Analysis: multimodal decision model Drex Max ranks #1. Both achieving SOTA and Pareto frontier.** (Notable; model_release; reddit) - Drex Max v1.1 claims state-of-the-art results on a decision-model benchmark with open weights (v1 on Hugging Face under Open RAIL-M) and a local-inference engine, though the claims are vendor-reporte…
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xr2rqk/artificial_analysis_multimodal_decision_model/

- **Claude Code sends your email address to websites** (Notable; agents_mcp_skills; web) - A reported Claude Code issue where it sends the user's email address to websites, which bears directly on privacy and security for anyone running it with agent workflows on their machine.
  - Link: https://github.com/anthropics/claude-code/issues/107757

- **Claude Code Looked Right but Missed $800K - Natalia Connolly & Kevin Madura, AlixPartners** (Notable; agents_mcp_skills; youtube) - A real-world case where Claude Code gave confident but wrong numbers on 40,000 contracts, with concrete fixes (staged data pipeline, custom tools with business rules) that are directly reusable for a…
  - Link: https://www.youtube.com/watch?v=u7fsyrXsPBE

## 2026-11-08

- **Claude Code 2.1.319** (AI / Claude tooling) - Latest changelog entry adds `permissions.denyInsteadOfPrompting`, background MCP tasks in the terminal, `/claude-api latency-optimize`, and several Bash permission fixes.
  - Why it matters: `denyInsteadOfPrompting` makes unattended/scheduled agent runs continue instead of stalling on a prompt; background MCP tasks suit long-running tool calls; the latency command helps tune Claude API code.
  - Link: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

(Quiet day: no other items could be verified against a primary source; no repos vetted.)

## 2026-11-07 (AKD)

- **Your Claude memory file is probably making it dumber. Anthropic just published how Claude's memory …** (Top pick; research; x) - Claude Code only loads the first 200 lines or 25 KB of MEMORY.md, so a bloated CLAUDE.md or MEMORY.md silently drops instructions and should be trimmed.
  - Link: https://x.com/RoundtableSpace/status/2118980523880050885

- **GPT-Image-2.6: Faster image generation with Flare and Sunburst** (Top pick; model_release; youtube) - GPT-Image-2.6 (Flare and Sunburst) is now in the API and Codex, with 50% faster generation, a relevant option if you build image features on the OpenAI API.
  - Link: https://www.youtube.com/watch?v=9ZxCOHkfn_8
  - Also covered by: [Introducing Images 2.6](https://openai.com/index/introducing-images-2-6/?utm_source=tldrdev) (email)

- **Higgs Realtime Duplex: a 45B MoE full-duplex model that listens, watches and talks at once, and thinks, calls tools and delegates in the background [N]** (Top pick; model_release; reddit) - Higgs Realtime Duplex is a closed-weights, waitlisted voice API where the model listens, speaks, and runs tool calls concurrently, so it's relevant to agent architecture but not adoptable this week.
  - Link: https://www.reddit.com/r/MachineLearning/comments/1xpn5pv/higgs_realtime_duplex_a_45b_moe_fullduplex_model/

- **Introducing Inkling 2 Small** (Top pick; model_release; email) - Inkling 2 Small is a 594B-parameter MoE (17B active) with image input and variable effort, but weights are closed initially and API access runs only through Tinker.
  - Link: https://thinkingmachines.ai/news/inkling-2-small/?utm_source=tldrai
  - Also covered by: [Thinking Machine's Inkling 2 Small is Here](https://www.youtube.com/watch?v=3fmkbkkhxQ8) (youtube)

- **How to Get Frontier Coding Results at 70% Lower Cost - Nouha Dziri, Cohere** (Top pick; research; youtube) - Relevant to agentic coding workflow: it gives measured guidance on when multi-agent teams beat a single agent and how to cut cost by mixing a strong lead with cheaper workers.
  - Link: https://www.youtube.com/watch?v=maitMe9HCvw

- **Your Old Prompts Are Making Claude Worse - Lance Martin, Anthropic** (Notable; agents_mcp_skills; youtube) - Practical prompt-audit and prompt-caching tactics from Anthropic's Lance Martin, including a claimed 72% cost cut and a 90% cost cut from switching to a stronger model at lower effort, directly appli…
  - Link: https://www.youtube.com/watch?v=ys6YQ2yfBpM

- **Stanford researchers develop a new AI memory system that recalls information from entire conversation histories using just 16 memory tokens. It reduces document-token usage by up to 4,212×, runs 27× faster in a 512-document test, and outperforms existing approaches on 5 of 8 benchmarks.** (Notable; research; reddit) - Stanford's 16-token memory compression claims 4,212x fewer document tokens and 27x speedups on 512-doc tests, but this is a Reddit post with no paper linked, so verify the source before building on i…
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xpvvg3/stanford_researchers_develop_a_new_ai_memory/

- **Tencent Launches Hy4** (Notable; model_release; email) - Tencent's open-weight Hy4 adds vision and CLI/GUI operation, with weights promised soon, so it's worth tracking as a self-hostable agent-capable model option.
  - Link: https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/?utm_source=tldrai

- **Your AI Agent Is Hiding Its Mistakes From You - Ben Holmes, Warp** (Notable; agents_mcp_skills; youtube) - Shows how to log Claude Code and Codex sessions and run LLM-as-judge scoring plus a daily agent that opens PRs to fix skills, with Skill Doctor runnable on your own history.
  - Link: https://www.youtube.com/watch?v=pz74r-4dGfQ

- **faster-chrome-devtools-skill** (Notable; agents_mcp_skills; email) - A dependency-free Node CLI and agent skill driving Chrome over the DevTools Protocol directly, with accessibility snapshots, screenshots, and no separate browser MCP server needed.
  - Link: https://github.com/zeke/faster-chrome-devtools-skill?utm_source=tldrdev

- **Claude Code cloud sessions now set up your repo for you on Pro, Max, and Ultra. Claude works out th…** (Notable; dev_tooling; x) - Claude Code cloud sessions can now auto-configure repo dependencies, network access, and API keys on Pro, Max, and Ultra, saving the environment for reuse.
  - Link: https://x.com/RoundtableSpace/status/2118897476749209878
  - Also covered by: [We've made it easier to get your repo running in Claude Code cloud sessions on Pro, Max, and Ultra.…](https://x.com/ClaudeDevs/status/2118795192090386454) (x)

- **Someone built a VM for every project folder, so your coding agents run in a sandbox instead of on y…** (Notable; agents_mcp_skills; x) - An open-source MIT tool that runs coding agents like Claude Code in per-project Lima VMs with allowlisted networking and secrets kept on the host, directly relevant to agent sandboxing.
  - Link: https://x.com/RoundtableSpace/status/2118874827683774478

- **Mirage: A 22 MB visual-language model that runs scene descriptions + object detection + OCR + segmentation + spatial relations analysis + extractions + decisions, in a single pass.** (Notable; model_release; reddit) - A 22 MB on-device vision model covering detection, OCR, segmentation and spatial reasoning at 74 ms on a phone NPU, relevant for local agent perception without cloud calls.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xpm8mw/mirage_a_22_mb_visuallanguage_model_that_runs/

- **shanselman/sandbox-mcp** (Notable; agents_mcp_skills; github) - An MCP server that drives Windows Sandbox so agents can run and test apps in disposable Windows environments, directly relevant to agent sandboxing and MCP tooling.
  - Link: https://github.com/shanselman/sandbox-mcp

- **NousResearch/Arete-27B · Hugging Face (Qwen finetune)** (Notable; model_release; reddit) - A 27B open-weight Qwen3.8 SFT finetune from Nous Research that reports fewer propaganda-framed answers, with its own eval numbers and a GGUF build for local use.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xpmj33/nousresearcharete27b_hugging_face_qwen_finetune/
  - Also covered by: [Most open models were trained to repeat one government's talking points. Nous Research just showed …](https://x.com/RoundtableSpace/status/2118957874487718323) (x)

## 2026-11-07

- **Claude Code v2.1.319** (AI/Claude tooling) - Auto mode now asks or denies instead of silently falling back to the built-in classifier when feature flags or telemetry are off. MCP tool calls that run as tasks now go to the background, and there is a new `permissions.denyInsteadOfPrompting` setting.
  - Why it matters: Setups behind LLM gateways need `CLAUDE_CODE_AUTO_MODE_SERVER=0` to keep the old behavior. `denyInsteadOfPrompting` suits unattended or scheduled agent runs, since a blocked tool call no longer stalls the turn. Background MCP tasks suit long-running tools.
  - Link: https://github.com/anthropics/claude-code/releases

- **Claude Code v2.1.317-2.1.318** (AI/Claude tooling) - The Nov 3-4 releases ask before a web or shell tool call sends your account email to the network. They also add `onFailure: "block"` for Agent SDK hook callbacks, and background subagents move shell commands to the background after 3 minutes so the prompt cache doesn't expire.
  - Why it matters: Update to 2.1.317 or later for the email-privacy check. Hook callbacks that fail closed give you safer guardrails when you build agents on the SDK. Non-interactive launches now refuse to overwrite an invalid `~/.claude.json`.
  - Link: https://github.com/anthropics/claude-code/releases

- **Claude API: message threads (beta)** (AI/Claude tooling) - With the `message-threads-2026-08-12` beta header, the API keeps the conversation on the server. Later requests send only the new messages.
  - Why it matters: It cuts request size and time to first token in long chats and agent loops. Threads expire 5 minutes after their last request and are deleted within 1 hour of last use, so keep your own transcript if you need one.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude API: 128 MB requests, new SDK majors, fast-mode deprecation** (AI/Claude tooling) - The Messages and Token Counting request limit rose from 32 MB to 128 MB (Oct 28). API version `2026-10-21` shipped with new SDK majors (Python 2.0.0, TypeScript 1.0.0, Go 2.0.0 and others). The SDKs are now Apache 2.0 licensed.
  - Why it matters: The bigger limit helps with large PDFs and images, and the SDK majors include breaking changes, so pin versions before upgrading. Fast mode for `claude-opus-4-8` is removed on Nov 30, so migrate to Opus 5.5.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude API: usage/cost analytics and IP allowlist (beta)** (AI/Claude tooling) - New `/v1/organizations/analytics/usage` and `/cost` endpoints (Oct 29) filter by model, workspace, API key and user. An IP allowlist (Nov 5) limits API access to up to 1,000 addresses or CIDR ranges per organization.
  - Why it matters: Use the analytics endpoints for per-agent cost tracking. The allowlist stops a leaked key from being used from arbitrary locations.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **claude-agent-sdk-python v0.2.179** (AI/Claude tooling) - The Nov 6 release follows v0.2.178, which bundled Claude CLI 2.1.318. The release page lists no changelog for 0.2.179.
  - Why it matters: Upgrade to pick up the CLI fixes if you build agents on the Python SDK.
  - Link: https://github.com/anthropics/claude-agent-sdk-python/releases

- **worktrunk** (GitHub repo) - A Rust CLI for Git worktree management, built for running several AI agents in parallel.
  - Why it matters: Giving each agent its own worktree avoids branch collisions when you run multiple Claude Code sessions on one repo. It was in this week's GitHub Trending list.
  - Link: https://github.com/max-sixty/worktrunk
  - Safety note: MIT OR Apache-2.0, about 11.9k stars, 5,511 commits. The README says the project was released at the start of this year, so it isn't brand new. I couldn't see the last commit date or the contributor count on the page, so skim the code before adding it to your workflow.

## 2026-11-06 (AKD)

- **Thinking Machines, Mira Murati's lab, just released Inkling 2 Small, and the full weights go open n…** (Top pick; model_release; x) - Open-weight 594B MoE coding model (17B active) from Thinking Machines, with Apache 2.0 weights promised next week and a free Tinker Playground to try now.
  - Link: https://x.com/RoundtableSpace/status/2118670985335578977
  - Also covered by: [Introducing Inkling 2 Small](https://www.reddit.com/r/LocalLLaMA/comments/1xp32od/introducing_inkling_2_small/) (reddit)
  - Also covered by: [Introducing Inkling 2 Small](https://thinkingmachines.ai/news/inkling-2-small/?utm_source=tldrai) (email)
  - Also covered by: [[AINews] Inkling 2 Small: 17A-594B trained in 68 hours on 12T tokens, beating Muse Spark](https://latent.space/p/ainews-inkling-2-small-17a-594b-trained-in-68-hours-on-12t-tokens-beating-muse-spark/) (web)

- **anthropics/claude-code v2.1.319** (Top pick; dev_tooling; github) - This release changes auto mode to deny or prompt instead of falling back to the built-in classifier when feature flags are off, so gateway setups need `CLAUDE_CODE_AUTO_MODE_SERVER` set to avoid brea…
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.319

- **Claude Code was quietly sending users' email addresses to the websites it visited. When it searched…** (Top pick; agents_mcp_skills; x) - Claude Code was leaking users' email addresses in web requests, so update to 2.1.317 or later and confirm the privacy setting via /plugins.
  - Link: https://x.com/RoundtableSpace/status/2118664104894144724
  - Also covered by: [Claude Code sends your email address to websites](https://github.com/anthropics/claude-code/issues/107757) (web)

- **Introducing ChatGPT Images 2.6** (Top pick; model_release; youtube) - Two new image models are coming to the OpenAI API with 50% faster generation, which may be worth benchmarking if you build AI image pipelines.
  - Link: https://www.youtube.com/watch?v=bJldMYfRvMQ
  - Also covered by: [GPT-Image-2.6: Faster image generation with Flare and Sunburst](https://www.youtube.com/watch?v=9ZxCOHkfn_8) (youtube)
  - Also covered by: [Introducing Images 2.6](https://openai.com/index/introducing-images-2-6) (web)

- **NVIDIA Cosmos 3 Open Models** (Top pick; model_release; email) - Open-weight world-simulation models for robotics and driving data generation; relevant to you only as a peripheral open-model release, with no direct link to your coding or agent stack.
  - Link: https://huggingface.co/blog/nvidia/cosmos-interactive-world-simulation?utm_source=tldrai

- **Your AI coding agent can write an entire website, but can it actually test if it works? Vercel’s Ag…** (Notable; dev_tooling; x) - Vercel's agent-browser gives Claude Code-style agents a real browser to click and test UIs, installable in three commands, directly useful for your Vite/React/Vercel workflow.
  - Link: https://x.com/RoundtableSpace/status/2118572837774455289

- **Stop Giving Your AI Agents API Keys - Kim Maida, Keycard & Mason Egger, Temporal** (Notable; agents_mcp_skills; youtube) - It shows a concrete pattern for replacing shared agent API keys with per-tool-call OAuth token exchange and durable, resumable agent execution, both adoptable in a week.
  - Link: https://www.youtube.com/watch?v=YqJ4asgj1R8

- **Personal Finance in Claude (beta, Nov 5): what Claude can actually see, what it can’t do, and who gets it** (Notable; model_release; reddit) - Anthropic's read-only Personal Finance beta (US, Pro/Max/Ultra) links bank accounts through Plaid and gives Claude two years of transaction data, which is mostly off-topic for this developer-focused…
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xp28a6/personal_finance_in_claude_beta_nov_5_what_claude/
  - Also covered by: [Personal Finance in Claude](https://claude.com/resources/articles/introducing-personal-finance-in-claude?utm_source=tldrai) (email)

- **How Salesforce uses Claude Code** (Notable; agents_mcp_skills; youtube) - Salesforce reports scaling Claude Code to thousands of engineers, with concrete ROI measurement, an agent maturity model, and a shared skills marketplace, all directly relevant to agentic coding work…
  - Link: https://www.youtube.com/watch?v=4ZsVR-6YOzs

- **Linum-AI/pjit-21k · Hugging Face - A Text-to-Image Model Trained for $21K** (Notable; model_release; reddit) - A low-cost, open text-to-image model (P-JiT, trained for about $21K) with public code, relevant to a builder tracking ComfyUI-style image tooling and open model options.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xpcpws/linumaipjit21k_hugging_face_a_texttoimage_model/

- **Matt Pocock released a free collection of skills that help Claude Code and Codex plan, debug, test …** (Notable; agents_mcp_skills; x) - A free set of planning, debugging, testing, and review skills for Claude Code and Codex, installable in one command via npx skills, directly applicable to your agent workflow.
  - Link: https://x.com/RoundtableSpace/status/2118580387052241012

- **Stop Making Your Customers Click Approve - Emil Chetty, Wise** (Notable; agents_mcp_skills; youtube) - Wise's pattern of a locked, once-agreed agreement enforced by existing payment software, rather than per-step approvals, is a concrete design for safely letting agents act, relevant to agent security…
  - Link: https://www.youtube.com/watch?v=V2UqEUA8NjM

- **HerdBuilderEstimate/roblox-studio-mcp** (Notable; agents_mcp_skills; github) - An open-source MCP server that lets Claude or Cursor read Roblox Studio object trees, edit scripts, and run playtests, adoptable quickly if you want agent access to a game engine.
  - Link: https://github.com/HerdBuilderEstimate/roblox-studio-mcp

- **[AINews] Behind Latent Space: Kill My SaaS, Jev & AI in 2026 | AIEi Shanghai** (Notable; research; web) - Frontier LLMs can reportedly generate or edit neural network weights directly without gradient training, with multiple replications; relevant to model-internals and tooling, though claims are contest…
  - Link: https://latent.space/p/ainews-behind-latent-space-kill-my-saas-jev-ai-in-2026-aiei-shanghai/

- **Cognition Introduces SWE-2 Flash** (Notable; model_release; email) - Cognition's SWE-2 Flash is a new coding model with an added mid-training stage before RL, worth evaluating if you use agentic coding tools like Claude Code for development work.
  - Link: https://cognition.com/blog/swe-2-flash?utm_source=tldrai

## 2026-11-06

- **Claude Code v2.1.316–2.1.318** (AI/Claude tooling) - Three patch releases (latest v2.1.318, published Nov 4).
  - Why it matters: v2.1.317 adds `onFailure: "block"` for Agent SDK hook callbacks and a check before web/shell tool calls send your account email to the network; v2.1.316 adds `CLAUDE_CODE_SUBAGENT_EFFORT` and deprecates fast mode for Opus 4.8 (removal scheduled Nov 30, 2026); v2.1.317 removes the Read tool's "unchanged since last read" stub.
  - Link: https://github.com/anthropics/claude-code/releases

- **anthropic-sdk-python v2.5.0 / v2.6.0** (AI/Claude tooling) - SDK adds typed error classes and error codes (`APIStatusError` gains `error_code`, `details`, `api_message`).
  - Why it matters: Bedrock/Vertex clients now raise error-code/status exception classes, so review `except` blocks; also path-parameter hardening, a memory-tool fix so `/memories` is no longer renamed/deleted, and sampling params no longer recorded on OpenTelemetry spans.
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases

- **MCP spec revision 2026-07-28 (stable)** (AI/Claude tooling) - Latest stable Model Context Protocol spec revision (released Jul 28; not new this week but the current stable release).
  - Why it matters: baseline to target when building or updating MCP servers/clients; see the linked changelog for changes.
  - Link: https://github.com/modelcontextprotocol/modelcontextprotocol/releases

- **addyosmani/agent-skills** (GitHub repo) - 25 production-grade engineering workflow skills, 9 slash commands and agent personas for AI coding agents (Claude Code, Cursor, Codex, Gemini CLI, Copilot).
  - Why it matters: drop-in spec/review/test workflows you can adopt in agent-driven projects.
  - Link: https://github.com/addyosmani/agent-skills
  - Safety note: MIT license; ~113.6k stars, 807 commits, named maintainers. Last commit date not verified. Includes a `hooks/` directory that runs automatically, and its docs suggest a global git `insteadOf` config change; read hooks and scripts before installing.

_Quiet feed: no new Claude model or notable new repo could be verified from primary sources today._

## 2026-11-05 (AKD)

- **AlphaEvolve (GitHub Repo)** (Top pick; repo_library; email) - Open-sourced minimal AlphaEvolve implementation: a Gemini-driven coding agent that evolves algorithms against automated evaluators, useful as a reference pattern for evaluator-driven agent loops.
  - Link: https://github.com/google-deepmind/alphaevolve?utm_source=tldrai

- **Ripple-65B Preview** (Top pick; model_release; email) - Open-weight Ripple-65B reports state-of-the-art TerminalBench 2.1 results, relevant if you want a self-hostable or cheap coding-agent backend via OpenRouter or Together AI.
  - Link: https://www.ricursive.com/ripple?utm_source=tldrai
  - Also covered by: [Ripple-65B: Thin and Deep Dense Model, Tested Locally](https://www.youtube.com/watch?v=Gd5tnklXxLY) (youtube)

- **OpenAI launches Images 2.6 with GIFs and image reference** (Top pick; model_release; email) - Relevant because GPT-Image-2.6 is now available through the API, so it's a possible drop-in for your image tooling, though the piece doesn't mention pricing or breaking changes.
  - Link: https://www.testingcatalog.com/openai-launches-images-2-6-with-gifs-and-image-reference/?utm_source=tldrai
  - Also covered by: [Introducing ChatGPT Images 2.6](https://www.youtube.com/watch?v=bJldMYfRvMQ) (youtube)
  - Also covered by: [GPT-Image-2.6: Faster image generation with Flare and Sunburst](https://www.youtube.com/watch?v=9ZxCOHkfn_8) (youtube)
  - Also covered by: [Introducing Images 2.6](https://openai.com/index/introducing-images-2-6) (web)

- **[Paper] FireFlash : An Open Recipe for Long-Horizon Agentic RL Achieving the Performance-Cost Pareto Frontier** (Top pick; research; reddit) - An open 300B agentic coding model claiming Terminal-Bench parity with frontier models at about 30× lower per-task cost, with the full RL recipe released, is relevant for cost-conscious agent builders…
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xomst7/paper_fireflash_an_open_recipe_for_longhorizon/

- **Vibe coding has a spec problem, and GitHub's Spec Kit is the most popular answer so far: 100K+ star…** (Top pick; repo_library; x) - GitHub's Spec Kit adds a spec-first workflow (/constitution through /implement) that supports Claude Code, so it's directly testable on a real project this week.
  - Link: https://x.com/RoundtableSpace/status/2118187800356966553

- **Kimi-K3.1-Pro** (Notable; model_release; email) - A new open-weight Kimi model with a million-token context window and gains in coding and multimodal work, worth testing against your Claude Code and agent workflows.
  - Link: https://huggingface.co/moonshotai/Kimi-K3.1-Pro?utm_source=tldrai

- **anthropics/anthropic-sdk-python v2.6.0** (Notable; dev_tooling; github) - The Python SDK v2.6.0 changes Bedrock and Vertex error classes to raise error-code and status exceptions, so any `except` blocks on those clients may need updating.
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.6.0

- **Make long-running agents faster with message threads** (Notable; dev_tooling; email) - Anthropic's message threads beta cuts time-to-first-token about 35% for long-running agents by sending only new messages each turn, relevant to Claude Agent SDK and API users.
  - Link: https://claude.com/resources/articles/message-threads?utm_source=tldrdev

- **A thousand fewer paths to root** (Notable; research; web) - An autonomous AI pipeline found and patched 948 Linux kernel privilege-escalation bugs, relevant to agent-driven security tooling and the risks of autonomous code changes.
  - Link: https://openai.com/index/a-thousand-fewer-paths-to-root

- **modelcontextprotocol/servers v2.3.0** (Notable; agents_mcp_skills; github) - The v2.3.0 release bumps the official MCP reference servers (filesystem, git, fetch, memory, and others) to new major-line versions, so pin-checking or testing these in existing MCP configs is worth…
  - Link: https://github.com/modelcontextprotocol/servers/releases/tag/v2.3.0

- **Claude Code can now make AI videos with Runway. Runway's plugin lets your coding agent generate vid…** (Notable; agents_mcp_skills; x) - Runway's plugin lets Claude Code generate video, image, and voiceover assets from the terminal, and it installs via /plugin install runway-api, so it's a quick test for the video tooling you already…
  - Link: https://x.com/RoundtableSpace/status/2118285947003371982

- **Introducing Pangram Image 1.0** (Notable; model_release; email) - Adds a heatmap-based AI image/video detector with an API, useful if you ever need to verify media in a pipeline you're building, though it's peripheral to your agentic coding focus.
  - Link: https://www.pangram.com/blog/introducing-pangram-image-1-0?utm_source=tldrai

- **AuroraIMG2-100M Releases!** (Notable; model_release; reddit) - A new Apache 2.0 open-weight image model (AuroraIMG2-100M, diffusers-compatible) that could slot into a local ComfyUI or diffusers image pipeline.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xnzynf/auroraimg2100m_releases/

- **GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents** (Notable; model_release; web) - A new OpenAI cybersecurity model aimed at finding exploitable vulnerabilities and drafting fixes, relevant to agent security and sandboxing work.
  - Link: https://openai.com/index/introducing-gpt-6-cyber

- **An open-source project just ranked #1 on EnterpriseRAG-Bench, ahead of the listed systems from OpenAI, Google, Microsoft and Amazon** (Notable; agents_mcp_skills; reddit) - An open-source, self-hostable agentic RAG system (PipesHub, MCP-connectable) reports #1 on EnterpriseRAG-Bench, but the author is a founder, so treat the claim cautiously.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xoiaye/an_opensource_project_just_ranked_1_on/

## 2026-11-05

- **Claude Code v2.1.316-v2.1.317** (AI/Claude tooling) - Releases from 31 Oct and 3 Nov: Agent SDK hook callbacks accept `onFailure: "block"`, a prompt before tools send your account email over the network, `CLAUDE_CODE_SUBAGENT_EFFORT`, and a cost report endpoint (`GET /v1/organizations/analytics/cost`) on the Claude apps gateway admin API.
  - Why it matters: `onFailure: "block"` makes SDK guardrail hooks fail closed instead of letting an action through, which suits policy or safety checks. Subagent effort can now be tuned separately to control cost.
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.317

- **Opus 4.8 fast mode deprecation** (AI/Claude tooling) - The v2.1.316 notes say fast mode for Opus 4.8 is deprecated as of 2026-10-30 and will be removed on 2026-11-30. After that, requests return an error instead of falling back to standard Opus 4.8. The notes recommend migrating to Opus 5.5.
  - Why it matters: Check scripts, configs, and SDK calls that pin Opus 4.8 fast mode before the 30 Nov cutoff.
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.316

- **max-sixty/worktrunk** (GitHub repo) - Rust CLI for Git worktree management built for running several AI agents in parallel. It has hooks, LLM-generated commit messages, a merge workflow, and PR checkout.
  - Why it matters: It gives each agent its own worktree and branch, which avoids agents overwriting each other's files when you run several Claude Code sessions on one repo.
  - Link: https://github.com/max-sixty/worktrunk
  - Safety note: MIT OR Apache-2.0, about 11.3k stars, 5,501 commits, on GitHub's weekly trending page. The last-commit date wasn't visible to me, so check activity yourself. I haven't audited the code or hooks.

- **pbakaus/impeccable** (GitHub repo) - A design vocabulary for coding agents: commands like `polish`, `bolder`, `critique`, and `audit`, plus a rule-based detector that flags generic "AI slop" UI patterns. It works with Claude Code, Cursor, and Codex CLI.
  - Why it matters: It gives agents repeatable commands for reviewing and improving generated frontends, where you would otherwise re-prompt each time.
  - Link: https://github.com/pbakaus/impeccable
  - Safety note: Apache-2.0, about 103k stars, 2,635 commits, trending this week. The last-commit date wasn't visible to me, and I haven't audited the code.

- Skipped on safety grounds: thedotmack/claude-mem is trending (Apache-2.0), but its README promotes a third-party token with a contract address, uses a `curl | bash` installer path, and has cloud sync with a paid trial. I can't vouch for it.

## 2026-11-04 (AKD)

- **Anthropic shipped message threads (beta): Claude Code now sends only new messages per turn, about 35% lower time to first token on 500k to 1M token requests** (Top pick; dev_tooling; reddit) - Anthropic's new Messages API "thread" beta (on by default in Claude Code) cuts time to first token about 35% on 500k–1M token requests, but threads expire after 5 idle minutes, forcing a full resend.
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xnc4ew/anthropic_shipped_message_threads_beta_claude/
  - Also covered by: [Claude Introduces Message Threads](https://claude.com/resources/articles/message-threads?utm_source=tldrai) (email)
  - Also covered by: [Claude Message Threads Tested: 34 of 50 Turns Faster](https://www.youtube.com/watch?v=nawZ1OvhpE0) (youtube)

- **Axion1-0/Axion-1.0-35B · Hugging Face** (Top pick; model_release; reddit) - An open-weight 35B agent model with a fully reproducible training recipe (data, prompts, and code), useful as a local or self-hosted agent backend to evaluate against your current stack.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xnjiu4/axion10axion1035b_hugging_face/

- **Vercel Labs open sourced a free tool that lets any AI agent operate desktop apps, so you can add co…** (Top pick; agents_mcp_skills; x) - Vercel Labs' agent-desktop lets coding agents drive desktop apps via the accessibility tree rather than screenshots, installable via npm on macOS, Windows, and Linux.
  - Link: https://x.com/RoundtableSpace/status/2117825412462240136

- **anthropics/claude-code v2.1.318** (Top pick; dev_tooling; github) - Claude Code v2.1.318 fixes a `--continue` regression from 2.1.314 that could drop earlier conversation, and adds login-expiry warnings for `claude -p` and CI jobs.
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.318

- **anthropics/anthropic-sdk-python v2.5.0** (Top pick; dev_tooling; github) - Breaking-risk check: OverloadedError and ServiceUnavailableError now subclass InternalServerError, so any `except InternalServerError` handlers will start catching them, and APIStatusError gains new…
  - Link: https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.5.0

- **Kimi-K3.1-Pro is now open-weights** (Notable; model_release; reddit) - Moonshot's Kimi-K3.1-Pro is now open-weights, so it can be self-hosted or run through providers, which matters if you want a strong alternative model behind your agent stack.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xnrhvb/kimik31pro_is_now_openweights/

- **Baseten launches Grid, Sandboxes, and Serverless Loops** (Notable; agents_mcp_skills; email) - Baseten's new VM-isolated, resumable Sandboxes for agent execution are directly relevant to your agent sandboxing and infrastructure interests, and Grid's model routing could matter if you build on m…
  - Link: https://www.baseten.co/blog/the-building-blocks-of-the-open-frontier?utm_source=tldrai

- **ricursiveAI/Ripple-65B-Preview · Hugging Face** (Notable; model_release; reddit) - A 65B open-weight model preview from ricursiveAI on Hugging Face, relevant if you're evaluating local models for agent or coding workloads on your own hardware.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xnx3cs/ricursiveairipple65bpreview_hugging_face/

- **Hackers stole $6.34B from Binance with a fake coding assignment. The same trick hits developers eve…** (Notable; agents_mcp_skills; x) - This is a practical, adoptable security habit: before running an unknown repo, ask Claude Code to audit install hooks, obfuscated code, network calls, and credential access without executing anything…
  - Link: https://x.com/RoundtableSpace/status/2117953758730588392
  - Also covered by: [Binance has revealed how the $6.3B theft happened, and it started months earlier than the heist. Bi…](https://x.com/RoundtableSpace/status/2117795213682855971) (x)

- **ComfyUI v0.44.0 released** (Notable; dev_tooling; reddit) - ComfyUI v0.44.0 ships a new release for your AI image and video tooling, so check whether it changes node APIs or workflow compatibility before upgrading your pipelines.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xngb2i/comfyui_v0440_released/

- **TinyWebUI - Lightweight Open WebUI alternative, just npx and go** (Notable; repo_library; reddit) - A lightweight, npx-installable local chat UI with built-in local web search, memory, and MCP support, directly adoptable for local-model workflows this week.
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xnmre2/tinywebui_lightweight_open_webui_alternative_just/

- **Limit what agents learn about private repos with enclaves** (Notable; agents_mcp_skills; email) - GitHub Next's enclaves limit what agents share across private repos, relevant to agent security and any multi-repo agentic workflow setup.
  - Link: https://githubnext.com/posts/enclaves/?utm_source=tldrai

- **djs** (Notable; agents_mcp_skills; email) - A Rust-built JS/TS engine that runs agent-generated code in a WebAssembly sandbox and can snapshot and resume mid-execution, relevant to agent security and tool-calling workflows.
  - Link: https://github.com/earendil-works/djs?utm_source=tldrdev

- **Building the AI Agent Is Easy. Proving It's Safe Isn't - Jonathan Osborne, NatWest** (Notable; agents_mcp_skills; youtube) - A practical look at how a regulated bank evaluates and safely rolls out production AI agents, including why LLM-as-judge scoring and single accuracy numbers can mislead, which is directly useful for…
  - Link: https://www.youtube.com/watch?v=5UgnatzpZ9E

- **Why Agents Are Soon Only Going to Have 1 Tool** (Notable; agents_mcp_skills; email) - This matters for how you design MCP servers and agent tool catalogs: collapsing many tools into one sandboxed exec tool could reduce tool-call round trips and context overhead.
  - Link: https://www.philschmid.de/code-mode?utm_source=tldrnewsletter

## 2026-11-04

- **Claude Code v2.1.318** (AI/Claude tooling) - Reliability release: fixes `--continue` losing history after malformed tool-call retries, and `claude mcp remove`/`/logout` falsely reporting success; adds a `claude -p` warning 10 days before sign-in expiry.
  - Why it matters: Useful for headless/CI use of `claude -p`; also adds an `effort` option for a mod's `$.model.fork`.
  - Link: https://github.com/anthropics/claude-code/releases

- **Claude Code v2.1.314-2.1.316 (Oct 30-31)** (AI/Claude tooling) - New `permissions.blockWritesOutsideWorkingDirectories` setting, `CLAUDE_CODE_SUBAGENT_EFFORT` env var, idle-conversation compaction in VS Code/Desktop, and `CLAUDE_CODE_DISABLE_ULTRATHINK`.
  - Why it matters: Lets you sandbox agent writes to the project and tune subagent cost. Note: Opus 4.8 fast mode is deprecated and removed Nov 30, 2026 - migrate to Opus 5.5.
  - Link: https://github.com/anthropics/claude-code/releases

- **Claude Haiku 5.5** (AI/Claude tooling) - Anthropic's cheapest/fastest small model (`claude-haiku-5-5`, announced Oct 7, so older than the 7-day window but worth knowing); $0.10/$0.50 per M input/output tokens (prompts up to 100k), first Haiku-class model with an effort setting, computer/browser use (beta) in the Python/TS SDKs.
  - Why it matters: Good fit for subagents, classification, summarization and compaction steps; Sonnet 5.5 cache reads also cut 50%.
  - Link: https://www.anthropic.com/news/claude-haiku-5-5

- **worktrunk** (GitHub repo) - Rust CLI for Git worktree management aimed at running AI agents in parallel (`wt switch/list/merge/remove`, hooks, LLM commit messages).
  - Why it matters: Makes it easy to run several coding agents on isolated branches without collisions.
  - Link: https://github.com/max-sixty/worktrunk
  - Safety note: MIT OR Apache-2.0; ~10.8k stars; installs via package managers (no curl|sh), but the suggested `wt config shell install` edits shell config - review first. Last-commit date not visible from the page.

- **obra/superpowers** (GitHub repo) - Composable agent-skills framework/methodology (brainstorm, plan, TDD, subagent-driven implementation, review) for Claude Code, Codex, Cursor, Gemini CLI; trending on GitHub this week.
  - Why it matters: Drop-in workflow skills that structure how agents implement features.
  - Link: https://github.com/obra/superpowers
  - Safety note: MIT; ~312k stars; skills are prompts/markdown plus shell - read before enabling. Last-commit date not visible from the page.

## 2026-11-03 (AKD)

- **Anthropic added “message threads” to the Messages API (public beta): send the conversation once, then only new messages. Already on by default in Claude Code** (Top pick; dev_tooling; reddit) - Anthropic's Messages API now offers message threads (public beta) so you send the full history once and then only new messages, cutting time-to-first-token about 35% on 500k+ token contexts, but thre…
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xmh012/anthropic_added_message_threads_to_the_messages/
  - Also covered by: [Claude Introduces Message Threads](https://claude.com/resources/articles/message-threads?utm_source=tldrai) (email)
  - Also covered by: [Claude Message Threads Tested: 34 of 50 Turns Faster](https://www.youtube.com/watch?v=nawZ1OvhpE0) (youtube)

- **anthropics/claude-code v2.1.317** (Top pick; agents_mcp_skills; github) - Adds a per-call prompt before tools send your account email over the network, plus `onFailure: "block"` for Agent SDK hooks, which changes how failing callbacks behave in agent builds.
  - Link: https://github.com/anthropics/claude-code/releases/tag/v2.1.317

- **New Anthropic research: progress on provable inference for large language models. Here, we introduc…** (Top pick; research; x) - Anthropic open-sourced FlashProve, a cryptographic tool that verifies a response came from a specific model, relevant to agent trust and serving-integrity checks.
  - Link: https://x.com/AnthropicAI/status/2117710942826123294
  - Also covered by: [Anthropic just open-sourced a way to prove which AI model actually answered you. Ever wonder if an …](https://x.com/RoundtableSpace/status/2117598919886864764) (x)

- **[Paper] RidgeFill: Training-Free Late-Layer Cache Fill for Faster Prefill** (Top pick; research; reddit) - RidgeFill is a training-free prefill speedup (1.25–1.6x TTFT) that skips most upper layers via a closed-form ridge map, with small accuracy losses; worth testing for long-context serving in vLLM or l…
  - Link: https://www.reddit.com/r/LocalLLaMA/comments/1xmarrf/paper_ridgefill_trainingfree_latelayer_cache_fill/

- **Leaflet 2.0 beta** (Top pick; repo_library; email) - Leaflet 2.0 beta brings tree-shaking, bundled TypeScript types, and breaking API changes, so check any existing map code before upgrading.
  - Link: https://github.com/Leaflet/Leaflet/releases/tag/v2.0.0-beta.1?utm_source=tldrdev

- **Hugging Face just released a safety guard for AI coding agents. Your agent can run any command it d…** (Notable; agents_mcp_skills; x) - A local proxy that inspects and blocks risky agent commands before execution, working with Claude Code via ANTHROPIC_BASE_URL; directly relevant to agent sandboxing and security, and adoptable in a f…
  - Link: https://x.com/RoundtableSpace/status/2117606470229397657

- **Users can now auto-connect plugins when they log in to Claude, with MCP servers that accept Claude …** (Notable; agents_mcp_skills; x) - Claude can now auto-connect MCP plugins at login, so MCP servers that trust Claude as an issuer can skip re-authorization; worth adding if you build plugins.
  - Link: https://x.com/ClaudeDevs/status/2117680635561312732

- **Maple ports 287,000 lines of React to Foldkit in 3 days** (Notable; agents_mcp_skills; email) - Shows a concrete large-scale agent migration (about 40 Claude agents, 287k lines in 3 days) with a visual-diff harness, but also that screenshot checks missed around 180 defects and the bundle roughl…
  - Link: https://maple.dev/blog/react-to-foldkit/?utm_source=tldrdev

- **Automating agentic AI Well-Architected reviews with the AWS Agentic AI Lens** (Notable; agents_mcp_skills; email) - Smarsh packaged the AWS Agentic AI Lens as a Claude skill that audits a GitHub repo against 150 best practices, a directly reusable pattern for agent-project reviews.
  - Link: https://aws.amazon.com/blogs/architecture/automating-agentic-ai-well-architected-reviews-with-the-aws-agentic-ai-lens/?utm_source=tldrdev

- **Your AI Agents Shouldn't Care Where They Run - Nikhil Harithas, Factory** (Notable; agents_mcp_skills; youtube) - Factory's Droid coding agent now runs on any compute inside a customer's own cloud with bring-your-own-key, a design the reader can study for agent sandboxing and VPC deployment, with the compute lay…
  - Link: https://www.youtube.com/watch?v=XIHZpZtYCzo

- **How Claude Code reacts when a repo has a no-AI contribution policy** (Notable; agents_mcp_skills; reddit) - Claude Code honors repo-level no-AI policy files (AGENTS.md or CLAUDE.md refuse instantly, AI_POLICY.md stops it before committing), so maintainers can enforce the rule as a soft agreement, not a har…
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xmgzia/how_claude_code_reacts_when_a_repo_has_a_noai/

- **SenseNova Loop 9B: Hands-On Test of a Looped Multimodal Model** (Notable; model_release; youtube) - A hands-on local test of SenseNova-Loop-9B-Preview, an open 9B multimodal model for agentic and long-context work, useful if you want a small local vision-plus-reasoning option.
  - Link: https://www.youtube.com/watch?v=_J4WyIZR8QA

- **OpenMausBot** (Notable; agents_mcp_skills; email) - Relevant to agent infrastructure and approval-gating: it wraps locally installed Claude Code, Codex, or Grok CLIs in a chat UI, with permission requests surfaced as approval cards.
  - Link: https://github.com/milind-soni/OpenMausBot?utm_source=tldrdev

- **wendersoon/radar-cnpj-mcp** (Notable; agents_mcp_skills; github) - An MCP server and CLI for querying Brazilian company (CNPJ) data by CNAE code and region, a niche tool that is only relevant if you build agents for Brazilian business data.
  - Link: https://github.com/wendersoon/radar-cnpj-mcp

- **Official Claude Code Extension Compromise: Security Advisory** (Notable; dev_tooling; reddit) - Security advisory says Claude Code VS Code extension versions 2.1.312 and 2.1.313 were compromised, so check your installed version and update or downgrade if affected.
  - Link: https://www.reddit.com/r/ClaudeAI/comments/1xmdwop/official_claude_code_extension_compromise/

## 2026-11-03

- **Claude Code v2.1.317 (and v2.1.314/316)** (AI/Claude) - Latest Claude Code releases: `/schedule` warns about unintended connectors, a prompt before tool calls send your account email to the network, Agent SDK hook callbacks accept `onFailure: "block"`, and `claude -p` now exits 1 on lost transcript writes.
  - Why it matters: v2.1.314 adds `permissions.blockWritesOutsideWorkingDirectories`, and v2.1.316 adds `CLAUDE_CODE_SUBAGENT_EFFORT` to set subagent effort. Both are useful when running agents unattended or in CI.
  - Link: https://github.com/anthropics/claude-code/releases

- **Opus 4.8 fast mode deprecated (removal 2026-11-30)** (AI/Claude) - Requests to `claude-opus-4-8` with `speed: "fast"` will error after Nov 30; the notes point to Claude Opus 5.5.
  - Why it matters: Any code or scheduled job that hardcodes Opus 4.8 fast mode needs migrating before the cutoff.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Claude SDK major versions with API version 2026-10-21** (AI/Claude) - Python 2.0.0, TypeScript 1.0.0, Go 2.0.0, Java 3.0.0 and others shipped on Oct 21 with breaking changes. The SDKs are now Apache 2.0 instead of MIT. The same notes list user profiles (per-end-customer enforcement) and request size raised from 32 MB to 128 MB.
  - Why it matters: Pinning older SDK versions or upgrading blindly can break builds. Per-customer user profiles matter for multi-tenant apps built on the API.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **Usage and Cost Analytics API (beta)** (AI/Claude) - New `/v1/organizations/analytics/usage` and `/cost` endpoints, grouped by model, workspace, API key or user. Needs the `analytics-usage-cost-2026-08-24` beta header. The older Usage and Cost API is now legacy.
  - Why it matters: Lets you build spend dashboards or budget alerts for agent workloads.
  - Link: https://platform.claude.com/docs/en/release-notes/api

- **vercel-labs/agent-desktop** (GitHub repo) - A CLI and C library that lets AI agents read and operate desktop apps through the OS accessibility tree, returning JSON snapshots with refs. Works on macOS, Windows and Linux.
  - Why it matters: A structured alternative to screenshot-based computer use for automating GUI apps from an agent.
  - Link: https://github.com/vercel-labs/agent-desktop
  - Safety note: Apache-2.0, about 11.7k stars, 325 commits on main, from Vercel Labs. I could not confirm the last commit date from the page. The npm package bundles native binaries, so review before installing. It needs Accessibility permission, and snapshots or clipboard reads can contain private data.

- **max-sixty/worktrunk** (GitHub repo) - A CLI for managing git worktrees for parallel AI agent workflows (`wt switch/list/merge/remove`), with hooks and LLM-generated commit messages.
  - Why it matters: Makes it practical to run several coding agents on separate branches at once without stepping on each other.
  - Link: https://github.com/max-sixty/worktrunk
  - Safety note: MIT OR Apache-2.0, about 10.3k stars, 5,480 commits. I could not confirm the last commit date from the page. Windows builds are signed through SignPath. The install flow runs `wt config shell install`, which edits your shell config, so check that first. No curl-pipe install.
