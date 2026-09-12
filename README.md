# 🐍 Python OOP Practice

A practical, problem-by-problem journey to mastering **Object-Oriented Programming (OOP) in Python**.

This repository contains the programs I have written while learning and practicing Python OOP concepts. The focus is on **writing code, solving problems, understanding object relationships, and applying OOP concepts to real-world scenarios** rather than only learning the theory.

---

## 🎯 Goal

The main goal of this repository is to become confident enough to:

* Design classes and objects for real-world problems
* Understand how objects interact with each other
* Choose between inheritance and composition
* Use polymorphism effectively
* Understand Python-specific OOP features
* Write reusable and maintainable object-oriented code
* Solve Python OOP interview problems independently

---

## 📚 Concepts Covered

### 🔹 OOP Fundamentals

* Classes and Objects
* `__init__()` Constructor
* `self`
* Instance Attributes
* Instance Methods
* Object State
* Multiple Objects
* Method Design

### 🔹 Encapsulation

* Data Validation
* Encapsulation
* Internal Attributes
* `@property`
* Property Getters
* Property Setters

### 🔹 Methods in Python

* Instance Methods
* `@classmethod`
* `@staticmethod`
* Alternative Constructors
* `self` vs `cls`

### 🔹 Inheritance

* Single Inheritance
* Parent and Child Classes
* `super()`
* Constructor Reuse
* Method Overriding
* Extending Parent Behavior

### 🔹 Polymorphism

* Runtime Polymorphism
* Method Overriding
* Polymorphism with Collections
* Duck Typing
* Common Interfaces

### 🔹 Abstraction

* Abstract Classes
* `ABC`
* `@abstractmethod`
* Abstract Interfaces
* Abstraction + Polymorphism

### 🔹 Composition

* `has-a` Relationship
* Object Composition
* One-to-One Composition
* One-to-Many Composition
* Object Collections
* Inheritance vs Composition

### 🔹 Multiple Inheritance

* Multiple Inheritance
* Method Resolution Order (MRO)
* `__mro__`
* Cooperative `super()`
* Multiple-Inheritance Method Chains
* Multiple-Inheritance Constructors

### 🔹 Class and Instance State

* Class Variables
* Instance Variables
* Attribute Lookup
* Shared Class State
* Instance-Level Attribute Override

### 🔹 Magic / Dunder Methods

* `__str__()`
* `__repr__()`
* `__eq__()`
* `__lt__()`
* Operator Overloading

---

## 📝 Practice Problems

| No. | Problem                           | Main Concepts                                          |
| --: | --------------------------------- | ------------------------------------------------------ |
|  01 | Student Management                | Classes, Objects, Constructor, Instance Methods        |
|  02 | Bank Account                      | Object State, Methods, Validation                      |
|  03 | Employee Management               | Instance Attributes, Object State                      |
|  04 | Rectangle                         | Attributes, Methods, Calculations                      |
|  05 | Product Management                | Constructor, Validation, Methods                       |
|  06 | Employee Salary                   | Encapsulation, `@property`                             |
|  07 | Bank Account Encapsulation        | Internal State, Encapsulation, Properties              |
|  08 | Employee from String              | `@classmethod`, Alternative Constructor                |
|  09 | Employee Salary Validation        | `@staticmethod`                                        |
|  10 | Employee & Developer              | Inheritance, `super()`, Method Overriding              |
|  11 | Animal Sounds                     | Polymorphism, Method Overriding                        |
|  12 | Payment System                    | Inheritance, Polymorphism, Object Attributes           |
|  13 | File Opening System               | Duck Typing                                            |
|  14 | Vehicle System                    | Abstraction, `ABC`, Abstract Methods                   |
|  15 | Shape System                      | Abstraction, Inheritance, Polymorphism                 |
|  16 | Car & Engine                      | Composition                                            |
|  17 | Student & Address                 | Composition, Object Relationships                      |
|  18 | Employee & Department             | Inheritance + Composition                              |
|  19 | Shopping Cart                     | Composition, Object Collections                        |
|  20 | Notification System               | Abstraction + Inheritance + Composition + Polymorphism |
|  21 | Father, Mother & Child            | Multiple Inheritance, MRO                              |
|  22 | ML Engineer System                | Multiple Inheritance, Cooperative `super()`            |
|  23 | Multiple-Inheritance Constructors | MRO + `super()` + `__init__()`                         |
|  24 | Employee Count                    | Class Variables, Class Methods                         |
|  25 | Class vs Instance Variables       | Attribute Lookup, Shared State                         |
|  26 | Employee Methods                  | Instance + Class + Static Methods                      |
|  27 | Student System                    | Instance + Class + Static Methods                      |
|  28 | Book Representation               | `__str__()`                                            |
|  29 | Book Representation               | `__str__()` + `__repr__()`                             |
|  30 | Book Equality                     | `__eq__()`                                             |
|  31 | Book Comparison                   | `__lt__()`                                             |
|  32 | Book Comparison                   | `__gt__()` + `__le__()`                                |

---

## 🚀 Current Progress

```text
✅ Classes & Objects
✅ Constructors
✅ self
✅ Instance Attributes
✅ Instance Methods
✅ Object State
✅ Data Validation
✅ Encapsulation
✅ @property
✅ @classmethod
✅ @staticmethod
✅ Inheritance
✅ super()
✅ Method Overriding
✅ Polymorphism
✅ Duck Typing
✅ Abstraction
✅ Abstract Classes
✅ Composition
✅ One-to-One Relationships
✅ One-to-Many Relationships
✅ Inheritance vs Composition
✅ Multiple Inheritance
✅ Method Resolution Order (MRO)
✅ Cooperative super()
✅ Multiple-Inheritance Constructors
✅ Class Variables
✅ Instance Variables
✅ Attribute Lookup
✅ __str__()
✅ __repr__()
✅ __eq__()
✅ __lt__()

⏳ __gt__()
⏳ __le__()
⏳ More Operator Overloading
⏳ Other Dunder Methods
⏳ Multiple Inheritance Design Patterns
⏳ Composition vs Aggregation
⏳ Advanced OOP Design
⏳ Real-world OOP Systems
⏳ OOP Mini Projects
```

---

## 🧠 Learning Approach

I am following a **hands-on, problem-by-problem approach**.

Instead of only memorizing definitions, I am focusing on questions such as:

> What should be a class?

> What should be an attribute?

> What should be a method?

> When should I use inheritance?

> When should I use composition?

> When should I use an abstract class?

> How can polymorphism reduce unnecessary conditional logic?

> How do objects communicate with each other?

> How should a class protect its internal state?

This approach helps me understand **why** an OOP concept is used, not just **how** to write its syntax.

---

## 🏗️ OOP Design Principles Practiced

Through the exercises in this repository, I am practicing:

### IS-A Relationship

Used for inheritance.

```text
Manager IS-A Employee
Developer IS-A Employee
```

### HAS-A Relationship

Used for composition.

```text
Car HAS-A Engine
Student HAS-A Address
Department HAS-A Manager
ShoppingCart HAS-A Products
NotificationService HAS-A Notifications
```

### Common Interface

Used for abstraction and polymorphism.

```text
Notification
    ├── EmailNotification
    ├── SMSNotification
    └── PushNotification
```

Each class implements:

```python
send(message)
```

while providing different behavior.

---

## 💻 How to Run

Clone the repository:

```bash
git clone https://github.com/Prasanna186/python-oops-practice.git
```

Navigate to the repository:

```bash
cd python-oops-practice
```

Run any Python program:

```bash
python filename.py
```

---

## 📈 Progress Tracking

This repository will continue to evolve as I solve more advanced OOP problems.

The difficulty will gradually increase from:

```text
Basic OOP
    ↓
Encapsulation
    ↓
Inheritance
    ↓
Polymorphism
    ↓
Abstraction
    ↓
Composition
    ↓
Multiple Inheritance
    ↓
Magic Methods
    ↓
Advanced OOP Design
    ↓
Real-world Systems
    ↓
OOP Mini Projects
```

---

## 🔮 Future Plans

The next stage of this repository will focus on:

* More operator overloading
* Important Python dunder methods
* Advanced inheritance problems
* Composition vs aggregation
* Real-world system design
* Larger object-oriented applications
* Interview-level OOP problems
* OOP-based mini projects

---

## ⭐ Why This Repository Exists

This repository is not intended to be a collection of copied programs.

Every problem is part of my process of learning how to **think in objects, design relationships, and solve programming problems using OOP principles**.

The ultimate goal is to move from:

```text
"I know OOP theory"
```

to:

```text
"I can design and implement an OOP solution to a new problem."
```

---

## 👨‍💻 Author

**Prasanna**

Python Developer | AI/ML Enthusiast | Learning through practical problem solving


