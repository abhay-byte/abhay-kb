---
layout: standalone
title: Coding Plans
---

# AI Coding Plans — Pricing & Usage Reference

Compiled April 2026. All plans compared across major providers.

---

## BytePlus ModelArk

ByteDance's AI inference platform. Coding Plan = subscription with shared quota across supported tools.

### Available Models

| Model | Type | Notes |
|-------|------|-------|
| Dola-Seed-2.0-Pro | Coding (flagship) | ByteDance's top-tier coding model |
| Dola-Seed-2.0-Lite | Coding (budget) | Cheaper, good for routine tasks |
| Ark-Coding-Pro | Coding | BytePlus proprietary coding model |
| O-Pro | Coding | BytePlus proprietary |
| ByteDance-Seed-Code | Coding | Code-specific optimization |
| GLM-5.1 | Frontier (Z.ai) | 754B MoE, SWE-Bench Pro 58.4%. **Quota drain: ~3x** |
| GLM-4.7 | General (Z.ai) | Reliable daily driver. 1x quota |
| Kimi-K2.5 | Frontier (Moonshot) | 1T MoE, 256K ctx. **Quota drain: ~2x** |
| DeepSeek-V3.2 | General | 73.0% SWE-Bench Verified |
| GPT-OSS-120B | Open-weight | 117B params, Apache 2.0 |

### Quotas

| Plan | Price | Per 5h | Per Week | Per Month |
|------|-------|--------|----------|-----------|
| Lite | ~$10/mo | ~800 | ~3,200 | ~24,000 |
| Pro | ~$40/mo | ~4,000 | ~16,000 | ~120,000 |

- Quota shared across: Claude Code, Cursor, Cline, Codex CLI, Kilo Code, Roo Code, OpenCode
- 5-hour sliding window + weekly reset. Monday 00:00 UTC+8
- No overflow billing — depleted = wait for next cycle
- Free tier: 500K tokens for new users (regular API only, NOT Coding Plan)

> **Personal Review (May 2026):** The BytePlus-provided models like Dola-Seed-2.0-Pro, O-Pro, and Ark-Coding-Pro are **significantly weaker** than alternatives available for free on other platforms — e.g. MiniMax M2.5 (80.2% SWE-Bench, free via OpenRouter) easily outperforms them. The real issue is with **frontier models like GLM-5.1**: despite being listed as available, the quota multiplier (3x drain during peak hours) means you get **only about 10–15 actual requests per 5h window**. The advertised quotas (“800 per 5h”) are based on the cheapest base models at 1x drain — not usable on any capable model. In practice, the plan is misleading for anyone wanting to use frontier models. Not recommended unless you only need the weak ByteDance models for simple completions.

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

## OpenCode Go Plan

OpenCode's official low-cost subscription. **$5 first month, then $10/month.**
Dollar-based limits (not request counts). Models hosted in US, EU, Singapore. Zero-retention policy.

| Window | Dollar Limit |
|--------|-------------|
| Per 5 hours | $12 |
| Per week | $30 |
| Per month | $60 |

### Available Models (12)

Source: [opencode.ai/docs/go](https://opencode.ai/docs/go/)

| Model | Provider | Per 5h | Per Week | Per Month | Notes |
|-------|----------|--------|----------|-----------|-------|
| DeepSeek V4 Flash | DeepSeek | 31,650 | 79,050 | 158,150 | Cheapest, huge quota |
| Qwen3.5 Plus | Alibaba | 10,200 | 25,200 | 50,500 | Best raw request count |
| MiniMax M2.5 | MiniMax | 6,300 | 15,900 | 31,800 | 80.2% SWE-Bench |
| MiniMax M2.7 | MiniMax | 3,400 | 8,500 | 17,000 | Newer, 196K ctx |
| Qwen3.6 Plus | Alibaba | 3,300 | 8,200 | 16,300 | 78.8% SWE-Bench |
| DeepSeek V4 Pro | DeepSeek | 3,450 | 8,550 | 17,150 | 80.6% SWE-Bench |
| MiMo-V2.5-Omni | Xiaomi | 2,150 | 5,450 | 10,900 | Multimodal |
| MiMo-V2.5-Pro | Xiaomi | 1,290 | 3,225 | 6,450 | Coding focus |
| Kimi K2.5 | Moonshot | 1,850 | 4,630 | 9,250 | 256K ctx |
| Kimi K2.6 | Moonshot | 1,150 | 2,880 | 5,750 | Updated K2.5 |
| GLM-5 | Z.ai | 1,150 | 2,880 | 5,750 | 77.8% SWE-Bench |
| GLM-5.1 | Z.ai | 880 | 2,150 | 4,300 | Best reasoning. 58.4% SWE-Bench Pro |

### Free Model

Big Pickle (~GLM-4.6, 200K ctx): 200 requests/5h - no subscription needed.

### Community Reviews

> **From Reddit (Mar 2026):** Described as "genuinely the worst coding plan I have ever used" - 94% upvotes. Criticism centered on quantized models and aggressive rate limits on reasoning models. (r/LocalLLaMA)

> **From APIYI review:** "Getting three flagship open-source models for $10/month ... you're getting 6x the model invocation value. MiniMax M2.5 is the most cost-effective choice - it has the highest limits and the strongest coding ability."

> **From Thomas Wiegold (Apr 2026):** "MiniMax gives you a good number of requests ... up to 31,800 per month with M2.5. These aren't toy models - M2.5 scored 80.2% on SWE-Bench Verified, within spitting distance of Claude Opus 4.6's 80.8%. The catch is that reasoning-heavy models like GLM-5.1 burn through limits fast."

> **Personal Review (May 2026):** Best and cheapest coding plan available. Generous quotas on MiniMax and Qwen models, super fast inference. Mostly reliable with top open-weight models like GLM-5.1 and Kimi K2.6 at good limits. MiniMax M2.5 at $10/month is unmatched value. DeepSeek V4 Flash gets 158K requests/month - absurdly cheap. Strongly recommended.

### Notes

- API endpoint: opencode.ai/zen/go/v1/
- Cancel anytime. Top-up credit if needed.
- Optional "Use balance" fallback to Zen credits after limits reached
- Models are periodically rotated as new ones are tested

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
