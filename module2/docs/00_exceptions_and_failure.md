# 00 — Exceptions and Failure

## The original challenge

The first challenge converted temperature text into an integer. One value, `"25"`, could be converted; another, `"abc"`, could not. This small contrast introduced the fact that an ordinary-looking operation may not finish normally.

Originally introduced in `ex0`.

## What can go wrong?

`int()` expects text that represents an integer. When it receives `"abc"`, it cannot produce the requested value. Python raises a `ValueError` and stops the current normal path through the function.

An exception is not merely text printed on the terminal. It is an object that participates in Python's control flow. Its type identifies the kind of failure, while its message carries information such as `invalid literal for int()`.

## The new Python concept

The conversion function remains intentionally small:

```python
def input_temperature(temp_str: str) -> int:
    return int(temp_str)
```

Its return annotation describes successful results. It does not promise that every string can be converted. If conversion fails, no integer is returned; the exception follows a different control-flow path.

## How control flow changes

Without a matching handler, the exception leaves `input_temperature()`, travels back to its caller, and may eventually stop the program. This movement upward through function calls is called **exception propagation**. Python continues looking for a compatible handler as the exception propagates.

The next chapter places the call inside `try` and supplies that handler.

## How my implementation demonstrates it

The public catching example preserves the original `input_temperature()` name, its `int(temp_str)` conversion, and the valid and invalid values. Keeping the conversion in its own function makes it visible that the failure begins inside one function and can be handled by its caller.

## Key takeaway

An exception is a typed object that changes control flow when an operation cannot complete normally; its message is only the descriptive information it carries.
