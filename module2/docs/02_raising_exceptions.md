# 02 — Raising Exceptions

## The original challenge

The temperature checker grew from one conversion failure into four test values: `"25"`, `"abc"`, `"-50"`, and `"100"`. Valid garden temperatures were limited to 0 through 40 degrees. Originally introduced in `ex1`.

## What can go wrong?

There are now two different reasons for a `ValueError`:

- `"abc"` is not an integer, so `int()` raises automatically.
- `-50` and `100` are integers, but the garden application's range rule rejects them.

The second case would not fail by itself. Python can represent both integers perfectly well.

## The new Python concept

`raise` deliberately starts exceptional control flow:

```python
temperature = int(temp_str)
if temperature < 0:
    raise ValueError("Temperature is too low")
if temperature > 40:
    raise ValueError("Temperature is too high")
```

Once raised, this manually created `ValueError` propagates and is handled in the same way as the one created by `int()`.

## How control flow changes

Successful conversion no longer guarantees a return:

```text
text → int()
  ├─ conversion fails → ValueError
  └─ integer produced → range check
                         ├─ rule fails → raised ValueError
                         └─ rule passes → return integer
```

## How my implementation demonstrates it

The public example preserves `input_temperature()`, the 0 and 40 boundaries, both original messages, and the original four-value loop. It also preserves the original choice to convert once into a local `temperature` variable before checking the rules; no extra validation framework is introduced.

Both failure sources use `ValueError` because each says the supplied value is unsuitable for the requested temperature operation. Their messages explain which source failed.

## Connection to the next concept

One exception type can describe related value problems, but not every operation fails for the same reason. The next stage uses different built-in types so handlers can respond precisely.

## Key takeaway

`raise` lets application rules create the same exceptional control-flow path that Python uses for failed built-in operations.
