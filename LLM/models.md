---
layout: standalone
title: Models Reference
---

# Models Reference

API pricing, context windows, and SWE-Bench scores for coding AI models.  
Compiled April 2026.

> **Common Benchmark:** [SWE-Bench Verified](https://www.swebench.com/) measures a model's ability to resolve real GitHub issues from code repositories.  
> Not all providers publish scores — only models with verified data are plotted below.  
> Lower price + higher score = better value. DeepSeek V4 Flash leads on value; Claude Opus 4.6 and GPT-5.4 lead on absolute performance.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 480" style="max-width:100%;height:auto;background:#0d0d0d;border-radius:8px;font-family:-apple-system,system-ui,sans-serif;">
<defs>
  <filter id="glow">
    <feDropShadow dx="0" dy="0" stdDeviation="2" flood-color="rgba(250,189,47,0.3)"/>
  </filter>
</defs>

<!-- Title -->
<text x="360.0" y="28" text-anchor="middle" fill="#fff" font-size="16" font-weight="700">SWE-Bench Verified vs. Input Price (per 1M tokens)</text>
<text x="360.0" y="44" text-anchor="middle" fill="#666" font-size="11">Lower price + higher score = best value · Only models with published scores shown</text>

<!-- Grid + axes -->
<g stroke="rgba(255,255,255,0.06)" stroke-width="1">
  <line x1="70" y1="350.0" x2="680" y2="350.0"/>
  <text x="62" y="354.0" text-anchor="end" fill="#666" font-size="11">60%</text>
  <line x1="70" y1="290.0" x2="680" y2="290.0"/>
  <text x="62" y="294.0" text-anchor="end" fill="#666" font-size="11">65%</text>
  <line x1="70" y1="230.0" x2="680" y2="230.0"/>
  <text x="62" y="234.0" text-anchor="end" fill="#666" font-size="11">70%</text>
  <line x1="70" y1="170.0" x2="680" y2="170.0"/>
  <text x="62" y="174.0" text-anchor="end" fill="#666" font-size="11">75%</text>
  <line x1="70" y1="110.0" x2="680" y2="110.0"/>
  <text x="62" y="114.0" text-anchor="end" fill="#666" font-size="11">80%</text>
  <line x1="70" y1="50.0" x2="680" y2="50.0"/>
  <text x="62" y="54.0" text-anchor="end" fill="#666" font-size="11">85%</text>
<text x="18" y="230" text-anchor="middle" fill="#888" font-size="12" transform="rotate(-90,18,230)">SWE-Bench Verified</text>
  <line x1="206.51448673872375" y1="50" x2="206.51448673872375" y2="410"/>
  <text x="206.51448673872375" y="428" text-anchor="middle" fill="#666" font-size="10">$0.25</text>
  <line x1="309.7837093739804" y1="50" x2="309.7837093739804" y2="410"/>
  <text x="309.7837093739804" y="428" text-anchor="middle" fill="#666" font-size="10">$0.50</text>
  <line x1="413.05293200923705" y1="50" x2="413.05293200923705" y2="410"/>
  <text x="413.05293200923705" y="428" text-anchor="middle" fill="#666" font-size="10">$1</text>
  <line x1="516.3221546444938" y1="50" x2="516.3221546444938" y2="410"/>
  <text x="516.3221546444938" y="428" text-anchor="middle" fill="#666" font-size="10">$2</text>
  <line x1="619.5913772797504" y1="50" x2="619.5913772797504" y2="410"/>
  <text x="619.5913772797504" y="428" text-anchor="middle" fill="#666" font-size="10">$4</text>
<text x="375" y="472" text-anchor="middle" fill="#888" font-size="12">Input Price per 1M tokens (log₂ scale)</text>
<rect x="70" y="50" width="610" height="360" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
</g>
<circle cx="120.12965108816996" cy="98.0" r="6" fill="#4ea8de" stroke="#0d0d0d" stroke-width="2" filter="url(#glow)"/>
<text x="120.12965108816996" y="84.0" text-anchor="middle" fill="#ccc" font-size="10" font-weight="500">DeepSeek V4 Flash</text>
<circle cx="130.40862272024955" cy="107.59999999999997" r="6" fill="#7b2d8e" stroke="#0d0d0d" stroke-width="2" filter="url(#glow)"/>
<text x="130.40862272024955" y="93.59999999999997" text-anchor="middle" fill="#ccc" font-size="10" font-weight="500">MiniMax M2.5</text>
<circle cx="245.60308783054555" cy="124.40000000000003" r="6" fill="#f4a261" stroke="#0d0d0d" stroke-width="2" filter="url(#glow)"/>
<text x="245.60308783054555" y="110.40000000000003" text-anchor="middle" fill="#ccc" font-size="10" font-weight="500">Qwen3.6 Plus</text>
<circle cx="276.5384452705133" cy="148.40000000000003" r="6" fill="#2a9d8f" stroke="#0d0d0d" stroke-width="2" filter="url(#glow)"/>
<text x="276.5384452705133" y="166.40000000000003" text-anchor="middle" fill="#ccc" font-size="10" font-weight="500">Kimi K2.5</text>
<circle cx="336.9470679907629" cy="290.0" r="6" fill="#e76f51" stroke="#0d0d0d" stroke-width="2" filter="url(#glow)"/>
<text x="336.9470679907629" y="308.0" text-anchor="middle" fill="#ccc" font-size="10" font-weight="500">GLM-4.7</text>
<circle cx="413.05293200923705" cy="136.40000000000003" r="6" fill="#264653" stroke="#0d0d0d" stroke-width="2" filter="url(#glow)"/>
<text x="413.05293200923705" y="110.40000000000003" text-anchor="middle" fill="#ccc" font-size="10" font-weight="500">GLM-5</text>
<circle cx="549.5674187479608" cy="110.0" r="6" fill="#10a040" stroke="#0d0d0d" stroke-width="2" filter="url(#glow)"/>
<text x="549.5674187479608" y="96.0" text-anchor="middle" fill="#ccc" font-size="10" font-weight="500">GPT-5.4</text>
<circle cx="652.8366413832174" cy="100.40000000000003" r="6" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#glow)"/>
<text x="652.8366413832174" y="86.40000000000003" text-anchor="middle" fill="#ccc" font-size="10" font-weight="500">Claude Opus 4.6</text>
<text x="138.12965108816996" y="94.0" fill="#4ea8de" font-size="9" font-style="italic">← Best value</text>
</svg>


---



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

Current as of May 2026. Source: [platform.minimax.io](https://platform.minimax.io/docs/pricing/overview), [OpenRouter](https://openrouter.ai/minimax/minimax-m2.7)

### Coding Models

| Model | Input /1M | Output /1M | Context | Max Output | SWE-Bench | Speed |
|-------|-----------|------------|---------|-----------|-----------|-------|
| M2.7 | $0.279 | $1.20 | 196K | 131K | — | Released Mar 18 2026 |
| M2.5 Standard | $0.15 | $1.20 | 256K | — | 80.2% | ~50 TPS |
| M2.5 Lightning | $0.30 | $2.40 | 256K | — | 80.2% | ~100 TPS |

M2.5 Standard: One of the best value coding models. Automatic cache (no config needed). Near Claude Opus 4.6 (80.8%).
OpenCode Go estimates: M2.5 ~6,300 req/5h, M2.7 ~3,400 req/5h.

### Subscription Plans

| Plan | Price | Description |
|------|-------|-------------|
| Token Plan | Subscription | Quotas for individual builders and Teams |
| Credits | Prepaid | Same resource coverage as Token Plan |
| Pay-as-you-go | Per-token | Standard API endpoint billing |

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

Current as of May 2026. Source: [docs.z.ai](https://docs.z.ai/guides/overview/pricing)

### Flagship Models (GLM-5 Series)

| Model | Context | SWE-Bench | Input /1M | Output /1M | Cached Input | License |
|-------|---------|-----------|-----------|------------|-------------|---------|
| GLM-5.1 | 202K | Pro 58.4% (best-in-class) | $1.40 | $4.40 | $0.26 | MIT, 754B params |
| GLM-5 | 202K | Verified 77.8% | $1.00 | $3.20 | $0.20 | MIT, 744B/40B MoE |
| GLM-5-Turbo | 202K | — | $1.20 | $4.00 | $0.24 | Proprietary |

GLM-5.1 (Apr 7 2026): 8-hour autonomous runs, 1,700 agentic steps. Surpasses GPT-5.4 and Claude Opus 4.6 on SWE-Bench Pro.
GLM-5: 744B params, 40B active MoE, 28.5T token pretraining.

### Previous Gen (GLM-4 Series)

| Model | Context | Input /1M | Output /1M | Cached Input | Notes |
|-------|---------|-----------|------------|-------------|-------|
| GLM-4.7 | 128K | $0.60 | $2.20 | $0.11 | Reliable daily driver |
| GLM-4.7-FlashX | 203K | $0.07 | $0.40 | $0.01 | Fast inference variant |
| GLM-4.6 | 128K | $0.60 | $2.20 | $0.11 | Previous generation |
| GLM-4.5-X | 128K | $2.20 | $8.90 | $0.45 | Premium tier |
| GLM-4.5 | 128K | $0.60 | $2.20 | $0.11 | Standard tier |
| GLM-4.5-Air | 128K | $0.20 | $1.10 | $0.03 | Lightweight, Haiku-class |
| GLM-4.5-AirX | 128K | $1.10 | $4.50 | $0.22 | Fast Air variant |
| GLM-4-32B-0414-128K | 128K | $0.10 | $0.10 | — | Budget open-weight |

### Free Models

| Model | Context | Input | Output |
|-------|---------|-------|--------|
| GLM-4.7-Flash | 203K | Free | Free |
| GLM-4.5-Flash | — | Free | Free |

### Vision Models

| Model | Input /1M | Output /1M | Cached Input |
|-------|-----------|------------|-------------|
| GLM-5V-Turbo | $1.20 | $4.00 | $0.24 |
| GLM-4.6V | $0.30 | $0.90 | $0.05 |
| GLM-4.6V-FlashX | $0.04 | $0.40 | $0.004 |
| GLM-4.6V-Flash | Free | Free | Free |

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
