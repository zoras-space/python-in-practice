# 03 — Exception Types

## The original challenge

The program deliberately performed four faulty operations and one successful operation, then continued through all five tests. Originally introduced in `ex2`.

## What can go wrong?

Each operation fails for a different reason:

- `int("abc")` raises `ValueError` because the value cannot be converted.
- `42 / 0` raises `ZeroDivisionError` because division by zero is undefined.
- opening a missing path raises `FileNotFoundError`.
- `"Hello" + 42` raises `TypeError` because those operand types cannot be added.

Operation 4 performs no faulty statement, providing the successful comparison path.

## The new Python concept

Exception types allow separate handlers:

```python
except ValueError as error:
    print(f"Caught ValueError: {error}")
except ZeroDivisionError as error:
    print(f"Caught ZeroDivisionError: {error}")
```

Python selects the first compatible handler. Related exception types can also be grouped in a tuple when their response is genuinely the same, for example `except (ValueError, TypeError)`. Separate handlers are kept here because seeing each category is the lesson.

## How control flow changes

Every failure skips the rest of its `try` block, enters its matching handler, and then returns to the loop for the next operation. A handled failure therefore does not end the demonstration.

## How my implementation demonstrates it

The original operations, ordering, handler types, loop, messages, and successful fifth test remain. The code does not catch bare `Exception`, because doing so would hide the distinction this stage is meant to teach.

## Runtime demonstration versus static warning

The expression `"Hello" + 42` is intentionally invalid. At runtime it raises the `TypeError` this example catches. A static type checker such as mypy can identify the incompatible operands before the program runs and correctly report them.

That warning and the runtime lesson are not in conflict: static checking predicts a problem, while this example demonstrates Python's runtime response. The line is not suppressed or rewritten merely to produce a clean mypy report.

## Key takeaway

The exception type communicates what kind of failure occurred and lets a program choose a precise response.
