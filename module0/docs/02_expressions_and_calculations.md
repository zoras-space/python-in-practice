# 02 — Expressions and Calculations

## The original challenge

`ex2` needed to calculate the area of a rectangular plot by multiplying its length and width. `ex3` needed to combine three harvest weights into one total.

Both exercises required the program to produce a new value from converted input rather than only repeat what the user entered.

## Expressions and statements

An expression evaluates to a value. A statement performs an action.

| Code | Role | Result |
|---|---|---|
| `plot_length * plot_width` | Expression | The calculated area |
| `harvest_weight + new_weight` | Expression | A new total |
| `harvest_weight = 0` | Assignment statement | Stores a starting value |
| `count += 1` | Assignment statement | Updates the stored counter |

The area calculation appears directly inside an f-string:

```python
print(f"Plot area: {plot_length * plot_width}")
```

The harvest total uses an accumulator. It starts at zero and preserves the combined weight as each new entry arrives:

```python
harvest_weight += int(input(f"Day {count} harvest: "))
```

The counter and accumulator have different jobs. `count` tracks how many entries have been processed, while `harvest_weight` combines their values.

Both implementations are preserved in [`input_and_data.py`](../examples/input_and_data.py). Accumulation becomes an important reason to use loops in the next stages.

## Takeaway

Expressions create values. Assignments, counters, and accumulators let a program keep and build on those results.
