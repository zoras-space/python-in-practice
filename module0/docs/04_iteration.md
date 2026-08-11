# 04 — Iteration

## The original challenge

Repetition appeared first in `ex3`, where a `while` loop collected three harvest weights. In `ex6`, the iterative solution asked for the number of days until harvest, printed every day number beginning with 1, and then printed `Harvest time!`.

The counting exercise deliberately had both iterative and recursive versions. The iterative version needed to use a loop and include the final requested day.

## Repeating with loops

A `while` loop repeats while its condition remains true. In the harvest-total function, a counter starts at 1 and the condition `count < 4` limits the program to three entries. The counter must change so the condition eventually becomes false.

A `for` loop visits values supplied by an iterable such as `range()`:

```python
for i in range(1, days_till_harvest + 1):
    print(f"Day {i}")
```

`range()` excludes its stop value. Adding 1 to the requested number includes the last day in the output.

| Loop tool | Role in the original code |
|---|---|
| `while` | Repeat input while updating a counter and accumulator |
| `for` with `range()` | Visit a known sequence of day numbers |

The loop-based counting remains in [`repetition.py`](../examples/repetition.py). It creates a direct comparison with the recursive version without changing the required output.

## Takeaway

Iteration repeats work in one function call. A condition or finite range determines when that repetition ends.
