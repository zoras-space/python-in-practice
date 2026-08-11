# 05 — Recursion

## The original challenge

The second half of `ex6` asked for the same countdown-to-harvest behavior without using the iterative structure. It still had to print day numbers from 1 through the requested day and finish with `Harvest time!`.

This made it possible to compare two mechanisms that produce the same visible result.

## Repeating with function calls

The original implementation uses a helper carrying the current day and final day:

```python
def count_helper(day, num):
    if day == num + 1:
        print("Harvest time!")
        return
    print(f"Day {day}")
    count_helper(day + 1, num)
```

The call to `count_helper(day + 1, num)` is the recursive case. It advances the state and calls the same function again.

The `if` branch is the base case. It stops further calls after the last day. Without a reachable base case, recursion would continue until Python raised an error for exceeding its recursion limit.

| Iteration | Recursion |
|---|---|
| Repeats with `for` or `while` | Repeats through function calls |
| Loop variables change in one call | Arguments carry changing state into new calls |
| A condition or range stops the loop | A base case stops recursive calls |

Both implementations remain beside each other in [`repetition.py`](../examples/repetition.py).

## Takeaway

Recursion needs both a case that advances the problem and a base case that guarantees it will stop.
