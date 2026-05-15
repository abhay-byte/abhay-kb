---
layout: standalone
title: Coding Plans
---

# AI Coding Plans — Pricing & Usage Reference

Compiled April 2026. All plans compared across major providers.

---

## BytePlus ModelArk

Subscription for frontier models (Claude etc.) via BytePlus infrastructure.  
**Quotas = request counts.** 5-hour sliding window + weekly reset.  
Intro discount suspended Mar 17 2026.

| Plan | Price | Per 5h | Per Week | Per Month |
|------|-------|--------|----------|-----------|
| Lite | ~$10/mo | ~80 | ~320 | ~24,000 |
| Pro | ~$40/mo | ~400 | ~1,600 | ~120,000 |

- Quota shared across: Claude Code, Cursor, Cline, Codex CLI, Kilo Code, Roo Code, OpenCode
- No overflow billing — depleted = wait for next cycle
- Weekly resets every Monday 00:00 UTC+8

---

## GitHub Copilot

Monthly reset only — no 5h or weekly windows. Extra requests: $0.04 each on Pro/Pro+.

| Plan | Price | Premium Req/mo | Completions | Agent | CLI | Review |
|------|-------|---------------|-------------|-------|-----|--------|
| Free | $0 | 50 | 2,000/mo | No | No | No |
| Pro | $10/mo ($100/yr) | 300 | Unlimited | Yes | Yes | Yes |
| Pro+ | $39/mo ($390/yr) | 1,500 | Unlimited | Yes | Yes | Yes+Spark |

Students, teachers, and OSS maintainers get Pro free.

---

## GLM / Z.ai

5h sliding window + weekly cap. Overseas price raised Apr 12 2026.  
Powered by GLM-5 (Feb 2026) and GLM-5.1 (Mar 27 2026).

| Plan | Domestic | Overseas | Per 5h | Per Week | Monthly Cap |
|------|----------|----------|--------|----------|-------------|
| Lite | ¥49/mo | $18/mo | ~80 prompts | ~320 | None published |
| Pro | ¥149/mo | $72/mo | ~400 prompts | ~2,000 | None published |
| Max | ¥469/mo | $160/mo | ~1,600 prompts | ~6,400 | None published |

### Model Quota Multipliers (Critical)

| Model / Time | Multiplier | Effective Lite prompts/5h |
|-------------|-----------|--------------------------|
| GLM-5.1 / GLM-5-Turbo at peak (14-18 UTC+8) | 3x drain | ~26 |
| GLM-5.1 / GLM-5-Turbo off-peak | 2x drain | ~40 |
| GLM-5.1 / GLM-5-Turbo off-peak (promo to Apr 30) | 1x drain | ~80 |
| GLM-5 (base) off-peak | 2x drain | ~40 |
| GLM-4.7 all times | 1x drain | ~80 |
| GLM-4.5-Air all times | 1x drain | ~80 |

- Each prompt invokes the model ~15–20 times internally
- GLM-5.1 at 44.3 tok/sec is ~6x slower than Grok 4.20
- MCP quotas: Lite 100/mo, Pro 1,000/mo, Max 4,000/mo
- Q2 2026 quarterly discounts available
- Free models (no sub): GLM-4.7-Flash, GLM-4.5-Flash

---

## OpenCode Go Plan (Beta)

Dollar-value limits (not request counts). Three windows: 5h + weekly + monthly.

| Window | Dollar Limit |
|--------|-------------|
| Per 5 hours | $12 |
| Per week | $30 |
| Per month | $60 |

First month $5, then $10/month. API: opencode.ai/zen/go/v1/. Zero-retention.

Fallback: free models or Zen balance when limits are hit.

---

## Claude Code (Anthropic)

Terminal coding agent. Exact request counts NOT published — only relative multipliers.  
All usage shared across claude.ai, Claude Code CLI, and Desktop.

### Individual Plans

| Plan | Price | Multiplier | Est. Req/5h | Context | CLI |
|------|-------|-----------|-------------|---------|-----|
| Pro | $20/mo ($17/yr) | 1x | ~10–40 | 200K (1M ext) | Yes |
| Max 5x | $100/mo | 5x | ~50–200 | 1M | Yes |
| Max 20x | $200/mo | 20x | ~200–800 | 1M | Yes |

### Team Plans

| Plan | Price | Multiplier | Weekly Cap | Min Seats |
|------|-------|-----------|------------|-----------|
| Team Standard | $25/seat/mo (annual) | 1.25x Pro | 7-day, 1 cap | 5 |
| Team Premium | $100/seat/mo (annual) | 6.25x Pro | 7-day, 2 caps | 5–150 |

- Max 5x: auto-switch Opus→Sonnet at 20% limit. Max 20x: at 50%.
- Team Premium (6.25x) is higher per-session than Max 5x (5x)
- Peak hours 5–11 AM PT: tighter limits
- Less than 5% of subscribers hit weekly cap
- Bug Apr 2026 v2.1.100: ~20K invisible tokens/request, burned 40% faster (fixed later)

---

## Xiaomi MiMo Token Plan

Launched Apr 2 2026. Pure monthly credit pool — NO 5h windows, NO weekly limits.  
Credits expire month-end, no rollover. Mid-month upgrades OK, downgrades not.

| Plan | Price | Credits/Mo | ~Tasks/mo (Omni 1:1) |
|------|-------|-----------|----------------------|
| Lite | $6/mo (¥39) | 60,000,000 | ~120 |
| Standard | $16/mo (¥99) | 200,000,000 | ~400 |
| Pro | $50/mo (¥329) | 700,000,000 | ~1,400 |
| Max | $100/mo (¥659) | 1,600,000,000 | ~3,200 |

### Credit Multiplier by Model

| Model | Context | Rate |
|-------|---------|------|
| MiMo-V2-Omni | up to 256K | 1 token = 1 Credit |
| MiMo-V2-Pro | up to 256K | 1 token = 2 Credits |
| MiMo-V2-Pro | 256K–1M | 1 token = 4 Credits |
| MiMo-V2-TTS | n/a | Free (limited time) |

API rates: Pro $1/$3 per 1M (256K), $2/$6 (1M ctx). 88% off first purchase.

---

## Kimi / Moonshot AI

Two products: Kimi membership (app quotas) and Kimi Code (developer).  
API billed separately — NOT included in membership.

Current model: **K2.6** (released Apr 18–21 2026).  
K2.5 predecessor: 1T params, 32B active, MoE, 384 experts, 256K ctx, MIT license.

### K2.6 Improvements

| Capability | K2.5 | K2.6 |
|-----------|------|------|
| SWE-Bench Pro | — | 58.6% |
| Multilingual | — | 76.7% |
| BrowseComp | 78.4% | 83.2% |
| Parallel sub-agents | 100 | 300 |
| Long-horizon | Hours | 4,000+ tool calls, 12+ hr |

Day-0 support on: vLLM, OpenRouter, Cloudflare, Baseten, MLX, Hermes, OpenCode.
