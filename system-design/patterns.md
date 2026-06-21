---
layout: standalone
title: Patterns
---

# Design Patterns

> *Comprehensive reference on design principles, GoF design patterns, and architecture patterns.*
> Standards: GoF, SOLID, UML 2.5

---

## Table of Contents

1. [Design Principles (SOLID, DRY, KISS, YAGNI)](#1-design-principles-solid-dry-kiss-yagni)
2. [Modularity, Coupling & Cohesion](#2-modularity-coupling--cohesion)
3. [Design Patterns: Creational](#3-design-patterns-creational)
4. [Design Patterns: Structural](#4-design-patterns-structural)
5. [Design Patterns: Behavioral](#5-design-patterns-behavioral)
6. [Architecture Patterns](#6-architecture-patterns)

---

## 1. Design Principles (SOLID, DRY, KISS, YAGNI)

### SOLID Principles

| Letter | Principle | Description |
|---|---|---|
| **S** | Single Responsibility | A class should have only one reason to change |
| **O** | Open/Closed | Open for extension, closed for modification |
| **L** | Liskov Substitution | Subtypes must be substitutable for their base types |
| **I** | Interface Segregation | No client should be forced to depend on methods it does not use |
| **D** | Dependency Inversion | Depend on abstractions, not concretions |

**Single Responsibility:** Each class, module, or function should have exactly one well-defined responsibility. If a class has more than one reason to change, split it.

**Open/Closed:** Classes should be open for extension (you can add behavior) but closed for modification (you don't change existing code to add behavior). Achieved through abstraction and polymorphism.

**Liskov Substitution:** If a program uses a base class, it should be able to use any derived class without knowing it. Derived classes must not weaken the base class's guarantees.

**Interface Segregation:** Large, general-purpose interfaces should be split into smaller, specific ones. Clients should not implement methods they don't need.

**Dependency Inversion:** High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.

### DRY — Don't Repeat Yourself

Every piece of knowledge should have **a single, unambiguous, authoritative representation** in the system. Duplication creates maintenance hazards — changing logic in one place while forgetting another causes bugs.

### KISS — Keep It Simple

Choose the **simplest solution** that satisfies the requirements. Complexity should only be introduced when the problem genuinely demands it. Simple code is easier to understand, test, and maintain.

### YAGNI — You Aren't Gonna Need It

Do not add functionality until it is **necessary**. Building speculative features increases complexity and wastes time on things that may never be used. YAGNI avoids premature abstraction but requires strong refactoring skills and test coverage.

---

## 2. Modularity, Coupling & Cohesion

### Modularity

Decompose the system into **cohesive, loosely coupled modules** with well-defined interfaces. Each module encapsulates a distinct concern.

**Benefits:**

- Independent development and testing
- Parallel team work
- Reusable components
- Isolated failure domains

### Coupling

The degree of **interdependence between modules**.

| Type | Description | Level |
|---|---|---|
| **Content Coupling** | Module directly accesses another's internals | Worst |
| **Common Coupling** | Modules share global state | Very High |
| **External Coupling** | Modules share external format/protocol | High |
| **Control Coupling** | One module tells another what to do via flags | Moderate |
| **Stamp Coupling** | Modules share composite data structure | Moderate |
| **Data Coupling** | Modules communicate via simple parameters | Low |
| **No Coupling** | Modules are completely independent | Best |

**Goal:** Minimize coupling. Prefer data coupling for inter-module communication.

### Cohesion

The degree to which elements **within a module** belong together.

| Type | Description | Level |
|---|---|---|
| **Coincidental** | Elements grouped arbitrarily | Worst |
| **Logical** | Similar kind of operations, flag-selected | Low |
| **Temporal** | Elements related only by timing | Low |
| **Procedural** | Related by execution order | Moderate |
| **Communicational** | Operate on same data | Moderate |
| **Sequential** | Output of one feeds the next | High |
| **Functional** | All elements contribute to one task | Best |

**Goal:** Maximize cohesion. Prefer functional cohesion.

### The Relationship

- **High cohesion + Low coupling** = ideal design
- **Low cohesion + High coupling** = worst design

---

## 3. Design Patterns: Creational

Creational patterns control **how objects are instantiated**, decoupling creation logic from business logic.

### Singleton

Ensures a class has only **one instance** and provides a global access point.

**Use when:** Exactly one instance must coordinate actions (logging, configuration managers, thread pools).

```python
class DatabaseConnection:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connect()
        return cls._instance
```

### Factory Method

Defines an interface for creating objects, but lets **subclasses decide which class to instantiate**.

**Use when:** The exact type of object to create isn't known at compile time.

```python
class NotificationFactory:
    @staticmethod
    def create(channel: str) -> Notification:
        options = {"email": EmailNotification, "sms": SMSNotification}
        return options[channel]()
```

### Abstract Factory

Creates **families of related objects** without specifying their concrete classes.

**Use when:** Cross-platform UI components, database drivers, or theme systems.

### Builder

Constructs complex objects **step by step**, allowing different representations.

**Use when:** Objects with many optional parameters; avoiding telescoping constructors.

### Prototype

Creates new objects by **cloning** an existing object.

**Use when:** Object creation is expensive; many similar objects needed.

---

## 4. Design Patterns: Structural

Structural patterns deal with **object composition** — assembling classes into larger structures.

### Adapter

Allows incompatible interfaces to work together by acting as a **translator**.

**Use when:** Integrating third-party libraries, legacy code, or wrapping external APIs.

### Decorator

Dynamically **adds responsibilities** to objects without altering their class.

**Use when:** Adding cross-cutting concerns (logging, caching, auth) without modifying the core class.

### Facade

Provides a **simplified interface** to a complex subsystem.

**Use when:** Presenting a clean API over a complex library or set of classes.

### Proxy

Provides a **placeholder or surrogate** that controls access to another object.

**Types:** Virtual (lazy loading), Protection (access control), Remote (distributed object), Caching.

### Composite

Treats **individual objects and compositions** uniformly using a tree structure.

**Use when:** File systems, UI component trees, organization hierarchies.

### Bridge

Decouples an **abstraction from its implementation** so both can vary independently.

**Use when:** Multiple dimensions of variation (e.g., shape + rendering platform).

### Flyweight

Shares **fine-grained objects** to reduce memory consumption.

**Use when:** Thousands of similar entities (game objects, text characters).

---

## 5. Design Patterns: Behavioral

Behavioral patterns define **how objects communicate** and distribute responsibilities.

### Observer (Pub/Sub)

Defines a one-to-many dependency so that when one object changes state, all dependents are **notified automatically**.

**Use when:** Event systems, UI event handling, notification services.

### Strategy

Defines a family of algorithms, encapsulates each one, and makes them **interchangeable at runtime**.

**Use when:** Multiple algorithms that can be swapped (sorting, payment, compression).

### Command

Encapsulates a **request as an object** — enabling parameterization, queuing, logging, and undo.

**Use when:** Undo/redo systems, transaction queuing, macro recording.

### Chain of Responsibility

Passes a request along a **chain of handlers**, each deciding whether to process or pass on.

**Use when:** HTTP middleware, authorization pipelines, event bubbling.

### State

Allows an object to **alter its behavior when its internal state changes**.

**Use when:** Order state machines, connection lifecycle, game character states.

### Template Method

Defines the **skeleton of an algorithm** in a base class, deferring specific steps to subclasses.

**Use when:** Data processing pipelines with fixed steps but variable implementations.

### Iterator

Provides a way to **sequentially access elements** of a collection without exposing its internal structure.

**Use when:** Custom collections, lazy data loading, paginated results.

### Mediator

Centralizes **communication between components**, preventing direct dependencies.

**Use when:** Chat rooms, complex UI forms, microservice orchestration.

---

## 6. Architecture Patterns

### MVC — Model-View-Controller

Separates application into three roles: Model (data/logic), View (presentation), Controller (input/flow).

**Used in:** Django, Rails, Spring MVC, ASP.NET MVC

### MVVM — Model-View-ViewModel

Extends MVC for data-binding. ViewModel exposes observable data to the View.

**Used in:** Angular, Vue, WPF, SwiftUI

### Repository Pattern

Abstracts data access behind an interface, separating domain logic from persistence.

### CQRS — Command Query Responsibility Segregation

Separates the write model (Commands) from the read model (Queries). Enables independent scaling.

### Event Sourcing

Stores every state-changing event as an immutable log. Current state is derived by replaying events.

### Saga Pattern

Manages long-running distributed transactions across multiple services without two-phase commit.

**Types:** Choreography (event-driven) and Orchestration (central coordinator).

### Strangler Fig

Gradually migrates legacy monolith to microservices by routing traffic to new services.

### Outbox Pattern

Ensures atomic database write + event publish by writing to an outbox table and relaying asynchronously.

---

*References: GoF, SOLID Principles, IEEE 1016-1998, microservices.io*

---

## Sources

- [college-prep-se-allquestions](source/college-prep-se-allquestions.md)
- [college-prep-se-notes-units](source/college-prep-se-notes-units.md)
- [college-prep-se-root](source/college-prep-se-root.md)
