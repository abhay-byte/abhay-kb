---
layout: standalone
title: Models Reference
---

# Models Reference

API pricing, context windows, and SWE-Bench scores for coding AI models.  
Compiled April 2026.

---

## Anthropic (Claude)

Current as of May 2026. Source: [platform.claude.com](https://platform.claude.com/docs/en/about-claude/pricing)

| Model | Input /1M | Output /1M | Batch (50% off) | Cache Writes (5m) | Cache Hits |
|-------|-----------|------------|-----------------|-------------------|------------|
| Opus 4.7 | $5.00 | $25.00 | ✓ | $6.25/MTok | $0.50/MTok |
| Opus 4.6 | $5.00 | $25.00 | ✓ | $6.25/MTok | $0.50/MTok |
| Sonnet 4.6 | $3.00 | $15.00 | ✓ | $3.75/MTok | $0.30/MTok |
| Haiku 4.5 | $1.00 | $5.00 | ✓ | $1.25/MTok | $0.10/MTok |

Opus 4.7 uses a new tokenizer — may use up to 35% more tokens for the same text.

---

## DeepSeek

Current as of May 2026. Source: [api-docs.deepseek.com](https://api-docs.deepseek.com/quick_start/pricing/)

DeepSeek V4 is the current flagship, launched March 2026. 671B total params, 37B active MoE, 1M context.
SWE-Bench Verified: 81%. V4 Flash is the default workhorse; V4 Pro is premium (75% off until May 31 2026).

| Model | Cache Hit Input /1M | Cache Miss Input /1M | Output /1M | Context | Notes |
|-------|--------------------|---------------------|-----------|---------|-------|
| deepseek-v4-flash | $0.0028 | $0.14 | $0.28 | 1M | Default route. 384K max output |
| deepseek-v4-pro (promo) | $0.003625 | $0.435 | $0.87 | 1M | 75% off until May 31 2026 15:59 UTC |
| deepseek-v4-pro (full) | $0.0145 | $1.74 | $3.48 | 1M | Full price after promo ends |

Cache hit prices reduced to 1/10 of launch price from Apr 26 2026.
Older aliases `deepseek-chat` and `deepseek-reasoner` map to V4 Flash (non-thinking / thinking) and retire after Jul 24 2026.
New accounts get 5M free tokens.

### Legacy Models

| Model | Input /1M | Output /1M | Cache Hit | Context | Notes |
|-------|-----------|------------|-----------|---------|-------|
| DeepSeek V3.2 (Chat) | $0.28 | $0.42 | $0.028 | 128K | Previous gen, still available |
| DeepSeek R1 | $0.55 | $2.19 | $0.14 | 128K | Dedicated reasoning model |

DeepSeek V3.2: 69% SWE-Bench Verified. R1: chain-of-thought reasoning, ~96% cheaper than OpenAI o1.
DeepSeek web chat at chat.deepseek.com is free for individual users.

---
## OpenAI (ChatGPT)

Current as of May 2026. Source: [openai.com/api/pricing](https://openai.com/api/pricing/)

### GPT-5 Family (Current Flagship)

| Model | Input /1M | Output /1M | Cached Input | Context | Notes |
|-------|-----------|------------|-------------|---------|-------|
| GPT-5.5 | $5.00 | $30.00 | $0.50 | 1M | Flagship reasoning + coding. Highest benchmark scores |
| GPT-5.5 Pro | $30.00 | $180.00 | — | 1M | Premium tier for research-grade problems |
| GPT-5.4 | $2.50 | $15.00 | $0.25 | 1M | Strong all-rounder, superseded by 5.5 |
| GPT-5.4 Mini | $0.75 | $4.50 | $0.075 | 400K | Affordable reasoning. Supports reasoning effort control |
| GPT-5.4 Nano | $0.20 | $1.25 | — | 400K | Fastest, cheapest 5.4 tier. Ideal for summaries, classification |
| GPT-5.3 Codex | $1.75 | $14.00 | — | 400K | Coding specialist. Superseded by GPT-5.5 |

### GPT-4.1 Family (Production Workhorse)

| Model | Input /1M | Output /1M | Cached Input | Context | Notes |
|-------|-----------|------------|-------------|---------|-------|
| GPT-4.1 | $2.00 | $8.00 | $0.50 | 1M | Recommended production model. Strong coding + long context |
| GPT-4.1 Mini | $0.40 | $1.60 | $0.10 | 1M | Good balance of power and affordability |
| GPT-4.1 Nano | $0.10 | $1.40 | — | 1M | Cheapest OpenAI model. Classification, extraction, routing |

### o-Series (Reasoning Models)

| Model | Input /1M | Output /1M | Cached Input | Context | Notes |
|-------|-----------|------------|-------------|---------|-------|
| o4-mini | $1.10 | $4.40 | $0.275 | 200K | Best-value reasoning. Math, science, complex logic |
| o3 | $2.00 | $8.00 | — | — | Flagship reasoning. Chain-of-thought built in |

Batch API saves 50% on all models. Prompt caching discounts: up to 90% off (GPT-5.5), 75% off (GPT-4.1).
GPT-5.4 scores ~80% SWE-Bench Verified. GPT-4.1 is OpenAI's recommended production default for most workloads.

---

## MiniMax

| Model | Input /1M | Output /1M | Context | SWE-Bench | Notes |
|-------|-----------|------------|---------|-----------|-------|
| M2.7 | $0.279 | $1.20 | 196K | — | Released Mar 18 2026. 131K max output |
| M2.5 Standard | $0.15 | $1.20 | 256K | 80.2% | ~50 TPS. Automatic caching. Near Claude Opus 4.6 |
| M2.5 Lightning | $0.30 | $2.40 | 256K | 80.2% | ~100 TPS. Same quality, 2x speed |

M2.5 Standard at $0.15/$1.20 is one of the best value coding models. Automatic cache support (no config needed).
OpenCode Go subscription estimates: M2.5 ~6,300 req/5h, M2.7 ~3,400 req/5h.

---

## Qwen (Alibaba)

Current as of May 2026. Source: [DashScope direct pricing](https://www.alibabacloud.com/help/en/model-studio/model-pricing)

### Current Gen (Qwen3.6)

| Model | Input /1M | Output /1M | Context | SWE-Bench | Notes |
|-------|-----------|------------|---------|-----------|-------|
| Qwen3.6 Plus | $0.325 | $1.95 | 1M | 78.8% Verified | Apr 2 2026. Hybrid attention + MoE. Reasoning by default |
| Qwen3.6 Flash | $0.25 | $1.50 | 1M | — | Cost-optimized tier |
| Qwen3.6 Max Preview | $0.861 | $3.441 | 252K | — | Top reasoning tier (preview) |

Qwen3.6 Plus: within 2 points of Claude Opus 4.6 (80.8%) at 1/30th the input price. 1M native context, 65K max output. Reasoning enabled by default (no mode toggle).

### Previous Gen (Qwen3.5)

| Model | Input /1M | Output /1M | Context | Notes |
|-------|-----------|------------|---------|-------|
| Qwen3.5 Plus | $0.26 | $1.56 | 1M | Feb 2026 release. 65K max output |
| Qwen3.5 397B A17B | Free | Free | 262K | Open-weight MoE flagship |

### Qwen-Max (Legacy Flagship)

| Model | Input /1M | Output /1M | Context |
|-------|-----------|------------|---------|
| qwen3-max (0-32K) | $1.20 | $6.00 | 252K |
| qwen3-max (32K-128K) | $2.40 | $12.00 | 252K |
| qwen3-max (128K-252K) | $3.00 | $15.00 | 252K |
| qwen-max (older) | $1.60 | $6.40 | — |

All Qwen models support native tool-calling, JSON-mode, and OpenAI-compatible API shapes. Batch calling: 50% off. Context caching discounts available on supported models.

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

Current as of May 2026. Launched Mar 18 2026. Source: [mimo-v2.com](https://www.mimo-v2.com/docs/pricing)

| Model | Input /1M | Output /1M | Context | Modalities | Notes |
|-------|-----------|------------|---------|------------|-------|
| MiMo-V2-Pro (≤256K) | $1.00 | $3.00 | 1M | Text | 1T params, 42B active. Top 3 Claw-Eval |
| MiMo-V2-Pro (256K–1M) | $2.00 | $6.00 | 1M | Text | Long-context tier |
| MiMo-V2-Omni | ~$1.00 | ~$3.00 | 256K | Text, Image, Audio, Video | Multimodal flagship |
| MiMo-V2-Flash | $0.10 | $0.30 | 256K | Text | Open-source foundation model |
| MiMo-V2-TTS | Free | Free | — | Audio | Limited time promo |

API at platform.xiaomimimo.com. OpenAI-compatible. Credit plans available: Lite $6/mo, Standard $16/mo, Pro $50/mo, Max $100/mo.

---

## Kimi / Moonshot AI (K2.6)

Current as of May 2026. Source: [kimi.com](https://www.kimi.com/resources/kimi-k2-6-pricing), [OpenRouter](https://openrouter.ai/moonshotai/kimi-k2.5)

Both models: 1T params, 32B active MoE, 384 experts, MIT license.

| Model | Cache Hit /1M | Cache Miss /1M | Output /1M | Context | SWE-Bench |
|-------|--------------|----------------|-----------|---------|-----------|
| kimi-k2.6 | $0.16 | $0.95 | $4.00 | 262K | Pro 58.6%, BrowseComp 83.2% |
| kimi-k2.5 | — | $0.40 | $1.90 | 256K | Verified 76.8%, BrowseComp 78.4% |

K2.6: 300 parallel sub-agents, 4,000+ tool calls, 12+ hr continuous execution.
K2.5: 100 parallel sub-agents.

### Membership Plans

| Plan | Price/mo | Agent Usage |
|------|----------|-------------|
| Adagio | Free | 6 |
| Moderato | $15 | 60 |
| Allegretto | $31 | 150 |
| Allegro | $79 | 360 |
| Vivace | $159 | 720 |

---

## OpenCode Go

Source: [docs.openclaw.ai](https://docs.openclaw.ai/providers/opencode-go). Dollar-value limits ($12/5h, $30/week, $60/month).

### Available Models

| Model Ref | Name |
|-----------|------|
| opencode-go/glm-5 | GLM-5 |
| opencode-go/glm-5.1 | GLM-5.1 |
| opencode-go/kimi-k2.5 | Kimi K2.5 |
| opencode-go/kimi-k2.6 | Kimi K2.6 (3x limits) |
| opencode-go/deepseek-v4-pro | DeepSeek V4 Pro |
| opencode-go/deepseek-v4-flash | DeepSeek V4 Flash |
| opencode-go/mimo-v2-omni | MiMo V2 Omni |
| opencode-go/mimo-v2-pro | MiMo V2 Pro |
| opencode-go/minimax-m2.5 | MiniMax M2.5 |
| opencode-go/minimax-m2.7 | MiniMax M2.7 |
| opencode-go/qwen3.5-plus | Qwen3.5 Plus |
| opencode-go/qwen3.6-plus | Qwen3.6 Plus |

### Request Estimates (Apr 17 2026)

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
