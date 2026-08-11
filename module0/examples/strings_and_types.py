"""Function parameters, string methods, and type annotations."""


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    unit_type = "Unknown unit type"
    prefix = " "
    if unit == "area":
        unit_type = "square meter"
        prefix = " covers "
    elif unit == "grams":
        unit_type = unit + " total"
    elif unit == "packets":
        unit_type = unit + " available"

    # capitalize() returns a changed string; it does not modify seed_type.
    print(f"{seed_type.capitalize()} seeds:{prefix}{quantity} {unit_type}")


def demonstrate() -> None:
    print("=== Strings and type hints ===")
    ft_seed_inventory("tomato", 15, "packets")
    ft_seed_inventory("carrot", 8, "grams")
    ft_seed_inventory("lettuce", 12, "area")
    ft_seed_inventory("basil", 5, "unknown")


if __name__ == "__main__":
    demonstrate()
