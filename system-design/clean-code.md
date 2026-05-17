---
layout: standalone
title: System Design — Clean Code
---

# Clean Code, Cohesion & Coupling: A Developer's Complete Reference

> *"Clean code is not written by following a set of rules. You don't become a software craftsman by learning a list of heuristics. Professionalism and craftsmanship come from values that drive disciplines."*
> — Robert C. Martin (Uncle Bob)

---

## Table of Contents

1. [What Is Clean Code?](#1-what-is-clean-code)
2. [Core Clean Code Principles](#2-core-clean-code-principles)
 - 2.1 Meaningful Names
 - 2.2 Single Responsibility Principle (SRP)
 - 2.3 DRY — Don't Repeat Yourself
 - 2.4 KISS — Keep It Simple, Stupid
 - 2.5 YAGNI — You Aren't Gonna Need It
 - 2.6 Small, Focused Functions
 - 2.7 Comments & Documentation
 - 2.8 Consistent Formatting
 - 2.9 Error Handling
 - 2.10 Avoid Magic Numbers & Strings
3. [SOLID Principles](#3-solid-principles)
4. [Cohesion](#4-cohesion)
 - 4.1 What Is Cohesion?
 - 4.2 Types of Cohesion (Worst -> Best)
 - 4.3 How to Achieve High Cohesion
5. [Coupling](#5-coupling)
 - 5.1 What Is Coupling?
 - 5.2 Types of Coupling (Worst -> Best)
 - 5.3 How to Achieve Low Coupling
6. [Cohesion vs. Coupling: The Relationship](#6-cohesion-vs-coupling-the-relationship)
7. [Project Types & Suitability](#7-project-types--suitability)
8. [Anti-Patterns to Avoid](#8-anti-patterns-to-avoid)
9. [Clean Code Metrics & Tools](#9-clean-code-metrics--tools)
10. [Quick Reference Cheat Sheet](#10-quick-reference-cheat-sheet)

---

## 1. What Is Clean Code?

Clean code is code that is **easy to read, understand, and modify**. It was popularized by Robert C. Martin ("Uncle Bob") in his 2008 book *Clean Code: A Handbook of Agile Software Craftsmanship*. The goal is not just functional code, but code that is:

- **Readable** — Another developer can understand it quickly
- **Maintainable** — Changes are safe and localized
- **Extensible** — New features can be added without breaking existing ones
- **Testable** — Logic can be verified in isolation
- **Efficient** — No unnecessary complexity or duplication

### Why It Matters

| Problem with Dirty Code | Cost |
|---|---|
| Hard to onboard new developers | Weeks of ramp-up time |
| Bugs ripple across unrelated modules | Expensive hotfixes |
| Refactoring is dangerous | Risk of regression |
| Technical debt compounds | Slower delivery over time |
| Documentation is inaccurate | Decisions made on wrong assumptions |

> Teams that prioritize clean code often see **reduced debugging time, faster development cycles, and fewer production bugs**. Developers working with clean codebases also report higher job satisfaction and lower burnout.

---

## 2. Core Clean Code Principles

### 2.1 Meaningful Names

Names for variables, functions, classes, and modules should **reveal intent**. A good name eliminates the need for a comment.

```python
# Bad
d = 86400 # seconds in a day
def calc(x, y):
 return x * y

# Good
SECONDS_IN_A_DAY = 86400
def calculate_total_price(unit_price, quantity):
 return unit_price * quantity
```

**Rules for naming:**
- Use pronounceable names (`customerRecord`, not `cstmrRcd`)
- Use searchable names (avoid single letters except loop counters)
- Classes -> Nouns (`OrderService`, `UserRepository`)
- Methods -> Verbs (`getUser`, `calculateDiscount`, `sendEmail`)
- Booleans -> Predicates (`isValid`, `hasPermission`, `canDelete`)
- Avoid abbreviations unless universally known (`URL`, `HTTP` are fine)

---

### 2.2 Single Responsibility Principle (SRP)

Every class, module, or function should have **one reason to change** — meaning it does one thing, and does it well.

```java
// Bad — this class does too much
class UserManager {
 void createUser() { ... }
 void sendWelcomeEmail() { ... }
 void generateUserReport() { ... }
 void logUserActivity() { ... }
}

// Good — responsibilities are separated
class UserService { void createUser() { ... } }
class EmailService { void sendWelcomeEmail() { ... } }
class ReportService { void generateUserReport() { ... } }
class AuditLogger { void logUserActivity() { ... } }
```

---

### 2.3 DRY — Don't Repeat Yourself

Every piece of knowledge should have **a single, unambiguous, authoritative representation** in the system.

```python
# Bad — discount logic duplicated in two places
def checkout_price(price):
 return price - (price * 0.1)

def cart_summary_price(price):
 return price - (price * 0.1)

# Good — single source of truth
DISCOUNT_RATE = 0.1

def apply_discount(price):
 return price - (price * DISCOUNT_RATE)

def checkout_price(price):
 return apply_discount(price)

def cart_summary_price(price):
 return apply_discount(price)
```

Violations of DRY create **maintenance hazards**: changing the discount in one place and forgetting another causes bugs.

---

### 2.4 KISS — Keep It Simple, Stupid

Choose the **simplest solution** that satisfies the requirements. Complexity should only be introduced when the problem genuinely demands it.

```javascript
// Overly complex
function isEven(n) {
 return n % Math.pow(2, 1) === 0 ? true : false;
}

// Simple
function isEven(n) {
 return n % 2 === 0;
}
```

KISS applies at all levels: naming, architecture, API design, and data modeling.

---

### 2.5 YAGNI — You Aren't Gonna Need It

**Do not add functionality until it is necessary.** Building speculative features increases complexity, adds maintenance burden, and wastes development time on things that may never be used.

> YAGNI is about avoiding *premature abstraction*, not avoiding all abstraction. Build for today's needs cleanly, leaving room for future extension — but don't build the extension speculatively.

**Caution:** YAGNI is most safely applied when a team has solid test coverage and strong refactoring skills. Without those, future extension becomes risky.

---

### 2.6 Small, Focused Functions

Functions should be **short** (ideally under 20 lines), **do one thing**, and **operate at one level of abstraction**.

```python
# Bad — one function doing three jobs
def process_order(order):
 # validate
 if not order.items:
 raise ValueError("Empty order")
 # calculate total
 total = sum(item.price * item.quantity for item in order.items)
 if order.discount_code == "SAVE10":
 total *= 0.9
 # save and notify
 db.save(order)
 email.send(order.customer_email, f"Order confirmed. Total: {total}")

# Good — each concern is isolated
def validate_order(order):
 if not order.items:
 raise ValueError("Empty order")

def calculate_total(order):
 total = sum(item.price * item.quantity for item in order.items)
 return apply_discount(total, order.discount_code)

def finalize_order(order):
 validate_order(order)
 total = calculate_total(order)
 db.save(order)
 email.send_confirmation(order.customer_email, total)
```

---

### 2.7 Comments & Documentation

Write comments to explain **why**, not **what**. The code should be expressive enough to explain what it does. Comments that say what the code does often mean the code itself is unclear.

```python
# Bad comment — restates the code
# Increment i by 1
i += 1

# Good comment — explains the why
# Skip the header row in CSV which contains column labels, not data
for row in csv_rows[1:]:
 process(row)
```

**When comments are appropriate:**
- Explaining non-obvious business rules or edge cases
- Warning about side effects or performance implications
- Public API documentation (docstrings)
- Legal or license notices

**Avoid:**
- Commented-out dead code (use version control instead)
- TODO comments that never get resolved
- Misleading or outdated comments

---

### 2.8 Consistent Formatting

Formatting is about **communication**. Code is read far more often than it is written. Consistent indentation, spacing, and layout reduce cognitive load.

- Follow language conventions: PEP 8 for Python, Google Style Guide for JS, etc.
- Use automated formatters: `Black`, `Prettier`, `gofmt`
- Enforce via linters in CI pipelines
- Keep related code close together; separate unrelated code with blank lines

---

### 2.9 Error Handling

Error handling is part of the program logic, not an afterthought.

```java
// Bad — silently swallows errors
try {
 processPayment(order);
} catch (Exception e) {
 // do nothing
}

// Good — meaningful error handling
try {
 processPayment(order);
} catch (PaymentGatewayException e) {
 logger.error("Payment failed for order {}: {}", order.getId(), e.getMessage());
 notifySupport(order, e);
 throw new OrderProcessingException("Payment could not be completed", e);
}
```

- Never swallow exceptions silently
- Fail fast and loud during development
- Provide meaningful error messages with context
- Separate error-handling code from the happy path

---

### 2.10 Avoid Magic Numbers & Strings

Hard-coded literals scattered in code are difficult to understand and dangerous to change.

```javascript
// Bad
if (user.role === 3) {
 redirectTo('/admin');
}

// Good
const USER_ROLES = {
 GUEST: 1,
 MEMBER: 2,
 ADMIN: 3
};

if (user.role === USER_ROLES.ADMIN) {
 redirectTo('/admin');
}
```

---

## 3. SOLID Principles

SOLID is an acronym coined by Robert C. Martin for five object-oriented design principles that together promote modularity, extensibility, and maintainability.

| Letter | Principle | One-Line Summary |
|---|---|---|
| **S** | Single Responsibility | A class should have only one reason to change |
| **O** | Open/Closed | Open for extension, closed for modification |
| **L** | Liskov Substitution | Subtypes must be substitutable for their base types |
| **I** | Interface Segregation | Don't force clients to depend on interfaces they don't use |
| **D** | Dependency Inversion | Depend on abstractions, not concretions |

### S — Single Responsibility Principle
*(Covered in section 2.2 above)*

### O — Open/Closed Principle

Classes should be **open for extension** (you can add behavior) but **closed for modification** (you don't change existing code to add behavior).

```python
# Bad — adding a new shape requires modifying the existing class
class AreaCalculator:
 def calculate(self, shape):
 if shape.type == 'circle':
 return 3.14 * shape.radius ** 2
 elif shape.type == 'rectangle':
 return shape.width * shape.height
 # Must modify this class every time a new shape is added

# Good — each shape extends behavior without modifying existing code
from abc import ABC, abstractmethod

class Shape(ABC):
 @abstractmethod
 def area(self): pass

class Circle(Shape):
 def area(self): return 3.14 * self.radius ** 2

class Rectangle(Shape):
 def area(self): return self.width * self.height

class Triangle(Shape): # New shape added with zero changes elsewhere
 def area(self): return 0.5 * self.base * self.height
```

### L — Liskov Substitution Principle

Objects of a subclass should be **drop-in replaceable** for objects of the parent class without altering program correctness.

```python
# Violation — Square breaks the Rectangle contract
class Rectangle:
 def set_width(self, w): self.width = w
 def set_height(self, h): self.height = h
 def area(self): return self.width * self.height

class Square(Rectangle):
 def set_width(self, w):
 self.width = w
 self.height = w # Forces height = width, violating Rectangle behavior
```

### I — Interface Segregation Principle

Clients should not be forced to depend on methods they do not use. Prefer **small, specific interfaces** over large, general ones.

```java
// Bad — a Printer is forced to implement irrelevant methods
interface MultifunctionDevice {
 void print();
 void scan();
 void fax();
 void copy();
}

// Good — segregated interfaces
interface Printable { void print(); }
interface Scannable { void scan(); }
interface Faxable { void fax(); }

class BasicPrinter implements Printable {
 public void print() { ... }
}
```

### D — Dependency Inversion Principle

High-level modules should not depend on low-level modules. Both should depend on **abstractions** (interfaces). This enables swapping implementations without changing business logic.

```python
# Bad — OrderService is tightly tied to a concrete EmailSender
class OrderService:
 def __init__(self):
 self.notifier = EmailSender() # Hard dependency

# Good — depends on an abstraction
class OrderService:
 def __init__(self, notifier: NotificationService):
 self.notifier = notifier # Any notifier can be injected

# Now you can inject EmailNotifier, SMSNotifier, SlackNotifier, or a mock in tests
```

---

## 4. Cohesion

### 4.1 What Is Cohesion?

**Cohesion** refers to the degree to which the elements *within* a module are related to each other and work toward a single, well-defined purpose.

- **High cohesion** -> module does one thing well; elements are tightly related
- **Low cohesion** -> module does many unrelated things; it's a "catch-all"

> **Goal: Maximize cohesion.**

A highly cohesive module is like a well-organized toolbox where every tool serves the same trade. A low-cohesion module is like a junk drawer.

---

### 4.2 Types of Cohesion (Worst -> Best)

#### Level 1: Coincidental Cohesion (Worst)
Elements are grouped **arbitrarily** — there is no meaningful relationship between them.

```python
# A "utilities" class with unrelated functions thrown together
class Utils:
 def parse_date(self, s): ...
 def send_email(self, to, body): ...
 def calculate_tax(self, amount): ...
 def resize_image(self, img, width): ...
```
**Problem:** Impossible to understand the purpose of the module. Changes are unpredictable.

---

#### Level 2: Logical Cohesion
Elements perform **similar kinds of operations** but are unrelated in execution. A flag or parameter determines which operation runs.

```python
class FileHandler:
 def handle(self, file, mode):
 if mode == 'read': ...
 elif mode == 'write': ...
 elif mode == 'delete': ...
```
**Problem:** Adding a new mode requires modifying the class. Violates Open/Closed.

---

#### Level 3: Temporal Cohesion
Elements are grouped because they happen **at the same time**, not because they are logically related.

```python
class AppStartup:
 def initialize(self):
 self.load_config()
 self.connect_database()
 self.start_scheduler()
 self.warm_cache()
```
**Problem:** Changes to startup sequence affect many unrelated behaviors at once.

---

#### Level 4: Procedural Cohesion
Elements are related because they **follow a specific execution order**.

```python
class DataPipeline:
 def run(self):
 self.read_file()
 self.parse_records()
 self.validate()
 self.transform()
 self.write_output()
```
**Problem:** Steps are interdependent by position; hard to reuse individual steps.

---

#### Level 5: Communicational/Informational Cohesion
Elements operate on the **same data** or data structure.

```python
class UserProfile:
 def get_username(self): ...
 def update_email(self): ...
 def change_password(self): ...
```
**Note:** Better — all operations share the same data object (user profile).

---

#### Level 6: Sequential Cohesion
Output of one element **feeds directly into** the next.

```python
class OrderProcessor:
 def process(self, raw_order):
 validated = self.validate(raw_order)
 priced = self.apply_pricing(validated)
 confirmed = self.confirm(priced)
 return confirmed
```
**Note:** Good, but still somewhat rigid to reordering or reusing steps independently.

---

#### Level 7: Functional Cohesion (Best)
Every element contributes to **one single, well-defined task**. Nothing is extraneous.

```python
class PasswordHasher:
 def hash(self, plain_text_password) -> str: ...
 def verify(self, plain_text, hashed) -> bool: ...
```
**Why it's best:** The class has a crystal-clear purpose. Easy to test, reuse, and reason about.

---

### 4.3 How to Achieve High Cohesion

1. **Apply SRP** — each class/module should have one reason to change
2. **Split "and" classes** — if you say "this class handles X *and* Y", split it
3. **Group by domain concept**, not by technical role
4. **Avoid utility/helper/misc classes** — they are cohesion graveyards
5. **Prefer small, purpose-driven modules** over large, general ones

---

## 5. Coupling

### 5.1 What Is Coupling?

**Coupling** is the degree of **interdependence between modules**. It measures how much changing one module requires changes in another.

- **High (tight) coupling** -> modules are intertwined; a change in one breaks others
- **Low (loose) coupling** -> modules are independent; changes are localized

> **Goal: Minimize coupling.**

Low coupling is essential for parallel development, independent testing, and safe refactoring.

---

### 5.2 Types of Coupling (Worst -> Best)

#### Level 1: Content Coupling (Worst)
Module A **directly accesses or modifies** the internal data or code of Module B.

```python
# Module A reaches into Module B's internals
class OrderService:
 def process(self, user):
 user._credit_limit -= 100 # Directly modifies private state!
```
**Problem:** A is completely dependent on B's internals. Any refactoring of B breaks A.

---

#### Level 2: Common Coupling
Multiple modules **share global state**.

```python
# Global variable shared by many modules
GLOBAL_CONFIG = {}

class PaymentService:
 def charge(self):
 rate = GLOBAL_CONFIG['tax_rate'] # Depends on mutable global

class InvoiceService:
 def generate(self):
 currency = GLOBAL_CONFIG['currency'] # Same shared state
```
**Problem:** Changes to global state have unpredictable ripple effects everywhere.

---

#### Level 3: External Coupling
Modules depend on an **external interface or format** (e.g., a specific file format, third-party API shape, or OS feature).

**Problem:** If the external dependency changes, all dependent modules must change.

---

#### Level 4: Control Coupling
Module A passes a **flag or control parameter** to Module B telling it what to do.

```python
def notify_user(user, method):
 if method == 'email':
 send_email(user)
 elif method == 'sms':
 send_sms(user)
```
**Problem:** A knows too much about B's internal logic. Violates Open/Closed.

---

#### Level 5: Stamp/Data-Structure Coupling
Modules share a **complex data structure**, but only use part of it.

```python
def get_user_display_name(user_object):
 return user_object.first_name # Needs only first_name, but gets the whole object
```
**Problem:** The module depends on more than it needs, creating hidden dependencies.

---

#### Level 6: Data Coupling
Modules communicate by passing **only the data they need** as simple parameters.

```python
def calculate_area(width: float, height: float) -> float:
 return width * height
```
**Why it's good:** The function is independent, testable, and can be reused anywhere.

---

#### Level 7: No Coupling (Best)
Modules operate **completely independently** with no direct communication.

**Note:** Rarely achievable in practice for an entire system, but the goal for leaf-level modules.

---

### 5.3 How to Achieve Low Coupling

1. **Program to interfaces**, not implementations (Dependency Inversion)
2. **Use Dependency Injection** — inject dependencies, don't instantiate them
3. **Apply the Law of Demeter** — "talk to your friends, not strangers"
 - `order.getCustomer().getAddress().getCity()` -> too much knowledge chain
 - Better: `order.getCustomerCity()` — delegate internally
4. **Use events/message queues** for cross-module communication (publish-subscribe)
5. **Avoid shared mutable state** (global variables, singletons)
6. **Pass only what's needed** — don't pass entire objects when a single field suffices
7. **Use facades or adapters** to isolate external dependencies

---

## 6. Cohesion vs. Coupling: The Relationship

These two concepts are **inversely related** in healthy code:

| Ideal Design | Problem Design |
|---|---|
| **High Cohesion** + **Low Coupling** | Low Cohesion + High Coupling |
| Modules do one thing well and are independent | Modules do many things and are tangled together |
| Easy to test, change, and reuse | Brittle, fragile, hard to understand |

![Design Quality Map](../assets/design-quality-map.svg)


**The golden rule:** A module should be internally cohesive (focused on one thing) and externally loosely coupled (independent of its neighbors).

---

## 7. Project Types & Suitability

Clean code principles, cohesion, and coupling apply everywhere — but the *emphasis* and *trade-offs* differ by project type.

---

### 7.1 Enterprise Applications (ERP, CRM, Banking)

**Best fit for:** SOLID principles, layered architecture, high cohesion, strict low coupling

**Why:**
- Large teams of 10-100+ developers work simultaneously on the same codebase
- Code lives for 10-20+ years; requirements change constantly
- Regulatory compliance requires clear audit trails and isolated business logic
- Testing coverage is mandatory; cohesive modules are individually testable

**Key practices:**
- Domain-Driven Design (DDD) with clearly bounded contexts
- Clean/Hexagonal Architecture separating business rules from infrastructure
- Dependency Injection frameworks (Spring, .NET DI)
- Strict naming conventions and code review processes

**Example:** A banking system separates `LoanProcessingService`, `RiskAssessmentService`, and `AuditLogService` — all cohesive, loosely coupled through interfaces.

---

### 7.2 Microservices Architecture

**Best fit for:** Loose coupling (between services), high cohesion (within services), DIP, SRP

**Why:**
- Each service must be independently deployable — tight coupling between services defeats the purpose
- Teams own individual services; internal code quality matters for maintainability
- Services communicate through APIs/events — natural enforcement of low coupling
- Clean Architecture within each microservice keeps business logic portable

**Key practices:**
- Each service has a single business capability (high cohesion at service level)
- Services communicate via REST, gRPC, or message brokers (no shared databases)
- Anti-Corruption Layers (ACL) isolate services from each other's data models
- Domain events for cross-service communication

**Example:** An e-commerce platform has `OrderService`, `InventoryService`, and `NotificationService` — each highly cohesive internally, communicating only through well-defined events.

---

### 7.3 Open Source Libraries & SDKs

**Best fit for:** KISS, DRY, Interface Segregation, Liskov Substitution, immaculate naming

**Why:**
- Thousands of users depend on a stable public API
- Breaking changes have enormous downstream impact
- Developers who didn't write the code must be able to use it intuitively
- Documentation and naming **are** the user experience

**Key practices:**
- Small, composable interfaces (ISP — don't force users to implement what they don't need)
- Backward compatibility as a first-class concern
- Every public function/class is a contract — apply Liskov carefully
- Zero magic — behavior must be predictable and explicit

**Example:** A date/time library exposes `parse()`, `format()`, `add()`, `subtract()` — each with a single, clear purpose.

---

### 7.4 Startups & MVPs

**Best fit for:** YAGNI, KISS, DRY, minimal over-engineering

**Why:**
- Speed to market is the primary constraint
- Requirements are highly uncertain and will change
- Small teams (2-5 engineers) mean less need for strict module boundaries
- Over-engineering burns runway before product-market fit is found

**Key practices:**
- YAGNI heavily — build only what the current user story needs
- Keep it simple — resist architectural patterns until complexity demands them
- Write clean names and small functions even without full SOLID
- Refactor aggressively as you learn what the product needs
- Add structure (layering, DI, abstraction) as the codebase grows

**Warning:** YAGNI requires strong refactoring skills and test coverage. Without tests, shortcuts today become catastrophic technical debt tomorrow.

---

### 7.5 Data Science & ML Pipelines

**Best fit for:** Functional cohesion, SRP, DRY, meaningful naming

**Why:**
- Notebooks encourage procedural sprawl — cohesion prevents spaghetti pipelines
- Reproducibility requires isolation of each pipeline step
- Experiments change frequently — low coupling between data loading, feature engineering, and modeling enables safe iteration

**Key practices:**
- Separate concerns: ingestion, preprocessing, feature engineering, model training, evaluation
- Wrap each step in a pure function (no global state)
- Use configuration files instead of hard-coded paths and hyperparameters
- Version datasets and models alongside code

**Example:** A recommendation system has `DataLoader`, `FeatureEngineer`, `ModelTrainer`, `Evaluator` — each cohesive, composable, and independently testable.

---

### 7.6 Embedded & Real-Time Systems

**Best fit for:** KISS, minimal coupling, careful use of abstraction

**Why:**
- Memory and CPU constraints require lean code
- Overhead from abstraction layers can violate real-time constraints
- Hardware interfaces change (different MCUs, sensor revisions) — abstraction isolates this
- Safety-critical systems require deterministic, auditable behavior

**Key practices:**
- Hardware Abstraction Layer (HAL) to isolate hardware-specific code
- Minimize dynamic memory allocation
- Simple, direct logic over clever abstractions
- MISRA-C / coding standards for safety-critical contexts

**Trade-off:** Full SOLID can introduce too much abstraction overhead. Apply SRP and DIP where beneficial; KISS everywhere.

---

### 7.7 Web Frontend (React, Vue, Angular)

**Best fit for:** Component cohesion, SRP, DRY, composability

**Why:**
- UI components are naturally modular — cohesion maps to component boundaries
- State management is a coupling challenge (avoid prop-drilling, global state misuse)
- Reusable components reduce duplication

**Key practices:**
- Single-purpose components (`UserAvatar`, `PriceTag`, not `UserDashboardEverything`)
- Keep business logic out of UI components (cohesion)
- Use custom hooks (React) or composables (Vue) to separate concerns
- Avoid deeply nested prop chains — use context or state management

---

### Summary Table

| Project Type | Highest Priority Principles | Coupling Target | Cohesion Target |
|---|---|---|---|
| Enterprise Apps | SOLID, DDD, Layered Architecture | Very Low | Functional |
| Microservices | SRP, DIP, ISP, Event-Driven | Extremely Low (between services) | High (within services) |
| Open Source / SDKs | Naming, ISP, Liskov, KISS | Low | Functional |
| Startups / MVPs | YAGNI, KISS, DRY | Moderate | Communicational+ |
| Data Science / ML | SRP, Functional Cohesion, DRY | Low | Functional |
| Embedded / Real-Time | KISS, HAL, SRP | Low | Procedural/Functional |
| Web Frontend | Component SRP, DRY | Low | Functional |

---

## 8. Anti-Patterns to Avoid

| Anti-Pattern | Description | Clean Code Violation |
|---|---|---|
| **God Class** | One class does everything | Violates SRP, destroys cohesion |
| **Spaghetti Code** | Tangled logic with no clear structure | Violates SRP, coupling everywhere |
| **Shotgun Surgery** | One change requires edits in many places | High coupling, low cohesion |
| **Feature Envy** | Method uses another class's data more than its own | Wrong cohesion boundaries |
| **Data Clumps** | Same group of variables passed everywhere | Missing abstraction, violates DRY |
| **Primitive Obsession** | Using primitives instead of domain objects | Weak semantics, low cohesion |
| **Long Parameter Lists** | Functions with 5+ parameters | Violates SRP, creates coupling |
| **Magic Numbers** | Hard-coded unexplained values | Violates readability |
| **Dead Code** | Unused variables, functions, imports | Clutter, misleads readers |
| **Divergent Change** | Class changes for multiple unrelated reasons | Violates SRP |

---

## 9. Clean Code Metrics & Tools

### Key Metrics to Monitor

| Metric | What It Measures | Healthy Range |
|---|---|---|
| **Cyclomatic Complexity** | Number of independent code paths in a function | <= 10 per function |
| **Lines of Code (per function)** | Function length | <= 20-30 lines |
| **Afferent Coupling (Ca)** | How many modules depend on this module | Low |
| **Efferent Coupling (Ce)** | How many modules this module depends on | Low |
| **Instability (I = Ce/Ca+Ce)** | Ratio of outgoing to total coupling | 0 (stable) to 1 (unstable) |
| **LCOM** | Lack of Cohesion in Methods | 0 is ideal |
| **Test Coverage** | Percentage of code covered by tests | >= 80% |

### Tools by Language

| Language | Linters / Formatters | Complexity / Quality |
|---|---|---|
| **Python** | `flake8`, `black`, `pylint` | `radon`, `SonarQube` |
| **JavaScript/TS** | `ESLint`, `Prettier` | `SonarQube`, `CodeClimate` |
| **Java** | `Checkstyle`, `PMD`, `SpotBugs` | `SonarQube`, `JaCoCo` |
| **C#** | `StyleCop`, `Roslyn Analyzers` | `SonarQube`, `NDepend` |
| **Go** | `gofmt`, `golangci-lint` | `SonarQube` |
| **All** | **Codacy**, **SonarCloud** | CI-integrated quality gates |

---

## 10. Quick Reference Cheat Sheet

```
CLEAN CODE QUICK REFERENCE
+=========================================+

NAMING
 - Reveal intent - Use domain language
 - Pronounceable - Avoid abbreviations (unless universal)
 - Searchable - Avoid single-letter variables (except loops)

FUNCTIONS
 - Do one thing - Keep under 20 lines
 - One level of abstraction - Avoid side effects
 - Descriptive verb names - Avoid flag/control parameters

SOLID
 S - One reason to change
 O - Extend without modifying
 L - Subtypes are substitutable
 I - Small, client-specific interfaces
 D - Depend on abstractions

KEY PRINCIPLES
 DRY - No duplication
 KISS - Simplest solution
 YAGNI - Build only what's needed now

COHESION (maximize)
 Functional - One task, all elements contribute
 Sequential - Output feeds next step
 Communicational - Operate on same data
 Procedural - Ordered steps
 Temporal - Same time = grouped
 Logical - Similar type, flag-selected
 Coincidental - Random grouping

COUPLING (minimize)
 No coupling - Fully independent
 Data - Minimal parameters
 Stamp - Shared data structure
 Control - Flag tells other module what to do
 External - Shared external format
 Common - Shared global state
 Content - Direct internal access

PROJECT FIT
 Enterprise -> SOLID + DDD + Layered Arch
 Microservices -> Low coupling between + High cohesion within
 Startups / MVPs -> YAGNI + KISS + grow structure as needed
 Open Source / SDK -> Naming + ISP + Liskov + KISS
 Data Science / ML -> SRP + Functional Cohesion + DRY
 Embedded -> KISS + HAL + minimal abstraction overhead
 Web Frontend -> Component SRP + DRY + composability

+=========================================+
```

---

## References & Further Reading

- **Clean Code** — Robert C. Martin (2008)
- **Clean Architecture** — Robert C. Martin (2017)
- **A Philosophy of Software Design** — John Ousterhout (2018)
- **Refactoring: Improving the Design of Existing Code** — Martin Fowler (2018)
- **Domain-Driven Design** — Eric Evans (2003)
- [SOLID Principles Explained — Codacy Blog](https://blog.codacy.com/clean-code-principles)
- [Cohesion & Coupling Deep Dive — Scaler](https://www.scaler.com/topics/cohesion-and-coupling-in-software-engineering/)
- [Clean Architecture for Microservices — Bitloops Docs](https://bitloops.com/docs/bitloops-language/learning/software-architecture/clean-architecture)

---

*Last updated: May 2026*
