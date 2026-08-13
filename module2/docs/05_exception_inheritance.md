# 05 — Exception Inheritance

## The original challenge

After catching plant and water failures separately, the same program needed one handler capable of catching every garden-related problem. Originally introduced in `ex3`.

## The new Python concept

The custom hierarchy is:

```text
Exception
  └── GardenError
        ├── PlantError
        └── WaterError
```

Inheritance means a `PlantError` **is also** a `GardenError`. The same is true for `WaterError`. Consequently, this broader handler matches either subclass:

```python
except GardenError as error:
    print(f"Caught GardenError: {error}")
```

## How control flow changes

When an exception reaches a series of handlers, Python tests them from top to bottom and enters the first compatible one. Compatibility includes parent classes, not only exact type equality.

This supports two levels of response:

- catch `PlantError` or `WaterError` when the distinction matters;
- catch `GardenError` when one response is suitable for any garden failure.

## Handler order

Specific handlers should generally appear before their broader parent:

```python
except PlantError as error:
    handle_plant_problem(error)
except GardenError as error:
    handle_other_garden_problem(error)
```

If `GardenError` came first, it would already match a `PlantError`, so the specific handler could never run. The focused public demonstration uses separate `try` statements for its specific and broad cases, keeping each relationship easy to see.

## How my implementation demonstrates it

The example first raises and catches each subclass by its own name. It then loops over the same `check_plant` and `check_water` functions and catches both through `GardenError`. This preserves the original progression without duplicating the exception definitions in later files.

The hierarchy is defined once in `custom_exceptions.py`. The cleanup example imports `PlantError` from there, showing that a custom exception is a reusable part of the program's interface.

## Connection to Module 1

Just as a `Flower` could be used where a `Plant` was expected, a `PlantError` can be handled where a `GardenError` is expected. The class hierarchy gives both systems their broad and specific interfaces.

## Key takeaway

Exception inheritance lets callers choose the level of detail they need, from one specific failure to an entire related family.
