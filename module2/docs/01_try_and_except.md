# 01 — `try` and `except`

## The original challenge

The program needed to attempt temperature conversion, respond to invalid input, and reach a final message instead of crashing. Originally introduced in `ex0`.

## What can go wrong?

Calling `input_temperature("abc")` raises `ValueError`. Any later statements in the same `try` block are skipped because normal execution has already been interrupted.

## The new Python concept

`try` marks code whose exception should be handled. It does **not** prevent the exception:

```python
try:
    temperature = input_temperature(value)
    print(f"Temperature is now: {temperature}°C")
except ValueError as error:
    print(f"Caught ValueError: {error}")
```

The operation still raises `ValueError`. Python then searches for a matching `except`. `as error` binds the actual exception object, so its message can be inspected or displayed.

## How control flow changes

```text
conversion succeeds → remaining try statements → after try/except
conversion fails    → matching except handler  → after try/except
```

Once `int()` raises, the success print is not executed for that value. The handler runs instead. After it finishes, execution continues after the whole `try`/`except` statement.

## How my implementation demonstrates it

The public example loops over `"25"` and `"abc"` so the two paths sit next to each other. The original code performed the same two tests in one `try` block; using one small `try` per value makes continuation after the failure directly visible and prepares for the multi-value loop in `ex1`.

The handler catches `ValueError`, not every possible exception. A precise handler documents the expected failure and avoids disguising unrelated programming mistakes.

## Connection to the next concept

So far, Python decides that conversion is impossible. Next, the application will reject integers that convert successfully but violate its temperature rules.

## Key takeaway

`try` allows an exception to be matched with a handler; it does not stop the exception from being raised.
