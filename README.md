# Python Modules

This repository documents the concepts learned across **10 Python modules**. Each module builds on the previous one, with the focus on understanding programming ideas rather than solving isolated exercises.

## Module Overview

| Module | Theme | New concepts |
|---|---|---|
| `py00` | Python Fundamentals | Functions, variables, input/output, operators, control flow, iteration, recursion, strings, type hints |
| `py01` | Object-Oriented Programming | Program structure, classes, objects, state, constructors, encapsulation, inheritance, overriding, class/static methods, nested classes |

> More modules will be added to this overview as the curriculum progresses.

# 🌱 py00 — Python Fundamentals

## 🧠 What this module teaches

`py00` introduces the basic building blocks of Python: organizing code in functions, moving data through a program, making decisions, and repeating work.

The garden-themed examples are intentionally small so that attention stays on the language and the ideas behind the code.

## 🧱 Building Blocks

### ⚙️ Functions

A function groups statements into a reusable, named unit of behavior.

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    # indented function body
```

- `def` begins a function definition.
- The function name describes the behavior being defined.
- **Parameters** are names that receive data; **arguments** are the values supplied when the function is called.
- The indented body contains the statements that run.
- `-> None` indicates that the function is intended to return no useful value.

The functions in this module mainly produce a **side effect**: they print to standard output instead of returning a computed value.

> Indentation is part of Python's syntax. It defines which statements belong to a function, loop, or conditional branch.

### 💬 Input & Output

`input()` reads text from the user. `print()` sends values to standard output. The module constructs output in several ways:

| Technique | Example | Purpose |
|---|---|---|
| Fixed string | `print("Hello, Garden Community!")` | Display text that never changes |
| Multiple `print()` arguments | `print("Total harvest:", harvest_weight)` | Print separate values with the default separator, `sep=" "` |
| String concatenation | `"Garden: " + garden_name` | Join strings with the `+` operator |
| Formatted string literal | `f"Plot area: {plot_length * plot_width}"` | Insert values or evaluated expressions into text |

Text such as `"Harvest time!"` is **fixed**. Text built from variables or expressions is **dynamic** because its content depends on program data.

An escape sequence represents a special character inside a string. For example, `\n` inserts a newline:

```python
print("Garden: " + garden_name + "\nStatus: Growing well!")
```

> Use multiple `print()` arguments for quick value output, concatenation when joining strings directly, and f-strings when mixing readable text with values or expressions.

### 📦 Variables & Data

Variables give names to values so that a program can store and reuse data.

```python
plot_length = int(input("Enter length: "))
```

This single statement reads a string, converts it to an integer, and assigns the result to `plot_length`.

```text
Input → Conversion → Processing → Output
 text      int()       arithmetic     print()
```

The module primarily works with:

- **strings** for names, prompts, and messages;
- **integers** for ages, dimensions, quantities, and counters;
- **variables** for preserving values between operations;
- **expressions** for producing new values from existing data.

> `input()` always returns a string. Numerical input must be converted with `int()` before integer arithmetic or comparison.

### ➕ Expressions & Operators

An **expression** evaluates to a value. A **statement** performs an action.

| Code | Role | Meaning |
|---|---|---|
| `plot_length * plot_width` | Expression | Produces an area |
| `day + 1` | Expression | Produces the next day number |
| `plant_age > 60` | Expression | Produces `True` or `False` |
| `count = 1` | Assignment statement | Stores `1` in `count` |
| `count += 1` | Assignment statement | Increases and stores the counter |

The distinction between assignment and comparison is essential:

| Operator | Purpose | Example |
|---|---|---|
| `=` | Assign a value | `day = 1` |
| `>` | Compare two values | `plant_age > 60` |

Python evaluates expressions before using their results in assignments, conditions, function calls, or formatted output.

### 🌿 Control Flow

Conditionals let a program choose which code runs.

```python
if condition:
    ...
elif another_condition:
    ...
else:
    ...
```

- `if` tests the first condition.
- `elif` tests another condition if earlier branches did not match.
- `else` handles everything that remains.

Only the first matching branch in a chain runs. This turns comparison results such as `days_since_wet > 2` into decisions.

### 🔁 Repetition

The module deliberately demonstrates two mechanisms for repeating work.

| Iteration | Recursion |
|---|---|
| Repeats with `for` or `while` | Repeats through function calls |
| `range()` supplies a sequence of loop values | Parameters carry changing state between calls |
| A loop condition or finite range controls termination | A base case controls termination |
| Counters and accumulators are updated in one function call | Each recursive call gets its own stack frame |
| Usually direct and memory-efficient for simple counting | Useful for problems with naturally self-similar structure |

#### Iteration

- A `for` loop visits values from an iterable such as `range()`.
- `range(1, days_till_harvest + 1)` starts at `1` and excludes its stop value, so `+ 1` includes the final day.
- A `while` loop repeats while its condition remains true.
- A **counter** tracks repetitions or position.
- An **accumulator** combines values over time, such as a running harvest total.

#### Recursion

The recursive implementation uses a helper function:

- the **recursive call** invokes the helper again;
- the **recursive case** advances from `day` to `day + 1`;
- the **base case** stops when the final day has been passed.

> Iteration and recursion can express the same repeated process through different mechanisms. This repository includes both implementations so their structure can be compared directly.

### 📝 Strings

Strings are objects representing text. Because they are objects, they provide methods:

```python
seed_type.capitalize()
```

`.capitalize()` returns a new string with its first character uppercase and the remaining characters lowercase. The original string is not modified.

Strings in this module are also:

- joined with `+` (**concatenation**);
- combined with values using f-strings (**formatting**);
- split across output lines using `\n` (**escape sequences**).

### 🏷️ Type Hints

Type hints communicate what kinds of values a function expects:

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
```

- `seed_type: str` annotates a string parameter.
- `quantity: int` annotates an integer parameter.
- `-> None` says the function is not intended to return a value.

Type hints improve readability and help editors and static-analysis tools such as `mypy` detect mismatches before execution. They do not normally enforce types at runtime by themselves.

## 🔍 Patterns Used Throughout the Module

The examples grow in size, but repeatedly use the same pipeline:

```text
Input
  ↓
Variables
  ↓
Conversion & Processing
  ↓
Decision / Repetition
  ↓
Output
```

In practical terms:

1. Read data with `input()` or receive it through parameters.
2. Store the data in clearly named variables.
3. Convert or transform it with methods, operators, and expressions.
4. Choose a path or repeat work when needed.
5. Present the result with `print()`.

## 💡 Implementation Notes

- Output progresses from a fixed `print()` call to concatenation, multiple positional arguments, and f-strings.
- Numerical input is converted at the point of entry with nested `int(input(...))` calls.
- The harvest total uses both a counter and an accumulator inside a `while` loop.
- Counting to harvest is implemented twice: once with `for` and `range()`, and once with a recursive helper and base case.
- Function signatures begin without annotations; the final example introduces parameter annotations and `-> None`.
- Larger functions are assembled from the same small pieces: input, assignment, expressions, conditions, repetition, and output.

## 📚 Vocabulary

| Term | Definition |
|---|---|
| Parameter | A name in a function definition that receives data. |
| Argument | A value supplied when a function is called. |
| Expression | Code that evaluates to a value. |
| Statement | An instruction that performs an action. |
| Assignment | Storing a value under a variable name. |
| Comparison | Evaluating the relationship between values to produce `True` or `False`. |
| Iteration | Repeating work with a loop. |
| Recursion | Repeating work by having a function call itself. |
| Base case | The condition that stops recursive calls. |
| Recursive case | The part that advances a recursive process toward its base case. |
| Counter | A variable that tracks repetitions or position. |
| Accumulator | A variable that combines values across repeated steps. |
| Type conversion | Explicitly changing a value from one type to another, such as with `int()`. |
| String concatenation | Joining strings with the `+` operator. |
| Formatted string literal | An f-string that embeds values or expressions inside `{}`. |
| Escape sequence | Characters such as `\n` that represent special behavior inside a string. |
| Side effect | An observable action, such as printing, beyond producing a return value. |
| Type annotation | A hint describing the expected type of a parameter, variable, or return value. |

## 🎯 Key Takeaways

| | After `py00`, I can... |
|---|---|
| ✅ | Define functions and understand parameters, arguments, and indentation |
| ✅ | Follow data from input through conversion, processing, and output |
| ✅ | Construct output with `print()` arguments, concatenation, and f-strings |
| ✅ | Store values and evaluate arithmetic and comparison expressions |
| ✅ | Make decisions with `if`, `elif`, and `else` |
| ✅ | Repeat work with `for` and `while` loops |
| ✅ | Explain recursion using recursive calls and a base case |
| ✅ | Use string methods and understand why type hints exist |

# 🌿 py01 — Object-Oriented Programming

## 🧠 What this module adds

`py01` moves from writing individual functions to modeling related data and behavior together. Its central idea is **Object-Oriented Programming**:

```text
data + behavior → objects
```

The `Plant` class evolves throughout the module: it begins as a simple container, gains behavior and protected state, and becomes the foundation for a family of specialized, interacting objects.

## 🧱 Building Objects

### ▶️ Python Program Structure

Python sets the special variable `__name__` when a file is loaded. When the file is run directly, its value is `"__main__"`:

```python
def main() -> None:
    print("=== Welcome to My Garden ===")


if __name__ == "__main__":
    main()
```

The guard separates two roles a Python file can have:

- running as a program calls `main()`;
- being imported makes its classes available without running the demonstration code.

This creates a clear entry point and allows the same file to be both executable and reusable.

### 🏗️ Classes & Objects

A **class** defines a reusable model. An **object** is one particular instance of that class.

```python
class Plant:
    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
```

Both objects share the behavior defined by `Plant`, but each carries its own data. Calling `rose.show()` passes `rose` to the method as `self`, while `sunflower.show()` operates on the sunflower.

> A class is the definition; an object is a concrete value created from that definition.

### 🔧 Constructors & Attributes

The constructor initializes a new object's state:

```python
def __init__(self, name: str, height: float, age: int) -> None:
    self.name = name
    self.height = height
    self.age = age
```

- `__init__` runs automatically after an object is created.
- `self` refers to that new object.
- `self.name`, `self.height`, and `self.age` are **instance attributes**.
- constructor arguments supply the initial values.

Creating several plants from data demonstrates why classes are reusable: one definition can produce many independent objects with the same structure.

### 🌱 State & Methods

An object's **state** is the collection of values currently stored in its attributes. Methods read or change that state:

```python
def grow(self, growth: float) -> None:
    self.height += growth

def age(self, days: int) -> None:
    self.plant_age += days
```

The same object persists across calls:

```text
Plant state → grow() → updated height
            → age()  → updated age
            → show() → current state as output
```

Unlike a function that receives every value separately, a method already has access to the object through `self`. This keeps the data and the operations that belong to it together.

## 🔐 Encapsulation

Encapsulation controls how an object's internal state is accessed and changed. The evolving `Plant` stores its core attributes with a leading underscore:

```python
self._name = name
self._height = 0.0
self._age = 0
```

The underscore communicates that an attribute is intended for internal use. Public getter and setter methods provide a controlled interface:

```python
def set_height(self, height: float) -> None:
    if height >= 0:
        self._height = height
    else:
        print(f"{self._name}: Error, height can't be negative")

def get_height(self) -> float:
    return self._height
```

This prevents methods from updating height without applying the same validation rule. The constructor also uses the setters, so initial values and later changes follow one consistent path.

```text
requested change → setter → validation → internal state
```

> In Python, a leading underscore is a convention rather than an absolute access restriction. Double underscores, used by the statistics component, additionally trigger name mangling.

## 🌳 Inheritance & Specialization

Inheritance creates a new class from an existing one. `Flower`, `Tree`, and `Vegetable` are all plants, so they reuse the common plant state and behavior:

```python
class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False
```

`super()` delegates the shared initialization to `Plant`. The subclass then adds only the state that makes it distinct.

| Class | Reused from `Plant` | Specialized behavior or state |
|---|---|---|
| `Flower` | Name, height, age, growth | Color, blooming state, `bloom()` |
| `Tree` | Name, height, age, growth | Trunk diameter, `produce_shade()` |
| `Vegetable` | Name, height, age, growth | Harvest season, nutritional value |
| `Seed` | The complete flower behavior | Number of seeds after blooming |

This represents an **is-a relationship**: a flower is a plant, and a seed-producing flower is also a flower.

### 🔄 Method Overriding

A subclass can replace a method while still reusing its parent implementation:

```python
def show(self) -> None:
    super().show()
    print(f"Color: {self.color}")
```

This is **method overriding**. Every plant responds to `show()`, but the result depends on the object's actual class. The common details come from `Plant.show()`, and the subclass appends its specialized details.

`Vegetable.age()` shows that overriding can also extend a state change: it first ages the plant through `super().age(days)`, then updates nutritional value.

### ⛓️ Inheritance Chains

`Seed` extends `Flower`, which already extends `Plant`:

```text
Plant
  └── Flower
        └── Seed
```

A `Seed` object therefore inherits plant state, plant growth and aging, flower color and blooming behavior, and its own seed count. Its `show()` call moves through the chain so each layer contributes one part of the output.

This demonstrates that specialization can be built in stages instead of duplicating all earlier behavior in every new class.

## 🧰 Methods Associated with the Class

Most methods operate on an instance through `self`. Static and class methods serve different roles.

### 📏 Static Methods

A static method belongs conceptually to a class but does not need an instance or class reference:

```python
@staticmethod
def check_age(age: int) -> bool:
    return age > 365
```

`Plant.check_age(400)` checks a plant-related rule without creating a `Plant` object. The input is supplied explicitly, and no object state is read or changed.

### 🏭 Class Methods

A class method receives the class as `cls` and can act as an alternative constructor:

```python
@classmethod
def create_anonymous_plant(cls):
    return cls("Unknown plant", 0, 0)
```

Using `cls` instead of writing `Plant(...)` keeps creation connected to the class on which the method was called. The method packages a meaningful default construction rule behind a descriptive name.

| Method kind | First parameter | Typical purpose |
|---|---|---|
| Instance method | `self` | Read or change one object's state |
| Class method | `cls` | Work with the class or construct objects |
| Static method | None automatically supplied | Perform a related, state-independent operation |

## 📊 Nested Components & Interacting Objects

Each plant contains a nested `Statistics` class that tracks how the surrounding object is used:

```python
class Plant:
    class Statistics:
        def __init__(self) -> None:
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0
```

Nesting communicates that this component belongs to the plant model. A plant owns a statistics object and delegates recording to it whenever `grow()`, `age()`, or `show()` runs:

```text
Plant.grow()
  ├── updates plant height
  └── records a grow call in Statistics
```

The counters use double underscores to keep their representation encapsulated. Other code asks the component to record or display information rather than modifying the counters directly.

Trees extend this relationship with their own nested statistics subclass. It inherits the common counters and adds a shade counter, mirroring the same specialization used by the outer plant classes.

A standalone `display_statistics(plant)` function works with any plant subtype. This shows **polymorphism**: shared behavior allows one function to collaborate with flowers, trees, seeds, and ordinary plants without separate logic for each one.

## 🔍 How the Model Evolves

The module develops one design in layers:

```text
Program entry point
  ↓
Plant class and independent objects
  ↓
Constructor-defined state
  ↓
Methods that evolve state
  ↓
Encapsulated and validated attributes
  ↓
Specialized subclasses and overridden methods
  ↓
Class-level creation and utility behavior
  ↓
Nested statistics and inheritance chains
```

Each layer preserves the earlier ideas while adding a new way to organize responsibility. The final model is not a collection of unrelated classes: it is a small system whose components reuse, extend, and interact with one another.

## 💡 Implementation Notes

- Every executable file uses a `main()` function and the `if __name__ == "__main__":` guard.
- Object creation progresses from individual instances to constructing several plants from a shared class definition.
- Growth and aging mutate persistent object state, while `show()` exposes the current state through output.
- Setters validate non-negative height and age values before changing protected attributes.
- `super()` avoids repeating initialization and shared display or update behavior in subclasses.
- Overridden methods preserve a common interface while adding class-specific behavior.
- `Seed → Flower → Plant` demonstrates multi-level inheritance.
- The nested statistics object separates analytics state from the plant's biological state.
- Tree statistics extend the shared statistics class with behavior unique to trees.
- Type annotations continue documenting constructor parameters, method inputs, and return values.

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
| Nested class | A class defined inside another class to express a closely related component. |
| Inheritance chain | Multiple levels of specialization, such as `Seed → Flower → Plant`. |
| Name mangling | Python's transformation of double-underscore attribute names to reduce accidental external access. |

## 🎯 Key Takeaways

| | After `py01`, I can... |
|---|---|
| ✅ | Structure an executable Python file with `main()` and the `__name__` guard |
| ✅ | Define classes and create independent objects from them |
| ✅ | Initialize and evolve object state through constructors and methods |
| ✅ | Encapsulate attributes behind validated getters and setters |
| ✅ | Reuse common behavior through inheritance and `super()` |
| ✅ | Specialize subclasses by adding state and overriding methods |
| ✅ | Follow behavior through multi-level inheritance chains |
| ✅ | Distinguish instance, class, and static methods |
| ✅ | Organize related analytics in an encapsulated nested class |
| ✅ | Design functions and components that work across related object types |
