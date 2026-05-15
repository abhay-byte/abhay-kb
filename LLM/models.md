---
layout: standalone
title: Models Reference
---

# Models Reference

API pricing, context windows, and SWE-Bench scores for coding AI models.  
Compiled April 2026.

---

## Anthropic (Claude)

| Model | Input /1M | Output /1M | Batch | Cache Read |
|-------|-----------|------------|-------|------------|
| Opus 4.6 | $5.00 | $25.00 | 50% off | up to 90% off |
| Sonnet 4.6 | $3.00 | $15.00 | 50% off | up to 90% off |
| Haiku 4.5 | $0.25 | $1.25 | 50% off | up to 90% off |

---

## GLM / Z.ai

| Model | Type | Context | SWE-Bench | Input /1M | Output /1M | Notes |
|-------|------|---------|-----------|-----------|------------|-------|
| GLM-5.1 | Flagship agentic | 202K | 68.7 CyberGym | $1.40 | $4.40 | MIT, 754B params |
| GLM-5-Turbo | Fast inference | 202K | — | $1.20 | $4.00 | Proprietary |
| GLM-5 | Base flagship | 202K | 77.8% Verified | $1.00 | $3.20 | MIT, 744B/40B MoE |
| GLM-5-Code | Coding variant | 202K | — | $1.20 | $5.00 | Higher quality coding |
| GLM-4.7 | Reliable daily | 128K | ~65% | ~$0.50 | ~$1.50 | 1x quota always |
| GLM-4.5-Air | Lightweight | 128K | — | $0.15 | $0.45 | Haiku-equivalent |
| GLM-4.7-Flash | Free tier | 203K | — | Free | Free | No subscription needed |

GLM-5: 744B params, 40B active MoE, 28.5T token pretraining, 202K context.  
GLM-5.1: 754B params, 28% improvement over GLM-5, 8-hour autonomous runs, 1,700 agentic steps.

---

## Xiaomi MiMo

| Model | Context | Rate | Input /1M | Output /1M |
|-------|---------|------|-----------|------------|
| MiMo-V2-Omni | up to 256K | 1 token = 1 Credit | $0.40 | $2.00 |
| MiMo-V2-Pro | up to 256K | 1 token = 2 Credits | $1.00 | $3.00 |
| MiMo-V2-Pro | 256K–1M | 1 token = 4 Credits | $2.00 | $6.00 |
| MiMo-V2-Flash | — | — | $0.09 | $0.29 |

---

## Kimi / Moonshot AI (K2.6)

| Spec | K2.5 | K2.6 (Current) |
|------|------|----------------|
| Released | Jan 27 2026 | Apr 18–21 2026 |
| Params | 1T, 32B active MoE | 1T, 32B active MoE |
| Experts | 384 | 384 |
| Context | 256K | 256K |
| SWE-Bench Verified | 76.8% | — |
| SWE-Bench Pro | — | 58.6% |
| Multilingual | — | 76.7% |
| BrowseComp | 78.4% | 83.2% |
| Parallel sub-agents | 100 | 300 |
| Long-horizon | — | 4,000+ calls, 12+ hr |
| License | MIT | MIT |

---

## OpenCode Go (estimates via subscription)

| Model | Per 5h | Per Week | Per Month |
|-------|--------|----------|-----------|
| GLM-5.1 | 880 | 2,150 | 4,300 |
| GLM-5 | 1,150 | 2,880 | 5,750 |
| Kimi K2.5 | 1,850 | 4,630 | 9,250 |
| MiMo-V2-Pro | 1,290 | 3,225 | 6,450 |
| MiMo-V2-Omni | 2,150 | 5,450 | 10,900 |
| Qwen3.6 Plus | 3,300 | 8,200 | 16,300 |
| MiniMax M2.7 | 3,400 | 8,500 | 17,000 |
| MiniMax M2.5 | 6,300 | 15,900 | 31,800 |
| Qwen3.5 Plus | 10,200 | 25,200 | 50,500 |

MiniMax M2.5: 80.2% SWE-Bench — near Claude Opus 4.6 (80.8%).

---

## Notes

- **BytePlus ModelArk**: Quota shared across Claude Code, Cursor, Cline, Codex CLI, Kilo Code, Roo Code, OpenCode
- **GitHub Copilot**: Premium requests shared across all features; extra $0.04 each on Pro/Pro+
- **Claude Code**: Exact request counts not published — only relative multipliers
- **GLM quota multipliers**: Peak hours drain 3x quota; off-peak 2x; GLM-4.7/4.5-Air always 1x
- **MiMo**: Pure credit pool, no 5h/windows, credits expire month-end
- **Kimi**: API billed separately — not included in membership
