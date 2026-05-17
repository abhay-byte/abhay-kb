---
layout: standalone
title: "Bun Rust Rewrite: Codebase Fails Miri Checks, Allows UB in Safe Rust"
date: 2026-05-17
source: "Hacker News"
source_url: "https://news.ycombinator.com/item?id=48150900"
category: "dev-news"
image: "https://placehold.co/800x400/1a1a2e/00d4ff?text=Bun+Rust+Rewrite+Miri+UB"
---

# Bun Rust Rewrite: Codebase Fails Miri Checks, Allows UB in Safe Rust
> Originally published on Hacker News — May 16, 2026
![Cover](https://placehold.co/800x400/1a1a2e/00d4ff?text=Bun+Rust+Rewrite+Miri+UB)

## Summary
A GitHub issue reports that Bun's newly rewritten Rust codebase contains undefined behavior (UB) in safe Rust code. The `PathString::init` function erases slice lifetimes and produces dangling references, raising questions about the safety guarantees of Bun's high-profile migration from Zig to Rust.

## Key Points
- The issue was filed on Bun's GitHub repo, with a fix proposed in PR #30728 marking the function as unsafe
- For a project billing itself as a faster, safer Node.js alternative, the find highlights tension between shipping speed and Rust's safety guarantees
- Developers noted the issue only appears under specific patterns, requiring deliberate testing to catch via Miri

## Read Original
→ [Read full discussion on Hacker News](https://news.ycombinator.com/item?id=48150900)
---
*Curated by Brain Bot for Abhay's KB — May 17, 2026*
