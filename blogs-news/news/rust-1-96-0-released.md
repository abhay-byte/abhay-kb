---
layout: standalone
title: "Rust 1.96.0 Released"
date: 2026-05-28
source: "Rust Blog"
source_url: "https://blog.rust-lang.org/2026/05/28/Rust-1.96.0/"
category: "dev-news"
image: "https://placehold.co/800x400/1a1a2e/00d4ff?text=Rust+1.96.0+Released"
---

# Rust 1.96.0 Released
> Originally published on Rust Blog — May 28, 2026

![Cover](https://placehold.co/800x400/1a1a2e/00d4ff?text=Rust+1.96.0+Released)

## Summary

Rust 1.96.0 introduces new `Copy`-implementing `Range*` types via RFC3550 that use `IntoIterator` instead of `Iterator`, making it possible to store slice accessors in Copy types without splitting start and end. The release also adds `assert_matches!` and `debug_assert_matches!` macros for pattern-matching assertions with better diagnostics, and WebAssembly targets now no longer pass `--allow-undefined` to the linker by default — making undefined symbols a linker error instead of silently converting them to WebAssembly imports from the "env" module.

## Read Original

→ [Read full article on Rust Blog](https://blog.rust-lang.org/2026/05/28/Rust-1.96.0/)
---
*Curated by Brain Bot for Abhay's KB — June 1, 2026*
