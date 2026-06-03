---
layout: standalone
title: "A Post-Quantum Future for Let's Encrypt — Merkle Tree Certificates"
date: 2026-06-03
source: "Let's Encrypt"
source_url: "https://letsencrypt.org/2026/06/03/pq-certs"
category: "dev-news"
image: "https://placehold.co/800x400/1a1a2e/00d4ff?text=Post-Quantum+Let%27s+Encrypt"
---

# A Post-Quantum Future for Let's Encrypt — Merkle Tree Certificates

> Originally published on Let's Encrypt — June 3, 2026

![Cover](https://placehold.co/800x400/1a1a2e/00d4ff?text=Post-Quantum+Let%27s+Encrypt)

## Summary

Let's Encrypt announced its plan for a post-quantum-safe Web PKI using Merkle Tree Certificates (MTCs), a new approach that adds quantum-resistant authentication without the massive TLS handshake bloat of standard NIST post-quantum signature schemes. With Google, Cloudflare, and the NSA all accelerating their post-quantum migration timelines toward 2029-2035, and Go 1.27 adding ML-DSA to its standard library, post-quantum authentication is becoming an urgent priority for the entire web ecosystem.

## Key Highlights

- **MTCs solve the size problem** — standard ML-DSA-44 signatures are ~2,420 bytes vs 64 bytes for ECDSA-P256; swapping all handshake signatures to ML-DSA would push a single TLS handshake past 10KB, causing connection failures
- **Timeline accelerated** — Google targets 2029, Cloudflare follows suit; NSA's CNSA 2.0 mandates 2030-2035 for national security systems
- **Go 1.27** now includes ML-DSA in the standard library — a sign post-quantum signatures are becoming practical infrastructure
- **MTCs are a different design** — instead of issuing signed certificates, MTCs use Merkle trees for authentication, keeping handshakes small
- Key for long-lived assets like root CAs, code-signing keys, and identity systems

## Read Original

→ [Read full article on Let's Encrypt](https://letsencrypt.org/2026/06/03/pq-certs)

---
*Curated by Brain Bot for Abhay's KB — June 3, 2026*
