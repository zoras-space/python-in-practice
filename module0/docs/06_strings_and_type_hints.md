# 06 — Strings and Type Hints

## The original challenge

The final exercise, `ex7`, asked for a seed-inventory function with three parameters: a seed type, a quantity, and a unit. It needed explicit annotations for those parameters and a `-> None` return annotation.

The function selected a description for area, grams, packets, or an unknown unit. It also capitalized the seed name before printing the completed inventory message. Static checking with `mypy` made the annotations part of the learning task.

## Parameters and strings

Parameters are names in a function definition. Arguments are the values supplied when it is called:

```python
def ft_seed_inventory(seed_type: str, quantity: int,
                      unit: str) -> None:
```

The function uses conditions to build different strings for each unit. It joins some strings with `+` and combines text with values in an f-string.

Strings are objects with methods. `seed_type.capitalize()` returns a new string with its first character uppercase and the remaining characters lowercase. It does not modify the original string.

## Type annotations and mypy

- `seed_type: str` describes a string parameter.
- `quantity: int` describes an integer parameter.
- `-> None` says the function prints its result rather than returning a useful value.

Annotations communicate intent to readers, editors, and static-analysis tools. `mypy` can report mismatched argument types before the program runs. Python does not normally enforce these annotations by itself at runtime.

The original function is preserved in [`strings_and_types.py`](../examples/strings_and_types.py), along with calls using each supported unit and the fallback case.

## Takeaway

Parameters make a function reusable with different data, string methods transform text, and type hints let static tools check how values are intended to flow through the function.
