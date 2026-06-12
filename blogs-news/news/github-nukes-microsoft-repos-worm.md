---
layout: standalone
title: "GitHub Nukes 70+ Microsoft Repos Amid Suspected Miasma Worm Attack"
date: 2026-06-12
source: "The Register"
source_url: "https://www.theregister.com/security/2026/06/08/github-nukes-70-microsoft-repos-amid-suspected-worm-attack/5252169"
category: "dev-news"
image: "https://placehold.co/800x400/1a1a2e/ff4444?text=GitHub+Worm+Attack"
---

# GitHub Nukes 70+ Microsoft Repos Amid Suspected Miasma Worm Attack

> Originally published on The Register — June 8, 2026

![Cover](https://placehold.co/800x400/1a1a2e/ff4444?text=GitHub+Worm+Attack)

## Summary

GitHub temporarily disabled over 70 Microsoft repositories after detecting signs of the "Miasma" worm in a major open source supply chain attack. The compromise started with a malicious commit to Azure/durabletask that dropped configuration files triggering remote code execution when developers opened the repo in IDEs or AI coding tools like Claude Code, Gemini CLI, and Cursor, breaking CI/CD pipelines across the ecosystem.

## Key Details

- **73 repos** were taken down within 105 seconds after GitHub's alarms triggered on June 5.
- The attack originated from a compromised contributor account pushing to Azure/durabletask.
- Malicious config files triggered RCE when opened in IDEs and AI coding tools.
- Azure/functions-action takedown broke every workflow referencing it, causing widespread CI/CD failures.
- Microsoft restored all repos after review and notified affected customers.

## Read Original

→ [Read full article on The Register](https://www.theregister.com/security/2026/06/08/github-nukes-70-microsoft-repos-amid-suspected-worm-attack/5252169)

---
*Curated by Brain Bot for Abhay's KB — June 12, 2026*
