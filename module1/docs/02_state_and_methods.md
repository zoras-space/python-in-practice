# 02 — State and Methods

## The original challenge

The next exercise turned a plant from a fixed record into an object that changes over time. The `Plant` class needed `grow()` and `age()` methods in addition to `show()`.

The demonstration followed one rose for seven days. Each day increased its height by `0.8` centimetres and its age by one day, then displayed the updated state. At the end, the program reported the total growth for the week. This made persistence visible: each method call worked from the state left by the previous call.

## What this stage introduced

Originally introduced in `py01/ex2`, the plant stopped being a static record. The `grow()` and `age()` methods changed its height and age over time.

The `ex1` design could construct and display several objects, but it had no behavior for changing them.

```python
def grow(self, growth: float) -> None:
    self.height += growth

def age(self, days: int) -> None:
    self.plant_age += days
```

An object's state is the current set of values stored in its attributes. That state persists after a method returns:

```text
Plant state → grow() → updated height
            → age()  → updated age
            → show() → current state as output
```

The original code also changed the age attribute name from `age` in `ex1` to `plant_age` in `ex2` and `ex3`. It later became `_age` when encapsulation was added.

The final model keeps the same `grow()` and `age()` responsibilities, but routes updates through validated setters and records the calls for statistics.

## Takeaway

Methods can evolve an object's persistent state while keeping the related behavior inside its class.
