"""Model garden-specific failures with an exception hierarchy."""

from examples.colors import GREEN, GREEN_BG, PINK_BG, RED, RESET


class GardenError(Exception):
    """Base exception for garden-related problems."""

    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Exception raised for plant-related problems."""

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Exception raised for watering-related problems."""

    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant() -> None:
    """Raise an error describing a problem with a plant."""
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    """Raise an error describing a problem with the water supply."""
    raise WaterError("Not enough water in the tank!")


def demonstrate() -> None:
    """Catch custom errors first specifically, then through their parent."""
    print(f"{GREEN_BG}=== Custom Garden Exceptions ==={RESET}")

    print(f"{GREEN}Testing PlantError...{RESET}")
    try:
        check_plant()
    except PlantError as error:
        print(f"Caught {RED}PlantError{RESET}: {PINK_BG}{error}{RESET}")

    print(f"{GREEN}Testing WaterError...{RESET}")
    try:
        check_water()
    except WaterError as error:
        print(f"Caught {RED}WaterError{RESET}: {PINK_BG}{error}{RESET}")

    print(f"{GREEN}Catching both through GardenError...{RESET}")
    for operation in (check_plant, check_water):
        try:
            operation()
        # A GardenError handler matches PlantError and WaterError subclasses.
        except GardenError as error:
            print(f"Caught {RED}GardenError{RESET}: {PINK_BG}{error}{RESET}")

    print("All custom exception types work correctly.")


if __name__ == "__main__":
    demonstrate()
