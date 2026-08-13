# 🪴 Python Module 2 — Exceptions

Module 2 follows failures as they become part of a program's design. It starts with `int()` rejecting invalid text, then adds handlers, deliberate `raise` statements, distinct built-in types, custom exception inheritance, and guaranteed cleanup.

The original 42 exercises and subject PDFs are not reproduced here. The challenges are summarized in my own words so this module stands on its own.

```text
Operation fails
      ↓
Catch and inspect the exception
      ↓
Raise an exception intentionally
      ↓
Distinguish exception types
      ↓
Define custom exceptions
      ↓
Use exception inheritance
      ↓
Guarantee cleanup
```

## Learning stages

| Stage | Documentation | Original exercise |
|---|---|---|
| 00 | [Exceptions and failure](docs/00_exceptions_and_failure.md) | `ex0` |
| 01 | [`try` and `except`](docs/01_try_and_except.md) | `ex0` |
| 02 | [Raising exceptions](docs/02_raising_exceptions.md) | `ex1` |
| 03 | [Exception types](docs/03_exception_types.md) | `ex2` |
| 04 | [Custom exceptions](docs/04_custom_exceptions.md) | `ex3` |
| 05 | [Exception inheritance](docs/05_exception_inheritance.md) | `ex3` |
| 06 | [`finally` and cleanup](docs/06_finally_and_cleanup.md) | `ex4` |

## Runnable examples

- [`catching_exceptions.py`](examples/catching_exceptions.py) — conversion, handling, and continuation
- [`raising_exceptions.py`](examples/raising_exceptions.py) — conversion failure versus validation failure
- [`exception_types.py`](examples/exception_types.py) — four built-in failure types and one success
- [`custom_exceptions.py`](examples/custom_exceptions.py) — garden-specific exceptions and inheritance
- [`cleanup_with_finally.py`](examples/cleanup_with_finally.py) — cleanup after success, failure, and `return`

Run the concept-based launcher from this directory:

```bash
python3 main.py
```

Run one focused example with, for example:

```bash
python3 -m examples.exception_types
```

These remain separate demonstrations rather than one large error system. The small color constants and custom exception hierarchy are shared where that makes their relationship clearer.

## Beyond the Exercises

[ANSI terminal colors](extras/ansi_terminal_colors.md) records the output-color experiment that developed alongside the exercises. It is not part of the formal exception-handling curriculum.
