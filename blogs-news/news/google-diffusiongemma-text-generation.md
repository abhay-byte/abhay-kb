---
layout: standalone
title: "Google Releases DiffusionGemma: 4x Faster Text Generation with Text Diffusion"
date: 2026-06-12
source: "Google AI Blog"
source_url: "https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/"
category: "dev-news"
image: "https://placehold.co/800x400/1a1a2e/00d4ff?text=DiffusionGemma"
---

# Google Releases DiffusionGemma: 4x Faster Text Generation with Text Diffusion

> Originally published on Google AI Blog — June 10, 2026

![Cover](https://placehold.co/800x400/1a1a2e/00d4ff?text=DiffusionGemma)

## Summary

Google introduced DiffusionGemma, an experimental 26B Mixture of Experts open model that uses text diffusion to generate entire blocks of text simultaneously instead of token-by-token, delivering up to 4x faster inference on GPUs. Released under Apache 2.0, the model activates only 3.8B parameters during inference and fits within 18GB VRAM on consumer GPUs, reaching 1000+ tokens per second on an NVIDIA H100.

## Key Details

- **Architecture:** 26B total MoE model, only 3.8B active parameters per inference step.
- **Speed:** Up to 4x faster than autoregressive models; 1000+ tok/s on H100, 700+ on RTX 5090.
- **Memory:** Fits within 18GB VRAM when quantized — runs on high-end consumer GPUs.
- **License:** Apache 2.0 — fully open and available for research and development.
- **Use Cases:** In-line editing, rapid iteration, non-linear text structures, speed-critical local workflows.
- Built on Gemma 4 family intelligence and Gemini Diffusion research.

## Read Original

→ [Read full article on Google AI Blog](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)

---
*Curated by Brain Bot for Abhay's KB — June 12, 2026*
