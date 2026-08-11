# 🌿 python01 — Object-Oriented Programming

Module 1 moves from small procedural programs to objects that keep related data and behavior together. The `Plant` model grows step by step, then becomes the base for several specialized and interacting types.

The original 42 exercises and subject PDFs are not reproduced here. Each chapter summarizes the relevant challenge in my own words, so the code and learning progression can be understood without access to the subject.

```text
Program structure
        ↓
Classes & objects
        ↓
State & methods
        ↓
Constructors
        ↓
Encapsulation
        ↓
Inheritance
        ↓
Advanced OOP
```

## Learning stages

| Stage | Documentation | Original exercise |
|---|---|---|
| 00 | [Program structure](docs/00_program_structure.md) | `ex0` |
| 01 | [Classes and objects](docs/01_classes_and_objects.md) | `ex1` |
| 02 | [State and methods](docs/02_state_and_methods.md) | `ex2` |
| 03 | [Constructors and object creation](docs/03_constructors.md) | `ex1` and `ex3` |
| 04 | [Encapsulation](docs/04_encapsulation.md) | `ex4` |
| 05 | [Inheritance](docs/05_inheritance.md) | `ex5` |
| 06 | [Advanced OOP](docs/06_advanced_oop.md) | `ex6` |

## Code and examples

The final model is collected in [`garden_system.py`](garden_system.py). The examples import that shared implementation instead of repeating the `Plant` class.

- [`basic_objects.py`](examples/basic_objects.py) — objects and independent state
- [`plant_growth.py`](examples/plant_growth.py) — state changing through methods
- [`specialized_plants.py`](examples/specialized_plants.py) — inheritance and specialization
- [`garden_analytics.py`](examples/garden_analytics.py) — class-level methods, statistics, and deeper inheritance

Run an example from this directory:

```bash
python3 -m examples.basic_objects
```

The original private 42 submission keeps every exercise standalone so it can be evaluated independently. This public version reorganizes the same implementation history around the learning progression and avoids publishing seven near-identical versions of `Plant`.

## 📚 Vocabulary

| Term | Definition |
|---|---|
| Class | A definition that groups related data and behavior. |
| Object | A concrete instance created from a class. |
| Instance | One independently stored object belonging to a class. |
| Attribute | A value stored on an object or class. |
| Method | A function defined in a class. |
| `self` | The conventional name for the current instance inside an instance method. |
| Constructor | The initialization process represented here by `__init__`. |
| State | The current values held by an object's attributes. |
| Encapsulation | Keeping internal state behind a controlled public interface. |
| Getter | A method that returns an encapsulated value. |
| Setter | A method that validates or controls an update to encapsulated state. |
| Inheritance | Defining a class by reusing and extending another class. |
| Parent class | The class whose behavior and state are inherited. |
| Subclass | A specialized class derived from another class. |
| Method overriding | Replacing an inherited method with specialized behavior. |
| `super()` | A way to delegate a method call to a parent class. |
| Polymorphism | Using one shared interface with objects of different classes. |
| Static method | A class-associated method that receives no automatic instance or class argument. |
| Class method | A method that receives its class through `cls`. |
| Alternative constructor | A class method that provides another named way to create an object. |
| Forward reference | A type hint written as a string when the referenced type is not yet available. |
| Nested class | A class defined inside another class to express a closely related component. |
| Inheritance chain | Multiple levels of specialization, such as `Seed → Flower → Plant`. |
| Name mangling | Python's transformation of double-underscore attribute names to reduce accidental external access. |
