# 04 — Encapsulation

## What this stage introduced

Originally introduced in `py01/ex4`, encapsulation placed height and age behind a controlled interface.

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
