---
layout: standalone
title: System Design
---

# System Design

> *Comprehensive reference on software architecture, system design principles, notations, and modeling.*
> Standards: IEEE 1016-1998 (SDD), UML 2.5, C4 Model

---

## Table of Contents

1. [System Design Fundamentals](#1-system-design-fundamentals)
2. [Software Architecture Styles](#2-software-architecture-styles)
3. [Design Strategies: Top-Down, Bottom-Up, Hybrid](#3-design-strategies-top-down-bottom-up-hybrid)
4. [Function-Oriented Design](#4-function-oriented-design)
5. [Object-Oriented Design](#5-object-oriented-design)
6. [User Interface Design](#6-user-interface-design)
7. [Design Notations & Modeling Diagrams](#7-design-notations--modeling-diagrams)
8. [Data Flow Diagrams (DFD)](#8-data-flow-diagrams-dfd)
9. [Entity-Relationship Diagrams (ERD)](#9-entity-relationship-diagrams-erd)
10. [UML Diagrams](#10-uml-diagrams)
11. [Data Dictionary](#11-data-dictionary)
12. [Software Design Document (SDD) IEEE 1016](#12-software-design-document-sdd-ieee-1016)
13. [Design for Non-Functional Requirements](#13-design-for-non-functional-requirements)
14. [Agentic System Design Considerations](#14-agentic-system-design-considerations)

---

## 1. System Design Fundamentals

System design is the process of defining the **architecture, components, modules, interfaces, and interactions** of a software system to satisfy specified requirements. It transforms requirements into a blueprint for construction.

**Software Design (IEEE):** The process of defining the architecture, components, interfaces, and other characteristics of a system or component. Also defined as the result of that process.

### Design vs Architecture

| Aspect | Architecture | Design |
|---|---|---|
| **Scope** | High-level structure, system-wide decisions | Module-level, component internals |
| **Concerns** | Quality attributes, constraints, trade-offs | Algorithms, data structures, APIs |
| **Stakeholders** | Architects, CTO, cross-team | Developers, team leads |
| **Decisions** | Hard to change (architecturally significant) | Easier to refactor |

### Design Quality Attributes

A good design must be:

- **Correct & Complete** — Satisfies all functional and non-functional requirements
- **Understandable** — Clear to developers, testers, and maintainers
- **Maintainable** — Easy to modify and extend without breaking existing functionality
- **At the right level** — Appropriate abstraction for the intended audience
- **Traceable** — Links back to requirements and forward to implementation

---

## 2. Software Architecture Styles

An architecture style defines the **family of systems** in terms of their structure, components, connectors, and constraints. The choice of style impacts scalability, maintainability, and deployment.

### Layered (n-Tier) Architecture

Organizes the system into horizontal layers, each with a specific responsibility. Each layer depends only on the layer below it.

| Layer | Responsibility |
|---|---|
| **Presentation** | User interface, client-side logic |
| **Business Logic** | Domain rules, workflows |
| **Data Access** | Database operations, ORM |
| **Database** | Data persistence |

- Separation of concerns — each layer has a single responsibility
- Easy to develop, test, and maintain independently
- Can suffer from layer leakage and performance overhead

### Microservices Architecture

Decomposes the system into small, independently deployable services. Each service owns its data and communicates via APIs.

- Independent deployment and scaling per service
- Technology heterogeneity — each service can use different tech stacks
- Complex inter-service communication and data consistency
- Requires DevOps maturity, monitoring, and observability

### Event-Driven Architecture

Components communicate through events. Producers emit events; consumers react. Loosely coupled via message broker.

- Highly scalable and responsive
- Loose coupling between producers and consumers
- Complex event handling and eventual consistency
- Tools: Kafka, RabbitMQ, AWS SNS/SQS, Azure Event Grid

### Microkernel (Plugin) Architecture

Core system provides minimal functionality. Extensions/plugins add features.

- Extensible and customizable
- Well-suited for product families
- Plugin contract management complexity
- Examples: Eclipse IDE, VS Code, Jira

### Pipe-and-Filter Architecture

Data flows through a sequence of processing steps (filters) connected by pipes.

- Reusable filters, easy to compose new pipelines
- Parallel execution possible
- Overhead from data transformation between filters

### Architecture Style Comparison

| Style | Scalability | Maintainability | Complexity | Use Case |
|---|---|---|---|---|
| Layered | Moderate | High | Low | Enterprise apps |
| Microservices | Very High | Moderate | High | Large-scale distributed systems |
| Event-Driven | Very High | Moderate | High | Real-time processing |
| Microkernel | Moderate | Very High | Medium | Extensible products |
| Pipe-and-Filter | Moderate | High | Low | Data processing |

---

## 3. Design Strategies: Top-Down, Bottom-Up, Hybrid

### Top-Down Design

Start with the **high-level system**, then decompose it into subsystems, modules, and components.

- Clear structure and hierarchy
- Works well when requirements are well-understood
- May miss low-level optimization opportunities
- Requires accurate high-level decomposition

### Bottom-Up Design

Build **primitive components first**, then compose them into larger structures.

- Focuses on reusability from the start
- Supports parallel development
- Integration challenges at higher levels
- Risk of abstraction mismatch

### Hybrid Design

Combine both approaches. Use top-down for architectural decomposition and bottom-up for reusable component libraries.

- Leverages strengths of both approaches
- Requires careful coordination
- Common in practice for complex systems

---

## 4. Function-Oriented Design

Focuses on **functions or processes** as the primary decomposition unit. The system is divided into functions that transform inputs to outputs.

### Key Concepts

- **Functional decomposition** — break down complex functions into simpler ones
- **Data flow** — track how data moves between functions
- **Data store** — persistent data repositories
- **Process specification** — detailed logic for each function

### When to Use

- Data processing systems (ETL, compilers)
- Systems with clear input/output transformations
- Legacy system modernization

### Limitations

- Data and behavior are separated
- Changes in data structure propagate across many functions
- Less suitable for interactive or stateful systems

---

## 5. Object-Oriented Design

Organizes the system as a collection of **objects** that encapsulate data and behavior. Each object is an instance of a class.

### Key Concepts

- **Encapsulation** — bundle data and methods; hide internal state
- **Inheritance** — derive new classes from existing ones
- **Polymorphism** — same interface, different implementations
- **Abstraction** — expose only what is necessary

### Design Process

1. Identify objects and classes from requirements
2. Define attributes and methods for each class
3. Establish relationships (inheritance, association, composition)
4. Design interfaces and abstract classes
5. Apply design patterns where appropriate

### When to Use

- Complex domain logic with rich relationships
- Systems requiring extensibility and maintainability
- Interactive applications with complex state

---

## 6. User Interface Design

UI design focuses on the interaction between users and the system.

### Design Principles

- **Consistency** — similar actions produce similar results
- **Feedback** — inform users of system state and results
- **Affordance** — visual cues suggest how elements are used
- **Error Prevention** — design to minimize mistakes
- **Recovery** — easy undo and error resolution
- **User Control** — users control the interaction flow

### UI Design Process

1. **User Research** — understand users, tasks, and context
2. **Information Architecture** — structure content and navigation
3. **Wireframing** — low-fidelity layout and flow
4. **Prototyping** — interactive mockups
5. **Visual Design** — colors, typography, branding
6. **Usability Testing** — validate with real users

---

## 7. Design Notations & Modeling Diagrams

### Purpose of Modeling

- Visualize system structure and behavior
- Communicate design intent across teams
- Analyze and validate design decisions
- Document architecture for maintenance

### The C4 Model

A hierarchical approach to visualizing software architecture:

| Level | Diagram | Audience |
|---|---|---|
| **Level 1: Context** | System context diagram | Technical and non-technical stakeholders |
| **Level 2: Containers** | Container diagram | Technical stakeholders, developers |
| **Level 3: Components** | Component diagram | Developers |
| **Level 4: Code** | Class/sequence diagram | Developers |

---

## 8. Data Flow Diagrams (DFD)

DFDs represent the **flow of data** through a system. They show how data enters, is processed, stored, and leaves the system.

### DFD Symbols (Yourdon/DeMarco)

| Symbol | Name | Description |
|---|---|---|
| Circle/oval | Process | Transforms input data to output |
| Rectangle | External Entity | External source or destination of data |
| Open rectangle | Data Store | Repository of data |
| Arrow | Data Flow | Movement of data between elements |

### DFD Levels

- **Level 0 (Context Diagram)** — single process, all external entities
- **Level 1** — decomposes the main process into major subsystems
- **Level 2** — further decomposition of each major subsystem

### Guidelines

- All data flows must start or end at a process
- Data stores must have both incoming and outgoing flows
- External entities should not connect directly to each other
- Maintain balance between levels (same inputs/outputs)

---

## 9. Entity-Relationship Diagrams (ERD)

ERDs model the **data entities** in a system and the **relationships** between them.

### Components

| Component | Notation | Description |
|---|---|---|
| **Entity** | Rectangle | A real-world object or concept (e.g., Customer, Order) |
| **Attribute** | Ellipse | Properties of an entity (e.g., name, email) |
| **Relationship** | Diamond | Association between entities (e.g., places, belongs to) |

### Relationship Types

- **One-to-One (1:1)** — each entity instance relates to exactly one of the other
- **One-to-Many (1:N)** — one entity instance relates to many of the other
- **Many-to-Many (M:N)** — many instances relate to many instances

### Cardinality Notation (Chen vs Crow's Foot)

| Chen | Crow's Foot | Meaning |
|---|---|---|
| 1 | \|\|--\|\| | Exactly one |
| M | \|\|--< | Many |
| Optional | o--\|\| | Zero or one |

---

## 10. UML Diagrams

UML (Unified Modeling Language) 2.5 provides a standardized set of diagrams for modeling software systems.

### Structure Diagrams (Static View)

| Diagram | Purpose |
|---|---|
| **Class Diagram** | Classes, attributes, methods, and relationships |
| **Component Diagram** | Physical components and their dependencies |
| **Deployment Diagram** | Hardware nodes and software deployment |
| **Package Diagram** | Grouping of model elements |

### Behavior Diagrams (Dynamic View)

| Diagram | Purpose |
|---|---|
| **Use Case Diagram** | Actors, use cases, and system boundaries |
| **Sequence Diagram** | Interactions between objects over time |
| **Activity Diagram** | Workflow and process flow |
| **State Machine Diagram** | States and transitions of an object |

### Class Diagram Relationships

| Relationship | Notation | Description |
|---|---|---|
| **Association** | Solid line | Structural relationship |
| **Inheritance** | Hollow triangle | Generalization/specialization |
| **Aggregation** | Hollow diamond | Part-of (weak ownership) |
| **Composition** | Filled diamond | Part-of (strong ownership, shared lifetime) |
| **Dependency** | Dashed arrow | Uses or depends on |

---

## 11. Data Dictionary

A data dictionary is a **centralized repository** of information about data elements in the system.

### Contents

| Element | Description |
|---|---|
| **Name** | Unique identifier for the data element |
| **Alias** | Alternative names |
| **Type** | Data type (string, integer, date, etc.) |
| **Length** | Maximum size |
| **Range** | Valid values or value range |
| **Nullability** | Whether null values are allowed |
| **Default Value** | Default if not specified |
| **Source** | Where the data originates |
| **Description** | Business meaning and usage |

### Data Dictionary Notation

- `=` — composed of
- `+` — and
- `[|]` — or (choose one)
- `{}` — iteration (one or more)
- `()` — optional

**Example:**

```
Customer Address = Street + City + State + ZipCode
Customer Name = [First Name | Last Name]
Order Items = {Item}
```

---

## 12. Software Design Document (SDD) IEEE 1016

The SDD is a **formal document** that describes the architecture and design of a software system.

### IEEE 1016-1998 SDD Structure

| Section | Content |
|---|---|
| **1. Introduction** | Purpose, scope, definitions, references |
| **2. Architectural Design** | Decomposition, component descriptions, connectors |
| **3. Detailed Design** | Module interfaces, data structures, algorithms |
| **4. Design Decisions** | Rationale, trade-offs, alternatives considered |
| **5. Requirements Traceability** | Mapping design elements to requirements |
| **6. Appendices** | Supporting information, glossaries |

### Design Viewpoints (IEEE 1016)

| Viewpoint | Focus |
|---|---|
| **Decomposition Viewpoint** | Module breakdown and hierarchy |
| **Dependency Viewpoint** | Inter-module dependencies and coupling |
| **Interface Viewpoint** | Module interfaces and protocols |
| **Detailed Design Viewpoint** | Internal design of each module |

---

## 13. Design for Non-Functional Requirements

### Performance

- Minimize latency (response time)
- Maximize throughput (requests per second)
- Use caching, connection pooling, async processing
- Profile and benchmark regularly

### Security

- Apply least privilege principle
- Validate and sanitize all inputs
- Encrypt data in transit and at rest
- Implement authentication and authorization

### Scalability

- Design for horizontal scaling (stateless services)
- Use load balancers and auto-scaling groups
- Partition/shared data stores
- Design for eventual consistency where acceptable

### Maintainability

- Apply modular design with clear interfaces
- Use consistent coding standards
- Document design decisions (ADRs)
- Keep modules loosely coupled and highly cohesive

---

## 14. Agentic System Design Considerations

### Design for Autonomous Agents

- **Clear interfaces** — agents need well-defined APIs and contracts
- **Observability** — agents must expose their state, decisions, and actions
- **Deterministic outcomes** — where possible, ensure repeatable behavior
- **Graceful degradation** — agents should handle failures and edge cases

### Multi-Agent Systems

- **Agent communication** — define protocols for inter-agent messaging
- **Task decomposition** — break complex tasks into agent-assignable units
- **State management** — shared vs. isolated state per agent
- **Coordination patterns** — orchestrator, choreography, auction-based

### Safety & Guardrails

- **Validation layers** — validate agent outputs before execution
- **Circuit breakers** — stop cascading failures between agents
- **Human-in-the-loop** — critical decisions require human approval
- **Audit trails** — every agent action must be logged and traceable

---

*References: IEEE 1016-1998, UML 2.5, GoF, C4 Model, SOLID Principles*

---

## Sources

- [college-prep-se-assignment](source/college-prep-se-assignment.md)
- [college-prep-se-files-misc](source/college-prep-se-files-misc.md)
- [college-prep-se-notes-units](source/college-prep-se-notes-units.md)
- [college-prep-se-root](source/college-prep-se-root.md)
- [college-prep-se-textbook-integral](source/college-prep-se-textbook-integral.md)
- [college-prep-se-textbook-pressman](source/college-prep-se-textbook-pressman.md)
