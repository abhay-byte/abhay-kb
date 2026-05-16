---
layout: standalone
title: MCP — Model Context Protocol
---

# Model Context Protocol (MCP)

MCP is an open standard developed by Anthropic for connecting AI agents to external data sources, tools, and services. It provides a standardized way for agents to interact with the world beyond their training data.

---

## Contents

- [How MCP Works](#how-mcp-works)
- [Key Concepts](#key-concepts)
- [Quick Start: Add an MCP Server](#quick-start-add-an-mcp-server)
- [Popular MCP Servers](#popular-mcp-servers)
  - [Filesystem](#filesystem-mcp-server)
  - [Git](#git-mcp-server)
  - [GitHub](#github-mcp-server)
  - [PostgreSQL](#postgresql-mcp-server)
  - [SQLite](#sqlite-mcp-server)
  - [Slack](#slack-mcp-server)
  - [Web / Brave Search](#web-search--brave-search-mcp-server)
  - [Puppeteer](#puppeteer-mcp-server)
  - [Playwright](#playwright-mcp-server)
  - [Memory](#memory-mcp-server)
  - [Sequential Thinking](#sequential-thinking-mcp-server)
  - [Time](#time-mcp-server)
  - [Context Mode](#context-mode-mcp-server)
  - [Context7](#context7-mcp-server)
  - [DuckDuckGo](#duckduckgo-mcp-server)
  - [Android MCP](#android-mcp-server)
- [Tools Supporting MCP](#tools-supporting-mcp)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## How MCP Works

<div align="center">
<svg viewBox="0 0 900 380" width="100%" height="380" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;border:2px solid #444;border-radius:12px;background:#1a1a1a;padding:10px;">

  <!-- Title -->
  <text x="450" y="30" text-anchor="middle" fill="#fff" font-size="18" font-weight="bold">MCP Architecture — 3-Layer Client-Server Model</text>

  <!-- Layer 1: Host -->
  <rect x="40" y="55" width="820" height="65" rx="8" fill="#2a2a4a" stroke="#888" stroke-width="2"/>
  <text x="60" y="80" fill="#fabd2f" font-size="14" font-weight="bold">Layer 1:</text>
  <text x="140" y="80" fill="#fff" font-size="14" font-weight="bold">HOST (AI Application)</text>
  <text x="60" y="102" fill="#ccc" font-size="12">Claude Code, OpenCode, Cursor, Windsurf, OpenClaw, Gemini CLI, Copilot</text>

  <!-- Arrow L1 -> L2 -->
  <line x1="450" y1="120" x2="450" y2="140" stroke="#fabd2f" stroke-width="3"/>
  <polygon points="445,138 450,148 455,138" fill="#fabd2f"/>
  <text x="470" y="134" fill="#888" font-size="11">MCP Protocol (stdio / SSE)</text>

  <!-- Layer 2: MCP Client -->
  <rect x="40" y="150" width="820" height="55" rx="8" fill="#2a4a3a" stroke="#888" stroke-width="2"/>
  <text x="60" y="175" fill="#fabd2f" font-size="14" font-weight="bold">Layer 2:</text>
  <text x="140" y="175" fill="#fff" font-size="14" font-weight="bold">MCP CLIENT (built into Host)</text>
  <text x="60" y="195" fill="#ccc" font-size="12">Manages connections, routes requests, handles authentication</text>

  <!-- Arrow L2 -> L3 -->
  <line x1="450" y1="205" x2="450" y2="225" stroke="#fabd2f" stroke-width="3"/>
  <polygon points="445,223 450,233 455,223" fill="#fabd2f"/>
  <text x="470" y="220" fill="#888" font-size="11">Tools / Resources / Prompts</text>

  <!-- Layer 3: MCP Servers -->
  <rect x="40" y="235" width="820" height="125" rx="8" fill="#3a2a4a" stroke="#888" stroke-width="2"/>
  <text x="60" y="258" fill="#fabd2f" font-size="14" font-weight="bold">Layer 3:</text>
  <text x="140" y="258" fill="#fff" font-size="14" font-weight="bold">MCP SERVERS</text>

  <!-- Server blocks - 3 rows x 4 -->
  <rect x="55" y="270" width="180" height="35" rx="6" fill="#2a3a3a" stroke="#6a8a5a" stroke-width="1.5"/>
  <text x="145" y="292" text-anchor="middle" fill="#8bc34a" font-size="13" font-weight="bold">📄 Filesystem</text>

  <rect x="250" y="270" width="180" height="35" rx="6" fill="#2a3a3a" stroke="#6a8a5a" stroke-width="1.5"/>
  <text x="340" y="292" text-anchor="middle" fill="#8bc34a" font-size="13" font-weight="bold">🐙 GitHub</text>

  <rect x="445" y="270" width="180" height="35" rx="6" fill="#2a3a3a" stroke="#6a8a5a" stroke-width="1.5"/>
  <text x="535" y="292" text-anchor="middle" fill="#8bc34a" font-size="13" font-weight="bold">🗄️ Database</text>

  <rect x="640" y="270" width="200" height="35" rx="6" fill="#2a3a3a" stroke="#6a8a5a" stroke-width="1.5"/>
  <text x="740" y="292" text-anchor="middle" fill="#8bc34a" font-size="13" font-weight="bold">🔍 Web Search</text>

  <rect x="55" y="315" width="180" height="35" rx="6" fill="#2a3a3a" stroke="#6a8a5a" stroke-width="1.5"/>
  <text x="145" y="337" text-anchor="middle" fill="#8bc34a" font-size="13" font-weight="bold">🌐 Browser</text>

  <rect x="250" y="315" width="180" height="35" rx="6" fill="#2a3a3a" stroke="#6a8a5a" stroke-width="1.5"/>
  <text x="340" y="337" text-anchor="middle" fill="#8bc34a" font-size="13" font-weight="bold">🧠 Memory</text>

  <rect x="445" y="315" width="180" height="35" rx="6" fill="#2a3a3a" stroke="#6a8a5a" stroke-width="1.5"/>
  <text x="535" y="337" text-anchor="middle" fill="#8bc34a" font-size="13" font-weight="bold">⏰ Time / Git</text>

  <rect x="640" y="315" width="200" height="35" rx="6" fill="#2a3a3a" stroke="#6a8a5a" stroke-width="1.5"/>
  <text x="740" y="337" text-anchor="middle" fill="#8bc34a" font-size="13" font-weight="bold">🤖 Sequential Thinking</text>

  <!-- Right side label -->
  <text x="770" y="48" text-anchor="end" fill="#666" font-size="11">MCP Server Examples →</text>
</svg>
</div>ayout: standalone
title: MCP — Model Context Protocol
---

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

## Popular MCP Servers

Most servers follow a similar pattern:

1. **Install the server** (usually via npm or docker)
2. **Configure in your agent's mcpServers config**
3. **Restart your agent** to detect new tools

---

### Filesystem MCP Server

Official server from Anthropic's MCP repository. Provides safe read/write access to local files and directories.

- **GitHub:** [modelcontextprotocol/servers — src/filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)
- **npm:** `@modelcontextprotocol/server-filesystem`

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-filesystem` |
| **Config** | No extra config needed |
| **Permissions** | Reads files, creates directories |
| **Best For** | Codebase navigation, local file operations |

**Installation**
```bash
npx -y @modelcontextprotocol/server-filesystem
```

**Configuration:**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"],
      "env": {
        "ALLOWED_DIRECTORIES": "/path/to/your/project"
      }
    }
  }
}
```

---

### Git MCP Server

Official Git server from Anthropic's MCP repository. Provides tools for reading, searching, and analyzing Git repositories — commit history, branches, diffs, file status.

- **GitHub:** [modelcontextprotocol/servers — src/git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)
- **npm:** `@modelcontextprotocol/server-git`

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-git` |
| **Config** | No extra config needed (runs in current repo) |
| **Permissions** | Read-only access to Git history |
| **Best For** | Code review, git log analysis, branch inspection |

**Installation**
```bash
npx -y @modelcontextprotocol/server-git
```

**Configuration:**
```json
{
  "mcpServers": {
    "git": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-git"]
    }
  }
}
```

**Features:**
- **Commit history:** Read commit messages, authors, dates
- **Branch listing:** List and inspect branches
- **File diff:** Show diffs between commits
- **Status check:** Current repo status (modified, staged files)

---

### GitHub MCP Server

Two options available — the official server from GitHub and the Anthropic MCP version.

**Option 1 — Official GitHub MCP Server**

- **GitHub:** [github/github-mcp-server](https://github.com/github/github-mcp-server)
- **npm:** `@github/github-mcp-server`

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @github/github-mcp-server` |
| **Config** | Requires `GITHUB_TOKEN` environment variable |
| **Best For** | GitHub-native PR review, issues, code management |

**Installation:**
```bash
npx -y @github/github-mcp-server
```

**Configuration:**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@github/github-mcp-server"],
      "env": {
        "GITHUB_TOKEN": "ghp_your-token-here"
      }
    }
  }
}
```

**Option 2 — Anthropic's MCP GitHub Server**

- **GitHub:** [modelcontextprotocol/servers — src/github](https://github.com/modelcontextprotocol/servers/tree/main/src/github)
- **npm:** `@modelcontextprotocol/server-github`

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-github` |
| **Config** | Requires `GITHUB_TOKEN` environment variable |
| **Best For** | General GitHub API access |

**Configuration:**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your-token-here"
      }
    }
  }
}
```

**Using Claude's managed endpoint:**
```json
{
  "mcpServers": {
    "github": {
      "url": "https://api.anthropic.com/v1/mcp/github"
    }
  }
}
```

**Token setup:** Create at [github.com/settings/tokens](https://github.com/settings/tokens) — use fine-grained tokens scoped to specific repos.

**Troubleshooting:**
- **Token not found:** Ensure `GITHUB_TOKEN` is set and valid
- **403 Forbidden:** Check token scopes (needs `repo` permission)
- **Rate limited:** GitHub has API rate limits (5000 req/hour for authenticated users)

---

### PostgreSQL MCP Server

Provides read-only access to PostgreSQL databases. Good for querying schemas, running migrations, and database introspection.

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-postgres` |
| **Config** | Requires `DATABASE_URL` environment variable |
| **Permissions** | Read-only database access |
| **Best For** | Backend development, database querying, schema analysis |

**Installation**
```bash
npx -y @modelcontextprotocol/server-postgres
```

**Configuration:**
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb"
      }
    }
  }
}
```

**Features:**
- **Schema introspection:** Agent can read table structures, columns, types
- **Query execution:** Run SELECT queries safely (read-only)
- **Transaction safety:** No write operations prevent data corruption

---

### SQLite MCP Server

Provides read/write access to SQLite databases. Good for local development, prototyping, and data inspection.

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-sqlite` |
| **Config** | Requires database file path |
| **Permissions** | Full read/write database access |
| **Best For** | Local development, data inspection, quick prototyping |

**Installation**
```bash
npx -y @modelcontextprotocol/server-sqlite
```

**Configuration:**
```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite"],
      "env": {
        "DATABASE_PATH": "./data/mydatabase.db"
      }
    }
  }
}
```

**Features:**
- **Full SQL access:** SELECT, INSERT, UPDATE, DELETE
- **Schema inspection:** Read table structures, indexes, triggers
- **Transaction support:** BEGIN/COMMIT transactions

---

### Slack MCP Server

Provides access to Slack channels, messages, and threads. Good for team communication workflows.

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-slack` |
| **Config** | Requires `SLACK_TOKEN` and optionally `SLACK_TEAM_ID` |
| **Permissions** | Read/write messages, join channels |
| **Best For** | Team communication, message retrieval, channel management |

**Installation**
```bash
npx -y @modelcontextprotocol/server-slack
```

**Configuration:** Create a Slack app at [api.slack.com/apps](https://api.slack.com/apps) with scopes: `channels:history`, `channels:read`, `chat:write`, `channels:join`, `users:read`.

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_TOKEN": "xoxb-your-token-here",
        "SLACK_TEAM_ID": "T1234567890"
      }
    }
  }
}
```

**Troubleshooting:**
- **"not_in_channel" error:** Bot needs to be invited to the channel first
- **Rate limiting:** Slack has API limits for team workspaces

---

### Web Search / Brave Search MCP Server

Provides internet search and web page fetching capabilities.

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-brave-search` |
| **Config** | No extra config needed for basic usage |
| **Best For** | Research, documentation lookup, current information |

**Installation**
```bash
npx -y @modelcontextprotocol/server-brave-search
```

**Configuration:** Works out of the box. Optionally add API key for higher rate limits:

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "optional-api-key-here"
      }
    }
  }
}
```

**Features:**
- **Web search:** Query Brave Search API
- **Page fetching:** Extract content from URLs
- **HTML-to-text:** Convert web pages to readable text

---

### Puppeteer MCP Server

Provides headless browser automation capabilities. Supports web scraping, testing, and web interaction.

- **GitHub:** [code-craka/puppeteer-mcp](https://github.com/code-craka/puppeteer-mcp)
- **MCP Servers listing:** [mcpservers.org/servers/code-craka/puppeteer-mcp](https://mcpservers.org/servers/code-craka/puppeteer-mcp)

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-puppeteer` |
| **Config** | No extra config needed |
| **Best For** | Web scraping, automated testing, web interaction |

**Installation**
```bash
npx -y @modelcontextprotocol/server-puppeteer
```

**Configuration:**
```json
{
  "mcpServers": {
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    }
  }
}
```

**Features:**
- **Page navigation:** Visit URLs, navigate within pages
- **Screenshot capture:** Take screenshots as base64
- **JavaScript execution:** Run custom scripts in browser context
- **PDF generation:** Save pages as PDF documents
- **Network monitoring:** Intercept and inspect network requests

---

### Playwright MCP Server

Microsoft's Playwright-based MCP server for browser automation. More feature-rich than Puppeteer — supports multiple browsers, network mocking, and accessibility snapshots.

- **GitHub:** [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @playwright/mcp` |
| **Config** | No extra config needed |
| **Best For** | Cross-browser testing, modern web automation |

**Installation**
```bash
npx -y @playwright/mcp
```

**Configuration:**
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp"]
    }
  }
}
```

**Features:**
- **Multi-browser:** Chromium, Firefox, WebKit support
- **Accessibility snapshots:** Read page structure via a11y tree
- **Network mocking:** Intercept and modify network requests
- **Screenshot & PDF:** Capture page states
- **Element interaction:** Click, type, navigate — any web action

---

### Memory MCP Server

Provides persistent memory storage across agent sessions. Good for long-running agents and context persistence.

- **GitHub:** [modelcontextprotocol/servers — src/memory](https://github.com/modelcontextprotocol/servers/blob/main/src/memory/README.md)
- **npm:** `@modelcontextprotocol/server-memory`

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-memory` |
| **Config** | Requires memory backend URL |
| **Best For** | Long-running agents, context persistence, cross-session memory |

**Installation**
```bash
npx -y @modelcontextprotocol/server-memory
```

**Configuration:**
```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "env": {
        "MEMORY_BACKEND_URL": "your-backend-url"
      }
    }
  }
}
```

**Features:**
- **Persistent storage:** Memory survives agent restarts
- **Session-scoped:** Different agents have separate memory
- **Search:** Retrieve memories by key or content
- **Namespaces:** Organize memories by project or topic

**Backend options:** Redis, PostgreSQL, Supabase, Local filesystem

---

### Sequential Thinking MCP Server

Enhances agent reasoning with structured thinking chains. Good for complex problem solving and step-by-step analysis.

- **GitHub:** [modelcontextprotocol/servers — src/sequentialthinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)
- **npm:** `@modelcontextprotocol/server-sequential-thinking`

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-sequential-thinking` |
| **Config** | No extra config needed |
| **Best For** | Complex problems, multi-step reasoning, analysis |

**Installation**
```bash
npx -y @modelcontextprotocol/server-sequential-thinking
```

**Configuration:**
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

**Features:**
- **Thinking chains:** Agent shows step-by-step reasoning
- **Tree visualization:** See decision paths
- **Context management:** Track what information is considered
- **Debug mode:** Inspect internal reasoning process

---

### Time MCP Server

Official Time server from Anthropic's MCP repository. Provides current time and timezone information for agents.

- **GitHub:** [modelcontextprotocol/servers — src/time](https://github.com/modelcontextprotocol/servers/tree/main/src/time)
- **npm:** `@modelcontextprotocol/server-time`

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-time` |
| **Config** | No extra config needed |
| **Best For** | Timezone-aware agents, scheduling, timestamps |

**Installation**
```bash
npx -y @modelcontextprotocol/server-time
```

**Configuration:**
```json
{
  "mcpServers": {
    "time": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-time"]
    }
  }
}
```

**Features:**
- **Current time:** Get current time in specified timezone
- **Timezone conversion:** Convert between timezones
- **Date calculations:** Add/subtract time, get day of week

---

### Context Mode MCP Server

An MCP server that enables context-aware agent behaviors with mode switching for different development scenarios.

- **GitHub:** [mksglu/context-mode](https://github.com/mksglu/context-mode)

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y context-mode` |
| **Config** | No extra config needed |
| **Best For** | Context-aware prompting, mode-based agent behavior |

**Installation**
```bash
npx -y context-mode
```

**Configuration:**
```json
{
  "mcpServers": {
    "context-mode": {
      "command": "npx",
      "args": ["-y", "context-mode"]
    }
  }
}
```

**Features:**
- **Mode switching:** Toggle between development, review, debug modes
- **Context awareness:** Provides contextual prompts based on mode
- **Workflow integration:** Adapts agent behavior to current task

---

### Context7 MCP Server

A context-aware MCP server by Upstash that provides relevant context from external sources to AI agents.

- **GitHub:** [upstash/context7](https://github.com/upstash/context7)

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @upstash/context7` |
| **Config** | Requires Upstash API key |
| **Best For** | RAG-based context injection, external knowledge retrieval |

**Installation**
```bash
npx -y @upstash/context7
```

**Configuration:**
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7"],
      "env": {
        "UPSTASH_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

**Features:**
- **External context:** Fetch relevant context from external sources
- **RAG integration:** Retrieve-augment-generate pipeline
- **Knowledge injection:** Provide agents with up-to-date external information

---

### DuckDuckGo MCP Server

Provides privacy-focused web search capabilities through DuckDuckGo search engine.

- **GitHub:** [nickclyde/duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @nickclyde/duckduckgo-mcp-server` |
| **Config** | No API key required (free, privacy-focused) |
| **Best For** | Privacy-respecting web search, research |

**Installation**
```bash
npx -y @nickclyde/duckduckgo-mcp-server
```

**Configuration:**
```json
{
  "mcpServers": {
    "duckduckgo": {
      "command": "npx",
      "args": ["-y", "@nickclyde/duckduckgo-mcp-server"]
    }
  }
}
```

**Features:**
- **Web search:** Query DuckDuckGo search engine
- **Privacy:** No tracking, no API key required
- **Instant answers:** Get direct answers where available

---

### Android MCP Server

Enables AI agents to interact with Android devices — take screenshots, tap, type, and automate Android UI.

- **GitHub:** [CursorTouch/Android-MCP](https://github.com/CursorTouch/Android-MCP)

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y android-mcp` |
| **Config** | Requires ADB connection to Android device |
| **Best For** | Android automation, UI testing, device control |

**Installation**
```bash
npx -y android-mcp
```

**Configuration:** Requires ADB connected to your Android device:
```bash
# Connect device via USB/Wi-Fi
adb devices
```

```json
{
  "mcpServers": {
    "android": {
      "command": "npx",
      "args": ["-y", "android-mcp"]
    }
  }
}
```

**Features:**
- **Screen capture:** Read device screen content
- **UI interaction:** Tap, swipe, type on device
- **App control:** Launch/kill apps, read notifications
- **Automation:** Script Android workflows

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

## Best Practices

| Practice | Description |
|-----------|-------------|
| **Security** | Use environment variables for secrets, never hardcode in config files |
| **Permissions** | Use minimum required scopes for tokens (principle of least privilege) |
| **Rate limiting** | Be aware of API rate limits (GitHub: 5000/hour, Slack: varies) |
| **Docker** | Containerize MCP servers for isolation and easy deployment |
| **Testing** | Test MCP servers with `npx -y` before full integration |

---

## Troubleshooting

| Issue | Solution |
|---------|----------|
| **MCP server not starting** | Check Node.js version (requires 18+), ensure npx is in PATH |
| **Tool not visible in agent** | Restart agent after updating mcpServers config |
| **Permission errors** | Verify token scopes and account permissions |
| **Connection refused** | Check firewall, ensure server is listening on correct port |

---

## Related

- [**AI Tools Index**](../AI-Tools/) — Full tools reference including MCP support
- [**Tools**](./tools) — AI coding agents and assistants compared
- [**AI Editors**](./ai-editors) — AI-powered editors comparison
- [**Skills**](./skills) — Agent skills explained
