# 🌱 py00 — Python Fundamentals

Module 0 introduces Python through small garden-themed programs. Each example adds one piece of the language and shows how input becomes data, decisions, repetition, and output.

The original 42 exercises and subject PDFs are not reproduced here. Each chapter summarizes the relevant challenge in my own words, so the code and learning progression can be understood without access to the subject.

```text
Functions & output
        ↓
Input, variables & conversion
        ↓
Expressions & calculations
        ↓
Conditions
        ↓
Iteration
        ↓
Recursion
        ↓
Strings & type hints
```

## Learning stages

| Stage | Documentation | Original exercise |
|---|---|---|
| 00 | [Functions and output](docs/00_functions_and_output.md) | `ex0` |
| 01 | [Input, variables, and conversion](docs/01_input_variables_conversion.md) | `ex1`–`ex3` |
| 02 | [Expressions and calculations](docs/02_expressions_and_calculations.md) | `ex2`–`ex3` |
| 03 | [Conditions](docs/03_conditions.md) | `ex4`–`ex5` |
| 04 | [Iteration](docs/04_iteration.md) | `ex3` and `ex6` |
| 05 | [Recursion](docs/05_recursion.md) | `ex6` |
| 06 | [Strings and type hints](docs/06_strings_and_type_hints.md) | `ex7` |

## Code and examples

Module 0 is a collection of independent demonstrations grouped by topic:

- [`functions_and_output.py`](examples/functions_and_output.py)
- [`input_and_data.py`](examples/input_and_data.py)
- [`decisions.py`](examples/decisions.py)
- [`repetition.py`](examples/repetition.py)
- [`strings_and_types.py`](examples/strings_and_types.py)

[`main.py`](main.py) provides a simple concept-based menu. Run it from this directory:

```bash
python3 main.py
```

Unlike Module 1's evolving shared object model, these small functions remain separate. They are grouped to make the relationships between fundamentals easier to follow without hiding their original beginner-friendly form.
