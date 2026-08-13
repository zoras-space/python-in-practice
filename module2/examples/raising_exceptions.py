"""Contrast conversion errors with deliberate validation errors."""

from examples.colors import GREEN_BG, PINK_BG, RED, RESET


def input_temperature(temp_str: str) -> int:
    """Convert and validate a garden temperature."""
    temperature = int(temp_str)

    # Conversion succeeded, but the application can still reject the value.
    if temperature < 0:
        raise ValueError("Temperature is too low")
    if temperature > 40:
        raise ValueError("Temperature is too high")

    return temperature


def demonstrate() -> None:
    """Run the original set of valid and invalid temperature values."""
    print(f"{GREEN_BG}=== Raising Exceptions ==={RESET}")
    for value in ("25", "abc", "-50", "100"):
        print(f"Input data is: '{value}'")
        try:
            temperature = input_temperature(value)
            print(f"Temperature is now: {temperature}°C")
        except ValueError as error:
            print(f"Caught {RED}ValueError{RESET}: {PINK_BG}{error}{RESET}")

    print("Conversion and validation failures were both handled.")


if __name__ == "__main__":
    demonstrate()
