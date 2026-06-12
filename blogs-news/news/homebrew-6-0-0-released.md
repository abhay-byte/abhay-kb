---
layout: standalone
title: "Homebrew 6.0.0 Released with Tap Trust Security and Performance Improvements"
date: 2026-06-12
source: "Homebrew Blog"
source_url: "https://brew.sh/2026/06/11/homebrew-6.0.0/"
category: "dev-news"
image: "https://placehold.co/800x400/1a1a2e/00d4ff?text=Homebrew+6.0.0+Released"
---

# Homebrew 6.0.0 Released with Tap Trust Security and Performance Improvements

> Originally published on Homebrew Blog — June 11, 2026

![Cover](https://placehold.co/800x400/1a1a2e/00d4ff?text=Homebrew+6.0.0+Released)

## Summary

Homebrew 6.0.0 introduces a major new tap trust security mechanism that requires third-party taps to be explicitly trusted before their code is evaluated or run, reducing risk from malicious or compromised taps. The release also includes a new faster, smaller default internal Homebrew JSON API, sandboxing on Linux, better defaults from user survey feedback, many brew bundle improvements, and initial support for macOS 27 Golden Gate.

## Key Highlights

- **Tap Trust:** Third-party taps now require explicit trust before running their code. Official Homebrew taps remain trusted by default.
- **Default JSON API:** New internal API is faster and smaller, replacing the old defaults.
- **Linux Sandboxing:** Brew now supports sandboxing on Linux for improved security.
- **Brew Bundle Improvements:** Enhanced dependency management, honoring the `trusted:` option and recording trusted bundle entries.
- **macOS 27 Support:** Initial compatibility with macOS 27 (Golden Gate).

## Read Original

→ [Read full article on Homebrew Blog](https://brew.sh/2026/06/11/homebrew-6.0.0/)

---
*Curated by Brain Bot for Abhay's KB — June 12, 2026*
