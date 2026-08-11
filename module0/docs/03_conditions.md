# 03 — Conditions

## The original challenge

Two exercises asked the program to choose between messages. In `ex4`, a plant older than 60 days was ready to harvest; otherwise it needed more time. In `ex5`, more than two days since watering meant the plants needed water; otherwise they were fine.

Both programs converted the entered number to an integer, compared it with a threshold, and printed exactly one outcome.

## What this stage introduced

A comparison such as `plant_age > 60` evaluates to either `True` or `False`. An `if` statement uses that result to choose a branch:

```python
if plant_age > 60:
    print("Plant is ready to harvest!")
else:
    print("Plant needs more time to grow.")
```

`=` assigns a value. `>` compares two values. Keeping those roles distinct is essential.

Only one branch runs. The `else` branch handles every value that did not satisfy the comparison, including the boundary value itself. A plant aged exactly 60 days therefore follows the “needs more time” branch in the original implementation.

Both decisions are preserved in [`decisions.py`](../examples/decisions.py).

## How it is reused later

Conditions later control whether loops continue, when recursion stops, and which seed-unit description is selected.

## Takeaway

Comparisons produce Boolean results, and conditional branches turn those results into different program behavior.
