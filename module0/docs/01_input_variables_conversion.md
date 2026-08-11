# 01 — Input, Variables, and Conversion

## The original challenge

The next exercises made the output depend on information entered by the user. `ex1` asked for a garden name. `ex2` asked for a plot length and width. `ex3` asked for three daily harvest weights and kept a combined total.

The programs needed to store each answer, turn numerical answers into integers, and use those values later. The expected behavior moved from a fixed greeting to results based on the user's data.

## What new problem appeared

`input()` always returns a string. That is already suitable for a garden name, but text such as `"5"` must be converted before integer arithmetic:

```python
plot_length = int(input("Enter length: "))
```

This statement follows a small data pipeline:

```text
Input → Conversion → Stored value → Processing → Output
 text      int()        variable       arithmetic   print()
```

Variables give values names so they can be reused. The original functions stored garden names, dimensions, harvest weights, and a counter this way.

`ex3` used a `while` loop earlier than the later loop-focused exercise. Here its role was practical: request exactly three values. The loop itself is examined in [Iteration](04_iteration.md).

These functions remain together in [`input_and_data.py`](../examples/input_and_data.py).

## Takeaway

User input starts as text. Variables preserve it, and explicit conversion prepares numerical input for calculations.
