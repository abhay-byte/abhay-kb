# BrainBot Discord MCP - Complete Setup & Usage Guide

> **Agent:** OpenClaw (running on Android chroot Debian)
> **Purpose:** Discord server management via Model Context Protocol (MCP)
> **Servers:** FluxLinux, FinalBenchmark 2, MKM
> **Last Updated:** 2026-05-25

---

## 1. Architecture Overview

```
┌─────────────────┐ HTTP/SSE ┌──────────────────┐ WebSocket ┌─────────────┐
│ OpenClaw │ ◄────────────────► │ discord-mcp │ ◄──────────────► │ Discord │
│ (BrainBot) │ MCP Protocol │ (Java/Spring) │ JDA Library │ API │
│ │ Port 8085 │ │ │ │
└─────────────────┘ └──────────────────┘ └─────────────┘
```

**discord-mcp** is a Java/Spring Boot server that exposes 75+ Discord management tools via the Model Context Protocol (MCP). It uses JDA (Java Discord API) to communicate with Discord.

---

## 2. Prerequisites

### On Android Chroot Debian

```bash
# Required packages
apt update
apt install -y openjdk-21-jre-headless curl git

# Verify Java
java -version # Should be Java 21+
```

### Discord Bot Setup (One-time)

1. Go to https://discord.com/developers/applications
2. Create application → Bot → Enable these **Privileged Intents**:

- ☑️ MESSAGE CONTENT INTENT
- ☑️ SERVER MEMBERS INTENT

1. OAuth2 → URL Generator → Select:

- `bot` scope
- `Administrator` permission (or minimum: Manage Channels, Manage Roles, Manage Messages, Read Messages, Send Messages, Create Public Threads, Embed Links, Attach Files, Read Message History)

1. Copy the **Bot Token** (keep secret!)

---

## 3. Installation

```bash
# 1. Clone the MCP server
cd ~/
git clone https://github.com/SaseQ/discord-mcp.git discord-support-mcp

# 2. Or use the local copy if already present
cd ~/discord-support-mcp

# 3. Check JAR exists
ls target/discord-mcp-*.jar
# If not, the start script will download/build it
```

---

## 4. Configuration

### 4.1 Environment Variables

Create `~/discord-support-mcp/.env`:

```bash
SPRING_PROFILES_ACTIVE=http
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
DISCORD_GUILD_ID=1508023908929114132
```

**Important:** The `DISCORD_GUILD_ID` is a default. Most tools accept `guildId` as a parameter, so you can manage ALL three servers with one bot.

### 4.2 The 3 Server IDs

| Server | Guild ID | Description |
|--------|----------|-------------|
| **FluxLinux** | `1508023908929114132` | FluxLinux official support server |
| **FinalBenchmark 2** | `1508147854760480848` | FinalBenchmark platform server |
| **MKM** | `1508147439729774802` | Minimal Kernel Manager server |

**Always specify `guildId` in tool calls when managing non-default servers.**

---

## 5. Running the MCP Server

```bash
cd ~/discord-support-mcp
chmod +x start-discord-mcp.sh
./start-discord-mcp.sh
```

This will:

1. Check for Java 21+
2. Download/build the JAR if needed
3. Start on `http://localhost:8085`
4. Health check: `curl http://localhost:8085/actuator/health`

**Keep it running** in a `screen` or `tmux` session:

```bash
screen -S discord-mcp
./start-discord-mcp.sh
# Ctrl+A, D to detach
```

---

## 6. Connecting OpenClaw to MCP

### 6.1 Configure opencode.json

Edit `~/.config/opencode/opencode.json` and add the MCP server:

```json
{
 "mcpServers": {
 "discord-mcp": {
 "command": "none",
 "url": "http://localhost:8085/mcp",
 "transport": "sse",
 "enabled": true
 }
 }
}
```

### 6.2 Session Initialization (CRITICAL)

Before using ANY tool, you MUST initialize an MCP session:

```bash
# Step 1: Initialize session
curl -s -D - "http://localhost:8085/mcp" \
 -H "Content-Type: application/json" \
 -H "Accept: text/event-stream, application/json" \
 -X POST \
 -d '{
 "jsonrpc": "2.0",
 "id": 1,
 "method": "initialize",
 "params": {
 "protocolVersion": "2024-11-05",
 "capabilities": {},
 "clientInfo": {"name": "brainbot", "version": "1.0"}
 }
 }'

# Response headers include: Mcp-Session-Id: <UUID>
# Extract it: SID=$(echo "$RESP" | grep -i "Mcp-Session-Id" | awk '{print $2}' | tr -d '\r')
```

### 6.3 Making Tool Calls

All tool calls require the `Mcp-Session-Id` header:

```bash
# Template
curl -s "http://localhost:8085/mcp" \
 -H "Content-Type: application/json" \
 -H "Accept: text/event-stream, application/json" \
 -H "Mcp-Session-Id: $SID" \
 -X POST \
 -d '{
 "jsonrpc": "2.0",
 "id": 999,
 "method": "tools/call",
 "params": {
 "name": "TOOL_NAME",
 "arguments": {
 "param1": "value1",
 "guildId": "GUILD_ID"
 }
 }
 }'
```

**Response format:** SSE (Server-Sent Events)
**Parse:** Look for lines starting with `data:` followed by JSON

---

## 7. Available Tools (75 Total)

### 7.1 Channel Management

| Tool | Purpose |
|------|---------|
| `create_text_channel` | Create text channels |
| `create_voice_channel` | Create voice channels |
| `create_category` | Create category channels |
| `create_forum_channel` | Create forum channels |
| `delete_channel` | Delete any channel |
| `move_channel` | Move channel to category (use `categoryId`) |
| `set_channel_permissions` | Set role permissions |
| `list_channels` | List all channels |

**Key params:**

- `guildId` (always required for server-scoped operations)
- `categoryId` (for move_channel, NOT `category`)
- `allowPermissions` / `denyPermissions` (JDA permission names: `VIEW_CHANNEL`, `MESSAGE_SEND`, `MESSAGE_HISTORY`, `MESSAGE_SEND_IN_THREADS`)

### 7.2 Message Management

| Tool | Purpose |
|------|---------|
| `send_message` | Send message (param: `message`, NOT `content`) |
| `send_webhook_message` | Send via webhook |
| `edit_message` | Edit existing message |
| `delete_message` | Delete message |
| `read_messages` | Read message history |
| `add_reaction` | Add emoji reaction |
| `remove_reaction` | Remove reaction |
| `get_attachment` | Get attachment metadata |

**Note:** `send_message` uses parameter name `message`, NOT `content`.

### 7.3 Forum Management

| Tool | Purpose |
|------|---------|
| `create_forum_post` | Create forum post/thread |
| `list_forum_posts` | List active posts |
| `list_forum_channels` | List forum channels |
| `list_forum_tags` | List available tags |

**Important:** `create_forum_post` uses `channelId` (the forum channel ID), NOT `forumId`.

### 7.4 Role Management

| Tool | Purpose |
|------|---------|
| `create_role` | Create roles |
| `delete_role` | Delete roles |
| `assign_role` | Assign to user |
| `remove_role` | Remove from user |
| `list_roles` | List all roles |

### 7.5 Member/User Management

| Tool | Purpose |
|------|---------|
| `ban_member` | Ban user |
| `unban_member` | Unban user |
| `kick_member` | Kick user |
| `timeout_member` | Timeout user |
| `list_members` | List members |
| `get_member` | Get member info |
| `send_private_message` | DM a user |
| `read_private_messages` | Read DMs |

### 7.6 Webhook Management

| Tool | Purpose |
|------|---------|
| `create_webhook` | Create webhook |
| `delete_webhook` | Delete webhook |
| `list_webhooks` | List webhooks |
| `send_webhook_message` | Send via webhook |

### 7.7 Emoji Management

| Tool | Purpose |
|------|---------|
| `create_emoji` | Upload emoji (base64 or URL) |
| `delete_emoji` | Delete emoji |
| `list_emojis` | List emojis |

### 7.8 Server Management

| Tool | Purpose |
|------|---------|
| `set_server_name` | Rename server |
| `set_server_description` | Set description |
| `list_invites` | List invites |
| `get_audit_log` | View audit log |

---

## 8. Common Patterns

### 8.1 Create a Complete Server Structure

```bash
# 1. Create categories
# 2. Create channels (they may not land in correct categories initially)
# 3. Move channels to categories using move_channel with categoryId
# 4. Set permissions
# 5. Send content
# 6. Create forum posts
```

### 8.2 Set Read-Only Info Channels

```json
{
 "name": "set_channel_permissions",
 "arguments": {
 "channelId": "CHANNEL_ID",
 "roleId": "EVERYONE_ROLE_ID",
 "allowPermissions": "VIEW_CHANNEL",
 "denyPermissions": "MESSAGE_SEND,MESSAGE_SEND_IN_THREADS",
 "guildId": "GUILD_ID"
 }
}
```

### 8.3 Hide Moderator-Only Channels

```json
{
 "name": "set_channel_permissions",
 "arguments": {
 "channelId": "MOD_LOGS_CHANNEL_ID",
 "roleId": "EVERYONE_ROLE_ID",
 "allowPermissions": "",
 "denyPermissions": "VIEW_CHANNEL",
 "guildId": "GUILD_ID"
 }
}
```

### 8.4 Create Forum Post

```json
{
 "name": "create_forum_post",
 "arguments": {
 "channelId": "FORUM_CHANNEL_ID",
 "title": "Post Title",
 "message": "Initial post content",
 "guildId": "GUILD_ID"
 }
}
```

---

## 9. Important Notes & Gotchas

1. **Parameter names matter:** `send_message` uses `message`, NOT `content`. `move_channel` uses `categoryId`, NOT `category`.

2. **Forum channels:** `create_forum_channel` via MCP may create a regular text channel instead of a true forum channel. Check with `list_channels` after creation. If it's not FORUM type, create it manually in Discord UI.

3. **Forum posts:** Use `channelId` (the forum channel ID), NOT `forumId` when calling `create_forum_post`.

4. **Guild ID:** Always pass `guildId` parameter for server-scoped operations, especially when managing non-default servers.

5. **Rate limits:** Discord has rate limits. If you get 429 errors, add `sleep 1` between calls.

6. **Missing tools:** These are NOT available in discord-mcp:

- `create_forum_tag` → Must set tags manually in Discord UI
- `set_default_reaction` → Must set manually in Discord UI
- File upload via message → Must use `create_emoji` with image URL, or upload manually

1. **Webhooks:** GitHub webhooks must target regular text channels, NOT forum channels. Use channels like `#general` or `#pull-requests`.

2. **Health check:** `curl http://localhost:8085/actuator/health` should return `{"status":"UP"}`

---

## 10. Server Reference Summary

### FluxLinux (ID: 1508023908929114132)

- **Categories:** INFORMATION, COMMUNITY, SUPPORT, DEVELOPMENT, FLUXLINUX, VOICE CHANNELS
- **Channels:** announcements, rules, welcome, links, faq, mod-logs, general, introductions, showcase, off-topic, help, installation-help, bug-reports, feature-requests, dev-chat, pull-requests, roadmap, testing, documentation, kernel-modules, boot-config, release-announcements, performance-tuning, screenshots, releases, community-events (forum)
- **Roles:** Member, Contributor, Moderator, Supporter

### FinalBenchmark 2 (ID: 1508147854760480848)

- **Categories:** INFORMATION, COMMUNITY, SUPPORT, DEVELOPMENT, FINALBENCHMARK, VOICE CHANNELS
- **Channels:** Same structure as FluxLinux but with FB-specific channels (benchmarking-results, hardware-database, methodology, leaderboard, etc.)
- **Roles:** Member, Contributor, Moderator, Supporter

### MKM (ID: 1508147439729774802)

- **Categories:** INFORMATION, COMMUNITY, SUPPORT, DEVELOPMENT, MKM, VOICE CHANNELS
- **Channels:** Same structure with MKM-specific channels (kernel-management, performance-overlay, swap-management, thermal-discussion, shizuku-help, etc.)
- **Roles:** Member, Contributor, Moderator, Supporter

---

## 11. Troubleshooting

| Problem | Solution |
|---------|----------|
| "Channel not found" | Wrong channel ID or bot lacks VIEW_CHANNEL permission |
| "Guild not found" | Wrong guild ID or bot not in that server |
| "message cannot be null" | Using `content` instead of `message` param |
| "categoryId cannot be null" | Using `category` instead of `categoryId` param |
| 429 Rate Limited | Add delays between calls |
| SSE parse failed | Response is empty; check if server is running |
| "Forum channel not found" | Channel is not actually a forum type; check with list_channels |

---

## 12. Quick Start Checklist

- [ ] Bot created at discord.com/developers with MESSAGE CONTENT INTENT + SERVER MEMBERS INTENT
- [ ] Bot invited to all 3 servers with Administrator permission
- [ ] Java 21+ installed on Android chroot Debian
- [ ] discord-mcp cloned to ~/discord-support-mcp
- [ ] .env file created with DISCORD_TOKEN
- [ ] start-discord-mcp.sh running (screen/tmux)
- [ ] Health check passes: `curl http://localhost:8085/actuator/health`
- [ ] opencode.json configured with MCP server URL
- [ ] MCP session initialized successfully
- [ ] Test tool call works (e.g., list_channels)

---

**Credentials Summary:**

- **Discord Bot Token:** `YOUR_DISCORD_BOT_TOKEN`
- **Default Guild ID:** `1508023908929114132` (FluxLinux)
- **FluxLinux:** `1508023908929114132`
- **FinalBenchmark 2:** `1508147854760480848`
- **MKM:** `1508147439729774802`
- **MCP Endpoint:** `http://localhost:8085/mcp`

**Repository:** `https://github.com/SaseQ/discord-mcp.git` (public upstream)
**Local Copy:** `~/repos/discord-support-mcp/` or `~/discord-support-mcp/`
