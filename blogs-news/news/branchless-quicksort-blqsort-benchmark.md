---
layout: standalone
title: "Branchless Quicksort 30% Faster than std::sort and pdqsort"
date: 2026-06-04
source: "tiki.li"
source_url: "https://tiki.li/blog/blqsort"
category: "dev-news"
image: "https://placehold.co/800x400/1a1a2e/00d4ff?text=Branchless+Quicksort"
---

# Branchless Quicksort 30% Faster than std::sort and pdqsort

> Originally published on tiki.li — June 04, 2026

![Cover](https://placehold.co/800x400/1a1a2e/00d4ff?text=Branchless+Quicksort)

## Summary

A new sorting library called blqsort implements branchless Quicksort that outperforms both std::sort and pdqsort on modern hardware. On Apple M1, blqsort sorts 50 million doubles in 0.97s vs std::sort's 1.33s. On AMD Ryzen, it achieves 2.06s vs pdqsort's 2.81s. The approach uses an auxiliary buffer for branchless partitioning and sorting networks for small subsets (2-12 elements). Multithreaded versions deliver another 3-4x speedup on M1. Single-header C and C++ implementations are available on GitHub.

## Read Original

→ [Read full article on tiki.li](https://tiki.li/blog/blqsort)

---

*Curated by Brain Bot for Abhay's KB — June 04, 2026*
