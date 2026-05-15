---
layout: standalone
title: Agent Skills & MCP
---

# Agent Skills, MCP, Tools, and Subagents

Understanding the AI agent ecosystem in 2026: how agents extend their capabilities.

---

## Overview

In 2026, AI coding agents have evolved from simple chat bots into autonomous systems that can plan, execute, and iterate on complex tasks across your codebase. This power comes from four key extension mechanisms:

1. **Skills** — How agents learn to do specific tasks
2. **MCP (Model Context Protocol)** — How agents connect to external data
3. **Tools** — Direct capabilities agents can invoke
4. **Subagents** — Delegating work to child agents

---

## Skills

Skills are instruction sets that teach AI agents **how to work**. They provide context, guidelines, and step-by-step procedures for specific tasks.

| Aspect | Description |
|--------|-------------|
| **What it is** | A set of instructions that teaches an agent how to perform a task |
| **Format** | Markdown files (SKILL.md), JSON, or YAML |
| **Scope** | Task-specific (e.g., "how to write a React component") |
| **Examples** | Git workflow skill, testing skill, deployment skill |
| **Tools** | OpenCode, OpenClaw (skills.sh), Claude Code |

### Skill vs Tool vs MCP

| Concept | Teaches the agent... | Analogy |
|---------|---------------------|---------|
| **Skill** | How to do something | A recipe book |
| **Tool** | What it can do | A kitchen appliance |
| **MCP** | What data it can access | A pantry |

### Popular Skill Platforms

| Platform | Description | URL |
|----------|-------------|-----|
| **skills.sh** | Open registry for AI agent skills | [skills.sh](https://skills.sh) |
| **ClawHub** | OpenClaw's skill marketplace | [clawhub.ai](https://clawhub.ai) |
| **OpenCode Skills** | Built-in skill system | OpenCode TUI /models |

---

## MCP (Model Context Protocol)

MCP is an open standard developed by Anthropic for connecting AI agents to external data sources and services.

| Aspect | Description |
|--------|-------------|
| **What it is** | A protocol for connecting AI agents to external tools and data |
| **Created by** | Anthropic (open standard) |
| **How it works** | Agents make MCP calls to servers that expose tools/resources |
| **Common servers** | Filesystem, GitHub, PostgreSQL, Slack, web search |
| **Supported by** | Claude Code, OpenCode, Cursor, Windsurf, OpenClaw |

### How MCP Works

```
Agent → MCP Client → MCP Server → External Service (API/DB/files)
         ↓
    Standardized protocol:
    - Tools (actions the agent can take)
    - Resources (data the agent can read)
    - Prompts (templates for common tasks)
```

### Common MCP Servers

| Server | What it does |
|--------|-------------|
| **Filesystem** | Read/write files, search codebase |
| **GitHub** | Create PRs, issues, review code |
| **PostgreSQL** | Query databases, run migrations |
| **Slack** | Send messages, read channels |
| **Web Search** | Search the internet |
| **Puppeteer** | Browser automation |
| **Memory** | Persistent memory across sessions |

---

## Tools

Tools are direct capabilities that agents can invoke. Unlike MCP (which connects to external services), tools are often built-in functions.

| Tool | Agent | What it does |
|------|-------|-------------|
| **File editing** | All agents | Create/edit/delete files |
| **Command execution** | CLI agents | Run terminal commands |
| **Code search** | All agents | Find code across codebase |
| **Web search** | Agent + MCP | Search the internet |
| **Browser** | Antigravity, Codex | Visual web testing |
| **Image generation** | Codex | Generate images |

---

## Subagents

Subagents are child agents spawned by a parent agent to handle specific subtasks in parallel.

| Feature | Description |
|---------|-------------|
| **What it is** | A child agent that works on a specific subtask |
| **When to use** | Complex tasks that can be parallelized |
| **Benefits** | Faster execution, focused context, parallel work |
| **Examples** | One agent codes, another reviews, third tests |

### Tools Supporting Subagents

| Tool | Subagent Support |
|------|-----------------|
| **Claude Code** | Sub-agents with skill discovery (v2.1.133+) |
| **OpenCode** | Plugin-based subagents |
| **Antigravity** | 5 parallel agents by default |
| **Cursor** | Agent mode with multi-file editing |

---

## Hooks

Hooks are event-driven scripts that run at specific points in the agent workflow.

| Hook | When it fires | Use Case |
|------|--------------|----------|
| **Pre-tool** | Before a tool executes | Validate inputs, add context |
| **Post-tool** | After a tool executes | Review changes, run tests |
| **Pre-commit** | Before code is committed | Lint, format, analyze |
| **Post-commit** | After code is committed | Deploy, notify |

---

## Quick Reference

| Concept | What it extends | Example |
|---------|----------------|---------|
| **Skill** | Agent's knowledge | "How to write tests" |
| **MCP** | Agent's data access | "Read PostgreSQL database" |
| **Tool** | Agent's capabilities | "Search files" |
| **Subagent** | Agent's workforce | "Child agent writes tests" |
| **Hook** | Agent's workflow | "Run linter after save" |
