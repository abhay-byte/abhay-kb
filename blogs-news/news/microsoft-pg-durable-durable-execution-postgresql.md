---
layout: standalone
title: "Microsoft Open-Sources pg_durable: In-Database Durable Execution for PostgreSQL"
date: 2026-06-05
source: "Microsoft / GitHub"
source_url: "https://github.com/microsoft/pg_durable"
category: "dev-news"
image: "https://placehold.co/800x400/1a1a2e/00d4ff?text=Microsoft+Open-Sources+pg_durable"
---

# Microsoft Open-Sources pg_durable: In-Database Durable Execution for PostgreSQL
> Originally published on Microsoft / GitHub — June 5, 2026

![Cover](https://placehold.co/800x400/1a1a2e/00d4ff?text=Microsoft+Open-Sources+pg_durable)

## Summary

Microsoft has open-sourced pg_durable, an in-database durable execution engine for PostgreSQL that lets developers define long-running, fault-tolerant SQL workflows directly inside the database. The system checkpoints each step of a function graph, allowing execution to resume automatically after crashes, restarts, or failed steps — eliminating the need to stitch together cron jobs, workers, queues, and status tables for reliable background work.

Built as a PostgreSQL extension, pg_durable is also a core component of Microsoft's new Azure HorizonDB cloud service. It targets backend and data engineers who want workflows to live next to their data, DBAs automating runbooks, and teams building data or AI pipelines requiring durable execution per row or batch.

## Read Original
→ [Read full article on GitHub](https://github.com/microsoft/pg_durable)

---
*Curated by Brain Bot for Abhay's KB — Saturday, June 6, 2026*
