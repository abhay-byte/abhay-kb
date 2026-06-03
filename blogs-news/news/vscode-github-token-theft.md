---
layout: standalone
title: "1-Click GitHub Token Stealing via a VSCode Bug"
date: 2026-06-03
source: "Ammar Askar's Blog"
source_url: "https://blog.ammaraskar.com/github-token-stealing/"
category: "dev-news"
image: "https://placehold.co/800x400/1a1a2e/00d4ff?text=VSCode+GitHub+Token+Theft"
---

# 1-Click GitHub Token Stealing via a VSCode Bug

> Originally published on Ammar Askar's Blog — June 3, 2026

![Cover](https://placehold.co/800x400/1a1a2e/00d4ff?text=VSCode+GitHub+Token+Theft)

## Summary

A security researcher discovered that simply clicking a malicious link can allow an attacker to steal GitHub OAuth tokens with full read/write access to all repositories. The exploit leverages a bug in VSCode's webview security model within github.dev — the browser-based version of VSCode — where a cross-origin bypass in the webview sandbox allows an attacker to exfiltrate the OAuth token that GitHub POSTs to github.dev for authenticated repo access. The bug has been reported to Microsoft and is now in full disclosure.

## Read Original

→ [Read full article on Ammar Askar's Blog](https://blog.ammaraskar.com/github-token-stealing/)

---
*Curated by Brain Bot for Abhay's KB — June 3, 2026*
