---
layout: standalone
title: Patterns
---

# Coding Patterns & Design Patterns

> *"Good architecture makes the system easy to understand, easy to develop, easy to maintain, and easy to deploy."*
> — Robert C. Martin

---

## Table of Contents

1. [What Are Design Patterns?](#1-what-are-design-patterns)
2. [Creational Patterns](#2-creational-patterns)
3. [Structural Patterns](#3-structural-patterns)
4. [Behavioral Patterns](#4-behavioral-patterns)
5. [Architectural / App-Level Patterns](#5-architectural--app-level-patterns)
6. [Pattern Selection Guide](#6-pattern-selection-guide)

---

## 1. What Are Design Patterns?

Design patterns are **reusable, proven solutions to recurring software design problems**. They were formalized by the "Gang of Four" (GoF) — Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides — in their 1994 book *Design Patterns: Elements of Reusable Object-Oriented Software*, introducing 23 canonical patterns.

Patterns are **not code** — they are blueprints, or templates, that you adapt to your context.

### Three Categories

| Category | Focus | Question Answered |
|---|---|---|
| **Creational** | Object creation | *How do I create objects flexibly?* |
| **Structural** | Object composition | *How do I assemble classes into larger structures?* |
| **Behavioral** | Object communication | *How do objects interact and share responsibilities?* |

### Why Use Patterns?

- Provide a **shared vocabulary** across engineering teams
- Encode **battle-tested solutions** from decades of real-world experience
- Make code **more flexible, reusable, and maintainable**
- Reduce design time by identifying recurring problems early
- Enable **communication at a higher level** of abstraction

---

## 2. Creational Patterns

Creational patterns control **how and when objects are instantiated**, decoupling creation logic from business logic.

---

### 2.1 Singleton

**Intent:** Ensure a class has only **one instance** and provide a global access point to it.

**When to use:**
- Logging systems, configuration managers, thread pools, database connection pools
- When exactly one instance must coordinate actions across the system

```python
class DatabaseConnection:
 _instance = None

 def __new__(cls):
 if cls._instance is None:
 cls._instance = super().__new__(cls)
 cls._instance.connect()
 return cls._instance

 def connect(self):
 print("Connection established")

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()
assert db1 is db2 # Same instance
```

**Trade-offs:**
- Controlled access to shared resource
- Global state is hard to test; can hide dependencies
- Violates SRP if overused

---

### 2.2 Factory Method

**Intent:** Define an interface for creating objects, but let **subclasses decide which class to instantiate**.

**When to use:**
- When the exact type of object to create isn't known at compile time
- When subclasses should control what gets created
- Frameworks and libraries that need to be extended

```python
from abc import ABC, abstractmethod

class Notification(ABC):
 @abstractmethod
 def send(self, message: str): pass

class EmailNotification(Notification):
 def send(self, message): print(f"Email: {message}")

class SMSNotification(Notification):
 def send(self, message): print(f"SMS: {message}")

class NotificationFactory:
 @staticmethod
 def create(channel: str) -> Notification:
 options = {"email": EmailNotification, "sms": SMSNotification}
 if channel not in options:
 raise ValueError(f"Unknown channel: {channel}")
 return options[channel]()

# Usage — no if/else in business code
notifier = NotificationFactory.create("email")
notifier.send("Your order shipped!")
```

**Trade-offs:**
- Open/Closed — add new types without changing existing code
- Decouples creation from usage
- Can lead to parallel class hierarchies

---

### 2.3 Abstract Factory

**Intent:** Create **families of related objects** without specifying their concrete classes.

**When to use:**
- Cross-platform UI components (Windows vs macOS vs Web)
- Database drivers (MySQL vs PostgreSQL vs SQLite)
- When the system must be independent of how its products are created

```python
class Button(ABC):
 @abstractmethod
 def render(self): pass

class Checkbox(ABC):
 @abstractmethod
 def render(self): pass

class WindowsButton(Button):
 def render(self): print("Windows Button")

class MacOSButton(Button):
 def render(self): print("macOS Button")

class WindowsCheckbox(Checkbox):
 def render(self): print("Windows Checkbox")

class MacOSCheckbox(Checkbox):
 def render(self): print("macOS Checkbox")

class UIFactory(ABC):
 @abstractmethod
 def create_button(self) -> Button: pass
 @abstractmethod
 def create_checkbox(self) -> Checkbox: pass

class WindowsFactory(UIFactory):
 def create_button(self): return WindowsButton()
 def create_checkbox(self): return WindowsCheckbox()

class MacOSFactory(UIFactory):
 def create_button(self): return MacOSButton()
 def create_checkbox(self): return MacOSCheckbox()
```

---

### 2.4 Builder

**Intent:** Construct complex objects **step by step**, allowing different representations using the same process.

**When to use:**
- Objects with many optional parameters (avoid telescoping constructors)
- Building complex objects like SQL queries, HTTP requests, documents, or test fixtures

```python
class QueryBuilder:
 def __init__(self):
 self._table = ""
 self._conditions = []
 self._limit = None
 self._order_by = None

 def from_table(self, table: str) -> "QueryBuilder":
 self._table = table
 return self

 def where(self, condition: str) -> "QueryBuilder":
 self._conditions.append(condition)
 return self

 def order_by(self, column: str) -> "QueryBuilder":
 self._order_by = column
 return self

 def limit(self, n: int) -> "QueryBuilder":
 self._limit = n
 return self

 def build(self) -> str:
 query = f"SELECT * FROM {self._table}"
 if self._conditions:
 query += " WHERE " + " AND ".join(self._conditions)
 if self._order_by:
 query += f" ORDER BY {self._order_by}"
 if self._limit:
 query += f" LIMIT {self._limit}"
 return query

# Usage — fluent, readable, no 8-parameter constructors
query = (QueryBuilder()
 .from_table("orders")
 .where("status = 'active'")
 .where("total > 100")
 .order_by("created_at")
 .limit(50)
 .build())
```

---

### 2.5 Prototype

**Intent:** Create new objects by **cloning** an existing object (the prototype).

**When to use:**
- Object creation is expensive (e.g., database queries, complex initialization)
- You need many similar objects that differ only slightly
- Game entities, document templates, configuration presets

```python
import copy

class GameCharacter:
 def __init__(self, name, health, abilities):
 self.name = name
 self.health = health
 self.abilities = abilities # Expensive to recompute

 def clone(self) -> "GameCharacter":
 return copy.deepcopy(self)

# Create once, clone many times
base_warrior = GameCharacter("Warrior", 100, ["slash", "block", "charge"])
warrior_2 = base_warrior.clone()
warrior_2.name = "Warrior II"
warrior_2.health = 120
```

---

## 3. Structural Patterns

Structural patterns deal with **object composition** — how classes and objects are assembled into larger, more functional structures.

---

### 3.1 Adapter

**Intent:** Allow incompatible interfaces to work together by acting as a **translator**.

**When to use:**
- Integrating third-party libraries that have incompatible interfaces
- Legacy code integration
- Wrapping external APIs

```python
# Existing interface your code expects
class JsonDataProcessor:
 def process(self, data: dict): pass

# Third-party legacy system using XML
class LegacyXMLSystem:
 def process_xml(self, xml_string: str):
 print(f"Processing XML: {xml_string}")

# Adapter — makes LegacyXMLSystem compatible
import json

class XMLAdapter(JsonDataProcessor):
 def __init__(self, legacy: LegacyXMLSystem):
 self._legacy = legacy

 def process(self, data: dict):
 # Convert JSON dict to XML format
 xml = f"<data>{json.dumps(data)}</data>"
 self._legacy.process_xml(xml)

# Usage
adapter = XMLAdapter(LegacyXMLSystem())
adapter.process({"user": "Alice", "order": 42})
```

---

### 3.2 Decorator

**Intent:** Dynamically **add responsibilities to objects** without altering their class.

**When to use:**
- Adding logging, caching, authentication, compression, or retry logic
- When inheritance would produce too many subclasses
- HTTP middleware, Python decorators, Java I/O streams

```python
class DataService:
 def fetch(self, query: str) -> dict:
 return {"result": "data"}

class CachingDecorator:
 def __init__(self, service: DataService):
 self._service = service
 self._cache = {}

 def fetch(self, query: str) -> dict:
 if query not in self._cache:
 self._cache[query] = self._service.fetch(query)
 print("Cache MISS — fetched from source")
 else:
 print("Cache HIT")
 return self._cache[query]

class LoggingDecorator:
 def __init__(self, service):
 self._service = service

 def fetch(self, query: str) -> dict:
 print(f"[LOG] Fetching: {query}")
 result = self._service.fetch(query)
 print(f"[LOG] Done: {result}")
 return result

# Stack decorators — compose behaviors
service = LoggingDecorator(CachingDecorator(DataService()))
service.fetch("SELECT * FROM users")
```

---

### 3.3 Facade

**Intent:** Provide a **simplified interface** to a complex subsystem.

**When to use:**
- Providing a clean API over a complex library or set of classes
- Layered architecture — presenting a simple public API while hiding complexity
- SDK design, microservice clients

```python
class VideoEncoder:
 def encode(self, path): print(f"Encoding {path}")

class AudioMixer:
 def mix(self, path): print(f"Mixing audio {path}")

class ThumbnailGenerator:
 def generate(self, path): print(f"Generating thumbnail {path}")

class CDNUploader:
 def upload(self, path): print(f"Uploading {path} to CDN")

# Facade — hides all the complexity
class VideoPublisher:
 def __init__(self):
 self._encoder = VideoEncoder()
 self._mixer = AudioMixer()
 self._thumbnailer = ThumbnailGenerator()
 self._uploader = CDNUploader()

 def publish(self, video_path: str):
 self._encoder.encode(video_path)
 self._mixer.mix(video_path)
 self._thumbnailer.generate(video_path)
 self._uploader.upload(video_path)
 print("Video published!")

# Client code is simple
publisher = VideoPublisher()
publisher.publish("/videos/intro.mp4")
```

---

### 3.4 Proxy

**Intent:** Provide a **placeholder or surrogate** that controls access to another object.

**Types:**
- **Virtual Proxy** — lazy initialization of expensive objects
- **Protection Proxy** — access control / authorization
- **Remote Proxy** — represents an object in a different process/machine
- **Caching Proxy** — stores results of expensive operations

```python
class ImageLoader:
 def __init__(self, filename):
 self._filename = filename
 self._image_data = self._load() # Expensive!

 def _load(self):
 print(f"Loading image from disk: {self._filename}")
 return f"<image data: {self._filename}>"

 def display(self):
 print(self._image_data)

# Virtual Proxy — defers loading until actually needed
class LazyImageProxy:
 def __init__(self, filename):
 self._filename = filename
 self._real_image = None

 def display(self):
 if self._real_image is None:
 self._real_image = ImageLoader(self._filename)
 self._real_image.display()

# Image is not loaded until display() is called
img = LazyImageProxy("hero-banner.png")
# ... code that may or may not call display()
img.display() # Only NOW does the load happen
```

---

### 3.5 Composite

**Intent:** Treat **individual objects and compositions** of objects uniformly using a tree structure.

**When to use:**
- File systems (files and folders)
- UI component trees (widgets containing other widgets)
- Organizational hierarchies
- Menu systems, XML/HTML document trees

```python
class FileSystemItem(ABC):
 @abstractmethod
 def get_size(self) -> int: pass
 @abstractmethod
 def display(self, indent=0): pass

class File(FileSystemItem):
 def __init__(self, name, size):
 self.name = name
 self._size = size

 def get_size(self): return self._size
 def display(self, indent=0): print(" " * indent + f"{self.name} ({self._size}B)")

class Directory(FileSystemItem):
 def __init__(self, name):
 self.name = name
 self._children: list[FileSystemItem] = []

 def add(self, item: FileSystemItem): self._children.append(item)
 def get_size(self): return sum(c.get_size() for c in self._children)

 def display(self, indent=0):
 print(" " * indent + f"{self.name}/")
 for child in self._children:
 child.display(indent + 2)

# Works for both files and directories uniformly
root = Directory("project")
src = Directory("src")
src.add(File("main.py", 1024))
src.add(File("utils.py", 512))
root.add(src)
root.add(File("README.md", 2048))
root.display()
print(f"Total: {root.get_size()}B")
```

---

### 3.6 Bridge

**Intent:** Decouple an abstraction from its implementation so both can **vary independently**.

**When to use:**
- Multiple dimensions of variation (e.g., shape + rendering platform)
- Switching implementations at runtime
- Avoiding a combinatorial explosion of subclasses

```python
class Renderer(ABC):
 @abstractmethod
 def render_circle(self, x, y, radius): pass

class SVGRenderer(Renderer):
 def render_circle(self, x, y, radius):
 print(f"<circle cx='{x}' cy='{y}' r='{radius}'/>")

class CanvasRenderer(Renderer):
 def render_circle(self, x, y, radius):
 print(f"ctx.arc({x}, {y}, {radius}, 0, 2*Math.PI)")

class Shape(ABC):
 def __init__(self, renderer: Renderer):
 self._renderer = renderer

class Circle(Shape):
 def __init__(self, renderer, x, y, radius):
 super().__init__(renderer)
 self.x, self.y, self.radius = x, y, radius

 def draw(self):
 self._renderer.render_circle(self.x, self.y, self.radius)

svg_circle = Circle(SVGRenderer(), 50, 50, 30)
canvas_circle = Circle(CanvasRenderer(), 50, 50, 30)
```

---

### 3.7 Flyweight

**Intent:** Share **fine-grained objects** to reduce memory consumption.

```python
class TreeType:
 def __init__(self, name, texture):
 self.name = name
 self.texture = texture

 def draw(self, x, y):
 print(f"Drawing {self.name} at ({x},{y})")

class TreeTypeFactory:
 _types = {}

 @classmethod
 def get(cls, name, texture):
 key = f"{name}_{texture}"
 if key not in cls._types:
 cls._types[key] = TreeType(name, texture)
 return cls._types[key]
```

---

## 4. Behavioral Patterns

---

### 4.1 Observer (Pub/Sub)

**Intent:** One-to-many dependency; when one object changes, all dependents are notified.

```python
class EventBus:
 def __init__(self):
 self._subscribers = {}

 def subscribe(self, event, observer):
 self._subscribers.setdefault(event, []).append(observer)

 def publish(self, event, data=None):
 for obs in self._subscribers.get(event, []):
 obs.update(event, data)

class EmailAlertService:
 def update(self, event, data):
 print(f"[EMAIL] {event}: {data}")

bus = EventBus()
bus.subscribe("order_placed", EmailAlertService())
bus.publish("order_placed", {"order_id": 123})
```

---

### 4.2 Strategy

**Intent:** Define a family of algorithms, encapsulate each one, and make them interchangeable.

```python
class PaymentStrategy(ABC):
 @abstractmethod
 def pay(self, amount): pass

class CreditCardPayment(PaymentStrategy):
 def pay(self, amount): print(f"Charging ${amount} to card")

class PayPalPayment(PaymentStrategy):
 def pay(self, amount): print(f"Sending ${amount} via PayPal")

class Checkout:
 def __init__(self, strategy):
 self._strategy = strategy
 def complete(self, amount):
 self._strategy.pay(amount)

checkout = Checkout(CreditCardPayment())
checkout.complete(49.99)
```

---

### 4.3 Command

**Intent:** Encapsulate a request as an object — enables undo/redo, queuing, and logging.

```python
class Command(ABC):
 @abstractmethod
 def execute(self): pass
 @abstractmethod
 def undo(self): pass

class WriteCommand(Command):
 def __init__(self, editor, text):
 self._editor = editor
 self._text = text
 def execute(self):
 self._editor.text += self._text
 def undo(self):
 self._editor.text = self._editor.text[:-len(self._text)]
```

---

### 4.4 Chain of Responsibility

**Intent:** Pass a request along a chain of handlers.

```python
class Handler:
 def __init__(self):
 self._next = None
 def set_next(self, handler):
 self._next = handler
 return handler
 def handle(self, request):
 if self._next:
 return self._next.handle(request)
 return "Unhandled"

class AuthHandler(Handler):
 def handle(self, request):
 if not request.get("token"):
 return "401 Unauthorized"
 return super().handle(request)
```

---

### 4.5 State

**Intent:** Object alters its behavior when its internal state changes.

```python
class OrderState(ABC):
 @abstractmethod
 def next(self, order): pass

class PendingState(OrderState):
 def next(self, order): order.set_state(ProcessingState())
class ProcessingState(OrderState):
 def next(self, order): order.set_state(ShippedState())
class ShippedState(OrderState):
 def next(self, order): order.set_state(DeliveredState())
class DeliveredState(OrderState):
 def next(self, order): print("Already delivered")

class Order:
 def __init__(self):
 self._state = PendingState()
 def advance(self):
 self._state.next(self)
```

---

### 4.6 Template Method

**Intent:** Define skeleton of an algorithm, deferring steps to subclasses.

```python
class DataReport(ABC):
 def generate(self):
 data = self.fetch_data()
 filtered = self.filter_data(data)
 formatted = self.format_data(filtered)
 self.export(formatted)

 @abstractmethod
 def fetch_data(self): pass
 def filter_data(self, data): return data
 @abstractmethod
 def format_data(self, data): pass
 def export(self, data): print(f"Export: {data}")
```

---

### 4.7 Iterator

**Intent:** Sequentially access elements without exposing internal structure.

```python
class Counter:
 def __init__(self, start=0, step=1):
 self._current = start
 self._step = step
 def __iter__(self): return self
 def __next__(self):
 value = self._current
 self._current += self._step
 return value
```

---

### 4.8 Mediator

**Intent:** Centralize communication between components, reducing direct dependencies.

```python
class ChatRoom:
 def __init__(self):
 self._participants = {}
 def join(self, user):
 self._participants[user.name] = user
 def send(self, msg, sender):
 for name, user in self._participants.items():
 if name != sender.name:
 user.receive(f"[{sender.name}]: {msg}")
```

---

## 5. Architectural / App-Level Patterns

### 5.1 MVC — Model-View-Controller
- **Model** — business logic and data
- **View** — presentation/UI
- **Controller** — handles input, updates model, selects view

*Used in: Django, Rails, Spring MVC, ASP.NET MVC*

### 5.2 MVVM — Model-View-ViewModel
Extends MVC for data-binding frameworks (Angular, Vue, WPF, SwiftUI).

### 5.3 Repository Pattern
Abstracts data access behind an interface, decoupling domain logic from persistence.

```python
class UserRepository(ABC):
 @abstractmethod
 def find_by_id(self, user_id): pass
 @abstractmethod
 def save(self, user): pass
```

### 5.4 CQRS — Command Query Responsibility Segregation
Separate write model (Commands) from read model (Queries). Scales independently.

### 5.5 Event Sourcing
Store every state-changing event as an immutable log. Current state is derived by replaying events.

---

## 6. Pattern Selection Guide

```
PROBLEM ---> PATTERN

Need exactly one global instance ---> Singleton
Create objects without knowing type ---> Factory Method
Create families of related objects ---> Abstract Factory
Build complex objects step by step ---> Builder
Clone expensive objects ---> Prototype

Incompatible interfaces ---> Adapter
Add behaviors dynamically ---> Decorator
Simplify a complex subsystem ---> Facade
Control access to an object ---> Proxy
Part-whole hierarchies (tree) ---> Composite
Two independent hierarchies ---> Bridge

One-to-many notifications ---> Observer
Swappable algorithms ---> Strategy
Undo/Redo, queuing requests ---> Command
Pipeline of handlers ---> Chain of Responsibility
Object changes behavior by state ---> State
Fixed algorithm, variable steps ---> Template Method

Separate presentation from logic ---> MVC / MVVM
Abstract data access ---> Repository
Scale reads/writes independently ---> CQRS
Immutable audit log ---> Event Sourcing
```

---

*References: GoF (1994), microservices.io, Refactoring Guru, DDIA*
