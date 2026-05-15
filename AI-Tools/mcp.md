---
layout: standalone
title: MCP
---

# Model Context Protocol (MCP)

MCP is an open standard developed by Anthropic for connecting AI agents to external data sources, tools, and services. It provides a standardized way for agents to interact with the world beyond their training data.

---

## How MCP Works

```
Agent/Client ←→ MCP Protocol ←→ MCP Server ←→ External Service
                                    (API, DB, Files, Slack, etc.)
```

MCP follows a client-server architecture:
- **Host**: The AI application (Claude Code, OpenCode, Cursor, etc.)
- **Client**: Built into the host, manages the connection
- **Server**: Exposes tools, resources, and prompts for the agent to use

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

---

## MCP vs Other Concepts

| Concept | Role | Analogy |
|---------|------|---------|
| **MCP** | Connects agents to external data/services | USB-C for AI |
| **Skills** | Teaches agents how to do tasks | Recipe book |
| **Tools** | Built-in agent capabilities | Kitchen appliances |
| **Subagents** | Child agents for parallel work | Extra hands |

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

## Quick Start

To add an MCP server to your agent, add it to the agent's configuration:

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
