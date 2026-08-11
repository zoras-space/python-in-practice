# 00 — Program Structure

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
