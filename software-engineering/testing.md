---
layout: standalone
title: Software Engineering — Testing
---

# Software Testing

> *An exhaustive reference on software testing principles, techniques, strategies, metrics, tools, and best practices for autonomous AI agents.*
> Standards: IEEE 829, ISO 9126, ISTQB, McCabe Metrics

---

## Table of Contents

1. [Foundations of Software Testing](#1-foundations-of-software-testing)
2. [Testing Levels & The V-Model](#2-testing-levels--the-v-model)
3. [Functional (Black-Box) Testing Techniques](#3-functional-black-box-testing-techniques)
4. [Structural (White-Box) Testing Techniques](#4-structural-white-box-testing-techniques)
5. [Grey-Box Testing](#5-grey-box-testing)
6. [Test Design & Documentation (IEEE 829)](#6-test-design--documentation-ieee-829)
7. [Test Automation & Frameworks](#7-test-automation--frameworks)
8. [Performance & Load Testing](#8-performance--load-testing)
9. [Security Testing](#9-security-testing)
10. [Usability & Accessibility Testing](#10-usability--accessibility-testing)
11. [Regression Testing Strategies](#11-regression-testing-strategies)
12. [Mutation Testing](#12-mutation-testing)
13. [Debugging Techniques](#13-debugging-techniques)
14. [Software Testing Metrics](#14-software-testing-metrics)
15. [Static vs Dynamic Analysis Tools](#15-static-vs-dynamic-analysis-tools)
16. [Testing in CI/CD Pipelines](#16-testing-in-cicd-pipelines)
17. [Defect Management & Lifecycle](#17-defect-management--lifecycle)
18. [Risk-Based Testing](#18-risk-based-testing)

---

## 1. Foundations of Software Testing

Software testing is the process of executing a program with the intent of finding errors. It is a critical quality assurance activity that spans the entire software development lifecycle. While testing itself is expensive, launching untested software can lead to costs exponentially higher — especially in safety-critical systems. The earlier errors are discovered, the lower the cost of removal.

**Formal Definition:** Testing is the process of evaluating a system or its components to find whether it satisfies specified requirements and to identify differences between expected and actual results.

### Why Testing Matters for Agentic Engineering

- Autonomous agents generate code; testing validates correctness without human oversight
- AI-generated code requires rigorous verification to prevent hallucinations and logic errors
- Testing provides the feedback loop for self-improving agentic systems
- Automated testing enables continuous verification in agent-driven CI/CD pipelines
- Defines the ground truth for agent task completion and success criteria

### Core Concepts & Terminology

| Term | Definition |
|---|---|
| **Fault (Defect)** | A flaw in any software artifact (requirements, design, code, docs). The representation of an error in the mode of expression (text, DFD, ER diagram, source code). |
| **Error (Mistake)** | A human action that produces an incorrect result. |
| **Failure** | A deviation of the software from its expected behavior. Occurs when a fault is executed. A single fault may cause different failures. |
| **Test Case** | A set of input values, execution preconditions, expected results, and postconditions developed for a particular objective. |
| **Test Suite** | A collection of test cases grouped for a specific testing purpose. |
| **Test Oracle** | The mechanism for determining whether a test has passed or failed. |
| **Test Harness** | The system of test drivers, stubs, and frameworks needed to execute tests. |

### Verification vs Validation

| Verification | Validation |
|---|---|
| Are we building the product right? | Are we building the right product? |
| Evaluates artifacts against conditions imposed at the start of the phase. | Evaluates the system during or after development to determine if it satisfies specified requirements. |
| Reviews, walkthroughs, static analysis. | Dynamic testing. |

### Testing Principles (ISTQB)

- **Exhaustive testing is impossible** — use risk-based prioritization
- **Defect clustering** — a small number of modules contain most defects (Pareto: 80/20 rule)
- **Pesticide paradox** — repeatedly running the same tests yields diminishing returns
- **Testing shows presence, not absence of defects**
- **Absence-of-errors fallacy** — verifying useless functionality does not create quality
- **Early testing saves time and money** — shift-left principle
- **Context-dependent** — no single testing approach works for all systems

---

## 2. Testing Levels & The V-Model

### Test Levels

| Level | Description | Who Performs |
|---|---|---|
| **Unit Testing** | Tests individual functions, methods, classes in isolation | Developers |
| **Integration Testing** | Tests interactions between modules or services | Developers + QA |
| **System Testing** | Tests the complete, integrated system | QA Team |
| **Acceptance Testing** | Validates against user requirements and business needs | End Users + QA |

### V-Model Mapping

```
Requirements Analysis ---> Acceptance Test Design
        |
        v
High-Level Design ---> System Test Design
        |
        v
Detailed Design ---> Integration Test Design
        |
        v
   Implementation ---> Unit Test Design
```

Each development phase has a corresponding test design phase. Tests are designed early, but executed after implementation.

### Acceptance Testing Types

- **User Acceptance Testing (UAT)** — real users validate against needs
- **Operational Acceptance Testing (OAT)** — verifies deployment, backup, recovery
- **Contract Acceptance Testing** — verifies compliance with contractual terms
- **Alpha Testing** — internal testing by the development team
- **Beta Testing** — external testing by a limited set of end users

---

## 3. Functional (Black-Box) Testing Techniques

Black-box testing derives tests from **specifications**, not code. The internal structure is ignored.

### Equivalence Partitioning (EP)

Divides input data into partitions (equivalence classes) where tests from the same class uncover the same defects. One representative test per partition suffices.

**Example:** Age field valid range 18-65

- Valid partition: 18-65
- Invalid partitions: less than 18, greater than 65, non-numeric

### Boundary Value Analysis (BVA)

Tests the boundaries between equivalence partitions. Defects cluster at boundaries.

**Example:** Age field valid range 18-65

- Test values: 17, 18, 19, 64, 65, 66
- Also: 0, max int for edge extremes

### Decision Table Testing

Models complex business logic in a table format. Each column is a business rule.

| Conditions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|---|---|---|---|---|
| Age > 18 | T | T | F | F |
| Has License | T | F | T | F |
| **Action: Can Rent** | **T** | **F** | **F** | **F** |

### State Transition Testing

Models system behavior as states and transitions triggered by events. Covers start state, events, transitions, and end states.

### Use Case Testing

Derives test scenarios from use case flows — both the happy path (basic flow) and error paths (alternative flows).

---

## 4. Structural (White-Box) Testing Techniques

White-box testing derives tests from **source code** and internal structure.

### Statement Coverage

Every statement in the code is executed at least once.

### Branch Coverage (Decision Coverage)

Every possible branch (true/false) of each decision point is executed.

### Path Coverage

Every possible path through the code is executed. Often impractical for large systems — use cyclomatic complexity to determine the minimum number of paths.

### Condition Coverage

Each boolean sub-expression in a condition evaluates to both true and false.

### Modified Condition/Decision Coverage (MC/DC)

Required for safety-critical systems (DO-178C). Each condition independently affects the decision outcome.

### Cyclomatic Complexity (McCabe)

Measures the number of linearly independent paths through code.

`M = E - N + 2P` where:

- E = number of edges in the control flow graph
- N = number of nodes
- P = number of connected components

| Complexity | Risk |
|---|---|
| 1-10 | Low risk, well-structured |
| 11-20 | Moderate risk |
| 21-50 | High risk |
| 50+ | Untestable, needs refactoring |

---

## 5. Grey-Box Testing

Combines black-box and white-box approaches. Tests are derived from specifications (like black-box) but enhanced with knowledge of internal data structures, algorithms, and architecture (like white-box).

**Common techniques:**

- Matrix testing — maps functional requirements to code paths
- Regression testing with architecture awareness — prioritize tests based on code changes
- Integration pattern testing — test based on known integration patterns and their failure modes

---

## 6. Test Design & Documentation (IEEE 829)

IEEE 829 defines the standard for software test documentation.

### Key Documents

| Document | Purpose |
|---|---|
| **Test Plan** | Scope, approach, resources, schedule of testing activities |
| **Test Design Specification** | Test conditions, test cases, pass/fail criteria for a feature |
| **Test Case Specification** | Input values, expected outputs, execution conditions |
| **Test Procedure Specification** | Steps to execute test cases |
| **Test Log** | Chronological record of test execution |
| **Test Incident Report** | Description of any unexpected events during testing |
| **Test Summary Report** | Summary of testing results and effectiveness |

### Test Case Template

| Field | Description |
|---|---|
| **Test Case ID** | Unique identifier |
| **Test Objective** | What is being tested |
| **Preconditions** | System state before execution |
| **Test Data** | Input values |
| **Steps** | Step-by-step execution instructions |
| **Expected Result** | Expected system behavior |
| **Actual Result** | Observed behavior (filled during execution) |
| **Status** | Pass / Fail / Blocked |
| **Notes** | Additional observations |

---

## 7. Test Automation & Frameworks

### The Test Pyramid

```
       /\
      /E2E\     (few — slow, brittle)
     /------\
    /Integration\ (some)
   /--------------\
  /   Unit Tests   \ (many — fast, reliable)
 /--------------------\
```

- **Unit Tests** — fast, isolated, high coverage (70%+)
- **Integration Tests** — test boundaries between units
- **E2E Tests** — test complete user journeys (critical paths only)

### Key Automation Principles

- **Repeatable** — same result every time under same conditions
- **Deterministic** — no flaky tests (intermittent failures)
- **Fast** — developers must run them frequently
- **Isolated** — tests should not depend on each other
- **Maintainable** — low cost to update when code changes

### Automation Frameworks

| Framework | Language | Best For |
|---|---|---|
| **pytest** | Python | Unit/API testing |
| **JUnit** | Java | Unit testing |
| **Jest** | JavaScript | Unit/integration testing |
| **Cypress** | JavaScript | E2E web testing |
| **Selenium** | Multi-language | Browser automation |
| **Postman/Newman** | JavaScript | API testing |
| **Gatling** | Scala | Performance testing |
| **Appium** | Multi-language | Mobile testing |

---

## 8. Performance & Load Testing

### Types

| Type | Purpose |
|---|---|
| **Load Testing** | System behavior under expected load |
| **Stress Testing** | System behavior beyond expected load (breaking point) |
| **Endurance Testing** | System behavior over extended periods (memory leaks) |
| **Spike Testing** | System response to sudden traffic surges |
| **Scalability Testing** | How system scales with increased resources |

### Key Metrics

| Metric | Description |
|---|---|
| **Response Time** | Time from request to response (p50, p95, p99) |
| **Throughput** | Requests per second (RPS) |
| **Error Rate** | Percentage of failed requests |
| **Resource Utilization** | CPU, memory, disk, network |
| **Concurrent Users** | Number of simultaneous active users |

### Performance Testing Tools

- **JMeter** — open-source load testing
- **Gatling** — Scala-based, high-performance
- **k6** — developer-centric, scriptable
- **Locust** — Python-based, distributed
- **Artillery** — Node.js based

---

## 9. Security Testing

### Security Testing Types

- **SAST (Static Application Security Testing)** — scans source code for vulnerabilities
- **DAST (Dynamic Application Security Testing)** — tests running application for vulnerabilities
- **Penetration Testing** — simulated attacks to find security gaps
- **Vulnerability Scanning** — automated scanning for known vulnerabilities
- **Fuzz Testing** — feeding invalid/malformed data to find crashes

### Common Vulnerabilities (OWASP Top 10)

1. Broken Access Control
2. Cryptographic Failures
3. Injection (SQL, XSS, Command)
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery (SSRF)

---

## 10. Usability & Accessibility Testing

### Usability Testing

Evaluates how intuitive and user-friendly the software is.

- **Learnability** — how fast can users accomplish basic tasks?
- **Efficiency** — how fast can experienced users work?
- **Memorability** — can users return after a break and still use it?
- **Errors** — how many errors do users make, and can they recover?
- **Satisfaction** — how pleasant is the interface to use?

### Accessibility Testing (WCAG)

Ensures software is usable by people with disabilities.

- **Perceivable** — content available to senses (alt text, captions)
- **Operable** — interface works with various input methods (keyboard, screen readers)
- **Understandable** — content and interface are clear and predictable
- **Robust** — works across assistive technologies

---

## 11. Regression Testing Strategies

Regression testing ensures that new changes **do not break existing functionality**.

### Strategies

| Strategy | Description | When to Use |
|---|---|---|
| **Retest All** | Execute all existing tests | Small systems, high-risk releases |
| **Selective Regression** | Execute tests impacted by changes | Large systems, frequent releases |
| **Risk-Based** | Prioritize tests by probability and impact of failure | Limited time/budget |
| **Impact Analysis** | Trace code changes to affected tests and functionality | Complex systems |

### Regression Test Selection Techniques

- **Minimization** — find minimum set of tests covering all changes
- **Prioritization** — order tests by failure probability and business criticality
- **Coverage-Based** — select tests that cover changed code paths
- **History-Based** — select tests that have historically found defects

---

## 12. Mutation Testing

Mutation testing evaluates the **quality of test suites** by introducing small changes (mutations) to the source code and checking whether the tests detect them.

### Process

1. Create mutants — introduce single syntactically correct changes

- Operators: `<` becomes `<=`, `true` becomes `false`, remove method body

1. Run test suite against each mutant
2. If tests pass on a mutant — the mutant **survived** (test gap)
3. If tests fail on a mutant — the mutant was **killed**

### Metrics

- **Mutation Score** = Killed Mutants / Total Mutants * 100
- Target: 90%+ mutation score for critical code

### Tools

| Language | Tool |
|---|---|
| Python | mutmut, cosmic-ray |
| Java | PITest |
| JavaScript | Stryker |
| Ruby | mutant |

---

## 13. Debugging Techniques

### Debugging Process

1. **Reproduce** the failure reliably
2. **Localize** the fault — find the defect causing the failure
3. **Analyze** root cause — understand why the fault exists
4. **Fix** the defect
5. **Verify** the fix with tests
6. **Regression test** — ensure the fix didn't break anything

### Techniques

- **Print Debugging** — adding log statements (simple but limited)
- **Breakpoint Debugging** — step through code with an interactive debugger
- **Rubber Duck Debugging** — explain the problem to someone/something else
- **Binary Search** — comment out half the code, narrow down the fault
- **Delta Debugging** — systematically simplify input/program to find minimal failure case
- **Static Analysis** — let tools find the bug pattern
- **Commit Bisect** — use git bisect to find which commit introduced the bug

---

## 14. Software Testing Metrics

### Effectiveness Metrics

| Metric | Formula |
|---|---|
| **Defect Detection Percentage (DDP)** | (Defects Found / Total Defects) * 100 |
| **Test Effectiveness** | (Defects Found by Testing / Defects Found in Total) * 100 |
| **Test Coverage** | (Code Executed / Total Code) * 100 |
| **Mutation Score** | (Killed Mutants / Total Mutants) * 100 |

### Efficiency Metrics

| Metric | Description |
|---|---|
| **Test Execution Time** | Total time to run test suite |
| **Test Case Throughput** | Tests executed per unit time |
| **Defects per Test Hour** | Defects found per hour of testing |
| **Test Automation Rate** | (Automated Tests / Total Tests) * 100 |

### Quality Metrics

| Metric | Description | Target |
|---|---|---|
| **Defect Density** | Defects per KLOC or Function Point | < 1 defect/KLOC for critical |
| **Defect Leakage** | Defects found in production after release | < 1% |
| **Mean Time to Detect** | Average time to discover a defect | Depends on system |
| **Mean Time to Repair** | Average time to fix a defect | < 24 hours for critical |
| **Test Case Pass Rate** | (Passed Tests / Executed Tests) * 100 | > 95% |

---

## 15. Static vs Dynamic Analysis Tools

### Static Analysis

Analyzes code **without executing** it. Finds defects early in the lifecycle.

**What it finds:**

- Syntax errors, type mismatches
- Null pointer dereferences
- Buffer overflows
- Security vulnerabilities (SAST)
- Code style violations
- Dead code

| Tool | Language |
|---|---|
| **SonarQube** | Multi-language |
| **ESLint** | JavaScript/TypeScript |
| **Pylint / Flake8** | Python |
| **Checkstyle / PMD** | Java |
| **golangci-lint** | Go |
| **clang-tidy** | C/C++ |

### Dynamic Analysis

Analyzes code **during execution**. Finds runtime defects that static analysis cannot.

**What it finds:**

- Memory leaks
- Race conditions
- Runtime crashes
- Performance bottlenecks
- Resource contention

| Tool | Purpose |
|---|---|
| **Valgrind** | Memory profiling |
| **GDB / LLDB** | Interactive debugging |
| **Profilers (perf, py-spy)** | Performance hotspots |
| **AddressSanitizer** | Memory error detection |
| **ThreadSanitizer** | Data race detection |

---

## 16. Testing in CI/CD Pipelines

### Pipeline Stages

```
Commit -> Build -> Static Analysis -> Unit Tests -> Integration Tests
    -> E2E Tests -> Security Scan -> Performance Tests -> Deploy
```

### Gate Criteria

Each stage must pass before the next begins. Gating ensures quality at every step.

| Stage | Gate Criteria |
|---|---|
| **Static Analysis** | Zero critical/high violations |
| **Unit Tests** | 100% pass rate, 80%+ coverage |
| **Integration Tests** | 100% pass rate |
| **E2E Tests** | Critical paths pass |
| **Security Scan** | No critical vulnerabilities |
| **Performance** | Response time within SLO |

### Agentic CI/CD Considerations

- Generate and commit test cases alongside production code
- Auto-detect flaky tests and quarantine them
- Adaptive test selection — use ML to select tests based on change impact
- Automated test generation for untested code paths

---

## 17. Defect Management & Lifecycle

### Defect Lifecycle

```
New -> Assigned -> Open -> Fixed -> Resolved -> Verified -> Closed
                 \-> Rejected
                 \-> Deferred
```

| State | Description |
|---|---|
| **New** | Defect reported, not yet reviewed |
| **Assigned** | Assigned to a developer for triage |
| **Open** | Developer accepts and begins work |
| **Fixed** | Code change submitted |
| **Resolved** | Fix deployed to test environment |
| **Verified** | QA confirms the fix |
| **Closed** | Defect fully resolved and accepted |
| **Rejected** | Not a valid defect or duplicate |
| **Deferred** | Fix postponed to future release |

### Defect Severity vs Priority

| Severity | Priority |
|---|---|
| How critical is the defect technically? | How urgently must it be fixed from a business perspective? |
| **Critical** — system crash, data loss | **High** — must fix immediately |
| **Major** — feature broken | **Medium** — should fix in current release |
| **Minor** — cosmetic issue | **Low** — fix when convenient |
| **Trivial** — small visual glitch | **Deferred** — consider for future |

---

## 18. Risk-Based Testing

Prioritizes testing based on the **risk of failure** and **impact of failure**.

### Risk Calculation

`Risk Score = Probability of Failure × Impact of Failure`

| Score | Action |
|---|---|
| High (9-25) | Thorough testing — all levels and techniques |
| Medium (4-8) | Standard testing — normal coverage |
| Low (1-3) | Minimal testing — smoke tests only |

### Risk Assessment Factors

**Probability Factors:**

- Code complexity (cyclomatic complexity)
- Change frequency and recency
- Defect history of the module
- Developer experience with the technology

**Impact Factors:**

- Business criticality of the feature
- Number of affected users
- Regulatory/compliance exposure
- Data sensitivity

---

*References: IEEE 829, ISO 9126, ISTQB, McCabe Metrics, OWASP Top 10*
