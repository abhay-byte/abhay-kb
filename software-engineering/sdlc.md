---
layout: standalone
title: Software Engineering — SDLC
---

# SDLC — Software Development Life Cycle

> *A comprehensive reference on Software Development Life Cycle for autonomous AI agents and agentic engineering workflows.*
> Based on IEEE Std 830, ISO 9126, CMM, COCOMO, Halstead Metrics

---

## Table of Contents

1. [Introduction to SDLC](#1-introduction-to-sdlc)
2. [Software Process Models](#2-software-process-models)
3. [Requirements Engineering](#3-requirements-engineering)
4. [Software Requirements Specification (SRS)](#4-software-requirements-specification-srs)
5. [Software Design Principles](#5-software-design-principles)
6. [Size & Cost Estimation](#6-size--cost-estimation)
7. [Software Metrics](#7-software-metrics)
8. [Risk Management](#8-risk-management)
9. [Software Testing](#9-software-testing)
10. [Software Quality Models](#10-software-quality-models)
11. [Software Maintenance & Evolution](#11-software-maintenance--evolution)
12. [Key Tools & Notations](#12-key-tools--notations)

---

## 1. Introduction to SDLC

The **Software Development Life Cycle (SDLC)** is a structured process that guides the development of software systems from initial concept through deployment and maintenance. For agentic engineering — autonomous AI agents that design, build, test, and maintain software — SDLC provides the foundational framework for systematic, repeatable, and high-quality software production.

### Key Phases of SDLC

| Phase | Description |
|---|---|
| **Requirements Analysis** | Elicit, analyze, and document stakeholder needs |
| **System Design** | Define architecture, components, interfaces, and data flow |
| **Implementation** | Write code following design specifications and coding standards |
| **Testing** | Verify functionality, performance, reliability through structured testing |
| **Deployment** | Install software on target platforms and make it available to users |
| **Maintenance** | Continuously improve, fix bugs, adapt to changing requirements |

### Why SDLC Matters for Agentic Engineering

- Provides a systematic, repeatable framework for autonomous agents
- Ensures quality through defined verification and validation checkpoints
- Manages complexity by decomposing work into discrete phases
- Enables predictable resource estimation and risk management
- Facilitates collaboration between multiple AI agents and human teams
- Creates auditable documentation trail for compliance and governance

### Software Engineering as a Discipline

Software engineering bridges theory and practice by providing structured methodologies, best practices, and systematic approaches. It emphasizes requirements engineering, design principles, coding standards, rigorous testing, documentation, project management, and risk mitigation.

---

## 2. Software Process Models

Software process models define the stages, activities, and tasks involved in developing software. The choice of model depends on project size, complexity, requirement stability, and team structure.

### Waterfall Model

A linear, sequential approach where each phase must complete before the next begins.

**Phases:** Requirements -> Design -> Implementation -> Testing -> Deployment -> Maintenance

| Pros | Cons |
|---|---|
| Clear structure and milestones | Limited flexibility — changes are difficult once a phase completes |
| Document-driven, easy to manage | Working software appears late in the lifecycle |
| Suitable for stable, well-understood requirements | Late discovery of design flaws |

### Iterative & Incremental Models

Development occurs in repeating cycles, each producing a more complete version. Includes Agile (Scrum, Kanban), Spiral, and RAD approaches.

| Pros | Cons |
|---|---|
| Early feedback and user involvement | Risk of scope creep if changes are not managed |
| Adaptable to changing requirements | Requires disciplined iteration management |
| Reduced risk through incremental delivery | More complex project tracking |

### Agile Model

A flexible, collaborative approach emphasizing individuals, working software, customer collaboration, and responding to change. Delivers working software in short iterations (sprints).

| Pros | Cons |
|---|---|
| Adaptability and rapid delivery | Active customer participation required |
| Frequent customer feedback | May lack comprehensive documentation |
| Early and continuous delivery of value | Difficult to predict final delivery date |

### V-Model (Verification & Validation)

Extends Waterfall by pairing each development phase with a corresponding testing phase. Emphasizes early test planning and quality assurance.

```
Requirements ---> Acceptance Testing
     |
     v
 High-Level Design ---> System Testing
     |
     v
 Detailed Design ---> Integration Testing
     |
     v
  Implementation ---> Unit Testing
```

| Pros | Cons |
|---|---|
| Strong focus on testing and quality | Limited flexibility for requirement changes |
| Well-structured approach | Not suitable for iterative/exploratory projects |
| Test planning begins early | High documentation overhead |

---

## 3. Requirements Engineering

Requirements engineering is the systematic process of **eliciting, analyzing, documenting, validating, and managing** requirements throughout the project lifecycle.

### Types of Requirements

- **Functional Requirements** — what the system should do (features, behaviors, data processing)
- **Non-Functional Requirements** — quality attributes (performance, security, usability, reliability)
- **Domain Requirements** — constraints and rules from the specific application domain
- **Business Rules** — organizational policies that govern system behavior

### Requirements Elicitation Techniques

- Stakeholder interviews and surveys
- Workshops and brainstorming sessions
- Document analysis (existing systems, business processes)
- Prototyping and mockups
- Observation and ethnography
- Use case modeling

### Requirements Analysis

- Identify and resolve conflicts
- Prioritize requirements (MoSCoW: Must have, Should have, Could have, Won't have)
- Model requirements with diagrams (UML, flowcharts)
- Trace requirements to business goals
- Validate feasibility with technical team

---

## 4. Software Requirements Specification (SRS)

An SRS is a **formal document** that defines the complete external behavior of a software system. It serves as a contract between stakeholders and developers.

### IEEE Std 830 SRS Structure

| Section | Content |
|---|---|
| **Introduction** | Purpose, scope, definitions, references, overview |
| **Overall Description** | Product perspective, user characteristics, constraints, assumptions |
| **Specific Requirements** | Functional requirements, external interfaces, performance, logical database, design constraints, software system attributes |
| **Appendices** | Additional supporting information |

### Characteristics of a Good SRS

- **Correct** — accurately represents stakeholder needs
- **Unambiguous** — every statement has one interpretation
- **Complete** — includes all significant requirements
- **Consistent** — no conflicting requirements
- **Verifiable** — testable with objective criteria
- **Modifiable** — easy to update without breaking structure
- **Traceable** — each requirement links to source and design

---

## 5. Software Design Principles

Design principles guide the creation of robust, maintainable, and scalable software architectures.

### Core Principles

- **Modularity** — decompose system into cohesive, loosely-coupled modules
- **Abstraction** — hide implementation details behind clean interfaces
- **Encapsulation** — bundle data and behavior, protect internal state
- **Separation of Concerns** — each module addresses a distinct concern
- **Information Hiding** — hide design decisions that may change
- **Layered Architecture** — organize code into hierarchical layers

### Design Approaches

- **Top-Down Design** — start with high-level system, decompose into subsystems
- **Bottom-Up Design** — build primitive components, compose into larger structures
- **Domain-Driven Design (DDD)** — model software around business domain concepts
- **Contract-First Design** — define interfaces before implementation

---

## 6. Size & Cost Estimation

### Estimation Techniques

| Technique | Description |
|---|---|
| **Expert Judgment** | Experienced professionals estimate based on past projects |
| **Analogous Estimation** | Compare with similar completed projects |
| **Parametric Models** | Use mathematical models (function points, LOC) |
| **Three-Point Estimation** | Optimistic + Most Likely + Pessimistic / 3 |
| **Planning Poker** | Agile team consensus estimation with story points |

### COCOMO (Constructive Cost Model)

COCOMO estimates effort, cost, and schedule based on project size and complexity.

| Model | Description |
|---|---|
| **Basic COCOMO** | Effort = a * (Size)^b where size is in KLOC |
| **Intermediate COCOMO** | Adds cost drivers (product, hardware, personnel, project) |
| **Detailed COCOMO** | Applies intermediate model to each phase separately |

### Function Point Analysis

Measures software size based on functionality delivered:

- External Inputs (user data entry)
- External Outputs (reports, messages)
- External Inquiries (queries, searches)
- Internal Logical Files (data stores)
- External Interface Files (data from other systems)

---

## 7. Software Metrics

### Process Metrics

- **Effort** — person-hours or person-months
- **Schedule** — calendar time to complete milestones
- **Productivity** — output per unit of effort (LOC/hour, FP/person-month)
- **Defect Density** — defects per KLOC or per function point
- **Cycle Time** — time from work start to completion

### Product Metrics

- **Size** — Lines of Code (LOC), Function Points (FP)
- **Complexity** — Cyclomatic complexity, Halstead metrics
- **Cohesion** — degree to which module elements belong together
- **Coupling** — degree of interdependence between modules
- **Test Coverage** — percentage of code exercised by tests

### Halstead Metrics

Based on count of operators and operands in the code:

- **Program Length:** N = N1 + N2 (total operators + operands)
- **Vocabulary:** n = n1 + n2 (unique operators + operands)
- **Volume:** V = N * log2(n)
- **Difficulty:** D = (n1/2) * (N2/n2)
- **Effort:** E = D * V

### Quality Metrics

- **Reliability** — Mean Time Between Failures (MTBF)
- **Availability** — uptime percentage (99.9%, 99.99%)
- **Maintainability** — Mean Time To Repair (MTTR), change impact analysis
- **Performance** — response time, throughput, resource utilization

---

## 8. Risk Management

### Risk Categories

| Category | Examples |
|---|---|
| **Technical** | Unfamiliar technology, complex integrations, scalability issues |
| **Schedule** | Unrealistic timelines, resource shortages, dependency delays |
| **Cost** | Budget overruns, estimation errors, scope creep |
| **Operational** | Deployment failures, environment mismatches, data migration |
| **Security** | Vulnerabilities, data breaches, compliance violations |

### Risk Management Process

1. **Identification** — discover and document potential risks
2. **Analysis** — assess probability and impact (qualitative + quantitative)
3. **Prioritization** — rank risks by severity (Risk Score = Probability * Impact)
4. **Response Planning** — define mitigation, contingency, and avoidance strategies
5. **Monitoring** — track risks throughout the project lifecycle

### Risk Response Strategies

- **Avoid** — eliminate the risk by changing approach
- **Mitigate** — reduce probability or impact
- **Transfer** — shift risk to third party (insurance, outsourcing)
- **Accept** — acknowledge and budget for consequences

---

## 9. Software Testing

### Testing Levels

| Level | Focus | Who Performs |
|---|---|---|
| **Unit Testing** | Individual functions, methods, classes | Developers |
| **Integration Testing** | Interactions between modules | Developers + QA |
| **System Testing** | Complete system behavior | QA Team |
| **Acceptance Testing** | User requirements validation | End Users + QA |

### Testing Types

- **Functional Testing** — does it do what it should? (black-box)
- **Performance Testing** — does it meet speed/scalability requirements?
- **Security Testing** — is it protected against threats?
- **Usability Testing** — is it easy to use?
- **Regression Testing** — did new changes break existing functionality?
- **Smoke Testing** — quick check of critical functionality

### Test Automation

Automated testing is essential for agentic engineering workflows. Key principles:

- **Test Pyramid:** Unit tests (many) > Integration tests (some) > E2E tests (few)
- **Continuous Testing:** Tests run automatically on every commit
- **Deterministic Tests:** Same input always produces same result
- **Isolation:** Tests should not depend on each other or external state

---

## 10. Software Quality Models

### ISO 9126 Quality Model

| Characteristic | Sub-Characteristics |
|---|---|
| **Functionality** | Suitability, accuracy, interoperability, security |
| **Reliability** | Maturity, fault tolerance, recoverability |
| **Usability** | Understandability, learnability, operability |
| **Efficiency** | Time behavior, resource utilization |
| **Maintainability** | Analyzability, changeability, stability, testability |
| **Portability** | Adaptability, installability, conformance, replaceability |

### CMM — Capability Maturity Model

| Level | Description |
|---|---|
| **Level 1 — Initial** | Ad-hoc processes, unpredictable outcomes |
| **Level 2 — Managed** | Project-level processes, repeatable practices |
| **Level 3 — Defined** | Organization-wide standard processes |
| **Level 4 — Quantitatively Managed** | Process measured and controlled with metrics |
| **Level 5 — Optimizing** | Continuous process improvement |

---

## 11. Software Maintenance & Evolution

### Types of Maintenance

- **Corrective** — fixing bugs and defects
- **Adaptive** — adapting to environmental changes (new OS, hardware, regulations)
- **Perfective** — adding new features, improving performance
- **Preventive** — preventing future issues (refactoring, documentation updates)

### Maintenance Challenges

- **Code Entropy** — code quality degrades over time without active management
- **Knowledge Loss** — original developers may no longer be available
- **Legacy Dependencies** — outdated libraries, frameworks, and platforms
- **Documentation Gap** — documentation diverges from actual implementation

### Evolution Strategies

- **Refactoring** — restructure code without changing external behavior
- **Reengineering** — rebuild system components with modern approaches
- **Reverse Engineering** — analyze existing system to understand its design
- **Strangler Fig Pattern** — gradually replace legacy components with new ones

---

## 12. Key Tools & Notations

### Modeling & Design Tools

| Tool | Purpose |
|---|---|
| **UML (Unified Modeling Language)** | Visual modeling of software systems |
| **ER Diagrams** | Entity-relationship data modeling |
| **DFD (Data Flow Diagrams)** | System data flow and processing |
| **Flowcharts** | Algorithm and process visualization |
| **Architecture Decision Records (ADR)** | Documenting architectural decisions |

### Project Management Tools

- JIRA, Linear, Trello — issue and sprint tracking
- Confluence, Notion — documentation and knowledge management
- Git, GitHub, GitLab — version control and collaboration
- Jenkins, GitHub Actions, GitLab CI — continuous integration

### Agentic Engineering Considerations

For autonomous AI agents, the following tools and practices are particularly relevant:

- **Automated Testing Frameworks** — pytest, Jest, Selenium
- **CI/CD Pipelines** — automated build, test, and deployment
- **Infrastructure as Code** — Terraform, Ansible, Docker
- **Monitoring & Observability** — Prometheus, Grafana, OpenTelemetry
- **Automated Documentation** — doc generators, API documentation tools

---

*References: IEEE Std 830, ISO 9126, CMM, COCOMO, Halstead Metrics*
