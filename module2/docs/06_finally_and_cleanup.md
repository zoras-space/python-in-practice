# 06 — `finally` and Cleanup

## The original challenge

The final watering demonstration opened a system, watered several plants, and always had to close the system. It tested both correctly capitalized names and the invalid lowercase `"lettuce"`. Originally introduced in `ex4`.

## What can go wrong?

`water_plant()` raises `PlantError` for the invalid name. Ordinary statements placed after that call in the `try` block would be skipped. Placing cleanup only on the success path could therefore leave the watering system conceptually open.

## The new Python concept

`finally` contains work that must run when control leaves the protected operation, whether the operation succeeded or raised:

```python
try:
    water_plant("lettuce")
except PlantError as error:
    print(f"Caught PlantError: {error}")
finally:
    print("Closing watering system")
```

## How control flow changes

```text
success   → finally → continue
exception → except  → finally → continue
```

The original failure handler also executes `return`. Even then, the function does not return immediately past the cleanup:

```text
exception → except requests return → finally → function returns
```

That guarantee is the point of this exercise. A context manager may be a common resource-management tool in later Python, but replacing the explicit structure here would hide the `finally` lesson.

## How my implementation demonstrates it

The public example preserves the original capitalization rule, plant names, success and failure runs, error message, `return`, and both `finally` blocks. Its only structural reuse is importing the already-defined `PlantError` instead of copying the hierarchy from `ex3` into the final file.

The output shows `Closing watering system` after all valid plants. It shows the same line after the invalid plant and after the handler announces its return. The enclosing demonstration then prints its final message, confirming that cleanup completed.

## Connection to the progression

Earlier handlers decided how to respond to particular failures. `finally` serves a different responsibility: it guarantees shared cleanup regardless of which control-flow path was taken.

## Key takeaway

Put required cleanup in `finally` when it must happen after both success and failure—even before a pending `return` completes.
