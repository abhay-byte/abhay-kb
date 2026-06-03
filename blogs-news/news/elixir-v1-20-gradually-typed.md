---
layout: standalone
title: "Elixir v1.20 Released: Now a Gradually Typed Language"
date: 2026-06-03
source: "Elixir Lang Blog"
source_url: "https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/"
category: "dev-news"
image: "https://placehold.co/800x400/1a1a2e/00d4ff?text=Elixir+v1.20+Gradual+Typing"
---

# Elixir v1.20 Released: Now a Gradually Typed Language

> Originally published on Elixir Lang Blog — June 3, 2026

![Cover](https://placehold.co/800x400/1a1a2e/00d4ff?text=Elixir+v1.20+Gradual+Typing)

## Summary

Elixir v1.20 marks a landmark release — the language now has a gradual type system powered by set-theoretic types. After years of research (including an award-winning 2023 paper), the team completed the first development milestone: performing type inference and gradual type checking on every Elixir program without requiring type annotations. The system can find dead code and verified bugs — typing violations guaranteed to fail at runtime — with extremely low false positive rates, and scores well on the "IfT" benchmark for type narrowing.

## Key Highlights

- **Gradual typing with `dynamic()` type** — Elixir's type system includes a `dynamic()` type that represents values whose precise type isn't known at compile time, enabling gradual adoption without annotations
- **Verified bugs without developer overhead** — the type system finds real bugs in existing codebases without developers adding a single type annotation
- **Set-theoretic foundations** — types are described using unions, intersections, and negations with clear error messages
- **Passes 12 of 13 categories** in the "IfT: Benchmark for Type Narrowing"
- Made possible by a partnership between CNRS and Remote, sponsored by Fresha and Tidewave

## Read Original

→ [Read full article on Elixir Lang Blog](https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/)

---
*Curated by Brain Bot for Abhay's KB — June 3, 2026*
