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
  - [GitHub](#github-mcp-server)
  - [PostgreSQL](#postgresql-mcp-server)
  - [SQLite](#sqlite-mcp-server)
  - [Slack](#slack-mcp-server)
  - [Web / Brave Search](#web-search--brave-search-mcp-server)
  - [Puppeteer](#puppeteer-mcp-server)
  - [Memory](#memory-mcp-server)
  - [Sequential Thinking](#sequential-thinking-mcp-server)
- [Tools Supporting MCP](#tools-supporting-mcp)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

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

Official filesystem server from Anthropic's Model Context Protocol. Provides safe read/write access to local files and directories.

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-filesystem` |
| **Config** | No extra config needed |
| **Permissions** | Reads files, creates directories |
| **Best For** | Codebase navigation, local file operations |
| **Security** | Requires allowed directory paths (configurable) |

**Installation**

**Using npx (recommended):**
```bash
npx -y @modelcontextprotocol/server-filesystem
```

**Using npm globally:**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Configuration:** By default, allows read access to the project directory you run the agent from. For security, you can configure which directories to allow:

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

**Docker:**
```bash
docker run -v $(pwd):/project:/project -it --rm ghcr.io/modelcontextprotocol/filesystem
```

---

### GitHub MCP Server

Provides access to GitHub repositories, issues, PRs, and CI/CD through the GitHub API. Inherits the same access restrictions as your GitHub account.

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-github` |
| **Config** | Requires `GITHUB_TOKEN` environment variable |
| **Permissions** | Repositories, issues, PRs, code review, CI/CD based on your GitHub access |
| **Best For** | GitHub workflows, code review automation |
| **Security** | Personal access tokens scoped to specific repos (recommended) |

**Installation**

**Using npx:**
```bash
npx -y @modelcontextprotocol/server-github
```

**Configuration:** Create a GitHub personal access token at https://github.com/settings/tokens

Generate a token with these scopes (minimum):
- `repo` (full access to private repos)
- `read:org` (if accessing org repos)
- `read:user` (if accessing user repos)

**IMPORTANT:** For security, create a **fine-grained token** with only the permissions you need and scoped to specific repositories rather than using a broad-scope token with admin access.

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

**Using Claude's managed endpoint:** If you're using Claude Code, you can skip local setup entirely and use GitHub's managed MCP endpoint directly via Claude's configuration:

```json
{
  "mcpServers": {
    "github": {
      "url": "https://api.anthropic.com/v1/mcp/github"
    }
  }
}
```

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
| **Security** | Connection string with credentials (keep secret) |

**Installation**

**Using npx:**
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

**Connection string format:**
```
postgresql://[user[:password]@][host][:port][/database][?params]
```

**Environment variables (alternative):**
```bash
export PGHOST=localhost
export PGPORT=5432
export PGUSER=myuser
export PGPASSWORD=mypassword
export PGDATABASE=mydb
```

**Features:**
- **Schema introspection:** Agent can read table structures, columns, types
- **Query execution:** Run SELECT queries safely (read-only)
- **Transaction safety:** No write operations prevent data corruption

**Security notes:**
- Use environment variables for credentials (never hardcode in files)
- Consider using a read-only database user for AI agents
- Restrict which tables the agent can access via database-level permissions

---

### SQLite MCP Server

Provides read/write access to SQLite databases. Good for local development, prototyping, and data inspection.

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-sqlite` |
| **Config** | Requires database file path |
| **Permissions** | Full read/write database access |
| **Best For** | Local development, data inspection, quick prototyping |
| **Security** | Database file should be in agent-accessible directory |

**Installation**

**Using npx:**
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
- **Performance optimization:** Agent can analyze query plans

**Docker setup:**
```bash
# Mount database directory
docker run -v $(pwd)/data:/data -it --rm ghcr.io/modelcontextprotocol/sqllite \
  -e DATABASE_PATH=/data/mydatabase.db
```

**Security notes:**
- Database file should not contain sensitive data in production
- Consider database journaling mode for recovery
- WAL mode recommended for concurrent access

---

### Slack MCP Server

Provides access to Slack channels, messages, and threads. Good for team communication workflows.

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-slack` |
| **Config** | Requires `SLACK_TOKEN` and optionally `SLACK_TEAM_ID` |
| **Permissions** | Read/write messages, join channels (based on token scopes) |
| **Best For** | Team communication, message retrieval, channel management |
| **Security** | Slack user tokens should be kept secret |

**Installation**

**Python setup:**
```bash
# Ensure Python 3.10+
python -m pip install slack-mcp-server

# Start the server
python -m slack_mcp_server
```

**npm setup:**
```bash
npx -y @modelcontextprotocol/server-slack
```

**Configuration:** Create a Slack app and generate a bot token at https://api.slack.com/apps

**Required scopes for token:**
- `channels:history`
- `channels:read`
- `chat:write`
- `channels:join`
- `users:read`

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

**Features:**
- **Channel listing:** Agent can browse available channels
- **Message history:** Read recent messages in threads
- **Thread support:** Context from conversation threads
- **User lookup:** Find users by ID or email

**Troubleshooting:**
- **"not_in_channel" error:** Bot needs to be invited to the channel first
- **Rate limiting:** Slack has API limits for team workspaces
- **Bot permissions:** Ensure bot has necessary scopes in Slack app settings

---

### Web Search / Brave Search MCP Server

Provides internet search and web page fetching capabilities. Good for research and accessing up-to-date information.

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-brave-search` |
| **Config** | No extra config needed for basic usage |
| **Permissions** | Full web search, page fetching |
| **Best For** | Research, documentation lookup, current information |
| **Security** | No credentials required (optional API key) |

**Installation**

**Using npx:**
```bash
npx -y @modelcontextprotocol/server-brave-search
```

**Configuration:** Works out of the box with no configuration. Optionally add API key for higher rate limits:

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
- **Multiple sources:** Can search across the web

---

### Puppeteer MCP Server

Provides headless browser automation capabilities. Good for web scraping, testing, and interacting with web applications.

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-puppeteer` |
| **Config** | No extra config needed |
| **Permissions** | Full browser automation (headless) |
| **Best For** | Web scraping, automated testing, web interaction |
| **Security** | Runs in sandboxed browser environment |

**Installation**

**Using npx:**
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
- **Element interaction:** click, type, scroll
- **Screenshot capture:** Take screenshots as base64
- **JavaScript execution:** Run custom scripts in browser context
- **PDF generation:** Save pages as PDF documents
- **Network monitoring:** Intercept and inspect network requests

**Common use cases:**
- **Web scraping:** Extract data from websites
- **Automated testing:** Run tests headlessly
- **Form submission:** Fill and submit forms
- **Screenshot testing:** Capture page states

**Performance notes:**
- Headless browser is resource-intensive
- For scraping, respect `robots.txt` and rate limits

---

### Memory MCP Server

Provides persistent memory storage across agent sessions. Good for long-running agents and context persistence.

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-memory` |
| **Config** | Requires memory backend URL |
| **Permissions** | Read/write memory storage |
| **Best For** | Long-running agents, context persistence, cross-session memory |
| **Security** | Backend authentication required |

**Installation**

**Using npx:**
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

**Backend options:**
- **Redis:** Fast, in-memory storage
- **PostgreSQL:** Persistent relational storage
- **Supabase:** Firebase-like storage
- **Local filesystem:** JSON file storage

---

### Sequential Thinking MCP Server

Enhances agent reasoning with structured thinking chains. Good for complex problem solving and step-by-step analysis.

| Aspect | Details |
|---------|---------|
| **Install** | `npx -y @modelcontextprotocol/server-sequential-thinking` |
| **Config** | No extra config needed |
| **Permissions** | Enhanced reasoning capabilities |
| **Best For** | Complex problems, multi-step reasoning, analysis |
| **Security** | Runs locally, no external deps |

**Installation**

**Using npx:**
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
