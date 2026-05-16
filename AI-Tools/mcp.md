---
layout: standalone
title: MCP Overview
---

# Model Context Protocol (MCP)

MCP is an open standard developed by Anthropic for connecting AI agents to external data sources, tools, and services. It provides a standardized way for agents to interact with the world beyond their training data.

---

## How MCP Works

MCP follows a **3-layer client-server architecture**:

| Layer | Component | Role |
|-------|-----------|------|
| **1** | **Host** (AI App) | The AI application you use — Claude Code, OpenCode, Cursor, OpenClaw |
| **2** | **MCP Client** (built into Host) | Manages connections, routes requests, handles authentication |
| **3** | **MCP Servers** | Expose tools, resources, and prompts for the agent |

The Agent (Layer 1) sends requests through its built-in MCP Client (Layer 2), which communicates with MCP Servers (Layer 3) that connect to real external services — filesystems, APIs, databases.

---

## Key Concepts

| Concept | Description | Example |
|---------|-------------|---------|
| **Tools** | Actions the agent can perform | Create a GitHub PR, query a database |
| **Resources** | Data the agent can read | Read a file, fetch a web page |
| **Prompts** | Pre-built templates for common tasks | "Review this PR" template |
| **Transports** | How client and server communicate | stdio (local), SSE (remote) |

---

## Popular MCP Servers

MCP servers extend your AI agent's capabilities by connecting it to external services. Here are the most popular ones:

| Server | What it Does | Best For |
|--------|-------------|----------|
| **Filesystem** | Read/write/search files, manage directories | Codebase navigation |
| **GitHub** | Create/manage repos, PRs, issues, reviews | CI/CD, code review |
| **PostgreSQL** | Query databases, run migrations, schema | Backend development |
| **SQLite** | Local database access | Prototyping, local dev |
| **Slack** | Send/read messages, manage channels | Team communication |
| **Web Search** | Search the internet | Research, documentation |
| **Puppeteer** | Headless browser automation | Web scraping, testing |
| **Memory** | Persistent memory across sessions | Long-running agents |
| **Sequential Thinking** | Structured reasoning | Complex problem solving |
| **Brave Search** | Web + local search | Web research |

_→ See [MCP Servers](./mcp-servers) for detailed installation guides and configuration_

---

## Tools Supporting MCP

| Tool | MCP Support | Notes |
|------|------------|-------|
| **Claude Code** | Full | Native MCP client. Configure in claude.json |
| **OpenCode** | Full | MCP server via config file |
| **Cursor** | Yes | Cursor MCP server support |
| **Windsurf** | Yes | MCP integration |
| **OpenClaw** | Yes | MCP tools support |

---

## Related

- [**MCP Servers**](./mcp-servers) — Popular MCP servers with detailed installation guides
- [**AI Tools Index**](../AI-Tools/) — Full tools reference including MCP support

---

## Quick Start: Add an MCP Server

To add an MCP server to your agent, add it to your agent's configuration:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-token"
      }
    }
  }
}
```

Then restart your agent and the new tools will be available automatically.
