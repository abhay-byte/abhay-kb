# 📚 Abhay's Knowledge Base

Personal knowledge base and portfolio site — built with Jekyll, hosted on GitHub Pages.

**Live at:** [abhay-byte.github.io/abhay-kb](https://abhay-byte.github.io/abhay-kb)

---

## What's Inside

| Section | Description |
|---------|-------------|
| **About Me** | Personal background, education, journey |
| **Projects Dashboard** | Live stats for all 85+ public repos, stars, forks, languages |
| **AI Tools** | Notes on AI coding agents, MCP servers, editors, and tools I use daily |
| **LLM** | Model comparisons, coding plans, job search context |
| **Job Search** | History, salary data, applications tracking |

### Structure

```
├── index.html              # Landing page
├── about-me.md             # Bio, background, story
├── PROJECTS.md             # GitHub projects dashboard (auto-synced)
├── job-search-history.md   # Job applications timeline
├── job-salary-cache.md     # Salary benchmarks & research
├── AI-Tools/               # AI tooling references
│   ├── index.md
│   ├── ai-editors.md       # Cursor, Windsurf, etc.
│   ├── mcp.md              # MCP server notes
│   ├── skills.md           # Skills & capabilities
│   └── tools.md            # CLI agent tools
├── LLM/                    # LLM notes & comparisons
│   ├── index.md
│   ├── models.md
│   ├── coding-plans.md
│   └── jobs.md
├── assets/                 # Images, static files
├── _layouts/               # Jekyll HTML templates
├── _config.yml             # Jekyll config
├── wrap_html.sh            # Markdown → HTML rendering pipeline
└── build.sh                # Build script
```

---

## Tech Stack

- **Static Site Generator:** Jekyll (GitHub Pages)
- **Content:** Markdown → HTML (custom `md_to_html.py` pipeline)
- **Dashboard:** Auto-synced via GitHub Actions from the [abhay-byte](https://github.com/abhay-byte) profile API
- **Hosting:** GitHub Pages

---

## Development

```bash
# Serve locally with Jekyll
jekyll serve

# Build markdown → HTML manually
bash build.sh
```

---

## License

All content © [Abhay Raj](https://github.com/abhay-byte). Code and assets shared openly — no paywalls, just FOSS.
