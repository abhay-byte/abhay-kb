---
layout: standalone
title: "Zeroserve: A Zero-Config Web Server Scriptable with eBPF"
date: 2026-06-06
source: "Hacker News / su3.io"
source_url: "https://su3.io/posts/introducing-zeroserve"
category: "dev-news"
image: "https://placehold.co/800x400/1a1a2e/00d4ff?text=Zeroserve+eBPF+Web+Server"
---

# Zeroserve: A Zero-Config Web Server Scriptable with eBPF

> Originally published on su3.io — June 6, 2026

![Cover](https://placehold.co/800x400/1a1a2e/00d4ff?text=Zeroserve+eBPF+Web+Server)

## Summary

Zeroserve is a new open-source HTTPS server that reimagines web serving by using eBPF programs as its configuration layer — replacing traditional declarative config files (nginx-style location blocks, rewrite rules) with sandboxed eBPF middleware that runs on every request. Built entirely on io_uring with TLS 1.3, HTTP/2, and Encrypted Client Hello baked in, it beats nginx on throughput for most workloads on a single core. The project aims to be an alternative to nginx and Caddy, collapsing the config/script split into one programmable surface. It scored 177 points on Hacker News.

## Read Original

→ [Read full article on su3.io](https://su3.io/posts/introducing-zeroserve)

---

*Curated by Brain Bot for Abhay's KB — June 6, 2026*
