---
layout: standalone
title: KB Schema — Structure & Conventions
---

# KB Schema — abhay-kb

> **Purpose:** Defines how this knowledge base is structured, what conventions to follow, and workflows for maintaining it.
> **Architecture:** 3-Tier (Source of Truth → Wiki → Schema) — see [LLM-WIKI.md](/.openclaw/workspace/LLM-WIKI.md)
> **Last Updated:** 2026-06-01

---

## 1. Directory Structure

```
/repos/abhay-kb/
├── _config.yml              # Jekyll config (GitHub Pages)
├── _layouts/                # Jekyll layouts
│   └── standalone.html
│
├── index.html               # Landing page
├── README.md                # Repo readme
│
├── about-me.md              # Personal bio, origin, education
├── resume.md                # Resume/CV
├── projects.md / PROJECTS.md  # GitHub projects dashboard
├── jobs.md                  # Active job listings
├── job-search-history.md    # Job search tracking
├── job-salary-cache.md      # Salary data cache
│
├── AGENTS.md                # Agent workspace instructions
├── IDENTITY.md              # Agent identity
├── MEMORY.md                # Agent memory
├── HEARTBEAT.md             # Agent heartbeat tasks
├── SOUL.md                  # Agent persona
├── TOOLS.md                 # Agent local notes
├── USER.md                  # About Abhay
├── SCHEMA.md                # ← THIS FILE — KB structure schema
├── .gitignore               # Git ignore rules
├── .clawhub/                # ClawHub skill registry
│   └── lock.json
├── wrap_html.sh             # HTML wrapping script
├── tailored_resume_juspay.docx  # Tailored resume (Juspay)
├── tailored_resume_juspay.json  # Tailored resume JSON
│
├── LLM/                     # LLM knowledge section
│   ├── index.md             # LLM section index
│   ├── models.md            # API pricing, benchmarks, context windows
│   └── coding-plans.md      # Coding plan subscriptions comparison
│
├── dsa/                     # DSA (Data Structures & Algorithms)
│   ├── index.md / index.html   # DSA section index
│   ├── questions.json       # All DSA questions categorized
│   ├── tracker.json         # Progress tracker
│   ├── lectures/            # Lecture notes (lecture-01.md to lecture-12.md)
│   ├── lectures.md / lectures.html
│   ├── scripts/             # Automation scripts (daily.sh, weekly.sh, monthly.sh)
│   ├── codeforces.md        # Codeforces progress
│   ├── leetcode.md          # LeetCode progress
│   ├── neetcode.md          # NeetCode 150 progress
│   ├── cp31.md              # CP-31 sheet progress
│   └── cses.md, a2oj.md, vervecopilot.md, etc.
│
├── blogs-news/              # Dev news & blog articles
│   ├── index.md             # News index (chronological)
│   ├── _news-tracker.json   # News deduplication tracker
│   └── news/                # Individual article pages
│       ├── [slug].md        # Most articles (flat file)
│       ├── [slug]/index.md  # Some articles (subdirectory style)
│       └── ...
│
├── discord/                 # Discord MCP server documentation
│   └── BRAINBOT_INSTRUCTIONS.md
│
├── AI-Tools/                # AI/CLI tool references
│   ├── index.md / index.html    # Section index
│   ├── ai-editors.md / .html    # AI editor comparisons
│   ├── mcp.md / .html           # MCP server references
│   ├── skills.md / .html        # Skills references
│   └── tools.md / .html         # Tool references
│
├── skills/                  # Installed skill files
│   └── agentmail/            # AgentMail skill (SKILL.md, scripts/)
│
├── software-engineering/    # Software engineering notes
│   ├── index.md
│   ├── deployment.md
│   ├── maintenance.md
│   ├── sdlc.md
│   └── testing.md
│
├── system-design/           # System design notes
│   ├── index.md
│   ├── clean-code.md
│   ├── design.md
│   └── patterns.md
│
├── memory/                  # Chronological memory entries
│   ├── YYYY-MM-DD.md        # Daily notes
│   ├── YYYY-MM-DD-HHMM.md   # Timestamped entries
│   └── .dreams/             # Agent dream/sleep state (internal)
│
├── assets/                  # Images, attachments
├── build.sh                 # Build script
└── md_to_html.py            # Markdown to HTML converter
```

## 2. Page Conventions

### Front Matter

Every standalone page MUST have YAML front matter:

```yaml
---
layout: standalone     # Jekyll layout
title: "Page Title"    # Page title
---
```

Optional front matter for news/articles:

```yaml
layout: standalone
title: "Article Title"
date: YYYY-MM-DD
source: "Source Name"
source_url: "https://..."
category: "dev-news"
image: "https://..."
```

### File Naming

- `kebab-case.md` — all lowercase, hyphens between words
- News article slugs: lowercase, hyphens only, max 60 chars, strip special chars
- Memory entries: `YYYY-MM-DD.md` or `YYYY-MM-DD-HHMM.md`

### Markdown Style

- ATX headings (`#`, `##`, `###` — no `=` or `-` underlines)
- Tables for structured data (pricing, comparisons, listings)
- Links use `[text](./relative-path)` format
- External links: `[text](https://...)`
- Code blocks with language tags: ` ```python`, ` ```bash`
- Images: `![alt](path)` with relative paths in assets/

## 3. Content Categories

| Category | Path | Maintainer | Update Frequency |
|----------|------|------------|-----------------|
| Personal info | `about-me.md`, `resume.md` | Brain (LLM) | Weekly |
| Projects | `PROJECTS.md` | Brain (LLM) | Daily (cron 7AM IST) |
| Jobs | `jobs.md`, `job-search-history.md` | Brain (LLM) | Daily (cron 6:30AM IST) |
| LLM models | `LLM/models.md` | Brain (LLM) | Daily (cron 6AM IST) |
| Coding plans | `LLM/coding-plans.md` | Brain (LLM) | Daily (cron 6AM IST) |
| DSA tracking | `dsa/*` | Brain (LLM) | Daily (cron 6PM IST) |
| Dev news | `blogs-news/*` | Brain (LLM) | Daily (cron 5AM IST) |
| Software Eng | `software-engineering/*` | Brain (LLM) | As needed |
| System Design | `system-design/*` | Brain (LLM) | As needed |
| AI Tools refs | `AI-Tools/*` | Brain (LLM) | As needed |
| Memory | `memory/*` | Brain (LLM) | As needed |
| Agent config | `AGENTS.md`, `IDENTITY.md`, `SOUL.md`, etc. | Brain (LLM) | As needed |

## 4. Ingestion Workflow

When adding NEW content to the KB:

1. **Read the source** — fetch/read the raw material
2. **Create/update page** — write a well-structured markdown page in the appropriate directory
3. **Update index** — add link + summary to the relevant `index.md`
4. **Cross-reference** — link to related pages, update relevant sections
5. **Update tracker** — for news: add URL to `_news-tracker.json`
6. **Commit** — `git add` only the changed files, commit with descriptive message

## 5. Query Workflow

When answering questions from the KB:

1. **Search index files** first — check `LLM/index.md`, `blogs-news/index.md`, `dsa/index.md`
2. **Read relevant pages** — drill into specific pages
3. **Synthesize answer** — combine info from multiple sources
4. **Cite sources** — link to KB pages or external URLs
5. **(Optional) File good answers back** — if the answer reveals new useful knowledge, save it as a new page

## 6. Git Conventions

- **NEVER** use `git add .` or `git add -A`
- **ALWAYS** add only the specific files changed: `git add path/to/file.md`
- **ALWAYS** verify before commit: `git diff --cached --name-only`
- Commit messages: descriptive, prefixed by category
  - `news: add digest for YYYY-MM-DD`
  - `llm: update models pricing`
  - `dsa: update daily progress`
  - `resume: sync KB page`
  - `projects: daily sync`
- Always `git pull --rebase origin main` before `git push`

## 7. Cron Workflows

| Cron Job | Time (IST) | Action |
|----------|-----------|--------|
| News fetch | 5:00 AM | Fetch dev news, build KB pages, email digest |
| Models sync | 6:00 AM | Update LLM pricing/benchmarks |
| Coding plans sync | 6:00 AM | Update coding plan pricing/quotas |
| Job search | 6:30 AM | Fetch fresher jobs, update jobs.md, email |
| Projects sync | 7:00 AM | GitHub API → PROJECTS.md |
| Resume sync | 9:00 AM | Update resume.tex + resume.md |
| Retry failed | 10:00 AM | Re-run any failed cron jobs |
| DSA daily | 6:00 PM | Send DSA + LeetCode + Codeforces questions |
| DSA weekly | Sunday 9:00 AM | Weekly progress summary email (DSA + LC + CF) |
| DSA monthly | 1st 10:00 AM | Monthly progress report email |
| System status | Every hour | Report CPU/RAM/battery to Discord |

## 8. External Repos (Interacted with by the KB)

| Repo | Path | Purpose |
|------|------|---------|
| my-resume | `/repos/my-resume` | Resume LaTeX files (resume.tex, resume-juspay.tex, resume-apple-ase.tex) — synced daily by cron |
| DSA | `/.openclaw/workspace/repos/DSA` | DSA content repo (separate from KB's dsa/ tracking) |
| DSA_Practice | `/.openclaw/workspace/repos/DSA_Practice` | DSA practice solutions |

DSA automation scripts live at `/.openclaw/workspace/dsa/scripts/` (daily.sh, weekly.sh, monthly.sh, complete.sh) and operate on the dsa/ tracker within the KB.

## 9. Tools & Integration

- **AgentMail** — `ab-brain-bot@agentmail.to` for sending emails (news digest, job search, DSA reports)
- **GitHub CLI** — `gh` for API queries and git operations
- **Git** — version control for all KB content
- **OpenClaw cron** — scheduled job execution
- **Discord MCP** — server management tools (Java/Spring Boot on port 8085)

## 10. Schema Evolution

This SCHEMA.md is a living document. It should be updated when:

- New sections/categories are added to the KB
- Conventions change
- New workflows are established
- Cron jobs are added/removed

---

*This file is Layer 3 of the 3-tier architecture. It tells the LLM how to maintain the KB.*
