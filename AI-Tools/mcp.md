---
layout: standalone
title: MCP
---

# Model Context Protocol (MCP)

MCP is an open standard developed by Anthropic for connecting AI agents to external data sources, tools, and services. It provides a standardized way for agents to interact with the world beyond their training data.

---

## How MCP Works

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" style="max-width:100%;height:auto;background:#0d0d0d;border-radius:10px;font-family:-apple-system,system-ui,sans-serif;margin:16px 0">

  <!-- Title -->
  <text x="400" y="35" text-anchor="middle" fill="#fff" font-size="16" font-weight="700">How MCP Works — Architecture Diagram</text>

  <!-- Layer 1: Host / Client -->
  <rect x="40" y="60" width="720" height="70" rx="8" fill="rgba(250,189,47,0.08)" stroke="rgba(250,189,47,0.25)" stroke-width="1.5"/>
  <text x="60" y="85" fill="#fabd2f" font-size="12" font-weight="600">LAYER 1: HOST — AI Application</text>
  
  <rect x="60" y="95" width="180" height="24" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="150" y="111" text-anchor="middle" fill="#ccc" font-size="11">Claude Code</text>
  <rect x="260" y="95" width="180" height="24" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="350" y="111" text-anchor="middle" fill="#ccc" font-size="11">OpenCode</text>
  <rect x="460" y="95" width="140" height="24" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="530" y="111" text-anchor="middle" fill="#ccc" font-size="11">Cursor</text>
  <rect x="620" y="95" width="120" height="24" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="680" y="111" text-anchor="middle" fill="#ccc" font-size="11">OpenClaw</text>

  <!-- Arrow: Host → MCP Client -->
  <line x1="400" y1="130" x2="400" y2="155" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
  <polygon points="395,150 400,160 405,150" fill="rgba(255,255,255,0.2)"/>

  <!-- Layer 2: MCP Client (built into host) -->
  <rect x="200" y="160" width="400" height="44" rx="8" fill="rgba(66,133,244,0.1)" stroke="rgba(66,133,244,0.3)" stroke-width="1.5"/>
  <text x="400" y="182" text-anchor="middle" fill="#4285f4" font-size="13" font-weight="600">MCP Protocol Client (built into Host)</text>
  <text x="400" y="196" text-anchor="middle" fill="#888" font-size="10">Manages connections · Routes requests · Handles auth · Transports: stdio / SSE</text>

  <!-- Arrow: MCP Client → MCP Servers -->
  <line x1="400" y1="204" x2="400" y2="225" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
  <polygon points="395,220 400,230 405,220" fill="rgba(255,255,255,0.2)"/>

  <!-- Layer 3: MCP Servers -->
  <rect x="40" y="235" width="720" height="70" rx="8" fill="rgba(52,168,83,0.08)" stroke="rgba(52,168,83,0.25)" stroke-width="1.5"/>
  <text x="60" y="258" fill="#34a853" font-size="12" font-weight="600">LAYER 2: MCP SERVERS</text>

  <rect x="60" y="268" width="100" height="24" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="110" y="284" text-anchor="middle" fill="#ccc" font-size="10">Filesystem</text>
  <rect x="175" y="268" width="90" height="24" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="220" y="284" text-anchor="middle" fill="#ccc" font-size="10">GitHub</text>
  <rect x="280" y="268" width="100" height="24" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="330" y="284" text-anchor="middle" fill="#ccc" font-size="10">PostgreSQL</text>
  <rect x="395" y="268" width="80" height="24" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="435" y="284" text-anchor="middle" fill="#ccc" font-size="10">Slack</text>
  <rect x="490" y="268" width="90" height="24" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="535" y="284" text-anchor="middle" fill="#ccc" font-size="10">Web Search</text>
  <rect x="595" y="268" width="85" height="24" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="637" y="284" text-anchor="middle" fill="#ccc" font-size="10">Puppeteer</text>
  <rect x="695" y="268" width="50" height="24" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="720" y="284" text-anchor="middle" fill="#ccc" font-size="10">+more</text>

  <!-- Arrow: MCP Servers → External Services -->
  <line x1="400" y1="305" x2="400" y2="325" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
  <polygon points="395,320 400,330 405,320" fill="rgba(255,255,255,0.2)"/>

  <!-- Layer 4: External Services -->
  <rect x="40" y="335" width="720" height="65" rx="8" fill="rgba(234,67,53,0.08)" stroke="rgba(234,67,53,0.25)" stroke-width="1.5"/>
  <text x="60" y="358" fill="#ea4335" font-size="12" font-weight="600">LAYER 3: EXTERNAL SERVICES</text>

  <rect x="60" y="368" width="110" height="22" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="115" y="383" text-anchor="middle" fill="#ccc" font-size="10">File System</text>
  <rect x="185" y="368" width="90" height="22" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="230" y="383" text-anchor="middle" fill="#ccc" font-size="10">GitHub API</text>
  <rect x="290" y="368" width="100" height="22" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="340" y="383" text-anchor="middle" fill="#ccc" font-size="10">Database</text>
  <rect x="405" y="368" width="80" height="22" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="445" y="383" text-anchor="middle" fill="#ccc" font-size="10">Slack API</text>
  <rect x="500" y="368" width="90" height="22" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="545" y="383" text-anchor="middle" fill="#ccc" font-size="10">Web APIs</text>
  <rect x="605" y="368" width="85" height="22" rx="4" fill="#1a1a2e" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
  <text x="647" y="383" text-anchor="middle" fill="#ccc" font-size="10">Browser</text>

  <!-- Data flow labels -->
  <text x="640" y="182" fill="rgba(255,255,255,0.15)" font-size="9" font-style="italic">← Tools, Resources, Prompts →</text>
  <text x="640" y="290" fill="rgba(255,255,255,0.15)" font-size="9" font-style="italic">← API calls, Data, Actions →</text>

</svg>

MCP follows a **3-layer client-server architecture**:

| Layer | Component | Role |
|-------|-----------|------|
| **1** | **Host** (AI App) | The AI application you use — Claude Code, OpenCode, Cursor, OpenClaw |
| **2** | **MCP Clients** (built into Host) | Manage connections, route requests, handle authentication via stdio or SSE transports |
| **3** | **MCP Servers** | Expose specific tools, resources, and prompts for the agent to use |

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
