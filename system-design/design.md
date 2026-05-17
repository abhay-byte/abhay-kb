---
layout: standalone
title: System Design — Design
---

# System Design

> *"Good architecture makes the system easy to understand, easy to develop, easy to maintain, and easy to deploy."*
> — Robert C. Martin

---

## Table of Contents

1. [System Design Fundamentals](#1-system-design-fundamentals)
2. [Scalability](#2-scalability)
3. [Databases at Scale](#3-databases-at-scale)
4. [Caching Strategies](#4-caching-strategies)
5. [Messaging & Event-Driven Architecture](#5-messaging--event-driven-architecture)
6. [Reliability & Fault Tolerance](#6-reliability--fault-tolerance)
7. [Security & API Design](#7-security--api-design)
8. [Advanced System Patterns](#8-advanced-system-patterns)
9. [System Design Interview Framework](#9-system-design-interview-framework)
10. [Real-World Architecture Examples](#10-real-world-architecture-examples)

---

## 1. System Design Fundamentals

System design is the process of **defining the architecture, components, modules, interfaces, and data flow** of a system to satisfy specified requirements.

### The Request Flow (Every System)

```
Client
 |
DNS Resolution
 |
Load Balancer
 |
Application Server(s)
 |
Cache Check (Redis / Memcached)
 | (cache miss)
Database Query
 |
Response to Client
```

### Key Properties to Design For

| Property | Description |
|---|---|
| **Scalability** | Handle growing traffic/data |
| **Availability** | System is up (99.9% = 8.7 hrs/yr downtime) |
| **Reliability** | Consistently correct results |
| **Latency** | Time to first byte (p50, p99) |
| **Throughput** | Requests per second (RPS) |
| **Consistency** | All nodes see the same data |
| **Durability** | Data is not lost once written |
| **Maintainability** | Easy to operate, debug, extend |

---

## 2. Scalability

### 2.1 Vertical vs. Horizontal Scaling

| | Vertical Scaling | Horizontal Scaling |
|---|---|---|
| **What** | Bigger machine (more CPU/RAM) | More machines |
| **Limit** | Hardware ceiling | Practically unlimited |
| **Cost** | Expensive at high end | Commodity hardware |
| **Failure** | Single point of failure | Fault tolerant |
| **Complexity** | Simple | Requires distributed system knowledge |
| **Use when** | Small to medium scale | Large scale, high availability needed |

### 2.2 Load Balancing

Distributes incoming requests across multiple servers.

**Algorithms:**
- **Round Robin** — requests cycle through servers equally
- **Least Connections** — routes to server with fewest active connections
- **IP Hash** — same client always goes to the same server
- **Weighted** — more capacity = more traffic

**Tools:** Nginx, HAProxy, AWS ELB, GCP Load Balancer

### 2.3 CDN — Content Delivery Network

Caches static assets at **edge servers geographically close to users**.
- Reduces latency
- Offloads origin servers
- DDoS protection

**Tools:** Cloudflare, AWS CloudFront, Akamai, Fastly

---

## 3. Databases at Scale

### 3.1 SQL vs. NoSQL

| | SQL | NoSQL |
|---|---|---|
| **Structure** | Tables, rows, columns | Documents, key-value, graph |
| **Schema** | Fixed, enforced | Flexible, schema-less |
| **Scaling** | Vertical (primarily) | Horizontal (design goal) |
| **ACID** | Full ACID | Often eventual consistency |
| **Use for** | Transactions, relational data | Scale, unstructured data |

### 3.2 Database Replication

```
Primary (Write) ---> Replica 1 (Read)
 ---> Replica 2 (Read)
```

### 3.3 Database Sharding

Splits data across multiple independent databases.

**Range-Based:** Partition by value range. Simple but can create hot spots.

**Hash-Based:** `shard = hash(user_id) % N`. Even distribution, hard to rebalance.

**Consistent Hashing:** Maps keys and shards to a hash ring. Adding/removing shards only remaps ~1/N of keys.

### 3.4 CAP Theorem

A distributed system can guarantee **only two of three**:
- **Consistency** — all nodes see same data
- **Availability** — every request gets a response
- **Partition Tolerance** — system works despite network failures

| Combination | Examples |
|---|---|
| **CP** (Consistency + Partition) | Zookeeper, HBase |
| **AP** (Availability + Partition) | Cassandra, DynamoDB |
| **CA** (Consistency + Availability) | Traditional RDBMS (single node) |

### 3.5 Database Indexing

- **B-Tree Index** — range queries and equality (default)
- **Hash Index** — O(1) equality lookups only
- **Composite Index** — multiple columns; order matters
- **Covering Index** — query answered entirely from index
- **Full-Text Index** — tokenized text search

---

## 4. Caching Strategies

### 4.1 Cache Levels

| Level | Examples | Latency |
|---|---|---|
| CPU L1/L2 | Processor cache | < 1 ns |
| In-process | App memory | ~ns |
| Distributed | Redis, Memcached | 0.1-1 ms |
| CDN | Cloudflare, Fastly | 1-50 ms |

### 4.2 Caching Patterns

**Cache-Aside (Lazy Loading)** — check cache first; on miss, load from DB.
```
Read: App -> Cache (miss) -> DB -> Cache (write) -> App
```

**Write-Through** — write to DB and cache simultaneously.
**Write-Behind** — write to cache first, sync to DB async.
**Read-Through** — cache handles loading from DB on miss.

### 4.3 Cache Invalidation

- **TTL** — data expires after fixed time
- **Event-Driven** — invalidate on write events
- **Versioned Keys** — `user:42:v3`

### 4.4 Cache Stampede Prevention

When a popular key expires, thousands of requests hit the DB at once.

**Solutions:** Mutex/lock, probabilistic early expiration, stale-while-revalidate.

---

## 5. Messaging & Event-Driven Architecture

### 5.1 Message Queues

```
Producer -> [Queue] -> Consumer
```

**Benefits:** Traffic spike absorption, retry, decoupling.
**Tools:** RabbitMQ, Amazon SQS, ActiveMQ

### 5.2 Event Streaming (Kafka)

Persistent, replayable logs — not consumed and deleted like queues.

```
Producers -> Kafka Topic (Partitioned) -> Consumer Groups
```

### 5.3 Pub/Sub vs. Message Queues

- **Pub/Sub** — all subscribers get every event
- **Queue** — competing consumers split the load

### 5.4 Saga Pattern

Manages long-running distributed transactions without two-phase commit.

**Choreography:** Each service emits events; the next service responds.
**Orchestration:** Central coordinator calls each service and manages compensation.

---

## 6. Reliability & Fault Tolerance

### 6.1 Circuit Breaker

Prevents cascading failures — stops calls to a failing service.

```
Closed -> (failures exceed threshold) -> Open -> (timeout) -> Half-Open
Half-Open -> (success) -> Closed
Half-Open -> (failure) -> Open
```

### 6.2 Retry with Exponential Backoff
```
Attempt 1: fail -> wait 1s
Attempt 2: fail -> wait 2s
Attempt 3: fail -> wait 4s + jitter
```

**Idempotency required** — same result regardless of how many times called.

### 6.3 Bulkhead Pattern

Isolate resources per service so one failure doesn't starve others.

### 6.4 Rate Limiting

**Algorithms:** Token Bucket, Leaky Bucket, Fixed Window, Sliding Window Log, Sliding Window Counter.

### 6.5 Redundancy
- **Active-Active** — all instances serve traffic
- **Active-Passive** — standby promotes on failure

---

## 7. Security & API Design

### 7.1 API Gateway

Single entry point for all client requests — auth, rate limiting, routing, transformation.

```
Mobile ---+
Web ------+-> API Gateway -> Services
External -+
```

**Tools:** Kong, AWS API Gateway, Nginx, Traefik

### 7.2 REST vs. GraphQL vs. gRPC

| | REST | GraphQL | gRPC |
|---|---|---|---|
| **Protocol** | HTTP/1.1 | HTTP/1.1 | HTTP/2 |
| **Format** | JSON/XML | JSON | Protobuf |
| **Over/Under fetch** | Common | Solved | N/A |
| **Best for** | Public APIs | Complex data graphs | Internal microservices |

### 7.3 Authentication & Authorization
- **JWT** — stateless tokens, validated without DB
- **OAuth 2.0** — delegation framework
- **API Keys** — machine-to-machine
- **mTLS** — mutual certificate auth

---

## 8. Advanced System Patterns

### 8.1 Strangler Fig Pattern
Gradually migrate legacy monolith by routing traffic to new services.

### 8.2 Outbox Pattern
Atomically write to DB + outbox table; separate relay publishes events. Solves the dual-write problem.

### 8.3 Backend for Frontend (BFF)
Dedicated API per client type (mobile, web, third-party).

### 8.4 Sidecar Pattern
Helper container alongside the main service (service mesh proxies).

### 8.5 Service Mesh
Infrastructure layer for service-to-service communication (retries, mTLS, observability).

**Tools:** Istio, Linkerd, Consul Connect

---

## 9. System Design Interview Framework

### Step 1: Clarify Requirements (5 min)
- Functional requirements, non-functional (scale, latency, availability)
- Read-heavy or write-heavy? Global or regional?

### Step 2: Capacity Estimation (5 min)
```
Storage: 500M tweets/day x 200 bytes = 100 GB/day
Writes: 500M / 86,400s = 6,000 writes/sec
Reads: 100:1 ratio = 600,000 reads/sec
```

### Step 3: High-Level Design (10 min)
Draw major components: clients, load balancers, services, databases, caches.

### Step 4: Deep Dive (15-20 min)
Database schema, sharding, caching, API design, fault tolerance.

### Step 5: Trade-offs & Bottlenecks (5 min)
Identify bottlenecks, discuss alternatives — demonstrate engineering judgment.

### Common System Design Questions

| System | Key Decisions |
|---|---|
| **URL Shortener** | Base62 encoding, KV store, bloom filter |
| **Twitter Feed** | Fan-out on write vs. read, timeline cache |
| **YouTube** | Object store + CDN, async video processing |
| **WhatsApp** | WebSocket connections, E2E encryption |
| **Uber** | Geospatial indexing, real-time matching, surge pricing |
| **Dropbox** | Block deduplication, delta sync, conflict resolution |

---

## 10. Real-World Architecture Examples

### Netflix
- **CDN:** Open Connect serves 95%+ of video traffic
- **Microservices:** 700+ independently deployable services
- **Chaos Engineering:** Chaos Monkey injects failures to test resilience
- **Patterns:** Circuit Breaker (Hystrix), Event Sourcing, CQRS, Bulkhead

### Uber
- **Kafka:** All real-time pipelines (location, surge pricing)
- **CQRS:** Separate write-heavy trip creation from read-heavy queries
- **Saga Pattern:** Trip booking across dispatch, payment, rating
- **Geospatial:** H3 hexagonal indexing for matching

### Twitter
- **Fan-out-on-write:** Precompute tweets into follower timelines
- **Exception:** Celebrities use fan-out-on-read (too many followers)
- **Redis:** Timeline sorted sets
- **Kafka:** Event streaming for all activity

### WhatsApp
- 2B+ users with ~70 engineers at acquisition
- Erlang/BEAM VM for millions of concurrent connections
- Sequence numbers for message ordering
- Signal Protocol for E2E encryption

---

## Quick Reference: Key Numbers

| Metric | Value |
|---|---|
| L1 cache reference | ~0.5 ns |
| Main memory reference | ~100 ns |
| SSD random read | ~150 us |
| HDD seek | ~10 ms |
| Packet: same datacenter | ~0.5 ms |
| Packet: US -> Europe | ~75 ms |
| 99% availability | 87.6 hrs/yr downtime |
| 99.9% availability | 8.76 hrs/yr downtime |
| 99.99% availability | 52.6 min/yr downtime |
| 99.999% availability | 5.26 min/yr downtime |

---

## Summary: Choosing the Right Approach

```
PROBLEM ---> SOLUTION
Handle 10x traffic ---> Horizontal scaling + Load balancer
Reduce DB load ---> Cache (Redis), Read replicas
DB too large ---> Sharding + Consistent hashing
Decouple services ---> Message queue (Kafka, RabbitMQ)
Audit trail ---> Event Sourcing
Scale reads/writes separately ---> CQRS
Distributed transactions ---> Saga pattern
Prevent cascade failures ---> Circuit Breaker + Bulkhead
Fast content delivery ---> CDN
Single API entry point ---> API Gateway
Multiple client types ---> BFF (Backend for Frontend)
Cross-cutting concerns ---> Service Mesh / Sidecar
Migrate legacy system ---> Strangler Fig pattern
```

---

*References: DDIA (Kleppmann), microservices.io, system design handbook, GeeksforGeeks*
