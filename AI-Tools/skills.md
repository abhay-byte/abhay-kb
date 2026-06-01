---
layout: standalone
title: Agent Skills
---

# Agent Skills

> A standardized way to give AI agents new capabilities and expertise. Skills are instruction sets that teach AI agents **how to work** — providing context, guidelines, and step-by-step procedures for specific tasks.

---

## How Skills Work

<div style="border:2px solid #444;border-radius:12px;background:#1a1a1a;padding:20px;margin:16px 0;">

<div style="border:1px solid #555;border-radius:8px;background:#2a2a4a;padding:14px;margin-bottom:12px;">
<div style="color:#fabd2f;font-weight:bold;font-size:14px;margin-bottom:4px;">✏️ SKILL CREATOR</div>
<div style="color:#ccc;font-size:13px;">Writes SKILL.md with name, description, and instructions in a skill directory</div>
<div style="color:#888;font-size:12px;">└── skill-name/SKILL.md  (YAML frontmatter + Markdown instructions)</div>
</div>

<div style="text-align:center;color:#fabd2f;font-size:18px;margin:4px 0;">↓</div>

<div style="border:1px solid #555;border-radius:8px;background:#2a4a3a;padding:14px;margin-bottom:12px;">
<div style="color:#fabd2f;font-weight:bold;font-size:14px;margin-bottom:4px;">🔍 AGENT DISCOVERS &amp; ACTIVATES THE SKILL</div>
<div style="color:#ccc;font-size:13px;">Agent scans skill directories → reads name + description → loads SKILL.md on match</div>
<div style="color:#888;font-size:12px;">Progressive disclosure: agent stores 100+ skills, loads only the one that matches</div>
</div>

<div style="text-align:center;color:#fabd2f;font-size:18px;margin:4px 0;">↓</div>

<div style="border:1px solid #555;border-radius:8px;background:#3a2a4a;padding:14px;margin-bottom:12px;">
<div style="color:#fabd2f;font-weight:bold;font-size:14px;margin-bottom:4px;">⚡ AGENT EXECUTES THE SKILL</div>
<div style="color:#ccc;font-size:13px;">Follows instructions → runs tools/commands → produces output</div>
<div style="color:#888;font-size:12px;">Can reference scripts/, references/, assets/ in the skill directory</div>
</div>

<div style="border:1px solid #444;border-radius:8px;background:#111;padding:12px;margin-top:8px;">
<div style="color:#fabd2f;font-weight:bold;font-size:13px;margin-bottom:4px;">📁 skill-name/</div>
<div style="color:#aaa;font-size:12px;font-family:monospace;line-height:1.7;">
├── SKILL.md<br>
├── scripts/<br>
├── references/<br>
└── assets/
</div>
</div>

</div>

---

## Contents

- [What is an Agent Skill](#what-is-an-agent-skill)
- [Specification](#specification)
- [Skill Directory Structure](#skill-directory-structure)
- [All Skills Reference](#all-skills-reference)
  - [Anthropic Skills](#anthropic-skills)
  - [Community Skills](#community-skills)
- [How to Install & Use Skills](#how-to-install--use-skills)
- [Creating Your Own Skill](#creating-your-own-skill)
- [Best Practices](#best-practices)
- [Which Tools Support Skills](#which-tools-support-skills)

---

## What is an Agent Skill

An **Agent Skill** is a set of instructions that teaches an AI agent how to perform a specific task. Skills are written in Markdown with YAML frontmatter and stored in a standardized directory structure.

| Aspect | Description |
|--------|-------------|
| **What it is** | Instructions that teach an agent how to work |
| **Format** | `SKILL.md` with YAML frontmatter + Markdown body |
| **Scope** | Task-specific (e.g., "how to process PDFs") |
| **Discovery** | Agent scans default skill directories on startup |
| **Activation** | Agent loads skill when user query matches its description |
| **Execution** | Agent follows instructions, can run scripts/commands |

### Skill vs Tool vs MCP

| Concept | Teaches the agent... | Analogy |
|---------|---------------------|---------|
| **Skill** | How to do something | A recipe book |
| **Tool** | What it can do | A kitchen appliance |
| **MCP** | What data it can access | A pantry |

Skills are **portable** — the same skill works in VS Code with GitHub Copilot, Claude Code, OpenCode, Gemini CLI, and any other agent that supports the [Agent Skills](https://agentskills.io) format.

---

## Specification

The Agent Skills specification defines a standard format for skills that works across all compatible AI agents.

### `SKILL.md` Format

Each skill lives in its own directory with a `SKILL.md` file containing YAML frontmatter followed by Markdown content.

**Frontmatter fields:**

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | Yes | Max 64 chars. Lowercase letters, numbers, hyphens only. Must match directory name |
| `description` | Yes | Max 1024 chars. Describes what the skill does and when to use it |
| `license` | No | License name or reference to bundled license file |
| `compatibility` | No | Max 500 chars. Environment requirements |
| `metadata` | No | Arbitrary key-value mapping for additional metadata |
| `allowed-tools` | No | Space-separated string of pre-approved tools (experimental) |

**Example:**

```markdown
---
name: pdf-processing
description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
license: Apache-2.0
metadata:
  author: example-org
  version: "1.0"
---

# Instructions

To process PDFs, use pdfplumber for text extraction...
```

---

## Skill Directory Structure

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code (bash, python, etc.)
├── references/       # Optional: documentation, examples, specs
├── assets/           # Optional: templates, resources, images
└── ...
```

The `SKILL.md` file is the **only required file**. All other directories are optional and provide supporting context the agent can reference.

---

## All Skills Reference

All skills below follow the Agent Skills specification and can be installed in any compatible tool.

### Table of Contents

| # | Skill | Source | Category | Description |
|---|-------|--------|----------|-------------|
| 1 | `algorithmic-art` | Anthropic | Design | Create algorithmic art with p5.js & seeded randomness |
| 2 | `brand-guidelines` | Anthropic | Design | Apply brand colors and typography to artifacts |
| 3 | `canvas-design` | Anthropic | Design | Create beautiful visual art in .png/.pdf |
| 4 | `claude-api` | Anthropic | Development | Build, debug, optimize Claude API / Anthropic SDK apps |
| 5 | `doc-coauthoring` | Anthropic | Writing | Co-author documentation with structured workflow |
| 6 | `docx` | Anthropic | Document | Read/write/edit .docx files |
| 7 | `frontend-design` | Anthropic | Design | Create production-grade frontend interfaces |
| 8 | `internal-comms` | Anthropic | Writing | Write internal communications with company formats |
| 9 | `mcp-builder` | Anthropic | Development | Create MCP servers for external API integration |
| 10 | `pdf` | Anthropic | Document | Extract PDF text, tables, forms using pdfplumber |
| 11 | `pptx` | Anthropic | Document | Create/manipulate .pptx slide decks |
| 12 | `skill-creator` | Anthropic | Development | Create, edit, optimize, and evaluate skills |
| 13 | `slack-gif-creator` | Anthropic | Design | Create animated GIFs optimized for Slack |
| 14 | `theme-factory` | Anthropic | Design | Style artifacts with 10 pre-set themes |
| 15 | `web-artifacts-builder` | Anthropic | Development | Build and deploy web artifacts |
| 16 | `webapp-testing` | Anthropic | Testing | Test local web apps with Playwright |
| 17 | `xlsx` | Anthropic | Document | Read/write/edit .xlsx spreadsheets |
| 18 | `caveman` | Community | Development | Agent-centric workflow orchestration |
| 19 | `spec-kit` | Community | Development | Specification-driven development tools |
| 20 | `agency-agents` | Community | Development | Multi-agent orchestration framework |

---

### Anthropic Skills

Official skills from Anthropic's skills repository. These cover common development, design, and document tasks.

<details>
<summary><strong>1. algorithmic-art</strong> — <em>Creating algorithmic art using p5.js with seeded randomness</em></summary>

- **GitHub:** [anthropics/skills/skills/algorithmic-art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art)
- **Description:** Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use when users request creating art using code.
- **Category:** Design
- **Install:** `git clone` or manual copy to `.agents/skills/algorithmic-art/`

```bash
git clone https://github.com/anthropics/skills.git
cp -r skills/algorithmic-art /your-project/.agents/skills/
```

</details>

<details>
<summary><strong>2. brand-guidelines</strong> — <em>Applies Anthropic's official brand colors and typography</em></summary>

- **GitHub:** [anthropics/skills/skills/brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines)
- **Description:** Applies Anthropic's official brand colors and typography to any sort of artifact. Use when brand colors or style guidelines apply.
- **Category:** Design

</details>

<details>
<summary><strong>3. canvas-design</strong> — <em>Create beautiful visual art in .png and .pdf documents</em></summary>

- **GitHub:** [anthropics/skills/skills/canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design)
- **Description:** Create beautiful visual art in .png and .pdf documents using design philosophy. Use when creating posters, pieces, or visual designs.
- **Category:** Design

</details>

<details>
<summary><strong>4. claude-api</strong> — <em>Build, debug, and optimize Claude API / Anthropic SDK apps</em></summary>

- **GitHub:** [anthropics/skills/skills/claude-api](https://github.com/anthropics/skills/tree/main/skills/claude-api)
- **Description:** Build, debug, and optimize Claude API / Anthropic SDK apps. Includes prompt caching, model migration, and feature configuration.
- **Category:** Development

</details>

<details>
<summary><strong>5. doc-coauthoring</strong> — <em>Guide users through a structured workflow for co-authoring documentation</em></summary>

- **GitHub:** [anthropics/skills/skills/doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring)
- **Description:** Guide users through a structured workflow for co-authoring documentation, proposals, technical specs, and decision documents.
- **Category:** Writing

</details>

<details>
<summary><strong>6. docx</strong> — <em>Read, write, and edit .docx files programmatically</em></summary>

- **GitHub:** [anthropics/skills/skills/docx](https://github.com/anthropics/skills/tree/main/skills/docx)
- **Description:** Handles .docx files as input or output. Creates formatted Word documents, reports, and templates via python-docx.
- **Category:** Document

</details>

<details>
<summary><strong>7. frontend-design</strong> — <em>Create distinctive, production-grade frontend interfaces</em></summary>

- **GitHub:** [anthropics/skills/skills/frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design)
- **Description:** Create distinctive, production-grade frontend interfaces with high design quality. Use when building web components, pages, and applications.
- **Category:** Design

</details>

<details>
<summary><strong>8. internal-comms</strong> — <em>Write all kinds of internal communications</em></summary>

- **GitHub:** [anthropics/skills/skills/internal-comms](https://github.com/anthropics/skills/tree/main/skills/internal-comms)
- **Description:** A set of resources to write internal communications using company-specific formats. Includes templates for memos, announcements, and updates.
- **Category:** Writing

</details>

<details>
<summary><strong>9. mcp-builder</strong> — <em>Guide for creating high-quality MCP servers</em></summary>

- **GitHub:** [anthropics/skills/skills/mcp-builder](https://github.com/anthropics/skills/tree/main/skills/mcp-builder)
- **Description:** Guide for creating high-quality MCP servers that enable LLMs to interact with external services through well-designed tools. Supports Python (FastMCP) and Node/TypeScript (MCP SDK).
- **Category:** Development

</details>

<details>
<summary><strong>10. pdf</strong> — <em>Extract text and tables from PDFs, fill forms, merge files</em></summary>

- **GitHub:** [anthropics/skills/skills/pdf](https://github.com/anthropics/skills/tree/main/skills/pdf)
- **Description:** Extract PDF text, tables, and forms using pdfplumber. Handles PDF as input or output, including HTML reports and database pipelines.
- **Category:** Document

</details>

<details>
<summary><strong>11. pptx</strong> — <em>Create and manipulate .pptx slide decks</em></summary>

- **GitHub:** [anthropics/skills/skills/pptx](https://github.com/anthropics/skills/tree/main/skills/pptx)
- **Description:** Use any time a .pptx file is involved — creating slide decks, pitch decks, or presentations. Handles both input and output.
- **Category:** Document

</details>

<details>
<summary><strong>12. skill-creator</strong> — <em>Create, edit, optimize, and evaluate skills</em></summary>

- **GitHub:** [anthropics/skills/skills/skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- **Description:** Create new skills, modify existing ones, run evals, benchmark performance with variance analysis, and optimize skill descriptions for better triggering accuracy.
- **Category:** Development

</details>

<details>
<summary><strong>13. slack-gif-creator</strong> — <em>Create animated GIFs optimized for Slack</em></summary>

- **GitHub:** [anthropics/skills/skills/slack-gif-creator](https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator)
- **Description:** Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts.
- **Category:** Design

</details>

<details>
<summary><strong>14. theme-factory</strong> — <em>Style artifacts with pre-set themes</em></summary>

- **GitHub:** [anthropics/skills/skills/theme-factory](https://github.com/anthropics/skills/tree/main/skills/theme-factory)
- **Description:** Toolkit for styling artifacts with 10 pre-set themes. Works with slides, docs, reports, HTML landing pages, and more.
- **Category:** Design

</details>

<details>
<summary><strong>15. web-artifacts-builder</strong> — <em>Build and deploy web artifacts</em></summary>

- **GitHub:** [anthropics/skills/skills/web-artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder)
- **Description:** Build and deploy web artifacts including HTML pages, interactive components, and web applications.
- **Category:** Development

</details>

<details>
<summary><strong>16. webapp-testing</strong> — <em>Toolkit for interacting with and testing local web applications</em></summary>

- **GitHub:** [anthropics/skills/skills/webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing)
- **Description:** Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing screenshots, and viewing browser logs.
- **Category:** Testing

</details>

<details>
<summary><strong>17. xlsx</strong> — <em>Read, write, and edit .xlsx spreadsheets</em></summary>

- **GitHub:** [anthropics/skills/skills/xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx)
- **Description:** Handles .xlsx files as input or output. Creates formatted spreadsheets, data reports, database pipelines, and Google Sheets API integrations.
- **Category:** Document

</details>

---

### Community Skills

<details>
<summary><strong>18. caveman</strong> — <em>Agent-centric workflow orchestration by Julius Brussee</em></summary>

- **GitHub:** [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main)
- **Description:** Caveman is a workflow orchestration framework for AI agents. It defines a declarative YAML format for agent workflows with sequential, parallel, and conditional execution steps. Skills in caveman focus on structured agent behavior, repeatable task patterns, and multi-step orchestration.
- **Category:** Development / Workflow Orchestration
- **Installation:**

```bash
git clone https://github.com/JuliusBrussee/caveman.git
# Place desired patterns in .agents/skills/
```

</details>

<details>
<summary><strong>19. spec-kit</strong> — <em>Specification-driven development tools by GitHub</em></summary>

- **GitHub:** [github/spec-kit](https://github.com/github/spec-kit)
- **Description:** Spec-kit provides tools and skills for specification-driven development. It enables agents to work from formal specifications, generate code from specs, and validate implementations against requirements. Particularly useful for contract-first development and API design workflows.
- **Category:** Development / Specification-Driven
- **Installation:**

```bash
git clone https://github.com/github/spec-kit.git
# Install specs and skills into your agent's skill directories
```

</details>

<details>
<summary><strong>20. agency-agents</strong> — <em>Multi-agent orchestration framework</em></summary>

- **GitHub:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)
- **Description:** Agency-agents is a framework for orchestrating multiple AI agents with defined roles, communication patterns, and task delegation. Skills in this framework define agent roles, handoff protocols, and coordination patterns for complex multi-agent workflows.
- **Category:** Development / Multi-Agent Orchestration
- **Installation:**

```bash
git clone https://github.com/msitarzewski/agency-agents.git
# Reference the agent patterns and role definitions
```

</details>

---

## How to Install & Use Skills

Skills are portable across all compatible agents. The installation process is the same whether you use VS Code, Claude Code, OpenCode, or any other skill-supporting tool.

### Method 1: Manual Installation (Works Everywhere)

```bash
# 1. Create the skills directory in your project
mkdir -p .agents/skills/

# 2. Clone the skill you want
git clone https://github.com/anthropics/skills.git /tmp/skills

# 3. Copy the skill into your project
cp -r /tmp/skills/skills/pdf .agents/skills/

# 4. (Optional) Remove the clone
rm -rf /tmp/skills
```

### Method 2: Quick Install with npx

Some skills can be installed directly:

```bash
npx -y @anthropic/skills install pdf
```

### Method 3: Clone Full Repository

```bash
git clone https://github.com/anthropics/skills.git
# Then copy individual skills as needed
```

### Default Skill Directories

Agents scan these directories for skills:

| Agent | Default Directory |
|-------|------------------|
| **VS Code + Copilot** | `.agents/skills/` |
| **Claude Code** | `.claude/skills/` or `.agents/skills/` |
| **OpenCode** | `.agents/skills/` |
| **Gemini CLI** | `.agents/skills/` |
| **OpenClaw** | `.openclaw/workspace/skills/` |
| **Junie** | `.agents/skills/` |

### Using Skills

Once installed:

1. **Restart your agent** or reload the session
2. Ask a question related to the skill — e.g., "Extract text from this PDF"
3. The agent automatically detects the matching skill and loads its instructions
4. The agent follows the skill's steps to complete your task

To **list installed skills**, ask your agent:

- "What skills do you have?"
- "List my available skills"
- In VS Code Copilot Chat Agent mode, type `/skills`

---

## Creating Your Own Skill

Creating a skill is straightforward — one file under 20 lines.

### Quickstart: Roll Dice Skill

Create `.agents/skills/roll-dice/SKILL.md`:

```markdown
---
name: roll-dice
description: Roll dice using a random number generator. Use when asked
  to roll a die (d6, d20, etc.) or generate a random dice roll.
---

To roll a die, use the following command:

**Bash:**
```bash
echo $((RANDOM % <sides> + 1))
```

**PowerShell:**

```powershell
Get-Random -Minimum 1 -Maximum (<sides> + 1)
```

Replace `<sides>` with the number of sides on the die.

```

Then in VS Code Copilot Chat Agent mode, ask "Roll a d20" — the agent activates the skill and runs the command.

### Progressive Disclosure

When an agent starts, it reads only the `name` and `description` of each skill. The full `SKILL.md` body is loaded **only when the skill is activated** by a matching query. This allows agents to carry hundreds of skills without context window bloat.

---

## Best Practices

| Practice | Description |
|----------|-------------|
| **Start from real expertise** | Base skills on real task execution, not generic instructions |
| **Refine with real execution** | Run the skill, then iterate based on results |
| **Spend context wisely** | Add what the agent lacks, omit what it already knows |
| **Well-scoped descriptions** | Include specific keywords for accurate activation |
| **Use progressive disclosure** | Keep SKILL.md focused; use scripts/ for dense code |
| **Test and evaluate** | Run evals to measure skill performance and activation accuracy |
| **Version your skills** | Use `metadata.version` field for tracking changes |

### Description Optimization Tips

Write descriptions that help the agent decide when to activate:
- Include both what the skill does AND when to use it
- Add specific keywords that trigger on relevant prompts
- Avoid vague descriptions like "Helps with PDFs" — be specific

**Good:** "Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction."

**Poor:** "Helps with PDFs."

---

## Which Tools Support Skills

The following tools support the Agent Skills format (Source: [agentskills.io](https://agentskills.io)):

| Tool | Support | Skills Config |
|------|---------|---------------|
| **GitHub Copilot** (VS Code) | Full | `.agents/skills/` |
| **Claude Code** | Full | `.claude/skills/` or `.agents/skills/` |
| **OpenCode** | Full | `.agents/skills/` |
| **Gemini CLI** | Full | `.agents/skills/` |
| **OpenHands** | Full | `.agents/skills/` |
| **Junie** (JetBrains) | Full | `.agents/skills/` |
| **Autohand Code CLI** | Full | `.agents/skills/` |
| **OpenClaw** | Full | Via skills.sh / ClawHub |
| **Mux** | Full | `.agents/skills/` |

---

## Related

- [**Agent Skills Specification**](https://agentskills.io/specification) — The complete format reference
- [**Skill Creation Quickstart**](https://agentskills.io/skill-creation/quickstart) — Create your first skill
- [**Best Practices**](https://agentskills.io/skill-creation/best-practices) — How to write effective skills
- [**Anthropic Skills Repository**](https://github.com/anthropics/skills) — Official skills on GitHub
- [**skills.sh**](https://skills.sh) — Open registry for AI agent skills
- [**ClawHub**](https://clawhub.ai) — OpenClaw's skill marketplace
- [**AI Tools Index**](../AI-Tools/) — Full tools reference
- [**MCP**](./mcp) — Model Context Protocol
- [**AI Editors**](./ai-editors) — AI-powered editors comparison
