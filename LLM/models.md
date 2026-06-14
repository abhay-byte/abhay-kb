---
layout: standalone
title: Models Reference
---

# Models Reference

<div style="font-size:12px;color:#666;margin-bottom:12px;">Last updated: 2026-06-14 | Auto-synced daily</div>

API pricing, context windows, and SWE-Bench scores for coding AI models.  
Compiled June 2026.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 550" style="max-width:100%;height:auto;background:#0d0d0d;border-radius:8px;font-family:-apple-system,system-ui,sans-serif;">
<defs>
  <filter id="g"><feDropShadow dx="0" dy="0" stdDeviation="2" flood-color="rgba(250,189,47,0.3)"/></filter>
</defs>

<text x="400.0" y="28" text-anchor="middle" fill="#fff" font-size="17" font-weight="700">SWE-Bench Verified vs Input Price (June 2026)</text>
<text x="400.0" y="46" text-anchor="middle" fill="#666" font-size="11">Source: marc0.dev leaderboard · Updated June 14 2026</text>

<g stroke="rgba(255,255,255,0.07)" stroke-width="1">
  <line x1="75" y1="413.9189" x2="750" y2="413.9189"/>
  <text x="65" y="417.9189" text-anchor="end" fill="#555" font-size="11">70%</text>
  <line x1="75" y1="357.8379" x2="750" y2="357.8379"/>
  <text x="65" y="361.8379" text-anchor="end" fill="#555" font-size="11">75%</text>
  <line x1="75" y1="301.7569" x2="750" y2="301.7569"/>
  <text x="65" y="305.7569" text-anchor="end" fill="#555" font-size="11">80%</text>
  <line x1="75" y1="245.6759" x2="750" y2="245.6759"/>
  <text x="65" y="249.6759" text-anchor="end" fill="#555" font-size="11">85%</text>
  <line x1="75" y1="189.5949" x2="750" y2="189.5949"/>
  <text x="65" y="193.5949" text-anchor="end" fill="#555" font-size="11">90%</text>
  <line x1="75" y1="133.51389999999998" x2="750" y2="133.51389999999998"/>
  <text x="65" y="137.51389999999998" text-anchor="end" fill="#555" font-size="11">95%</text>
  <line x1="75" y1="77.43290000000002" x2="750" y2="77.43290000000002"/>
  <text x="65" y="81.43290000000002" text-anchor="end" fill="#555" font-size="11">100%</text>
  <line x1="100" y1="55" x2="100" y2="470"/>
  <text x="100" y="488" text-anchor="middle" fill="#555" font-size="10">0.25</text>
  <line x1="200" y1="55" x2="200" y2="470"/>
  <text x="200" y="488" text-anchor="middle" fill="#555" font-size="10">0.5</text>
  <line x1="300" y1="55" x2="300" y2="470"/>
  <text x="300" y="488" text-anchor="middle" fill="#555" font-size="10">1</text>
  <line x1="400" y1="55" x2="400" y2="470"/>
  <text x="400" y="488" text-anchor="middle" fill="#555" font-size="10">2</text>
  <line x1="500" y1="55" x2="500" y2="470"/>
  <text x="500" y="488" text-anchor="middle" fill="#555" font-size="10">4</text>
  <line x1="600" y1="55" x2="600" y2="470"/>
  <text x="600" y="488" text-anchor="middle" fill="#555" font-size="10">8</text>
  <line x1="700" y1="55" x2="700" y2="470"/>
  <text x="700" y="488" text-anchor="middle" fill="#555" font-size="10">16</text>
<rect x="75" y="55" width="675" height="415" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
<text x="18" y="262" text-anchor="middle" fill="#888" font-size="12" transform="rotate(-90,18,262)">SWE-Bench Verified</text>
<text x="412" y="540" text-anchor="middle" fill="#888" font-size="12">Input Price per 1M tokens (log₂ scale)</text>
</g>
<rect x="70" y="485" width="12" height="12" rx="2" fill="#10a040"/>
<text x="86" y="496" fill="#999" font-size="10">OpenAI</text>
<rect x="170" y="485" width="12" height="12" rx="2" fill="#d62828"/>
<text x="186" y="496" fill="#999" font-size="10">Anthropic</text>
<rect x="300" y="485" width="12" height="12" rx="2" fill="#4285f4"/>
<text x="316" y="496" fill="#999" font-size="10">Google</text>
<rect x="400" y="485" width="12" height="12" rx="2" fill="#4ea8de"/>
<text x="416" y="496" fill="#999" font-size="10">DeepSeek</text>
<rect x="520" y="485" width="12" height="12" rx="2" fill="#888"/>
<text x="536" y="496" fill="#999" font-size="10">Others</text>
<circle cx="16.349737226217883" cy="312.97281081081087" r="5.5" fill="#4ea8de" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="16.349737226217883" y="330.97281081081087" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">DeepSeek V4 Flash</text>
<circle cx="26.303332465650556" cy="299.5133513513513" r="5.5" fill="#7b2d8e" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="26.303332465650556" y="285.5133513513513" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">MiniMax M2.5</text>
<circle cx="116.35001737041418" cy="380.27010810810816" r="5.5" fill="#48c774" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="116.35001737041418" y="398.27010810810816" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">DeepSeek V3.2</text>
<circle cx="137.8513667021127" cy="315.2160540540541" r="5.5" fill="#f4a261" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="137.8513667021127" y="333.2160540540541" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Qwen3.6 Plus</text>
<circle cx="167.80747880807795" cy="337.64848648648655" r="5.5" fill="#2a9d8f" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="167.80747880807795" y="355.64848648648655" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Kimi K2.5</text>
<circle cx="226.3038927540432" cy="371.29713513513514" r="5.5" fill="#e76f51" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="226.3038927540432" y="389.29713513513514" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">GLM-4.7</text>
<circle cx="292.60057975208673" cy="299.5133513513513" r="5.5" fill="#e9c46a" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="292.60057975208673" y="285.5133513513513" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Kimi K2.6</text>
<circle cx="300.00065862729787" cy="326.4322702702704" r="5.5" fill="#264653" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="300.00065862729787" y="344.4322702702704" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">GLM-5</text>
<circle cx="300.00065862729787" cy="324.189027027027" r="5.5" fill="#00b4d8" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="300.00065862729787" y="342.189027027027" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">MiMo-V2-Pro</text>
<circle cx="379.9096130943694" cy="295.02686486486493" r="5.5" fill="#4ea8de" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="379.9096130943694" y="281.02686486486493" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">DeepSeek V4 Pro</text>
<circle cx="400.0009387714943" cy="295.02686486486493" r="5.5" fill="#4285f4" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="400.0009387714943" y="281.02686486486493" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Gemini 3.1 Pro</text>
<circle cx="458.49735271745953" cy="306.2430810810811" r="5.5" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="458.49735271745953" y="324.2430810810811" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Claude Sonnet 4.6</text>
<circle cx="432.19383844651793" cy="301.75659459459473" r="5.5" fill="#10a040" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="432.19383844651793" y="287.75659459459473" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">GPT-5.4</text>
<circle cx="532.1941185907142" cy="291.67551351351347" r="5.5" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="532.1941185907142" y="277.67551351351347" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Claude Opus 4.5</text>
<circle cx="532.1941185907142" cy="292.7836216216217" r="5.5" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="532.1941185907142" y="278.7836216216217" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Claude Opus 4.6</text>
<circle cx="532.1941185907142" cy="216.51335135135147" r="7" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="532.1941185907142" y="197.51335135135147" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Claude Opus 4.7</text>
<circle cx="532.1941185907142" cy="204.17551351351347" r="7" fill="#10a040" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="532.1941185907142" y="195.17551351351347" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">GPT-5.5</text>
<circle cx="632.1928094887362" cy="127.9058" r="7" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="632.1928094887362" y="113.9058" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Claude Mythos 5</text>
<circle cx="632.1928094887362" cy="133.51389999999998" r="7" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="632.1928094887362" y="119.51389999999998" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Claude Fable 5</text>
<circle cx="532.1928094887362" cy="205.29758000000007" r="7" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="532.1928094887362" y="191.29758000000007" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Claude Opus 4.8</text>
<circle cx="432.1928094887362" cy="297.27041999999994" r="5.5" fill="#f4a261" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="432.1928094887362" y="283.27041999999994" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Qwen 3.7 Max</text>
<circle cx="226.30344058337937" cy="296.1488" r="5.5" fill="#7b2d8e" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="226.30344058337937" y="282.1488" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">MiniMax M3</text>
</svg>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 480" style="max-width:100%;height:auto;background:#0d0d0d;border-radius:8px;font-family:-apple-system,system-ui,sans-serif;">
<defs>
  <filter id="g"><feDropShadow dx="0" dy="0" stdDeviation="2" flood-color="rgba(250,189,47,0.3)"/></filter>
</defs>

<text x="360.0" y="28" text-anchor="middle" fill="#fff" font-size="16" font-weight="700">SWE-Bench Pro vs Input Price (June 2026)</text>
<text x="360.0" y="44" text-anchor="middle" fill="#666" font-size="11">Harder benchmark — tests multi-language, multi-step repo tasks · Source: marc0.dev + Scale SEAL · Updated June 14 2026</text>

<g stroke="rgba(255,255,255,0.07)" stroke-width="1">
  <line x1="75" y1="400" x2="670" y2="400"/>
  <text x="65" y="404" text-anchor="end" fill="#555" font-size="11">50%</text>
  <line x1="75" y1="342.5" x2="670" y2="342.5"/>
  <text x="65" y="346.5" text-anchor="end" fill="#555" font-size="11">55%</text>
  <line x1="75" y1="285" x2="670" y2="285"/>
  <text x="65" y="289" text-anchor="end" fill="#555" font-size="11">60%</text>
  <line x1="75" y1="227.5" x2="670" y2="227.5"/>
  <text x="65" y="231.5" text-anchor="end" fill="#555" font-size="11">65%</text>
  <line x1="75" y1="170" x2="670" y2="170"/>
  <text x="65" y="174" text-anchor="end" fill="#555" font-size="11">70%</text>
  <line x1="75" y1="112.5" x2="670" y2="112.5"/>
  <text x="65" y="116.5" text-anchor="end" fill="#555" font-size="11">75%</text>
  <line x1="75" y1="55" x2="670" y2="55"/>
  <text x="65" y="59" text-anchor="end" fill="#555" font-size="11">80%</text>
  <line x1="75" y1="-2.5" x2="670" y2="-2.5"/>
  <text x="65" y="1.5" text-anchor="end" fill="#555" font-size="11">85%</text>
  <line x1="100" y1="55" x2="100" y2="400"/>
  <text x="100" y="418" text-anchor="middle" fill="#555" font-size="10">0.25</text>
  <line x1="200" y1="55" x2="200" y2="400"/>
  <text x="200" y="418" text-anchor="middle" fill="#555" font-size="10">0.5</text>
  <line x1="300" y1="55" x2="300" y2="400"/>
  <text x="300" y="418" text-anchor="middle" fill="#555" font-size="10">1</text>
  <line x1="400" y1="55" x2="400" y2="400"/>
  <text x="400" y="418" text-anchor="middle" fill="#555" font-size="10">2</text>
  <line x1="500" y1="55" x2="500" y2="400"/>
  <text x="500" y="418" text-anchor="middle" fill="#555" font-size="10">4</text>
  <line x1="600" y1="55" x2="600" y2="400"/>
  <text x="600" y="418" text-anchor="middle" fill="#555" font-size="10">8</text>
  <line x1="700" y1="55" x2="700" y2="400"/>
  <text x="700" y="418" text-anchor="middle" fill="#555" font-size="10">16</text>
<rect x="75" y="55" width="595" height="345" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
<text x="18" y="227" text-anchor="middle" fill="#888" font-size="12" transform="rotate(-90,18,227)">SWE-Bench Pro</text>
<text x="372" y="470" text-anchor="middle" fill="#888" font-size="12">Input Price per 1M tokens (log₂ scale)</text>
</g>
<rect x="70" y="415" width="12" height="12" rx="2" fill="#10a040"/>
<text x="86" y="426" fill="#999" font-size="10">OpenAI</text>
<rect x="170" y="415" width="12" height="12" rx="2" fill="#d62828"/>
<text x="186" y="426" fill="#999" font-size="10">Anthropic</text>
<rect x="300" y="415" width="12" height="12" rx="2" fill="#4285f4"/>
<text x="316" y="426" fill="#999" font-size="10">Google</text>
<rect x="400" y="415" width="12" height="12" rx="2" fill="#264653"/>
<text x="416" y="426" fill="#999" font-size="10">Z.ai</text>
<circle cx="400" cy="444.84999999999997" r="6" fill="#4285f4" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="400" y="462.84999999999997" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Gemini 3.1 Pro</text>
<circle cx="532.1928094887362" cy="447.1499999999999" r="6" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="532.1928094887362" y="465.1499999999999" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Claude Opus 4.5</text>
<circle cx="532.1928094887362" cy="378.1499999999999" r="6" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="532.1928094887362" y="396.1499999999999" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Claude Opus 4.6</text>
<circle cx="432.1928094887362" cy="295.34999999999997" r="6" fill="#10a040" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="432.1928094887362" y="313.34999999999997" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">GPT-5.4</text>
<circle cx="348.5426827170242" cy="303.40000000000003" r="6" fill="#264653" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="348.5426827170242" y="321.40000000000003" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">GLM-5.1</text>
<circle cx="532.1928094887362" cy="235.55000000000004" r="6" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="532.1928094887362" y="221.55000000000004" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Claude Opus 4.7</text>
<circle cx="380.7354922057604" cy="321.80000000000007" r="6" fill="#10a040" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="380.7354922057604" y="339.80000000000007" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">GPT-5.3 Codex</text>
<circle cx="532.1949579831933" cy="301.09999999999997" r="6" fill="#10a040" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="532.1949579831933" y="319.09999999999997" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">GPT-5.5</text>
<circle cx="292.59159663865546" cy="301.09999999999997" r="6" fill="#4ea8de" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="292.59159663865546" y="319.09999999999997" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Kimi K2.6</text>
<circle cx="632.1928094887362" cy="51.55000000000001" r="6" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="632.1928094887362" y="37.55000000000001" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Claude Mythos 5</text>
<circle cx="632.1928094887362" cy="55" r="6" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="632.1928094887362" y="41" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Claude Fable 5</text>
<circle cx="532.1928094887362" cy="179.19999999999996" r="6" fill="#d62828" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="532.1928094887362" y="165.19999999999996" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Claude Opus 4.8</text>
<circle cx="432.1928094887362" cy="278.09999999999997" r="6" fill="#f4a261" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="432.1928094887362" y="264.09999999999997" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">Qwen 3.7 Max</text>
<circle cx="226.30344058337937" cy="296.5" r="6" fill="#7b2d8e" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="226.30344058337937" y="314.5" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">MiniMax M3</text>
<circle cx="379.90873060740034" cy="337.90000000000003" r="6" fill="#4ea8de" stroke="#0d0d0d" stroke-width="2" filter="url(#g)"/>
<text x="379.90873060740034" y="355.90000000000003" text-anchor="middle" fill="#ccc" font-size="9" font-weight="500">DeepSeek V4 Pro</text>
</svg>

---

## Anthropic (Claude)

Current as of June 2026. Source: [platform.claude.com](https://platform.claude.com/docs/en/about-claude/pricing)

| Model | Input /1M | Output /1M | Batch (50% off) | Cache Writes (5m) | 1h Cache Writes | Cache Hits |
|-------|-----------|------------|-----------------|-------------------|-----------------|------------|
| Fable 5 | $10.00 | $50.00 | ✓ | $12.50/MTok | $20.00/MTok | $1.00/MTok |
| Mythos 5 | $10.00 | $50.00 | ✓ | $12.50/MTok | $20.00/MTok | $1.00/MTok |
| Opus 4.8 | $5.00 | $25.00 | ✓ | $6.25/MTok | $10.00/MTok | $0.50/MTok |
| Opus 4.7 | $5.00 | $25.00 | ✓ | $6.25/MTok | $10.00/MTok | $0.50/MTok |
| Opus 4.6 | $5.00 | $25.00 | ✓ | $6.25/MTok | $10.00/MTok | $0.50/MTok |
| Opus 4.5 | $5.00 | $25.00 | ✓ | $6.25/MTok | $10.00/MTok | $0.50/MTok |
| Sonnet 4.6 | $3.00 | $15.00 | ✓ | $3.75/MTok | $6.00/MTok | $0.30/MTok |
| Haiku 4.5 | $1.00 | $5.00 | ✓ | $1.25/MTok | $2.00/MTok | $0.10/MTok |
| Mythos Preview | $25.00 | $125.00 | — | — | — | — |

Fable 5 (Jun 2026): Next-gen Anthropic flagship, $10/$50 per MTok. Limited availability.
Mythos 5 (Jun 2026): Premium reasoning tier at $10/$50 per MTok. Also limited availability.
Opus 4.8 (May 28 2026): 88.6% SWE-Bench Verified (#2). Opus 4.7: 87.6%, 64.3% SWE-Bench Pro (#1). Opus 4.5: 80.9%. Opus 4.6: 80.8%. Sonnet 4.6: 79.6%.
Mythos Preview: Research-only preview at $25/$125 per MTok. 93.9% SWE-Bench Verified (#1) — very expensive, limited API access.

---

## Google Gemini

Current as of June 2026. Source: [ai.google.dev](https://ai.google.dev/gemini-api/docs/pricing), [SWE-Bench](https://www.swebench.com/)

### Current Models

| Model | Input /1M | Output /1M | Cached Input | Context | Max Output | SWE-Bench Verified | Notes |
|-------|-----------|------------|-------------|---------|-----------|-------------------|-------|
| Gemini 3.1 Pro Preview | $2.00 ($4.00 >200K) | $12.00 ($18.00 >200K) | $0.20 ($0.40 >200K) | 2M | 16K | **80.6%** | Preview. Top-tier reasoning. 2M ctx |
| Gemini 3.5 Flash | $1.50 | $9.00 | $0.15 | 1M | 64K | — | GA May 19 2026. Fast, high-volume agentic tasks. 76.2% Terminal-Bench 2.1 |
| Gemini 3 Flash Preview | $0.50 | $3.00 | $0.05 | 1M | 64K | — | Efficient, general-purpose |
| Gemini 3.1 Flash-Lite Preview | $0.25 | $1.50 | $0.025 | 1M | 64K | — | Fast, high-volume agentic tasks |
| Gemini 2.5 Pro | $1.25 ($2.50 >200K) | $10.00 ($15.00 >200K) | — | 2M | 64K | — | Complex reasoning, coding, long docs |
| Gemini 2.5 Flash | $0.30 | $2.50 | — | 1M | 64K | — | Balanced cost and capability |
| Gemini 2.5 Flash-Lite | $0.10 | $0.40 | — | 1M | 64K | — | Lowest-cost current Gemini route |

### Batch / Flex Pricing (50% off)

| Model | Batch Input /1M | Batch Output /1M |
|-------|----------------|-----------------|
| Gemini 3.1 Pro (≤200K) | $1.00 | $6.00 |
| Gemini 3.5 Flash | $0.75 | $4.50 |
| Gemini 3 Flash | $0.25 | $1.50 |
| Gemini 3.1 Flash-Lite | $0.125 | $0.75 |
| Gemini 2.5 Pro (≤200K) | $0.625 | $5.00 |
| Gemini 2.5 Flash | $0.15 | $1.25 |
| Gemini 2.5 Flash-Lite | $0.05 | $0.20 |

### Deprecated

| Model | Input /1M | Output /1M | Note |
|-------|-----------|------------|------|
| Gemini 2.0 Flash | $0.10 | $0.40 | Retired June 1 2026 — shutdown complete |

Gemini 3.1 Pro is a preview model (restrictive rate limits). Free tier available for development and small projects.
Gemini 3.5 Flash GA May 19 2026 — fast, high-volume tier at 25% less than 3.1 Pro. 76.2% Terminal-Bench 2.1, 83.6% MCP Atlas, 84.2% CharXiv Reasoning.
Gemini 3 Flash Preview is a budget-friendly general-purpose model ($0.50/$3.00 per MTok).
Gemini 3.1 Pro scores 80.6% on SWE-Bench Verified — competitive with Claude Opus 4.6 (80.8%) and DeepSeek V4 Flash (79%).

---

## DeepSeek

Current as of June 2026. Source: [api-docs.deepseek.com](https://api-docs.deepseek.com/quick_start/pricing/)

DeepSeek V4 is the current flagship, launched March 2026. 671B total params, 37B active MoE, 1M context.
SWE-Bench Verified: V4 Pro Max 80.6%, V4 Flash ~79%. V4 Flash is the default workhorse; V4 Pro standard pricing at $0.435/$0.87 per MTok.

### New: DeepSeek V4 Pro Max

Released Apr 24 2026. 1.6T params, 49B active MoE, 1M context, open-weight on HuggingFace. 80.6% SWE-Bench Verified. Available at V4 Pro pricing (same API endpoint).

| Model | Cache Hit Input /1M | Cache Miss Input /1M | Output /1M | Context | Notes |
|-------|--------------------|---------------------|-----------|---------|-------|
| deepseek-v4-flash | $0.0028 | $0.14 | $0.28 | 1M | Default route. 384K max output |
| deepseek-v4-pro | $0.003625 | $0.435 | $0.87 | 1M | Standard pricing. 1.6T params. 80.6% SWE-Bench Verified |

Cache hit prices reduced to 1/10 of launch price from Apr 26 2026.
Older aliases `deepseek-chat` and `deepseek-reasoner` map to V4 Flash (non-thinking / thinking) and retire after Jul 24 2026.
New accounts get 5M free tokens.

### Legacy Models

| Model | Input /1M | Output /1M | Cache Hit | Context | Notes |
|-------|-----------|------------|-----------|---------|-------|
| DeepSeek V3.2 (Chat) | $0.28 | $0.42 | $0.028 | 128K | Previous gen, still available |
| DeepSeek R1 | $0.55 | $2.19 | $0.14 | 128K | Dedicated reasoning model |

DeepSeek V3.2: 73.0% SWE-Bench Verified. R1: chain-of-thought reasoning, ~96% cheaper than OpenAI o1.
DeepSeek web chat at chat.deepseek.com is free for individual users.

---

## OpenAI (ChatGPT)

Current as of June 2026. Source: [openai.com/api/pricing](https://openai.com/api/pricing/)

### GPT-5 Family (Current Flagship)

| Model | Input /1M | Output /1M | Cached Input | Context | Notes |
|-------|-----------|------------|-------------|---------|-------|
| GPT-5.5 (≤272K) | $5.00 | $30.00 | $0.50 | 1M | **88.7% SWE-Bench Verified** (#1), **58.6% SWE-Bench Pro**. Flagship reasoning + coding |
| GPT-5.5 (>272K) | $10.00 | $45.00 | $1.00 | 1M | Long context tier >272K tokens |
| GPT-5.5 Pro | $30.00 | $180.00 | — | 1M | Premium tier for research-grade problems |
| GPT-5.4 (≤272K) | $2.50 | $15.00 | $0.25 | 1M | ~80% SWE-Bench Verified. 59.1% SWE-Bench Pro |
| GPT-5.4 (>272K) | $5.00 | $22.50 | $0.50 | 1M | Long context tier >272K tokens |
| GPT-5.4 Mini | $0.75 | $4.50 | $0.075 | 400K | Affordable reasoning. Supports reasoning effort control |
| GPT-5.4 Nano | $0.20 | $1.25 | — | 400K | Fastest, cheapest 5.4 tier. Ideal for summaries, classification |
| GPT-5.3 Codex | $1.75 | $14.00 | — | 400K | **85.0% SWE-Bench Verified** (#3). 56.8% SWE-Bench Pro. Coding specialist |

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
GPT-5.5 scores 88.7% SWE-Bench Verified and 58.6% SWE-Bench Pro. GPT-5.4 scores ~80% SWE-Bench Verified and 59.1% SWE-Bench Pro (xHigh). GPT-5.5 Pro tier ($30/$180) is available for research-grade problems. GPT-5.3 Codex scores 85.0% SWE-Bench Verified and 56.8% SWE-Bench Pro. GPT-4.1 is OpenAI's recommended production default for most workloads.

---

## MiniMax

Current as of June 2026. Source: [platform.minimax.io](https://platform.minimax.io/docs/pricing/overview), [OpenRouter](https://openrouter.ai/minimax/minimax-m2.7)

### Coding Models

| Model | Input /1M | Output /1M | Context | Max Output | SWE-Bench | Speed | Notes |
|-------|-----------|------------|---------|-----------|-----------|-------|-------|
| M3 (≤512K) | $0.30 (permanent 50% off, was $0.60) | $1.20 (permanent 50% off, was $2.40) | 512K+ | — | — | ~50 TPS | Permanent 50% off. $0.06/M cached read |
| M3 (>512K) | $0.60 (permanent 50% off, was $1.20) | $2.40 (permanent 50% off, was $4.80) | 512K+ | — | — | — | Long-context tier. Permanent 50% off |
| M2.7 | $0.30 | $1.20 | 205K | 131K | — | ~80 TPS | Released Mar 18 2026. $0.06/M cached read |
| M2.5 Standard | $0.30 | $1.20 | 256K | — | 80.2% | ~50 TPS | Legacy. Automatic cache (no config) |
| M2.5 Lightning | $0.60 | $2.40 | 256K | — | 80.2% | ~100 TPS | Legacy. Priority scheduling |

M2.5 Standard: Still one of the best value coding models at $0.30/$1.20. Near Claude Opus 4.6 (80.8%).
M3: Latest generation. $0.30/$1.20 (≤512K, permanent 50% off list $0.60/$2.40). $0.60/$2.40 (>512K, also permanent 50% off list $1.20/$4.80). Supports >512K context via Priority tier.
OpenCode Go estimates: M2.5 ~6,300 req/5h (legacy price), M2.7 ~3,400 req/5h, M3 ~3,000 req/5h.

### Subscription Plans

| Plan | Price | Description |
|------|-------|-------------|
| Token Plan | Subscription | Quotas for individual builders and Teams |
| Credits | Prepaid | Same resource coverage as Token Plan |
| Pay-as-you-go | Per-token | Standard API endpoint billing |

---

## Qwen (Alibaba)

Current as of June 2026. Source: [DashScope direct pricing](https://www.alibabacloud.com/help/en/model-studio/model-pricing)

### Current Gen (Qwen3.7 & Qwen3.6)

#### Qwen3.7 (Latest — May 2026)

| Model | Input /1M | Output /1M | Context | Notes |
|-------|-----------|------------|---------|-------|
| Qwen3.7 Max | $2.50 | $7.50 | 1M | May 20 2026. Closed-weights text flagship. 1M context. Intelligence Index v4.0 #5 overall. Lowest hallucination rate among frontier models (22.9%). Anthropic API protocol native. 35h autonomous operation. Also available via Novita at $1.25/$3.75 (third-party). |
| Qwen3.7 Plus | TBA | TBA | 1M | Multimodal (vision + text) variant. Announced May 21 2026. |

Qwen3.7 Max (May 20-21 2026): Alibaba's newest flagship, announced at Alibaba Cloud Summit. $2.50/$7.50 per MTok — ~6x cheaper than Claude Opus 4.7. 1M context. Terminal-Bench Hard: 50.8%. MCP-Atlas: 76.4. Anthropic API protocol support means it works as a drop-in Claude Code backend. Open-weight variants expected June/July 2026 following Qwen3.6 release pattern.

#### Qwen3.6

| Model | Input /1M | Output /1M | Context | SWE-Bench | Notes |
|-------|-----------|------------|---------|-----------|-------|
| Qwen3.6 Plus | $0.325 | $1.95 | 1M | 78.8% Verified | Apr 2 2026. Hybrid attention + MoE. Reasoning by default |
| Qwen3.6 Flash | $0.25 | $1.50 | 1M | — | Cost-optimized tier |
| Qwen3.6 Max Preview | $1.30 | $7.80 | 256K | **SWE-Bench Pro #1** | Apr 20 2026. Closed-weights flagship. Leads SWE-Bench Pro, Terminal-Bench 2.0, SkillsBench, SciCode |

Qwen3.6 Plus: 78.8% SWE-Bench Verified — within 2 points of Claude Opus 4.6 (80.8%) at 1/30th the input price. 1M native context, 65K max output. Reasoning enabled by default (no mode toggle).
Qwen3.6-27B (dense, Apache 2.0): 77.2% SWE-Bench Verified — strong self-hosting option.
Qwen3.6-Max-Preview (Apr 20 2026): First closed-weights Qwen flagship. $1.30/$7.80 per MTok. 256K context. 57.3% SWE-Bench Pro — surpasses GPT-5.3-Codex (56.8%) and MiMo-V2.5-Pro (57.2%). Tops SWE-Bench Pro + 5 other coding benchmarks (Terminal-Bench 2.0, SkillsBench, QwenClawBench, QwenWebBench, SciCode) at launch.

### Previous Gen (Qwen3.5)

| Model | Input /1M | Output /1M | Context | Notes |
|-------|-----------|------------|---------|-------|
| Qwen3.5 Plus | $0.40 ($0.115 Global) | $2.40 ($0.688 Global) | 1M | Feb 2026 release. 65K max output. Thinking mode: output at same price |
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

Current as of June 2026. Source: [docs.z.ai](https://docs.z.ai/guides/overview/pricing)

### Flagship Models (GLM-5 Series)

| Model | Context | SWE-Bench | Input /1M | Output /1M | Cached Input | License |
|-------|---------|-----------|-----------|------------|-------------|---------|
| GLM-5.1 | 203K | Pro 58.4% (best-in-class) | $1.40 | $4.40 | $0.26 | MIT, 754B params |
| GLM-5 | 202K | Verified 77.8% | $1.00 | $3.20 | $0.20 | MIT, 744B/40B MoE |
| GLM-5-Turbo | 202K | — | $1.20 | $4.00 | $0.24 | Proprietary |

GLM-5.1 (Apr 7 2026): 8-hour autonomous runs, 1,700 agentic steps. Surpasses GPT-5.4 and Claude Opus 4.6 on SWE-Bench Pro.
GLM-5: 744B params, 40B active MoE, 28.5T token pretraining.

### Previous Gen (GLM-4 Series)

| Model | Context | Input /1M | Output /1M | Cached Input | Notes |
|-------|---------|-----------|------------|-------------|-------|
| GLM-4.7 | 128K | $0.60 | $2.20 | $0.11 | 73.8% SWE-Bench Verified |
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
| GLM-OCR | $0.03 | $0.03 | — |
| GLM-4.6V-Flash | Free | Free | Free |

---

## Xiaomi MiMo

Current as of June 2026. V2 launched Mar 18 2026, V2.5 launched Apr 22 2026. Source: [mimo-v2.com](https://www.mimo-v2.com/docs/pricing)

| Model | Input /1M | Output /1M | Context | Modalities | Notes |
|-------|-----------|------------|---------|------------|-------|
| MiMo-V2-Pro (≤256K) | $1.00 | $3.00 | 1M | Text | 78.0% SWE-Bench. 1T params, 42B active |
| MiMo-V2-Pro (256K–1M) | $2.00 | $6.00 | 1M | Text | Long-context tier |
| MiMo-V2.5 (≤256K) | $0.40 ($0.08 cached) | $2.00 | 1M | Text, Image, Audio, Video | Apr 22 2026. Native omnimodal. 1M context. OpenAI-compatible |
| MiMo-V2.5 (256K–1M) | $0.80 | $4.00 | 1M | Text, Image, Audio, Video | Long-context tier |
| MiMo-V2.5-Pro (≤256K) | $1.00 ($0.20 cached) | $3.00 | 1M | Text | Apr 22 2026. MIT license. 1T params. 57.2% SWE-Bench Pro |
| MiMo-V2.5-Pro (256K–1M) | $2.00 | $6.00 | 1M | Text | Long-context tier |
| MiMo-V2-Omni | ~$1.00 | ~$3.00 | 256K | Text, Image, Audio, Video | Multimodal flagship |
| MiMo-V2-Flash | $0.10 | $0.30 | 256K | Text | Open-source foundation model |
| MiMo-V2-TTS | Free | Free | — | Audio | Limited time promo |

API at platform.xiaomimimo.com. OpenAI-compatible. Credit plans available: Lite $6/mo, Standard $16/mo, Pro $50/mo, Max $100/mo.

---

## Kimi / Moonshot AI (K2.6)

Current as of June 2026. Source: [kimi.com](https://www.kimi.com/resources/kimi-k2-6-pricing), [OpenRouter](https://openrouter.ai/moonshotai/kimi-k2.5)

Both models: 1T params, 32B active MoE, 384 experts, MIT license.

| Model | Cache Hit /1M | Cache Miss /1M | Output /1M | Context | SWE-Bench |
|-------|--------------|----------------|-----------|---------|-----------|
| kimi-k2.6 | $0.16 | $0.95 | $4.00 | 262K | Verified 80.2%, Pro 58.6%, BrowseComp 83.2% |
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

## Mistral (Medium 3.5)

Current as of June 2026. Source: [la-plateforme.mistral.ai](https://la-plateforme.mistral.ai/), [tokencost.app](https://tokencost.app/models/mistral-medium-3-5)

| Model | Input /1M | Output /1M | Context | Max Output | SWE-Bench Verified | Notes |
|-------|-----------|------------|---------|-----------|-------------------|-------|
| Mistral Medium 3.5 | $1.50 | $7.50 | 256K | 33K | **77.6%** | 128B dense, multimodal. Released Apr 29 2026.

Mistral Medium 3.5 consolidates Medium 3.1 + Magistral + Devstral 2 into one unified model. Modified MIT license with open weights. 77.6% SWE-Bench Verified — competitive with Qwen3.6-27B (77.2%) and ahead of DeepSeek V3.2 (73.0%).

---

## xAI (Grok)

Current as of June 2026. Source: [docs.x.ai](https://docs.x.ai/developers/models), [xAI pricing](https://docs.x.ai/developers/models)

| Model | Input /1M | Output /1M | Cached Input | Context | SWE-Bench | Notes |
|-------|-----------|------------|-------------|---------|-----------|-------|
| Grok 4.3 | $1.25 | $2.50 | — | 1M | ~72-75% (self-reported) | Launched Apr 30 2026. Current flagship. 1M context.
| Grok 4.20 | $1.25 | $2.50 | $0.20 | 1M | — | 85% cached-input discount. Retired slugs (Grok 4, Grok 4.1 Fast) redirect here.
| Grok 4 | $3.00 | $15.00 | — | 256K | 72-75% (self-reported) | Original Grok 4 flagship. Deprecated May 15 2026 — now redirects to Grok 4.3.
| Grok Build 0.1 | $1.00 | $2.00 | — | 256K | — | Coding specialist. 20% cheaper than Grok 4.3.

Grok 4.3 self-reports ~72-75% on SWE-Bench Verified (independent testing with SWE-agent scaffold: 58.6%). Aider Polyglot: 79.6%. xAI retired Grok 4, Grok 4.1 Fast, and Grok Code Fast 1 slugs on May 15, 2026 — these now redirect to Grok 4.3 at $1.25/$2.50 pricing. xAI offers up to $150/month free API credits via data-sharing program. Unique real-time X search grounding.

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
| opencode-go/mimo-v2.5 | MiMo V2.5 |
| opencode-go/mimo-v2.5-pro | MiMo V2.5 Pro |
| opencode-go/minimax-m2.5 | MiniMax M2.5 |
| opencode-go/minimax-m2.7 | MiniMax M2.7 |
| opencode-go/minimax-m3 | MiniMax M3 |
| opencode-go/qwen3.5-plus | Qwen3.5 Plus |
| opencode-go/qwen3.6-plus | Qwen3.6 Plus |
| opencode-go/qwen3.6-max-preview | Qwen3.6 Max Preview |
| opencode-go/mistral-medium-3.5 | Mistral Medium 3.5 |
| opencode-go/grok-4.3 | Grok 4.3 |
| opencode-go/grok-4.20 | Grok 4.20 |

### Request Estimates (June 2 2026)

| Model | Per 5h | Per Week | Per Month |
|-------|--------|----------|-----------|
| GLM-5.1 | 880 | 2,150 | 4,300 |
| GLM-5 | 1,150 | 2,880 | 5,750 |
| Kimi K2.5 | 1,850 | 4,630 | 9,250 |
| MiMo-V2-Pro | 1,290 | 3,225 | 6,450 |
| MiMo-V2.5 | 1,290 | 3,225 | 6,450 |
| MiMo-V2.5-Pro | 1,290 | 3,225 | 6,450 |
| MiMo-V2-Omni | 2,150 | 5,450 | 10,900 |
| Qwen3.6 Plus | 3,300 | 8,200 | 16,300 |
| Qwen3.6 Max Preview | 820 | 2,050 | 4,100 |
| MiniMax M3 | ~3,000 | ~7,500 | 15,000 |
| MiniMax M2.7 | 3,400 | 8,500 | 17,000 |
| MiniMax M2.5 | 3,150 | 7,950 | 15,900 |
| Mistral Medium 3.5 | ~2,500 | ~6,200 | 12,500 |
| Qwen3.5 Plus | 10,200 | 25,200 | 50,500 |

MiniMax M2.5: 80.2% SWE-Bench — near Claude Opus 4.6 (80.8%).
DeepSeek V4 Pro: Standard pricing at $0.435/$0.87 per MTok.

---

## Notes

- **BytePlus ModelArk**: Quota shared across Claude Code, Cursor, Cline, Codex CLI, Kilo Code, Roo Code, OpenCode
- **GitHub Copilot**: Premium requests shared across all features; extra $0.04 each on Pro/Pro+
- **Claude Code**: Exact request counts not published — only relative multipliers
- **GLM quota multipliers**: Peak hours drain 3x quota; off-peak 2x; GLM-4.7/4.5-Air always 1x
- **MiMo**: Pure credit pool, no 5h/windows, credits expire month-end
- **Kimi**: API billed separately — not included in membership

> **Benchmark Note:** [SWE-Bench Verified](https://www.swebench.com/) measures a model's ability to resolve real-world GitHub issues from code repositories. Not all providers publish scores — the chart above only includes models with verified data.
