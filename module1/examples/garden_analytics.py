"""Demonstrate the advanced OOP features from the final exercise."""

from garden_system import Plant, Seed, Tree, display_statistics


def main() -> None:
    print("=== Static method ===")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")

    print("=== Seed inheritance ===")
    sunflower = Seed("Sunflower", 80, 45, "yellow", 42)
    sunflower.show()
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("=== Specialized statistics ===")
    oak = Tree("Oak", 200, 365, 5)
    oak.produce_shade()
    display_statistics(oak)

    print("=== Class method ===")
    anonymous = Plant.create_anonymous_plant()
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    main()
