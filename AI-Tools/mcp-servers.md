---
layout: standalone
title: MCP Servers
---

# Popular MCP Servers

MCP servers expose tools, resources, and data sources to AI agents. Here are the most popular ones with what they do and what they're best for.

| Server | What it Does | Best For |
|--------|-------------|----------|
| **Filesystem** | Read/write/search files, manage directories | Codebase navigation |
| **GitHub** | Create/manage repos, PRs, issues, reviews | CI/CD, code review |
| **PostgreSQL** | Query databases, run migrations, schema | Backend development |
| **SQLite** | Local database access | Prototyping, local dev |
| **Slack** | Send/read messages, manage channels | Team communication |
| **Web Search** | Search&u0019f internet | Research, documentation |
| **Puppeteer** | Headless browser automation | Web scraping, testing |
| **Memory** | Persistent memory across sessions | Long-running agents |
| **Sequential Thinking** | Structured reasoning | Complex problem solving |
| **Brave Search** | Web + local search | Web research |

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

---

## Related

- [**MCP Overview**](./mcp) — What MCP is and how it works
- [**AI Tools Index**](../AI-Tools/) — Full tools reference
