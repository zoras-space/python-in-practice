# Beyond the Exercises — ANSI Terminal Colors

This color experiment accompanied my Module 2 programs, but it is **not part of the formal exception-handling curriculum**. The exceptions remain understandable if every color code is ignored.

## From raw codes to named constants

The early temperature examples embedded escape sequences directly in strings:

```python
"\033[31m"
"\033[45m"
"\033[0m"
```

They worked, but a reader had to remember what each number meant. Later exercises gave the same values names:

```python
RED = "\033[31m"
GREEN = "\033[32m"
PINK_BG = "\033[45m"
GREEN_BG = "\033[42m"
RESET = "\033[0m"
```

This is a small readability progression:

```text
raw control code → works, but its meaning is hidden
named constant   → the output intent is visible
```

The public examples centralize these five constants in [`examples/colors.py`](../examples/colors.py). This removes repeated definitions while preserving the exact codes and names reached in the original implementation. It is deliberately a constants file, not a color framework or third-party dependency.

## What supplies the color?

Python's `print()` does not create these colors itself. The strings contain ANSI escape or control sequences. A compatible terminal recognizes them as formatting instructions while displaying the surrounding text.

The Module 2 code used only:

- `31` for a red foreground;
- `32` for a green foreground;
- `42` for a green background;
- `45` for a magenta background, named `PINK_BG` in my code;
- `0` to reset formatting.

Foreground and background settings are separate. That is why red or green can color letters while codes 42 and 45 color the area behind them.

`RESET` matters because terminal formatting can remain active after the intended word. Appending `\033[0m` restores the default so later output does not accidentally inherit the previous color or background.

## Why color fit these examples

Error-handling output naturally separates into categories: the operation being tested, the exception type, its message, and successful completion. My implementation used green for test labels, red within error names, a pink background for messages, and a green background for headings. The color is supportive presentation; exception types and plain text still carry the lesson.
