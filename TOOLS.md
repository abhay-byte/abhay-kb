# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Related

- [Agent workspace](/concepts/agent-workspace)

## AgentMail

- **Inbox:** ab-brain-bot@agentmail.to
- **API:** https://api.agentmail.to/v0
- **Key:** am_us_inbox_1f3e4c9f980cd74da03b8ac2bd4748ece495515d62f7b024c5d3f5217324c70f
- **Skill:** agentmail (installed via ClawHub, enabled in config)
- **Usage:** Create inboxes, send/receive emails, manage threads, attachments, drafts
- **Default send-to:** abhay02delhi@gmail.com (always use this unless specified otherwise)
- **Capabilities:** Sending emails, checking inbox, replying, forwarding, creating on-demand inboxes

## AI Coding CLI Tools Reference

A comprehensive reference of AI-powered terminal/CLI coding agents. Great for understanding the landscape and choosing the right tool for the job.

### Claude Code

- **By:** Anthropic
- **Install:** `npm install -g @anthropic-ai/claude-code`
- **GitHub:** [github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)
- **Site:** [anthropic.com/product/claude-code](https://www.anthropic.com/product/claude-code)
- **Type:** Agentic coding system (terminal, IDE, GitHub @claude)
- **Model:** Claude (Sonnet/Opus)
- **Features:** Reads full codebase, edits files across project, runs tests, git workflows, natural language commands. First released Feb 2025 (beta with Claude 3.7 Sonnet), GA May 2025. Most popular premium CLI agent.

### Codex CLI

- **By:** OpenAI
- **Install:** Via GitHub (Rust binary)
- **GitHub:** [github.com/openai/codex](https://github.com/openai/codex)
- **Site:** [developers.openai.com/codex/cli](https://developers.openai.com/codex/cli)
- **Type:** Open-source terminal coding agent
- **Model:** OpenAI (GPT-4o/o3/o4-mini)
- **Features:** Built in Rust, reads/edits/runs code locally, git workflows, approval modes, MCP server support, multi-agent workflows. Free with ChatGPT plans. VS Code/Cursor/Windsurf IDE extensions available.

### Gemini CLI

- **By:** Google
- **Install:** Via GitHub or geminicli.com
- **GitHub:** [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- **Docs:** [google-gemini.github.io/gemini-cli](https://google-gemini.github.io/gemini-cli/)
- **Site:** [blog.google/.../introducing-gemini-cli](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-open-source-ai-agent/)
- **Type:** Open-source AI agent for terminal
- **Model:** Gemini 2.5 Pro (unmatched free usage tier)
- **Features:** ReAct loop agent, local/remote MCP servers, code analysis, bug fixing, test coverage, content creation. Open-source under Apache 2.0.

### Aider

- **By:** Paul Gauthier (community)
- **Install:** `pip install aider-chat`
- **Site:** [aider.chat](https://aider.chat/)
- **GitHub:** [github.com/paul-gauthier/aider](https://github.com/paul-gauthier/aider)
- **Type:** Open-source AI pair programming in terminal
- **Model:** Any LLM (Claude, GPT-4, Gemini, DeepSeek, local via Ollama)
- **Features:** Git-native commits, multi-file edits, codebase awareness, map of repo architecture, auto-commit with descriptive messages, supports 40K+ GitHub stars, 5.7M+ PyPI installs. One of the most mature open-source options.

### OpenCode

- **By:** SST / Anomaly team
- **Install:** `npx opencode` or Go binary
- **GitHub:** [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode)
- **Site:** [opencode.ai](https://opencode.ai/)
- **Type:** Open-source Go CLI coding agent with TUI
- **Model:** 75+ providers (OpenAI, Anthropic, Gemini, Bedrock, Groq, OpenRouter, local Ollama)
- **Features:** Rich TUI built with Bubble Tea, vim-like editing, persistent SQLite sessions, LSP integration for 40+ languages, 160K+ GitHub stars, 7.5M+ monthly users. Leading open-source Claude Code alternative. No subscription, bring your own key.

### Qwen Code

- **By:** Alibaba (QwenLM)
- **Install:** `npm install -g @qwen/qwen-code` or pip
- **GitHub:** [github.com/QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)
- **Docs:** [qwenlm.github.io/qwen-code-docs](https://qwenlm.github.io/qwen-code-docs/en/)
- **Site:** [qwen.ai/qwencode](https://qwen.ai/qwencode)
- **Type:** Open-source AI agent for terminal
- **Model:** Qwen3-Coder (480B-A35B strongest), plus multi-protocol (OpenAI/Anthropic/Gemini compatible)
- **Features:** Optimized for Qwen series models, multi-protocol flexible providers, codebase understanding, MCP servers, IDE integration, workflows, automation. Alibaba Cloud Coding Plan support.

### Junie CLI

- **By:** JetBrains
- **Install:** Via JetBrains Toolbox or GitHub
- **GitHub:** [github.com/JetBrains/junie](https://github.com/JetBrains/junie)
- **Docs:** [junie.jetbrains.com](https://junie.jetbrains.com/docs/junie-cli.html)
- **Type:** LLM-agnostic terminal coding agent
- **Model:** BYO LLM (agent-agnostic)
- **Features:** Interactive terminal interface, code review, write/modify code, CI/CD pipeline integration, IDE integration with JetBrains IDEs, PR review capabilities. Built for real-world dev workflows.

### Kiro

- **By:** Amazon Web Services (AWS)
- **Install:** Via kiro.dev/cli/
- **Site:** [kiro.dev](https://kiro.dev/)
- **GitHub:** [github.com/kirodotdev/Kiro](https://github.com/kirodotdev/Kiro)
- **Type:** Agentic IDE + CLI (spec-driven development)
- **Model:** Multi-model
- **Features:** Spec-driven development methodology — generates requirements docs, technical designs, implementation task lists before coding. CLI agents for writing/reviewing/modifying code, automating workflows. Released in public preview July 2025.

### Kilo Code

- **By:** Kilo-Org
- **Install:** VS Code Marketplace extension
- **GitHub:** [github.com/Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode)
- **Site/Marketplace:** [marketplace.visualstudio.com/.../Kilo-Code](https://marketplace.visualstudio.com/items?itemName=kilocode.Kilo-Code)
- **Type:** Open-source VS Code AI coding extension
- **Model:** 500+ models (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, Gemini 3.1 Pro Preview)
- **Features:** Superset of Roo Code/Cline — planning, generation, refactoring, debugging, orchestration. Transparent pricing matching provider rates. Free tier available. Also has a standalone Kilo platform.

### Cline

- **By:** Cline (Saoud Rizwan)
- **Install:** VS Code Marketplace extension, or standalone CLI via npm
- **GitHub:** [github.com/cline/cline](https://github.com/cline/cline)
- **Site/CLI Docs:** [docs.cline.bot/cline-cli/getting-started](https://docs.cline.bot/cline-cli/getting-started)
- **Marketplace:** [marketplace.visualstudio.com/.../claude-dev](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev)
- **Type:** Open-source AI coding assistant (VS Code, JetBrains, standalone CLI)
- **Model:** 30+ LLM providers
- **Features:** Full agentic capabilities — create/edit files, run terminal commands, browser access, multi-step tasks, human-in-the-loop (approval-based). Reads project structure, understands file relationships. Standalone CLI for headless/CI/CD use.

### Continue

- **By:** Continue Dev
- **Install:** VS Code / JetBrains plugin, or CLI
- **GitHub:** [github.com/continuedev/continue](https://github.com/continuedev/continue)
- **Docs:** [docs.continue.dev](https://docs.continue.dev)
- **Type:** Open-source AI coding assistant (IDE + CLI)
- **Model:** Any LLM (OpenAI, Claude, Gemini, local via Ollama/LM Studio)
- **Features:** IDE integration (VS Code, JetBrains), source-controlled AI checks enforceable in CI, model-agnostic, tab autocomplete, chat, inline editing, custom slash commands, rules files. Focus on developer freedom and local model support.

### Goose

- **By:** Block (formerly Square)
- **Install:** Desktop app or CLI via npm/cargo
- **GitHub:** [github.com/aaif-goose/goose](https://github.com/aaif-goose/goose)
- **Site:** [goose-docs.ai](https://goose-docs.ai/)
- **Type:** Open-source general-purpose AI agent (desktop + CLI + API)
- **Model:** BYO LLM
- **Features:** Not just for code — shell commands, file editing, code execution, multi-step workflows, research, writing, automation, data analysis. Native MCP integration for extensibility. Desktop app for macOS/Linux/Windows + CLI. Apache 2.0 license. Launched Jan 2025 by Block's OSPO.

### Amp

- **By:** Sourcegraph
- **Install:** CLI or VS Code extension
- **Site:** [ampcode.com](https://ampcode.com/)
- **Docs/Manual:** [ampcode.com/manual](https://ampcode.com/manual)
- **Type:** Agentic coding agent (CLI + VS Code)
- **Model:** Frontier models (multi-model)
- **Features:** Auto-refactors entire codebases, code review (bugs, security, performance, style), `amp review` CLI command, test generation, terminal-native agents (Amp Neo CLI with plugins, remote control, compaction). Leverages Sourcegraph's code intelligence for enterprise-scale codebases.
