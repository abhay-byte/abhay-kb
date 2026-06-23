---
layout: standalone
title: Coding Plans
---

# AI Coding Plans — Pricing & Usage Reference

<div style="font-size:12px;color:#666;margin-bottom:12px;">Last updated: 2026-06-21 | Auto-synced daily</div>

Compiled April 2026. All plans compared across major providers.

---

## BytePlus ModelArk [Subscribe](https://www.byteplus.com/en/activity/codingplan)

ByteDance's AI inference platform. Coding Plan = subscription with shared quota across supported tools.
Now integrates with OpenClaw and Hermes Agent as supported coding tools.

### Available Models

| Model | Type | Notes |
|-------|------|-------|
| Dola-Seed-2.0-Pro | Coding (flagship) | ByteDance's top-tier coding model. 256K context. Multimodal. Officially launched on BytePlus ModelArk May 2026 |
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

- Quota shared across: Claude Code, Cursor, Cline, Codex CLI, Kilo Code, Roo Code, OpenCode, OpenClaw, Hermes Agent
- 5-hour sliding window + weekly reset. Monday 00:00 UTC+8
- No overflow billing — depleted = wait for next cycle
- Free tier: 500K tokens for new users (regular API only, NOT Coding Plan)
- New Team plan now available for enterprise: scalability, management controls, digital employee capabilities

> **Personal Review (June 2026):** The BytePlus-provided models like Dola-Seed-2.0-Pro, O-Pro, and Ark-Coding-Pro are **significantly weaker** than alternatives available for free on other platforms — e.g. MiniMax M2.5 (80.2% SWE-Bench, free via OpenRouter) easily outperforms them. The real issue is with **frontier models like GLM-5.1**: despite being listed as available, the quota multiplier (3x drain during peak hours) means you get **only about 10–15 actual requests per 5h window**. The advertised quotas (“800 per 5h”) are based on the cheapest base models at 1x drain — not usable on any capable model. In practice, the plan is misleading for anyone wanting to use frontier models. Not recommended unless you only need the weak ByteDance models for simple completions.

---

## GitHub Copilot [Plans](https://github.com/features/copilot/plans)

Source: [docs.github.com](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing), [docs.github.com/plans](https://docs.github.com/en/copilot/get-started/plans), [github.blog](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

### Plans (Current — June 10 2026 — Usage-Based Billing LIVE)

Source: [docs.github.com](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing), [docs.github.com/billing-individuals](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals), [github.blog (May 12)](https://github.blog/news-insights/company-news/github-copilot-individual-plans-introducing-flex-allotments-in-pro-and-pro-and-a-new-max-plan/), [github.blog (Apr 27)](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/), [github.blog changelog (Jun 1)](https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/)

| Plan | Price | AI Credits (Base + Flex) | Completions | Agent/CLI | Status |
|------|-------|---------------------------|-------------|-----------|--------|
| Free | $0 | Limited AI credits (auto model) | 2,000/mo | Limited | Available |
| Student | Free (verified) | Old PRU-based (not migrated) | Unlimited | Yes | **Signups paused since Apr 20**. Not migrating to usage-based billing |
| Pro | $10/mo | 1,000 base + 500 flex = 1,500/mo | Unlimited | Yes | **New sign-ups paused**. Auto-migrated Jun 1 |
| Pro+ | $39/mo | 3,900 base + 3,100 flex = 7,000/mo | Unlimited | Yes | **New sign-ups paused**. Auto-migrated Jun 1 |
| Max (new) | $100/mo | 10,000 base + 10,000 flex = 20,000/mo | Unlimited | Yes | Available as upgrade for existing users. **New sign-ups paused**, reopening in coming weeks |
| Business | $19/seat/mo | $19 base/seat ($30 promo Jun-Aug) | Unlimited | Yes | Available |
| Enterprise | $39/seat/mo | $39 base/seat ($70 promo Jun-Aug) | Unlimited | Yes | Available |

### Key Changes (Apr–Jun 2026)

- **Usage-based billing LIVE (Jun 1):** All Copilot plans transitioned to GitHub AI Credits on June 1, 2026. PRUs replaced by token-based metering. 1 AI Credit = $0.01 USD. Code completions remain unlimited and not billed in AI Credits
- **Flex allotments (May 12):** Pro gets $10 base + $5 flex = $15/mo. Pro+ gets $39 base + $31 flex = $70/mo. Flex allotments may vary over time
- **Max plan (May 12, upgrades live Jun 1):** $100/mo with 10,000 base + 10,000 flex = 20,000 credits/mo total included usage. Available as upgrade for existing Student/Pro/Pro+ subscribers
- **Copilot code review now consumes Actions minutes** in addition to AI Credits. Default runner is standard GitHub-hosted; org admins can set default runners
- **User-level budgets** now GA for organizations and enterprises — granular spend controls with email notifications
- **Signups paused (ongoing):** Pro, Pro+, Student, and Max new sign-ups remain paused as of Jun 1. Reopening in coming weeks
- **Student plan:** Not migrating to usage-based billing. Signups remain paused. Claude Opus/Sonnet removed (Mar 14). GPT-5.3-Codex removed from manual picker (Apr 27)
- **Opus exclusive to Pro+ & Max:** Claude Opus 4.7 removed from Pro tier. Only Pro+ ($39/mo) and Max ($100/mo)
- **Code completions remain unlimited** on all paid plans — not billed in AI Credits
- **Copilot code review** consumes both AI Credits and GitHub Actions minutes
- **Claude Fable 5 marked unavailable (Jun 13):** First Mythos-class model from Anthropic, designed for long-horizon autonomous coding. GitHub Copilot docs now list Claude Fable 5 as **currently unavailable**. Previously available on Pro+, Max, Business, Enterprise. Priced at $10/$50 per 1M tokens. Likely temporary — Anthropic is restricting access while deploying safety classifiers with 30-day data retention
- **GPT-5.2 closing down (Jun 1):** GPT-5.2 marked as closing down effective June 1, 2026 on the supported models page. GPT-5.2-Codex remains GA. Users should migrate to GPT-5.3-Codex or GPT-5.4

### Per-Token Pricing (Jun 2026 — Usage-Based)

Per-token rates from [docs.github.com](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing). 1 AI credit = $0.01 USD. Over-usage billed at these rates.

**OpenAI:**

Long context pricing: GPT-5.5 and GPT-5.4 have **Long context** tiers for input > 272K tokens on Copilot.

| Model | Input /1M (≤272K) | Input /1M (>272K) | Cached Input | Output /1M (≤272K) | Output /1M (>272K) | Release Status |
|-------|------------------:|------------------:|:------------:|------------------:|-------------------:|----------------|
| GPT-5.5 | $5.00 | $10.00 | $0.50 | $30.00 | $45.00 | GA |
| GPT-5.4 | $2.50 | $5.00 | $0.25 | $15.00 | $22.50 | GA |
| GPT-5.4 mini | $0.75 | — | $0.075 | $4.50 | — | GA |
| GPT-5.4 nano | $0.20 | — | $0.02 | $1.25 | — | GA |
| GPT-5.3-Codex | $1.75 | $0.175 | $14.00 | GA |
| GPT-5.2 | $1.75 | $0.175 | $14.00 | Closing down (Jun 1) |
| GPT-5.2-Codex | $1.75 | $0.175 | $14.00 | GA |
| GPT-5 mini | $0.25 | $0.025 | $2.00 | GA |

**Anthropic (includes cache write cost):**

| Model | Input /1M | Cached Input | Cache Write | Output /1M |
|-------|----------:|:------------:|:-----------:|-----------:|
| Claude Fable 5 ★ | $10.00 | $1.00 | $12.50 | $50.00 |
| Claude Opus 4.8 | $5.00 | $0.50 | $6.25 | $25.00 |
| Claude Opus 4.7 | $5.00 | $0.50 | $6.25 | $25.00 |
| Claude Opus 4.6 | $5.00 | $0.50 | $6.25 | $25.00 |
| Claude Opus 4.5 | $5.00 | $0.50 | $6.25 | $25.00 |
| Claude Sonnet 4.6 | $3.00 | $0.30 | $3.75 | $15.00 |
| Claude Sonnet 4.5 | $3.00 | $0.30 | $3.75 | $15.00 |
| Claude Sonnet 4 | $3.00 | $0.30 | $3.75 | $15.00 |
| Claude Haiku 4.5 | $1.00 | $0.10 | $1.25 | $5.00 |

★ Claude Fable 5 — Released June 9, 2026. First Anthropic Mythos-class model. Available on Copilot Pro+, Max, Business, Enterprise. **Currently unavailable on Copilot** as of June 13 (Anthropic restricting access during rollout). Priced at $10/$50 per 1M tokens.

**Google:**

Long context pricing: Gemini 3.1 Pro has a **Long context** tier for input > 200K tokens on Copilot.

| Model | Input /1M (≤200K) | Input /1M (>200K) | Cached Input | Output /1M (≤200K) | Output /1M (>200K) | Release Status |
|-------|------------------:|------------------:|:------------:|------------------:|-------------------:|----------------|
| Gemini 3.5 Flash | $1.50 | — | $0.15 | $9.00 | — | GA |
| Gemini 3.1 Pro | $2.00 | $4.00 | $0.20 | $12.00 | $18.00 | Public preview |
| Gemini 2.5 Pro | $1.25 | — | $0.125 | $10.00 | — | GA |
| Gemini 3 Flash | $0.50 | — | $0.05 | $3.00 | — | Public preview |

**Fine-tuned (GitHub):**

| Model | Input /1M | Cached Input | Output /1M | Release Status |
|-------|----------:|:------------:|-----------:|----------------|
| Raptor mini | $0.25 | $0.025 | $2.00 | Public preview |

**Microsoft:**

| Model | Input /1M | Cached Input | Output /1M | Release Status |
|-------|----------:|:------------:|-----------:|----------------|
| MAI-Code-1-Flash | $0.75 | $0.075 | $4.50 | GA |

### Plans Summary (Jun 7, 2026 — Usage-Based Billing LIVE)

| Plan | Price | Base | Flex | Total Credits | Notes |
|------|-------|:----:|:----:|:-------------:|-------|
| Free | $0 | — | — | 2000 completions/mo + limited AI credits (auto model) |
| Pro | $10/mo | 1,000 ($10) | 500 ($5) | 1,500 ($15) | Auto-migrated Jun 1. **Upgrades paused** |
| Pro+ | $39/mo | 3,900 ($39) | 3,100 ($31) | 7,000 ($70) | Auto-migrated Jun 1. **Upgrades paused** |
| Max | $100/mo | 10,000 ($100) | 10,000 ($100) | 20,000 ($200) | Effective Jun 1. Upgrade available for existing users. **New sign-ups paused** |
| Business | $19/seat/mo | 1,900 ($19) | Promo Jun-Aug ($30) | — | $30/seat promo active Jun-Aug |
| Enterprise | $39/seat/mo | 3,900 ($39) | Promo Jun-Aug ($70) | — | $70/seat promo active Jun-Aug |

**Note:** Paid Copilot plans qualify for a **10% discount** on model costs when using auto model selection in Copilot Chat, Copilot CLI, or Copilot cloud agent.

### Individual Plan Feature Highlights (Current UI — pre-June 1)

Per [github.com/features/copilot/plans](https://github.com/features/copilot/plans) as of May 26:

| Feature | Free | Pro ($10/mo) | Pro+ ($39/mo) |
|---------|:----:|:------------:|:-------------:|
| Premium requests/mo | 50 | 300 | 1,500 |
| Agent mode (GPT-5 mini) | 50/mo | Unlimited | Unlimited |
| Inline suggestions/mo | 2,000 | Unlimited | Unlimited |
| Claude Opus models | — | — | ✔️ |
| Delegate to Codex/Claude agents | — | — | ✔️ (Preview) |
| MCP server integration | — | ✔️ | ✔️ |
| Purchase additional requests | — | $0.04/request | $0.04/request |

### Community Reviews

> **From techsifted (Apr 2026):** "Microsoft paused new signups for Copilot Pro, Pro+, and Student plans. Then they removed Opus models from the Pro tier entirely. If you'd built workflows around Opus inside GitHub Copilot at $10/month, those workflows are broken now."

> **From piunikaweb (Mar 2026):** "To manage costs, GitHub has decided to remove access to flagship Claude models such as Opus and Sonnet, on the student plan."

> **From Reddit (r/github):** Users widely criticized the student plan downgrades and Pro signup pause. Many students reported being locked out of models they relied on for coursework.

> **Personal Review (June 2026):** GitHub Copilot was the most reliable and good coding plan I used. A lot of models were available and the IDE integration was seamless. I used it on the Student plan which was fantastic initially. The bad part: they progressively removed all frontier models from the Student plan — Claude Opus/Sonnet went first, then GPT-5.3-Codex was pulled from the model picker. What started as a generous free plan for students got hollowed out over time. With usage-based billing now live (June 1), the value proposition is even more uncertain — your $10 Pro gets you 1,500 AI Credits worth $15, and heavy agent sessions will burn through that fast. The Max plan ($100/mo for 20,000 credits) is the realistic choice for heavy users. Claude Opus 4.8 is now available on Pro+/Max plans, which is a nice addition. Still a solid product for light use, but heavy users will need the $100 Max plan. New sign-ups remain paused across all paid individual plans (Pro, Pro+, Student, Max) as of June 1 — you can only upgrade if already subscribed. Copilot code review now burns both AI Credits and GitHub Actions minutes. Goldeneye model removed from the model lineup; new Microsoft MAI-Code-1-Flash model added at lightweight pricing ($0.75/$4.50 per 1M tokens).

---

## GLM / Z.ai [Subscribe](https://z.ai/subscribe)

5h sliding window + weekly cap. Pricing restructured May 2026 with higher prices and monthly billing.  
Powered by GLM-5 (Feb 2026) and GLM-5.1 (Mar 27 2026). GLM-5.1 now open to all tiers.

| Tier | Price | 5h Limit | Models Included |
|------|-------|----------|----------------|
| Lite | **$18/mo** | ~80 prompts | GLM-5.1, 5-Turbo, 4.7, 4.5-Air |
| Pro | **$72/mo** | ~400 prompts | Same models, higher quota. ~5x Lite |
| Max | **$160/mo** | ~1,600 prompts | Same models, ~4x Pro |

### Model Quota Multipliers (Critical)

| Model / Time | Multiplier | Effective Lite prompts/5h |
|-------------|-----------|--------------------------|
| GLM-5.1 / GLM-5-Turbo at peak (14-18 UTC+8) | 3x drain | ~26 |
| GLM-5.1 / GLM-5-Turbo off-peak | 2x drain | ~40 |
| GLM-5.1 / GLM-5-Turbo off-peak (promo ended Apr 30) | 1x drain | ~80 |
| GLM-5 (base) off-peak | 2x drain | ~40 |
| GLM-4.7 all times | 1x drain | ~80 |
| GLM-4.5-Air all times | 1x drain | ~80 |

- Each prompt invokes the model ~15–20 times internally
- GLM-5.1 at 44.3 tok/sec is ~6x slower than Grok 4.20
- MCP quotas: Lite 100/mo, Pro 1,000/mo, Max 4,000/mo
- **Pricing restructured May 2026**: Switched from quarterly ($27/$81/$216) to monthly ($18/$72/$160). Previously ~$10/$30/$80 equivalent, now significantly more expensive. GLM-5.1 opened to all tiers.
- Free models (no sub): GLM-4.7-Flash, GLM-4.5-Flash

---

## OpenCode Go Plan [Subscribe](https://opencode.ai/go)

OpenCode's official low-cost subscription. **$5 first month, then $10/month.**
Dollar-based limits (not request counts). Models hosted in US, EU, Singapore. Zero-retention policy.

| Window | Dollar Limit |
|--------|-------------|
| Per 5 hours | $12 |
| Per week | $30 |
| Per month | $60 |

### Available Models (14)

Source: [opencode.ai/docs/go](https://opencode.ai/docs/go/) (verified June 13, 2026)

| Model | Provider | Per 5h | Per Week | Per Month | Notes |
|-------|----------|--------|----------|-----------|-------|
| DeepSeek V4 Flash | DeepSeek | 31,650 | 79,050 | 158,150 | Cheapest, huge quota |
| MiMo-V2.5 | Xiaomi | 30,100 | 75,200 | 150,400 | V2.5 Omni-class, 1M ctx |
| Qwen3.7 Plus | Alibaba | 4,300 | 10,800 | 21,600 | Mid-tier Qwen |
| MiniMax M2.7 | MiniMax | 3,400 | 8,500 | 17,000 | 196K ctx |
| DeepSeek V4 Pro | DeepSeek | 3,450 | 8,550 | 17,150 | 80.6% SWE-Bench |
| MiMo-V2.5-Pro | Xiaomi | 3,250 | 8,150 | 16,300 | Coding focus, 1M ctx |
| Qwen3.6 Plus | Alibaba | 3,300 | 8,200 | 16,300 | 78.8% SWE-Bench |
| MiniMax M3 | MiniMax | 3,200 | 8,000 | 16,000 | Newest MiniMax model |
| Kimi K2.7 Code | Moonshot | 1,350 | 4,630 | 9,250 | 256K ctx, new coding variant |
| Kimi K2.6 | Moonshot | 1,150 | 2,880 | 5,750 | 58.6% SWE-Bench Pro |
| GLM-5 | Z.ai | 1,150 | 2,880 | 5,750 | 77.8% SWE-Bench |
| Qwen3.7 Max | Alibaba | 950 | 2,390 | 4,770 | Newest Qwen, 128K ctx |
| GLM-5.1 | Z.ai | 880 | 2,150 | 4,300 | Best reasoning. 58.4% SWE-Bench Pro |

### Go API Pricing (per 1M tokens)

| Model | Input | Output | Cached Read | Cached Write |
|-------|------:|-------:|:-----------:|:------------:|
| GLM-5.1 | $1.40 | $4.40 | $0.26 | — |
| GLM-5 | $1.00 | $3.20 | $0.20 | — |
| Kimi K2.7 Code | $0.95 | $4.00 | $0.19 | — |
| Kimi K2.6 | $0.95 | $4.00 | $0.16 | — |
| MiMo V2.5 | $0.14 | $0.28 | $0.0028 | — |
| MiMo V2.5 Pro | $1.74 | $3.48 | $0.0145 | — |
| MiniMax M3 | $0.30 | $1.20 | $0.06 | — |
| MiniMax M2.7 | $0.30 | $1.20 | $0.06 | $0.375 |
| Qwen3.7 Max | $2.50 | $7.50 | $0.50 | $3.125 |
| Qwen3.7 Plus (≤256K) | $0.40 | $1.60 | $0.04 | $0.50 |
| Qwen3.7 Plus (>256K) | $1.20 | $4.80 | $0.12 | $1.50 |
| Qwen3.6 Plus (≤256K) | $0.50 | $3.00 | $0.05 | $0.625 |
| Qwen3.6 Plus (>256K) | $2.00 | $6.00 | $0.20 | $2.50 |
| DeepSeek V4 Pro | $1.74 | $3.48 | $0.0145 | — |
| DeepSeek V4 Flash | $0.14 | $0.28 | $0.0028 | — |

### Free Model

Big Pickle (~GLM-4.6, 200K ctx): 200 requests/5h - no subscription needed.

### Community Reviews

> **From Reddit (Mar 2026):** Described as "genuinely the worst coding plan I have ever used" - 94% upvotes. Criticism centered on quantized models and aggressive rate limits on reasoning models. (r/LocalLLaMA)

> **From APIYI review:** "Getting three flagship open-source models for $10/month ... you're getting 6x the model invocation value. MiniMax M2.5 is the most cost-effective choice - it has the highest limits and the strongest coding ability."

> **From Thomas Wiegold (Apr 2026):** "MiniMax gives you a good number of requests ... up to 31,800 per month with M2.5. These aren't toy models - M2.5 scored 80.2% on SWE-Bench Verified, within spitting distance of Claude Opus 4.6's 80.8%. The catch is that reasoning-heavy models like GLM-5.1 burn through limits fast."

> **Personal Review (June 2026):** Best and cheapest coding plan available. Generous quotas on MiniMax and Xiaomi models, super fast inference. Mostly reliable with top open-weight models like GLM-5.1 and Kimi K2.6 at good limits. DeepSeek V4 Flash gets 158K requests/month - absurdly cheap. Qwen3.5 Plus has been removed from the model lineup, replaced by Qwen3.6 Plus and Qwen3.7 Max. MiniMax M2.5 has been rotated out of the model lineup — replaced by Kimi K2.7 Code as the new addition. Qwen3.7 Plus fills the mid-tier Qwen slot between Qwen3.6 Plus and Qwen3.7 Max. Strongly recommended.

### Notes

- Cancel anytime. Top-up credit if needed.
- Optional "Use balance" fallback to Zen credits after limits reached
- Models are periodically rotated as new ones are tested
- **OpenAI-compatible endpoint** (GPT/DeepSeek/Qwen-style): opencode.ai/zen/go/v1/chat/completions — used by GLM-5.1, GLM-5, Kimi K2.5, Kimi K2.6, DeepSeek V4 Pro, DeepSeek V4 Flash, MiMo-V2.5, MiMo-V2.5-Pro
- **Anthropic-compatible endpoint** (Claude-style): opencode.ai/zen/go/v1/messages — used by MiniMax M3, M2.7, M2.5, Qwen3.7 Max, Qwen3.7 Plus, Qwen3.6 Plus
- Models hosted in US, EU, and Singapore

---

## Claude Code (Anthropic) [Pricing](https://claude.com/pricing)

Terminal coding agent. All usage shared across claude.ai, Claude Code CLI, and Desktop.
Source: [claude.com/pricing](https://claude.com/pricing), [Anthropic blog](https://www.anthropic.com/news/claude-code), community instrumentation.

### Individual Plans

| Plan | Price | Multiplier | Est. Msgs/5h (Opus) | Context | CLI |
|------|-------|-----------|---------------------|---------|-----|
| Pro | $20/mo ($17/yr) | 1x (doubled) | ~45-90 | 200K (1M ext) | Yes |
| Max 5x | $100/mo | 5x (doubled) | ~225-450 | 1M | Yes |
| Max 20x | $200/mo | 20x (doubled) | ~900-1,800 | 1M | Yes |

**New: Claude Opus 4.8** — Now available on all Claude plans. Latest Opus model with improved reasoning. On GitHub Copilot Pro+/Max as of June 1.

**New: Claude Fable 5 (Mythos class)** — Released June 9, 2026. Available on all Claude surfaces (claude.ai, Claude Code CLI, Claude Cowork) through June 22 on subscription plans; billed extra after that. On GitHub Copilot Pro+/Max/Business/Enterprise. First model in Anthropic's Mythos class — designed for long-horizon autonomous coding. Requires 30-day data retention for safety classifiers.

### Team Plans

| Plan | Price | Multiplier | Weekly Cap | Min Seats |
|------|-------|-----------|------------|-----------|
| Team Standard | $25/seat/mo ($20 annual) | ~1.25x Pro (doubled) | 7-day, 1 cap | 5 |
| Team Premium | $125/seat/mo ($100 annual) | ~5x Pro | 7-day, 2 caps | 5-150 |

- Max 5x: ~$0.44/message (Opus). Max 20x: ~$0.22/message -- actual volume discount kicks in here
- Max 5x: auto-switch Opus->Sonnet at 20% limit. Max 20x: at 50%
- **Peak hours throttling removed** as of May 2026 (SpaceX Colossus 1 deal)
- Team Standard added Claude Code access late April 2026 (was Premium-only before)
- Pro had Claude Code briefly removed (Apr 2026 test on 2% of signups) then restored within hours

### API Pay-per-Token

| Model | Input /1M | Output /1M | Cache Read | Batch (50% off) |
|-------|-----------|------------|------------|-----------------|
| Fable 5 | $10.00 | $50.00 | $2.00 | TBD |
| Opus 4.8 | $5.00 | $25.00 | $0.50 | Yes |
| Opus 4.7 | $5.00 | $25.00 | $0.50 | Yes |
| Sonnet 4.6 | $3.00 | $15.00 | $0.30 | Yes |
| Haiku 4.5 | $1.00 | $5.00 | $0.10 | Yes |

### Recent Changes (May–Jun 2026)

- **Rate limits doubled** for Pro, Max, Team, and Enterprise plans (SpaceX Colossus 1 deal — 220K+ NVIDIA GPUs, 300+ MW capacity). Announced May 6 at Code with Claude event
- **Peak hours throttling removed** — same rate limits at 3 AM and 3 PM
- **Opus API rate limits raised** — higher maximums across all API tiers
- **Managed Agents launched** — Dreaming, Outcomes, multi-agent orchestration now available at claude.ai/code
- **Claude Cowork** now bundled into Pro (visual canvas-based workspace, GA since Apr 2026)

### Programmatic Usage Billing Split (Effective June 15, 2026)

Source: [buildthisnow.com](https://www.buildthisnow.com/blog/guide/mechanics/claude-billing-change-june-2026), [codersera.com](https://codersera.com/blog/anthropic-june-2026-billing-change-claude-code/)

Anthropic announced on May 13 that **effective June 15, 2026** (tomorrow), programmatic Claude Code usage will be moved onto a separate monthly credit pool billed at full API rates.

| Plan | Separate Credit Pool | What Triggers It |
|------|---------------------|------------------|
| Pro | $20/mo | Agent SDK, `claude -p`, CI pipelines |
| Max 5x | $100/mo | Agent SDK, `claude -p`, CI pipelines |
| Max 20x | $200/mo | Agent SDK, `claude -p`, CI pipelines |

**What this means:** Interactive Claude Code sessions in the terminal and IDE keep using your existing subscription limits (5-hour rolling window). But programmatic usage through the Claude Agent SDK, the `claude -p` command, and CI/CD pipelines will draw from this separate credit pool. A single Opus 4.7 review pass on a 500-line PR can consume 50,000–100,000 tokens, costing $0.25–$2.75 depending on output length at API rates.

**Impact:** Teams running Claude Code in multi-agent setups alongside Codex CLI will need to budget separately for programmatic usage after June 15. Previously, a Max 20x subscription's generous token allowance could absorb heavy programmatic usage — now that same workload costs real dollars.

### Known Issues

- **v2.1.100 bug (Apr 2026 — still ongoing):** ~20K invisible tokens added per request, burning quota ~40% faster. Root cause: broken prompt caching forcing full re-processing on every turn. Three independent bugs break Anthropic's prefix-based prompt caching (cache_creation charges instead of cache_read). Six releases shipped through v2.1.133 (May 8) with features but no public fix. Workaround: downgrade to v2.1.34 or reinstall via npm
- **Opus 4.7/4.8 tokenizer:** 4.7 tokenizer uses up to 35% more tokens for equivalent text vs Opus 4.6. Opus 4.8 may have similar behavior
- **5-hour rolling window:** Hit limit at 2pm? Wait until 7pm. Not a daily reset

### Community Reviews

> **From Reddit (r/ClaudeAI):** "The difference of Claude Pro and Max5 plan usage limit are enormous. It is not only 5x" -- users report Max 5x is a dramatically better experience for daily coding, not just numerically 5x better.

> **From dev.to review:** "Pro costs ~$0.44 per Opus message; Max 5x costs the same per message but prevents hitting rate limits sooner. Max 20x cuts per-message cost in half (~$0.22) and is the only plan offering true volume discount."

> **From findskill.ai:** "Pro $20/mo for solo devs, Max 5x $100/mo for full-time on Claude Code, Max 20x $200/mo for pair-programming all day. The v2.1.100 token inflation bug is real -- burns quotas ~40% faster."

> **From felloai review:** "Max 5x at $100/month gives five times the Pro usage and priority access during peak demand. It is the sweet spot for full-time developers who use Claude Code as their default coding partner."

> **Personal Review (June 2026):** Claude Code Pro ($20/mo) is decent for light use but the 5-hour rolling window makes it impractical for serious daily development -- you WILL hit the wall. The good news: Anthropic doubled rate limits and removed peak hours throttling (thanks to SpaceX Colossus 1), so Pro is now much more usable — ~90 Opus messages per 5h instead of 45. Max 5x ($100/mo) is still the minimum for real work, but the gap is narrower. On the plus side, code quality is unmatched -- Opus 4.7 and now Opus 4.8 are genuinely the smartest models for complex refactoring and architecture decisions. Claude Fable 5 (June 9) was exciting — Mythos-class model for long-horizon autonomous coding — but as of June 13, GitHub Copilot docs mark it as **currently unavailable**, suggesting Anthropic is restricting access during the rollout. The main frustration is Anthropic's opaque quota system and the ongoing v2.1.100 prompt caching bug (still unfixed as of June) silently eating into your limits by ~40%. Compared to OpenCode Go ($10/mo), Claude Code is still 5-10x the price for incrementally better quality. Only worth it if you need Opus-level reasoning for complex codebases.

---

## GPT Codex (OpenAI) [Pricing](https://developers.openai.com/codex/pricing)

OpenAI's agentic coding tool — CLI, IDE extension, ChatGPT app, and cloud. Codex is **bundled into ChatGPT plans** (no separate subscription).  
Source: [developers.openai.com/codex/pricing](https://developers.openai.com/codex/pricing)

### ChatGPT Plans (Codex Included)

| Plan | Price | Best For |
|------|-------|----------|
| Free | $0 | Limited Codex Mini access |
| Go | $20/mo | Budget-friendly Codex Mini (select regions). Reduced limits |
| Plus | $20/mo | Entry point for Codex CLI + IDE + cloud |
| Pro ($100) | $100/mo | 5x higher limits. Includes GPT-5.3-Codex-Spark preview |
| Pro ($200) | $200/mo | 20x higher limits. Heavy daily use |
| Business | $25/seat/mo | Team workspace + admin controls |
| API Key | Pay-per-token | CI/CD, automation, programmatic |

### Codex Usage Limits (Plus — 5-hour rolling window)

| Model | Local Msgs/5h | Cloud Tasks/5h | Code Reviews/5h |
|-------|--------------|----------------|-----------------|
| GPT-5.5 | 15-80 | — | — |
| GPT-5.4 | 20-100 | — | — |
| GPT-5.4-mini | 60-350 | — | — |
| GPT-5.3-Codex | 30-150 | 10-60 | 20-50 |

Pro tiers: 5x to 20x these limits depending on tier. **Promos expired May 31** — previous $100 2x promo and $200 25x promo both ended.

### API Pay-per-Token (Codex API)

| Model | Input /1M | Output /1M |
|-------|-----------|------------|
| GPT-5.5 | $2.50 | $10.00 |
| GPT-5.5 mini | $0.40 | $1.60 |
| GPT-5.5 nano | $0.10 | $0.40 |
| Codex (specialized) | $5.00 | $15.00 |

### Notes

- Usage shared across all Codex surfaces (CLI, IDE, ChatGPT, cloud, iOS)
- Soft caps slow you down; hard caps cut off until window resets
- Extra credits can be purchased on Plus/Pro plans
- Credits now billed per-token (API token-based rates as of Apr 2, 2026). 1 credit = varies by model
- **Pro promos expired May 31, 2026:** Pro $100 2x promo ended — back to standard 5x. Pro $200 25x promo ended — back to standard 20x. Both promos confirmed expired.
- **Go plan ($20/mo)**: Budget Codex Mini tier available in select regions. Reduced limits, same models
- **Business/Edu/Enterprise** flexible pricing: credits per token table available in settings

### Referral Program (June 11–24, 2026)

From June 11 through June 24, 2026, eligible Plus and Pro users can invite up to three friends. When an eligible recipient sends their first Codex message, both people receive a banked rate-limit reset (usable for 30 days).

### Community Reviews

> **From aitoolsrecap (2026):** "The April 16, 2026 update added computer use, memory, image generation, and 90+ plugins -- turning it from a coding assistant into a full developer workstation. Included from $20/mo on ChatGPT Plus."

> **From elite-ai-assisted-coding review:** "Codex CLI performed well throughout testing. GPT-5's capabilities were the key differentiator -- the model followed instructions precisely, learned from documentation effectively, and applied knowledge appropriately."

> **Personal Review (June 2026):** Overall positive experience. The limits are fine and good enough for daily use -- the mini models (GPT-5.4-mini) were the best thing about the plan, offering generous quotas for routine tasks. The main problem is with the frontier models (GPT-5.4 and GPT-5.5): when they understand you correctly from the start, they work really well and do exactly what's asked. But if they misinterpret the intent, things go spectacularly wrong -- they commit to wrong approaches confidently and produce deeply broken code. It's an all-or-nothing experience. The Plus plan at $20/mo is reasonable value, but Pro at $200/mo is hard to justify vs OpenCode Go or BytePlus. The 2x Pro $100 and 25x Pro $200 promos both expired May 31 — standard limits are now in effect. New referral program active June 11-24: invite up to 3 friends, both get a banked rate-limit reset.

---

## Antigravity 2.0 (Google IDE) [Download](https://antigravity.google/download) - [Pricing](https://antigravity.google/pricing)

Released **Antigravity 2.0** at **Google I/O 2026 (May 19)** — expanded from a single IDE into a five-surface platform: desktop app, CLI, SDK, Managed Agents API, and Enterprise Agent Platform.  
Includes Claude models (Sonnet & Opus) alongside Gemini — all in one IDE.  
Source: [antigravity.google/pricing](https://antigravity.google/pricing), [TechCrunch](https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool-at-io-2026/)

### Plans (Updated May 19, 2026 — Google I/O)

Source: [antigravity.google/pricing](https://antigravity.google/pricing), [TechCrunch (May 19)](https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool-at-io-2026/), [Mashable (May 19)](https://mashable.com/article/google-io-2026-gemini-ultra-ai-subscription-tiers), [techmymoney.com (May 21)](https://techmymoney.com/2026/05/21/google-ai-ultra-100-plan/)

Google restructured its AI subscription lineup at I/O 2026. The top plan was restructured into two tiers: a new **AI Ultra at $100/mo** (5x Pro limits) and **AI Ultra Premium at $200/mo** (was $250, 20x Pro limits). Both now include Antigravity access as part of the subscription. Usage is tracked by compute consumption (not message counts), refreshed every 5 hours until a weekly cap.

| Plan | Price | Models | Notes |
|------|-------|--------|-------|
| Preview (Free) | $0 | All models (rate-limited) | Access to all models. 92% quota cut since Dec 2025 |
| AI Pro | $20/mo | All models (higher limits) | Built-in credits. Multi-day lockouts reported. Now includes YouTube Premium Lite |
| AI Ultra | **$100/mo** (new) | 5x Pro limits | **New tier** launched at I/O 2026 (May 19). 5x higher limits than Pro. Includes 20TB storage + YouTube Premium + Antigravity access |
| AI Ultra Premium | **$200/mo** (was $250) | 20x Pro limits | **$50 price drop** at I/O 2026. Includes Project Genie access. Antigravity access |
| Pay-as-you-go | $25/2,500 credits | Full access | Overflow / burst usage. $0.01/credit. Opaque credit-to-token conversion |

### Antigravity 2.0 New Surfaces

| Surface | What it is |
|---------|-----------|
| Desktop App 2.0 | Updated IDE with dynamic subagents, scheduled tasks, native voice commands. Gemini 3.5 Flash co-developed using Antigravity |
| Antigravity CLI | Terminal-based agent creation (replaces Gemini CLI). Users asked to migrate from Gemini CLI |
| Antigravity SDK | Programmatic access to Google's agent harness for custom agents |
| Managed Agents (Gemini API) | API endpoints for hosted agentic workflows |
| Gemini Enterprise Agent Platform | Enterprise deployment for Google Cloud customers |

### Available Models

| Model | Provider | Type | Notes |
|-------|----------|------|-------|
| Gemini 3.5 Flash | Google | Fast | Co-developed using Antigravity. GA since I/O 2026 |
| Gemini 3.1 Pro | Google | Reasoning (High/Low) | Google's flagship. **Good for frontend work only** |
| Gemini 3 Flash | Google | Fast | Very capable for frontend. Reliable |
| Claude Opus 4.8 | Anthropic | Premium | **$200/mo value, available here**. Best for backend |
| Claude Opus 4.7 | Anthropic | Premium | Available here alongside Opus 4.8 |
| Claude Sonnet 4.6 | Anthropic | Mid-tier | Fast, reliable for backend code |
| GPT-OSS 120B | OpenAI | Open-weight | Free model |

### Usage Tips

- Use **Claude models for backend** work — they handle complex logic, refactoring, and architecture
- Use **Gemini models for frontend** — Gemini 3 Flash / 3.5 Flash in particular are excellent for UI work
- **Never use Gemini for backend** or complex logic tasks — it performs poorly
- Limits are **separate per provider** — running out on Claude? Switch to Gemini and keep working
- Multi-agent missions can assign different models to different agents within the same task
- **New in 2.0:** Dynamic subagents can parallelize work across microservices. Native voice commands. Scheduled tasks. Antigravity export tool to AI Studio. Five surfaces: Desktop App, CLI, SDK, Managed Agents API, Enterprise Agent Platform

### Known Issues

- **Quota cuts:** Free tier quotas cut 92% since Dec 2025 (250 -> 20 requests/day)
- **Pro lockouts:** Multiple reports of 7-day lockouts even with low usage. Advertised 5-hour refresh unreliable
- **Credit system opaque:** Credit-to-token conversion rate undisclosed. Per-model credit costs unknown
- **Ultra lockouts:** Even $200-$250/mo Ultra users report unexpected quota restrictions since Mar 2026

### Community Reviews

> **From aitoolanalysis (Mar 2026):** "The most promising and most frustrating editor I've ever used." Free tier gives access to Claude Opus 4.6 ($200/mo value) for $0. But the rate limit crisis is real -- Pro subscribers hit 7-day lockouts instead of 5-hour refresh.

> **From vibecoding.app:** "One developer documented a single Claude Opus 4.6 session consuming 635 out of 1,000 credits. One or two complex coding sessions can trigger a lockout for the rest of the week."

> **From claude-world.com:** "Google Antigravity users reported multi-day account lockouts, a 92% free-tier quota cut, and pricing that pushes developers toward a $250/month plan."

> **From TechCrunch (May 19):** "Google is also reducing the price of its top AI Ultra plan from $250 to $200, which allows for 20x higher limits." Antigravity 2.0 adds CLI, SDK, subagents, scheduled tasks, and voice commands.

> **Personal Review (June 2026):** I've used it extensively. The best thing is having Claude models (Sonnet, Opus 4.7 & 4.8) alongside Gemini in one IDE -- I use Claude for backend and Gemini for frontend, each with separate limits. Gemini 3.5 Flash (co-developed using Antigravity) is genuinely capable for frontend work. The downside: limits remain terrible — 92% free tier quota cut, multi-day lockouts reported even on paid plans. The new $100 AI Ultra tier at I/O 2026 is a welcome addition and the $200 Ultra Premium price cut ($50 off) helps, but the rate limit issues persist. Worth trying the free tier for the multi-model access, but don't rely on it for daily production work. The 5-hour compute window (replacing daily caps) is a structural change that aligns with Anthropic's and OpenAI's approach.

---

## Xiaomi MiMo Token Plan [Subscribe](https://platform.xiaomimimo.com/token-plan)

Launched Apr 2 2026. Pure monthly credit pool — NO 5h windows, NO weekly limits.  
Credits expire month-end, no rollover. Mid-month upgrades OK, downgrades not.  
Now supports V2.5 model series — one subscription unlocks all 8 MiMo models.  
Auto-renewal discounts: up to $144 off annual plans.

**Updated May 26/27, 2026**: Credits quotas upgraded 5-8x across all tiers with no price increase. Old credits refunded within validity window. API pricing permanently reduced. Now standard.

| Plan | Price | Credits/Mo (Old) | Credits/Mo (New, May 26) | ~Tasks/mo (V2.5 1:1) |
|------|-------|-----------------|--------------------------|----------------------|
| Lite | $6/mo (¥39) | 60,000,000 | **300,000,000** | ~600 |
| Standard | $16/mo (¥99) | 200,000,000 | **1,600,000,000** | ~3,200 |
| Pro | $50/mo (¥329) | 700,000,000 | **5,600,000,000** | ~11,200 |
| Max | $100/mo (¥659) | 1,600,000,000 | **8,000,000,000** | ~16,000 |

### Credit Multiplier by Model

| Model | Context | Rate |
|-------|---------|------|
| MiMo-V2-Omni | up to 256K | 1 token = 1 Credit |
| MiMo-V2-Pro | up to 256K | 1 token = 2 Credits |
| MiMo-V2-Pro | 256K–1M | 1 token = 4 Credits |
| MiMo-V2.5 | up to 256K | 1 token = ~1 Credit (Omni-class) |
| MiMo-V2.5-Pro | up to 256K | 1 token = ~2 Credits |
| MiMo-V2-TTS | n/a | Free (limited time) |

### API Pay-per-Token (Permanent rates since May 27, 2026)

| Model | Input /1M | Output /1M | Cached /1M | Context |
|-------|----------:|-----------:|-----------:|---------|
| MiMo V2.5 Pro | **$1.00** | **$3.00** | $0.20 | 1M tokens |
| MiMo V2 Flash | ~$0.10 | ~$0.40 | $0.02 | 256K tokens |

- **Permanent price reduction** — not promotional. Old long-context multiplier (256K+) eliminated
- Down from ~$50/MTok effective for long-context to flat $1/$3
- API old rate for V2.5: $0.4/$2.00 per 1M (≤256K). New flat rate with no surcharge for longer context
- Token Plan quotas increased 5-8x (now standard), existing credits refunded within validity period
- **V2 series models (MiMo-V2-Omni, MiMo-V2-Pro) slated for deprecation** — V2.5 models are the current focus

---

## Kimi / Moonshot AI [Kimi Code](https://www.kimi.com/code)

Two products: Kimi membership (app quotas) and Kimi Code (developer).  
API billed separately — NOT included in membership.

Current model: **K2.6** (released Apr 18–21 2026).  
K2.5 predecessor: 1T params, 32B active, MoE, 384 experts, 256K ctx, MIT license.  
**K2 (original) discontinued** — stopped serving **May 25, 2026**. Migrated to K2.5 or K2.6.

### K2.6 Improvements

| Capability | K2.5 | K2.6 |
|-----------|------|------|
| SWE-Bench Pro | — | 58.6% |
| Multilingual | — | 76.7% |
| BrowseComp | 78.4% | 83.2% |
| Parallel sub-agents | 100 | 300 |
| Long-horizon | Hours | 4,000+ tool calls, 12+ hr |

### API Pricing (K2.6)

| | Input (Cache Miss) | Input (Cache Hit) | Output |
|-|-------------------|-------------------|--------|
| Per 1M tokens | $0.95 | $0.16 | $4.00 |

Context window: 262,144 tokens.

### Membership Plans (Kimi App + Kimi Code)

| Tier | Price (annual/mo) | Agent Usage/mo | Concurrent Tasks | Kimi Code Credits | Agent Swarm |
|------|------------------|----------------|-----------------|-------------------|-------------|
| Adagio | Free | 6 | 1 task | — | — |
| Moderato | $15/mo | 60 | 2 tasks | 1× credits | — |
| Allegretto | $31/mo | 150 | 2 tasks | 5× credits | 50 uses included |
| Allegro | $79/mo | 360 | 4 tasks | 15× credits | 120 uses included |
| Vivace | $159/mo | 720 | 4 tasks | 30× credits | 240 uses included |

### Additional Membership Features

| Feature | Adagio | Moderato | Allegretto | Allegro | Vivace |
|---------|--------|----------|------------|---------|--------|
| Kimi Claw | — | — | ✔️ | ✔️ | ✔️ |
| Deploy Website w/ DB | — | ✔️ | ✔️ | ✔️ | ✔️ |
| Professional Data Requests | 200 | 2,000 | 5,000 | 12,000 | 24,000 |
| Priority Queue | — | 4× speed | 4× speed | 4× speed | 4× speed |
| Concurrent Subagents | — | — | 4 | 4 | 8 |
| Group Chat w/ Claw | — | — | 10 chats | 10 chats | 10 chats |

Kimi Code available via: `curl -L code.kimi.com/install.sh | bash`. Powered by Kimi K2.6.

Day-0 support on: vLLM, OpenRouter, Cloudflare, Baseten, MLX, Hermes, OpenCode.

