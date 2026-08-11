"""Demonstrate state that persists and changes between method calls."""

from garden_system import Plant


def main() -> None:
    rose = Plant("Rose", 25, 30)
    starting_height = rose.get_height()

    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 4):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.age(1)
        rose.show()

    growth = rose.get_height() - starting_height
    print(f"Growth over three days: {growth:.1f}cm")


if __name__ == "__main__":
    main()
