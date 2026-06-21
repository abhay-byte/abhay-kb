---
layout: standalone
title: Software Engineering — Maintenance
---

# Maintenance

> *Comprehensive reference on software maintenance models, evolution, reverse engineering, and legacy system modernization.*
> Models: Boehm ACT, Belady-Lehman, CMM Level 5

---

## Table of Contents

1. [Software Maintenance Fundamentals](#1-software-maintenance-fundamentals)
2. [Categories of Maintenance](#2-categories-of-maintenance)
3. [Maintenance Process & Activities](#3-maintenance-process--activities)
4. [Maintenance Cost Models](#4-maintenance-cost-models)
5. [Software Evolution (Lehman's Laws)](#5-software-evolution-lehmans-laws)
6. [Reverse Engineering](#6-reverse-engineering)
7. [Software Re-engineering & Legacy Modernization](#7-software-re-engineering--legacy-modernization)
8. [Configuration Management & Version Control](#8-configuration-management--version-control)
9. [Software Documentation](#9-software-documentation)
10. [Retirement & Decommissioning](#10-retirement--decommissioning)

---

## 1. Software Maintenance Fundamentals

Software maintenance is the process of **modifying a software system after delivery** to correct faults, improve performance, adapt to changing environments, and prevent future issues. It is the longest and most expensive phase of the SDLC — often consuming 60-90% of total lifecycle costs.

### Key Maintenance Objectives

- Ensure continued operational effectiveness
- Adapt to evolving environments (OS, hardware, regulations)
- Fix defects discovered post-release
- Enhance functionality to meet emerging needs
- Improve system performance, security, and usability
- Preserve institutional knowledge through documentation

### Maintenance Challenges

| Challenge | Impact |
|---|---|
| **Code Entropy** | Code quality degrades over time without active management |
| **Knowledge Loss** | Original developers may no longer be available |
| **Legacy Dependencies** | Outdated libraries, frameworks, and platforms |
| **Documentation Gap** | Documentation diverges from actual implementation |
| **Team Turnover** | New team members lack historical context |
| **Technical Debt** | Shortcuts accumulate, making changes increasingly expensive |

---

## 2. Categories of Maintenance

| Category | Description | Example | Effort % |
|---|---|---|---|
| **Corrective** | Fixing bugs and defects discovered post-release | Fixing a null pointer exception in production | ~20% |
| **Adaptive** | Adapting to environmental changes | Upgrading to a new OS version, new database driver | ~25% |
| **Perfective** | Adding new features, improving performance | Adding a new report, optimizing query speed | ~50% |
| **Preventive** | Preventing future issues before they occur | Refactoring, code cleanup, documentation updates | ~5% |

### Corrective Maintenance

Fixes defects found after the software is in use. Includes:

- Emergency fixes (critical production bugs)
- Routine bug fixes (non-critical defects from backlog)
- Patch releases for reported issues

### Adaptive Maintenance

Modifications required when the software's external environment changes:

- Operating system upgrades
- Database platform migrations
- Hardware changes
- Regulatory and compliance updates
- Third-party API deprecations

### Perfective Maintenance

The largest category — enhancements to improve the software:

- New features and functionality
- Performance optimization
- Usability improvements
- UI/UX refinements
- Code restructuring for better maintainability

### Preventive Maintenance

Proactive measures to reduce future maintenance costs:

- Refactoring (improve structure without changing behavior)
- Code reviews and quality improvements
- Test coverage expansion
- Documentation updates
- Dependency upgrades (before they become critical)

---

## 3. Maintenance Process & Activities

### Maintenance Process Flow

```
Change Request -> Impact Analysis -> Planning -> Implementation
    -> Review -> Testing -> Deployment -> Verification
```

### Key Activities

| Activity | Description |
|---|---|
| **Change Request Management** | Log, categorize, and prioritize incoming requests |
| **Impact Analysis** | Assess scope, cost, risk, and affected components |
| **Planning** | Schedule changes, assign resources, define acceptance criteria |
| **Implementation** | Code changes following standards and guidelines |
| **Code Review** | Peer review for quality, correctness, consistency |
| **Testing** | Unit, integration, regression, and acceptance testing |
| **Deployment** | Release changes to production using deployment strategies |
| **Verification** | Post-deployment validation and monitoring |

### Maintenance Priority Levels

| Priority | Description | Response Time |
|---|---|---|
| **Critical** | System down, data loss | Within 1 hour |
| **High** | Major feature broken, no workaround | Within 4 hours |
| **Medium** | Feature partially broken, workaround available | Within 24 hours |
| **Low** | Cosmetic issue, minor enhancement | Next release cycle |

---

## 4. Maintenance Cost Models

### Boehm's ACT (Annual Change Traffic)

ACT measures the fraction of a software product's source instructions that undergo change during a year.

`ACT = (Total Lines Changed + Added + Deleted) / Total Lines`

**Cost Estimation:**
`Annual Maintenance Cost = Development Cost × ACT`

**Typical ACT values:**

- Stable system: 10-20% per year
- Active development: 30-50% per year
- Rapidly evolving: 60%+ per year

### Belady-Lehman Model

Cost increases exponentially with lack of maintenance:

`Maintenance Cost = C × exp(D × Time Since Last Redesign)`

Where:

- C = initial maintenance cost
- D = design deterioration factor
- Time = elapsed since last significant redesign

This model suggests that periodic major redesigns are more economical than continuous small patches in the long run.

### Cost Factors

| Factor | Impact on Cost |
|---|---|
| **Code Complexity** | Higher complexity = higher cost |
| **Documentation Quality** | Poor documentation = higher cost |
| **Staff Experience** | Less experienced = higher cost |
| **Module Age** | Older modules = higher cost |
| **Test Coverage** | Low coverage = higher risk, higher cost |

---

## 5. Software Evolution (Lehman's Laws)

Lehman formulated eight laws describing the inevitable evolution of software systems over time:

| Law | Description |
|---|---|
| **1. Continuing Change** | A system must be continually adapted or it becomes progressively less satisfactory |
| **2. Increasing Complexity** | As a system evolves, its complexity increases unless work is done to maintain or reduce it |
| **3. Self-Regulation** | System evolution processes are self-regulating with statistically invariant distributions |
| **4. Conservation of Organizational Stability** | The average effective global activity rate in an evolving system is invariant over the product lifetime |
| **5. Conservation of Familiarity** | The incremental growth (satisfaction/decline) of a system is regulated by familiarity constraints |
| **6. Continuing Growth** | The functional capability of a system must be continually increased to maintain user satisfaction |
| **7. Declining Quality** | The quality of a system will appear to decline unless it is rigorously maintained and adapted |
| **8. Feedback System** | Evolution processes are multi-level, multi-loop feedback systems |

### Practical Implications

- **Plan for change** — architecture must accommodate evolution
- **Combat complexity** — active refactoring is mandatory, not optional
- **Invest in quality** — without maintenance, quality inevitably declines
- **Accept continuous growth** — systems naturally expand; plan capacity accordingly

---

## 6. Reverse Engineering

Reverse engineering is the process of **analyzing a system to identify its components and their relationships** without modifying it. It recovers design information from existing code or binaries.

### Goals

- Understand how a system works when documentation is missing
- Discover hidden dependencies and side effects
- Extract business rules embedded in legacy code
- Prepare for re-engineering or migration
- Identify security vulnerabilities

### Techniques

| Technique | Description | Tools |
|---|---|---|
| **Static Analysis** | Analyze code without execution | SonarQube, IDA Pro |
| **Dynamic Analysis** | Analyze code during execution | strace, ltrace, Wireshark |
| **Decompilation** | Convert binary to high-level code | Ghidra, IDA Pro |
| **Disassembly** | Convert binary to assembly | objdump, radare2 |
| **Call Graph Analysis** | Map function call relationships | Doxygen, CodeViz |
| **Dependency Analysis** | Identify module dependencies | JDepend, NDepend |

### Reverse Engineering Process

1. **Information Extraction** — gather all available data (source, binaries, docs)
2. **Abstraction Generation** — create models at higher abstraction levels
3. **Design Recovery** — reconstruct design decisions and rationale

---

## 7. Software Re-engineering & Legacy Modernization

Re-engineering is the **examination and alteration of a system to reconstitute it in a new form** with improved quality, maintainability, or performance.

### Re-engineering Process

```
Reverse Engineering (understand current system)
       |
       v
Restructuring (improve structure without changing function)
       |
       v
Forward Engineering (create improved version)
```

### Legacy Modernization Strategies

| Strategy | Description | Risk | Cost |
|---|---|---|---|
| **Wrap** | Add an API layer around legacy system | Low | Low |
| **Rehost (Lift & Shift)** | Move to new infrastructure without changes | Low | Medium |
| **Replatform** | Move to managed platform (e.g., VMs to containers) | Medium | Medium |
| **Refactor** | Restructure code without changing external behavior | Medium | Medium-High |
| **Rearchitect** | Redesign architecture while preserving functionality | High | High |
| **Rebuild** | Rewrite from scratch | Very High | Very High |
| **Replace** | Replace with COTS or SaaS solution | Low-Medium | Medium |

### Strangler Fig Pattern

Gradually migrate legacy functionality to new services:

1. Route specific features to new service
2. Keep remaining traffic on legacy system
3. Remove migrated code from legacy system
4. Repeat until legacy system is empty

---

## 8. Configuration Management & Version Control

### Configuration Management (CM)

CM tracks and controls changes to software artifacts throughout the lifecycle.

**Key Functions:**

- **Identification** — uniquely identify all configuration items (CI)
- **Version Control** — track versions of all artifacts
- **Change Control** — manage changes to baselines
- **Auditing** — verify that what's documented matches reality
- **Status Accounting** — report on the status of CIs

### Version Control Best Practices

| Practice | Description |
|---|---|
| **Commit often** | Small, atomic commits with descriptive messages |
| **Branch strategy** | GitFlow, GitHub Flow, or Trunk-based development |
| **Tag releases** | Semantic versioning (v1.2.3) |
| **Code reviews** | All changes reviewed before merging |
| **Signed commits** | GPG-sign commits for authenticity |
| **git bisect** | Binary search to find the commit that introduced a bug |

### Semantic Versioning

`MAJOR.MINOR.PATCH` (e.g., v2.5.1)

| Increment | When |
|---|---|
| **MAJOR** | Breaking API changes |
| **MINOR** | New features, backward compatible |
| **PATCH** | Bug fixes, backward compatible |

---

## 9. Software Documentation

### Documentation Types

| Type | Purpose | Audience |
|---|---|---|
| **User Documentation** | How to install, configure, and use the software | End users |
| **System Documentation** | Architecture, design, and internals | Developers, maintainers |
| **Operations Documentation** | Deployment, monitoring, runbooks | DevOps, SREs |
| **API Documentation** | Interface specifications | Integrators, developers |

### Documentation Best Practices

- **Treat docs like code** — version-controlled, reviewed, tested
- **Keep docs close to code** — README files, docstrings, ADRs
- **Automate generation** — API docs from annotations, changelogs from commits
- **Document why, not what** — code expresses what; docs explain why
- **Living documentation** — update alongside code changes
- **Architecture Decision Records (ADR)** — document design decisions and context

---

## 10. Retirement & Decommissioning

### When to Retire a System

- No longer meets business needs
- Maintenance costs exceed replacement cost
- Technology is obsolete and unsupported
- Regulatory or compliance requirements change
- A replacement system is operational

### Decommissioning Process

1. **Assessment** — evaluate data, dependencies, and usage
2. **Data Migration** — archive or migrate business data
3. **User Communication** — notify users of timeline and transition plan
4. **System Shutdown** — gracefully terminate services
5. **Verification** — confirm no remaining dependencies or active users
6. **Cleanup** — de-provision infrastructure, remove credentials

### Decommissioning Checklist

- [ ] All data archived or migrated
- [ ] Dependencies documented and redirected
- [ ] Users notified and transitioned
- [ ] Infrastructure de-provisioned
- [ ] Code archived in version control
- [ ] Documentation preserved
- [ ] DNS and load balancer entries removed
- [ ] Secrets and credentials rotated

---

*References: Boehm ACT, Belady-Lehman, Lehman's Laws, CMM Level 5, IEEE Standard for Software Maintenance*

---

## Sources

- [college-prep-se-notes-all](source/college-prep-se-notes-all.md)
- [college-prep-se-root](source/college-prep-se-root.md)
- [college-prep-se-textbook-aggarwal](source/college-prep-se-textbook-aggarwal.md)
- [college-prep-se-textbook-pressman](source/college-prep-se-textbook-pressman.md)
