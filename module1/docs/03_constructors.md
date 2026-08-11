# 03 — Constructors and Object Creation

## What this stage introduced

The original implementation introduced `__init__` in `py01/ex1`, earlier than the rough exercise summary suggests. By `py01/ex3`, the main new emphasis was using that constructor repeatedly to build a collection cleanly.

Without a constructor, code would need to create an object and assign each attribute separately. That makes incomplete objects possible and repeats setup at every call site.

```python
def __init__(self, name: str, height: float, age: int) -> None:
    self.name = name
    self.height = height
    self.plant_age = age
```

`__init__` runs during object creation and gives every new object its starting state. In `ex3`, five calls such as `Plant("Rose", 25, 30)` were placed in a list and displayed with a loop. This made the benefit of consistent construction visible even though the mechanism already existed.

The final constructor in [`garden_system.py`](../garden_system.py) initializes protected attributes, creates a separate statistics object, and uses setters so initial values receive the same validation as later changes.

## Takeaway

A constructor establishes valid starting state in one predictable step. In this implementation, `ex3` reinforced scalable creation rather than introducing `__init__` for the first time.
