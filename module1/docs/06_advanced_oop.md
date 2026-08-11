# 06 — Advanced OOP

## The original challenge

The final exercise combined the earlier model with several new forms of class behavior. `Plant` needed a static method that checks whether an age is greater than one year and a class method that creates an anonymous plant. It also needed a nested statistics class that counted calls to `grow()`, `age()`, and `show()`.

The garden then gained a `Seed` type derived from `Flower`, and tree statistics extended the common counters with calls to `produce_shade()`. A shared `display_statistics()` function had to work with different plant subtypes through the same interface. The expected demonstration checked ages, changed and displayed specialized plants, showed their counters, and created the anonymous plant.

These requirements brought static methods, class methods, nested classes, deeper inheritance, method overriding, and polymorphism into one final program. Running `mypy --strict` later also revealed that the anonymous-plant class method needed an explicit return type, leading to the forward-reference note below.

## What this stage introduced

Originally introduced in `ex6`, the final exercise added class-associated methods, nested statistics, deeper inheritance, and a function that works across plant types.

Earlier objects could model different plants, but they did not track method usage or demonstrate behavior associated with a class rather than one instance.

## Static and class methods

`Plant.check_age()` is a static method because it applies a plant-related rule without reading object or class state. `Plant.create_anonymous_plant()` is a class method and receives `cls`, providing an alternative named way to construct a plant.

```python
@staticmethod
def check_age(age: int) -> bool:
    return age > 365

@classmethod
def create_anonymous_plant(cls) -> "Plant":
    return cls("Unknown plant", 0, 0)
```

The decorators change how Python supplies the first argument: instance methods receive `self`, class methods receive `cls`, and static methods receive neither automatically.

### Forward references in type hints

The original class method had no return annotation. Running `mypy --strict` exposed that omission and led to adding `-> "Plant"`.

`Plant` is still being defined while Python executes the class body. Without postponed annotation evaluation, writing `-> Plant` there asks Python to resolve a name that is not available yet and raises a `NameError`. Quoting it creates a **forward reference**: the annotation refers to `Plant` by name and can be resolved after the class exists.

This is why the final method uses:

```python
@classmethod
def create_anonymous_plant(cls) -> "Plant":
    return cls("Unknown plant", 0, 0)
```

The annotation describes the result as a `Plant`, while `cls(...)` preserves the class-method construction behavior introduced in the exercise.

## Nested statistics

`Statistics` is nested inside `Plant` because it is a closely related component. Every plant owns a statistics object, and `grow()`, `age()`, and `show()` delegate call recording to it. Its double-underscore counters use name mangling to discourage direct outside access.

`Tree.Statistics` inherits the common counters and adds a shade counter. This mirrors the specialization of the outer `Tree` class.

## Deeper inheritance and polymorphism

`Seed` extends `Flower`, which already extends `Plant`:

```text
Plant
  └── Flower
        └── Seed
```

Calling `Seed.show()` moves through the inheritance chain so every level contributes to the output. The standalone `display_statistics(plant)` function accepts the shared `Plant` interface and works with plants, flowers, trees, and seeds. This is polymorphism: the same operation can collaborate with different related object types.

All of these features are preserved in [`garden_system.py`](../garden_system.py), which is based on the final `ex6` implementation.

## Takeaway

Class-level behavior, cooperating objects, and inheritance chains turn the original class into a small system without abandoning its shared interface.
