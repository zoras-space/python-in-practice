# Python Modules

This repository documents the concepts learned across **10 Python modules**. Each module builds on the previous one, with the focus on understanding programming ideas rather than solving isolated exercises.

## Module Overview

| Module | Theme | New concepts |
|---|---|---|
| `py00` | Python Fundamentals | Functions, variables, input/output, operators, control flow, iteration, recursion, strings, type hints |

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

