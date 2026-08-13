"""Catch a conversion failure and allow the program to continue."""

from examples.colors import GREEN_BG, PINK_BG, RED, RESET


def input_temperature(temp_str: str) -> int:
    """Convert text to an integer temperature."""
    return int(temp_str)


def demonstrate() -> None:
    """Compare normal execution with a handled ValueError."""
    print(f"{GREEN_BG}=== Catching an Exception ==={RESET}")
    for value in ("25", "abc"):
        print(f"Input data is: '{value}'")
        try:
            # int() still raises; this block marks where failure may happen.
            temperature = input_temperature(value)
            print(f"Temperature is now: {temperature}°C")
        except ValueError as error:
            print(f"Caught {RED}ValueError{RESET}: {PINK_BG}{error}{RESET}")

    print("The demonstration continued after the handled exception.")


if __name__ == "__main__":
    demonstrate()
