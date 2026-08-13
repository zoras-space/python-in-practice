"""Guarantee watering-system cleanup with finally."""

from examples.colors import GREEN, GREEN_BG, PINK_BG, RED, RESET
from examples.custom_exceptions import PlantError


def water_plant(plant_name: str) -> None:
    """Water a plant if its name is correctly capitalized."""
    if plant_name.capitalize() != plant_name:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    """Close the watering system after successful and failed runs."""
    print(f"{GREEN}Testing valid plants...{RESET}")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print(f"Caught {RED}PlantError{RESET}: {PINK_BG}{error}{RESET}")
    finally:
        # Closing belongs here because it is required on every control path.
        print("Closing watering system")

    print(f"{GREEN}Testing invalid plants...{RESET}")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as error:
        print(f"Caught {RED}PlantError{RESET}: {PINK_BG}{error}{RESET}")
        print(".. ending tests and returning to main")
        return
    finally:
        # This runs before the return in the matching except takes effect.
        print("Closing watering system")


def demonstrate() -> None:
    """Run the garden watering-system demonstration."""
    print(f"{GREEN_BG}=== Cleanup with finally ==={RESET}")
    test_watering_system()
    print("Cleanup always happens, even with errors.")


if __name__ == "__main__":
    demonstrate()
