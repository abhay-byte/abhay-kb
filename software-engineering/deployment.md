---
layout: standalone
title: Software Engineering — Deployment
---

# Deployment

> *Comprehensive reference on software deployment strategies, release management, CI/CD, and infrastructure automation.*
> Models: DevOps, CMM Level 5

---

## Table of Contents

1. [Deployment Fundamentals](#1-deployment-fundamentals)
2. [Deployment Strategies & Patterns](#2-deployment-strategies--patterns)
3. [Release Management](#3-release-management)
4. [CI/CD Pipelines for Deployment](#4-cicd-pipelines-for-deployment)
5. [Infrastructure as Code (IaC)](#5-infrastructure-as-code-iac)
6. [Containerization & Orchestration](#6-containerization--orchestration)
7. [Monitoring, Observability & Incident Response](#7-monitoring-observability--incident-response)
8. [Rollback Strategies & Disaster Recovery](#8-rollback-strategies--disaster-recovery)
9. [Configuration Management](#9-configuration-management)

---

## 1. Deployment Fundamentals

Software deployment is the process of making a software system available for use. It encompasses all activities that make the software operational on target environments, from installation and configuration through activation and verification. Deployment is a critical SDLC phase that directly impacts user experience, system reliability, and business continuity.

### Key Deployment Objectives

- Zero or minimal downtime during deployment
- Consistent and repeatable deployment process across environments
- Rapid recovery in case of deployment failure
- Auditable trail of changes and deployments
- Environment parity between development, staging, and production
- Secure handling of credentials, secrets, and configuration

### Deployment Environments

| Environment | Purpose |
|---|---|
| **Development** | Local machines or shared dev servers. Frequent, unstable changes. Auto-deployed from feature branches. |
| **Testing/QA** | Dedicated environment for test execution. Deployed from integration branches. |
| **Staging** | Production-like environment. Final validation before release. Mirrors production configuration, data subset. |
| **Production** | Live environment serving real users. Controlled, gated deployments with monitoring. |
| **DR (Disaster Recovery)** | Geographically separate environment for failover. Synchronized data and configuration. |

### Environment Parity Principle

Environments should be as identical as possible. Differences between staging and production are the #1 cause of deployment failures. Use identical OS, middleware, library versions, configuration, and data volume.

### Deployment Deliverables

- Executable binaries / compiled artifacts
- Configuration files (environment-specific)
- Database migration scripts
- Deployment runbook / playbook
- Health check endpoints and verification procedures
- Rollback plan and scripts
- Release notes and changelog

---

## 2. Deployment Strategies & Patterns

Choosing the right deployment strategy depends on risk tolerance, system architecture, downtime requirements, and rollback capabilities.

### Big Bang (Recreate)

All instances are updated simultaneously by replacing the old version with the new one.

| Pros | Cons |
|---|---|
| Simple and fast | Significant downtime |
| Straightforward rollback (full revert) | High risk — all-or-nothing |

Suitable for low-traffic systems or scheduled maintenance windows.

### Rolling Update

Instances are updated one by one (or in batches). Old and new versions coexist during deployment.

| Pros | Cons |
|---|---|
| Zero downtime | Slow deployment time |
| Gradual rollout limits blast radius | Must support backward compatibility (API, DB schema) |

Common in Kubernetes, AWS ECS, and load-balanced environments.

### Blue-Green Deployment

Two identical environments (Blue = current, Green = new). Traffic is switched instantly from Blue to Green.

| Pros | Cons |
|---|---|
| Instant switchover and rollback (flip back to Blue) | Requires 2x infrastructure cost during transition |
| Full environment validation before cutover | |

Ideal for critical systems where downtime is unacceptable.

### Canary Release

New version is rolled out to a small subset of users first, then gradually expanded.

| Pros | Cons |
|---|---|
| Real user validation with minimal risk | Requires sophisticated traffic routing and monitoring |
| Gradual exposure; halt rollout if issues detected | |

Common in SaaS, mobile apps, and web services.

### Feature Flags (Feature Toggles)

Code is deployed with features hidden behind flags; features are enabled for specific users or percentages.

| Pros | Cons |
|---|---|
| Decouple deployment from release | Flag management complexity |
| Instant feature enable/disable without redeployment | Technical debt from stale flags |
| Trunk-based development enabled | |

---

## 3. Release Management

Release management governs the **planning, scheduling, and controlling** of software builds through different stages and environments.

### Release Process

1. **Plan** — define scope, timeline, and approval gates
2. **Build** — create release artifacts from tagged source
3. **Test** — execute regression, integration, and acceptance tests
4. **Stage** — deploy to staging for final validation
5. **Approve** — obtain sign-off from stakeholders
6. **Deploy** — roll out to production using chosen strategy
7. **Verify** — confirm deployment success with health checks and monitoring
8. **Release** — make the release visible to all users (if feature-flagged, enable the flag)

### Release Types

| Type | Frequency | Risk | Examples |
|---|---|---|---|
| **Major** | Quarterly | High | New architecture, breaking changes |
| **Minor** | Monthly | Medium | New features, improvements |
| **Patch** | Weekly/Daily | Low | Bug fixes, security patches |
| **Hotfix** | As needed | Critical | Emergency production fixes |

### Release Gates

Quality checkpoints that must pass before promotion to the next environment:

- Code review approval
- All tests passing (unit, integration, E2E)
- Security scan passed
- Performance benchmarks met
- Stakeholder sign-off
- Change advisory board (CAB) approval for critical systems

---

## 4. CI/CD Pipelines for Deployment

### CI/CD Pipeline Stages

```
Source -> Build -> Test -> Package -> Stage -> Deploy -> Verify
```

| Stage | Activities |
|---|---|
| **Source** | Code commit, branch trigger, webhook |
| **Build** | Compile, dependency resolution, static analysis |
| **Test** | Unit tests, integration tests, code coverage |
| **Package** | Create artifact (Docker image, binary, zip), version tag |
| **Stage** | Deploy to staging, smoke tests, integration validation |
| **Deploy** | Roll out to production using chosen strategy |
| **Verify** | Health checks, monitoring alerts, synthetic tests |

### CI/CD Best Practices

- **Commit early, commit often** — small, frequent changes reduce integration risk
- **Build once, deploy many** — identical artifact progresses through all environments
- **Immutable artifacts** — never modify a built artifact; rebuild instead
- **Fail fast** — stop the pipeline immediately on failure; notify the team
- **Self-service** — teams should own their own pipelines
- **Security scanning** — integrate SAST, dependency scanning, container scanning

### Tools

| Category | Tools |
|---|---|
| **CI/CD Platforms** | Jenkins, GitHub Actions, GitLab CI, CircleCI, ArgoCD |
| **Artifact Repositories** | Docker Hub, ECR, Artifactory, Nexus |
| **Secret Management** | Vault, AWS Secrets Manager, SOPS |

---

## 5. Infrastructure as Code (IaC)

IaC manages infrastructure (servers, networks, databases) through **machine-readable definition files** rather than manual configuration.

### Benefits

- **Repeatable** — same configuration produces same environment every time
- **Version-controlled** — infrastructure changes go through code review
- **Automated** — no manual SSH, no click-ops
- **Self-documenting** — configuration files document the infrastructure
- **Disposable** — recreate environments instantly

### IaC Approaches

| Approach | Description | Tools |
|---|---|---|
| **Declarative (Desired State)** | Define what the infrastructure should look like; tool makes it so | Terraform, CloudFormation, Pulumi |
| **Imperative (Step-by-Step)** | Define the specific steps to achieve the desired state | Ansible, Chef, Puppet |

### IaC Best Practices

- Store configurations in version control
- Use modules for reusable infrastructure components
- Plan changes before applying (terraform plan)
- Use remote state with locking
- Validate IaC with static analysis and policy as code

---

## 6. Containerization & Orchestration

### Containers

Containers package application code with its dependencies into a **single, portable unit** that runs consistently across environments.

**Benefits:** Consistency, isolation, lightweight, fast startup, reproducible builds.

### Container Images

- **Base image** — OS and runtime (Alpine, Ubuntu, node:18)
- **Application layer** — code, libraries, configuration
- **Immutable tag** — never use `:latest` in production; use commit SHA or semantic version

### Orchestration (Kubernetes)

Kubernetes automates deployment, scaling, and management of containerized applications.

| Component | Purpose |
|---|---|
| **Pod** | Smallest deployable unit (one or more containers) |
| **Deployment** | Declarative update for Pods and ReplicaSets |
| **Service** | Stable network endpoint for a set of Pods |
| **Ingress** | External HTTP/HTTPS routing to Services |
| **ConfigMap / Secret** | Configuration and sensitive data management |

### Container Best Practices

- Use minimal base images (distroless, Alpine)
- Run as non-root user
- Scan images for vulnerabilities
- Pin dependency versions
- Keep layers small (combine RUN commands)

---

## 7. Monitoring, Observability & Incident Response

### Observability Pillars

| Pillar | Description | Tools |
|---|---|---|
| **Metrics** | Numerical measurements over time (CPU, latency, error rate) | Prometheus, Datadog, CloudWatch |
| **Logs** | Structured or unstructured event records | ELK Stack, Loki, Splunk |
| **Traces** | End-to-end request paths across distributed services | Jaeger, OpenTelemetry, Zipkin |

### Key Metrics to Monitor

- **Latency** — p50, p95, p99 response times
- **Traffic** — requests per second (RPS)
- **Errors** — error rate, HTTP 5xx count
- **Saturation** — CPU, memory, disk, connection pool usage (USE Method)

### Incident Response Lifecycle

1. **Detect** — alert triggers based on metric thresholds
2. **Respond** — acknowledge, assess severity, assemble response team
3. **Mitigate** — stop the bleeding (rollback, feature flag off, scale up)
4. **Resolve** — deploy the fix
5. **Learn** — postmortem, root cause analysis, action items

### Alerting Best Practices

- Alert on symptoms, not causes
- Define clear escalation paths
- Use runbooks for common incidents
- Avoid alert fatigue — only alert when human action is needed

---

## 8. Rollback Strategies & Disaster Recovery

### Rollback Strategies

| Strategy | Description | Speed |
|---|---|---|
| **Recreate (Big Bang)** | Deploy previous version over current | Fast |
| **Blue-Green Flip** | Switch traffic back to Blue environment | Instant |
| **Rolling Rollback** | Reverse the rolling update | Moderate |
| **Feature Flag Disable** | Turn off the offending feature | Instant |

### Disaster Recovery (DR) Strategies

| Strategy | RPO (Data Loss) | RTO (Downtime) | Cost |
|---|---|---|---|
| **Backup & Restore** | Hours | Hours | Low |
| **Pilot Light** | Minutes | Minutes | Medium |
| **Warm Standby** | Seconds | Minutes | Medium-High |
| **Active-Active Multi-Region** | Near zero | Seconds | High |

### Disaster Recovery Playbook

- Documented runbooks for each failure scenario
- Regular DR drills (quarterly minimum)
- Automated failover testing
- Clear escalation and communication plan

---

## 9. Configuration Management

Configuration management ensures that the **behavior of a system is predictable, consistent, and auditable** across all environments.

### Configuration Types

| Type | Examples |
|---|---|
| **Application Config** | Database URLs, feature flags, logging levels |
| **Infrastructure Config** | Instance sizes, network CIDRs, region |
| **Secrets** | API keys, passwords, certificates |
| **Runtime Config** | Environment variables, startup parameters |

### Configuration Best Practices

- **Separate config from code** — never hardcode environment-specific values
- **Use environment variables** or config files loaded at runtime
- **Version control** configuration templates (not secrets)
- **Secret management** — use Vault, AWS Secrets Manager, or encrypted variables
- **Validation** — validate configuration at startup (fail fast on misconfiguration)
- **Audit trail** — track who changed what configuration and when

---

*References: DevOps, CMM Level 5, Kubernetes Documentation, Site Reliability Engineering (Google)*

---

## Sources

- [college-prep-se-notes-all](source/college-prep-se-notes-all.md)
- [college-prep-se-root](source/college-prep-se-root.md)
- [college-prep-se-textbook-integral](source/college-prep-se-textbook-integral.md)
