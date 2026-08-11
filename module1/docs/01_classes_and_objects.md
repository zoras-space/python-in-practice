# 01 — Classes and Objects

## What this stage introduced

Originally introduced in `py01/ex1`, `Plant` groups plant data with the `show()` behavior that uses it. A class is the reusable definition; each object is an independent instance made from that definition.

The earlier script stored one plant in separate local variables. It could display that plant, but it did not provide one reusable model for a rose, sunflower, and cactus.

```python
rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)

rose.show()
sunflower.show()
```

Both objects use the same method. Inside a method, `self` refers to the particular object that received the call, so `rose.show()` and `sunflower.show()` read different state.

This stage already used `__init__` in the original implementation. The constructor is discussed separately in the next stages so the ideas remain layered, but it was not added later in your code.

In [`garden_system.py`](../garden_system.py), `Plant` remains the common definition from which independent plant objects are created.

## Takeaway

One class can create many objects that share behavior without sharing their individual state.
