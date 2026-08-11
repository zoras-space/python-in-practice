# 04 — Encapsulation

## The original challenge

This exercise asked for the plant's name, height, and age to be treated as protected state. Height and age had to be read through getters and changed through setters rather than updated freely from outside the class.

The setters also had to reject negative values. The demonstration created a plant, accepted valid height and age changes, rejected invalid negative changes, and finally showed that the last valid state had been preserved. These requirements explain why the implementation uses explicit getters and setters instead of a different interface.

## What this stage introduced

Originally introduced in `ex4`, encapsulation placed height and age behind a controlled interface.

Earlier methods and outside code could update public attributes directly. Nothing prevented a negative height or age.

```python
def set_height(self, height: float) -> None:
    if height >= 0:
        self._height = height
    else:
        print(f"{self._name}: Error, height can't be negative")
```

The leading underscore marks `_name`, `_height`, and `_age` as internal by convention. It is not an absolute access restriction. Getters expose values, while setters apply validation before changing them.

```text
requested change → setter → validation → internal state
```

The constructor also calls the setters. This avoids having one validation rule during construction and another during later updates. The final shared model preserves this design instead of replacing it with properties.

## Takeaway

Encapsulation gives all state changes one consistent path and protects the rules an object is meant to maintain.
