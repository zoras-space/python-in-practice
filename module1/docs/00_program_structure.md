# 00 — Program Structure

## The original challenge

The first exercise asked for a directly executable garden program. It stored the name, height, and age of one plant, printed them between a welcome and closing message, and started through a `main()` function.

The important structural requirement was the `if __name__ == "__main__":` entry-point pattern. The expected behavior was simple output, but the real lesson was learning how Python distinguishes a file being run from one being imported.

## What this stage introduced

Originally introduced in `py01/ex0`, this stage organized a small script around a `main()` function and the `if __name__ == "__main__":` guard.

Before this step, statements could simply run from top to bottom as soon as Python loaded the file. That becomes inconvenient when a file should also be imported elsewhere.

```python
def main() -> None:
    print("=== Welcome to My Garden ===")


if __name__ == "__main__":
    main()
```

Python sets `__name__` to `"__main__"` when a file is run directly. When another file imports it, `__name__` identifies the module instead, so the demonstration does not run automatically.

The public examples use the same structure. This lets each file act as a runnable demonstration while keeping its functions safe to import.

## Takeaway

A clear entry point separates code that defines reusable behavior from code that starts a program.
