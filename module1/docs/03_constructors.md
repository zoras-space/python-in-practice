# 03 — Constructors and Object Creation

## The original challenge

This stage focused on creating a group of plants with complete initial values. The program constructed five different plants, stored them in a list, and used a loop to display each one as factory output.

Supplying name, height, and age during construction kept object creation consistent and avoided repeating attribute assignment after every object was made. In my implementation, `__init__` was already present in `ex1`; this exercise made its practical value clearer by using it repeatedly rather than introducing it for the first time.

## What this stage introduced

The original implementation introduced `__init__` in `ex1`, earlier than the rough exercise summary suggests. By `ex3`, the main new emphasis was using that constructor repeatedly to build a collection cleanly.

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
