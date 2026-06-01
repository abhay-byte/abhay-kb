---
layout: standalone
title: "Streambed: Stream Postgres to Iceberg on S3"
date: 2026-05-31
source: "GitHub (viggy28/streambed)"
source_url: "https://github.com/viggy28/streambed"
category: "dev-news"
image: "https://placehold.co/800x400/1a1a2e/00d4ff?text=Streambed+Postgres+to+Iceberg"
---

# Streambed: Stream Postgres to Iceberg on S3
> Originally published on GitHub — May 31, 2026

![Cover](https://placehold.co/800x400/1a1a2e/00d4ff?text=Streambed+Postgres+to+Iceberg)

## Summary

Streambed is an open-source CDC (Change Data Capture) engine that streams Postgres WAL changes via logical replication directly to Apache Iceberg tables on S3 — no ETL or Spark required. It writes Parquet files to S3, commits Iceberg metadata, and includes a built-in query server using embedded DuckDB that speaks the Postgres wire protocol, so you can connect with psql. Features include copy-on-write merging for updates/deletes, one-shot backfill via `COPY`, and configurable S3 prefixes for multi-tenant setups.

## Read Original

→ [Read full article on GitHub](https://github.com/viggy28/streambed)
---
*Curated by Brain Bot for Abhay's KB — June 1, 2026*
