# 04 — Custom Exceptions

## The original challenge

Built-in exceptions describe general Python failures, but the garden now needed names for its own problems: a wilting plant and an insufficient water supply. Originally introduced in `ex3`.

## What can go wrong?

Neither problem is a failed conversion, missing file, nor invalid Python operation. Reusing an unrelated built-in type would lose the meaning that the application already knows.

## The new Python concept

A custom exception is a class derived from `Exception`, directly or indirectly:

```python
class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)
```

`GardenError` is the garden-wide parent. `PlantError` and `WaterError` inherit from it and supply more specific default messages. Each constructor calls `super().__init__(message)` so the parent exception stores and exposes the message in the normal way.

## How control flow changes

Custom exceptions use the same `raise`, propagation, and matching rules as built-in exceptions:

```python
raise PlantError("The tomato plant is wilting!")
```

The class adds domain meaning; it does not invent a separate error mechanism.

## How my implementation demonstrates it

The public hierarchy preserves all three original class names, docstrings, default messages, constructors, and `super()` calls. It also preserves `check_plant()` and `check_water()`, including their explicit messages.

The first demonstrations catch `PlantError` and `WaterError` separately. This shows that callers can react to the exact application problem rather than parsing message text. Messages are for people and context; exception types are the structured categories used by control flow.

## Connection to Module 1

This is the same inheritance relationship learned with plant classes, now applied to exception types. The next chapter explains why that relationship changes which handlers match.

## Key takeaway

Custom exception classes give application-specific failures meaningful, catchable types while retaining Python's standard exception behavior.
