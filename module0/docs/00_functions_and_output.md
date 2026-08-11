# 00 — Functions and Output

## The original challenge

The first exercise asked for one function named `ft_hello_garden()` that printed a fixed greeting. Calling the function was expected to produce `Hello, Garden Community!` and nothing depended on user input yet.

## What this stage introduced

Originally introduced in `ex0`, this was the smallest reusable unit in the module:

```python
def ft_hello_garden():
    print("Hello, Garden Community!")
```

`def` begins a function definition. The indented body belongs to the function and runs when the function is called. Giving this behavior a name means another file can import and reuse it.

`print()` sends the greeting to standard output. Printing is a side effect: the function changes what the user can observe instead of returning a calculated value.

At this stage there are no parameters, variables, or decisions. [`functions_and_output.py`](../examples/functions_and_output.py) deliberately keeps the example that small.

## How it is reused later

Every later exercise still organizes behavior in a function and uses `print()` to present a result. The output gradually changes from fixed text to text built from input, expressions, and conditions.

## Takeaway

A function groups statements into a named action, and indentation defines which statements belong to it.
