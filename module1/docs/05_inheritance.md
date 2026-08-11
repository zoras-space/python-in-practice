# 05 — Inheritance

## The original challenge

This exercise expanded the garden with three specialized plant types. A `Flower` added color and blooming behavior, a `Tree` added trunk diameter and shade production, and a `Vegetable` added a harvest season and nutritional value that changed as it aged.

The specialized classes were expected to inherit the common plant state and behavior, call `super()` to reuse parent initialization or methods, and override `show()` where extra details were needed. The demonstration exercised each type's distinct behavior while keeping the shared `Plant` foundation visible.

## What this stage introduced

Originally introduced in `py01/ex5`, inheritance extended the common plant model into `Flower`, `Tree`, and `Vegetable`.

Without inheritance, each type would need to repeat the plant name, height, age, validation, growth, and display behavior. The new classes reuse that shared foundation and add only their specialized state and behavior.

```python
class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
```

`super()` delegates shared initialization to `Plant`. This represents an is-a relationship: a flower is a plant.

Subclasses also override methods. `Flower.show()` first calls `Plant.show()` and then adds its color and blooming state. `Vegetable.age()` keeps the inherited age update and also changes nutritional value.

| Class | Reused behavior | Specialized behavior or state |
|---|---|---|
| `Flower` | Plant state, growth, and aging | Color, blooming state, `bloom()` |
| `Tree` | Plant state, growth, and aging | Trunk diameter, `produce_shade()` |
| `Vegetable` | Plant state and growth | Harvest season and nutritional value |

These classes appear unchanged in purpose in the final shared model.

## Takeaway

Inheritance reuses a common model, while overriding lets a subtype extend shared behavior where its responsibilities differ.
