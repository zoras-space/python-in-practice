"""Use specialized plant types that share Plant behavior."""

from garden_system import Flower, Tree, Vegetable


def main() -> None:
    rose = Flower("Rose", 15, 10, "red")
    oak = Tree("Oak", 200, 365, 5)
    tomato = Vegetable("Tomato", 5, 10, "April", 0)

    print("=== Flower ===")
    rose.show()
    rose.bloom()
    rose.show()

    print("=== Tree ===")
    oak.show()
    oak.produce_shade()

    print("=== Vegetable ===")
    tomato.show()
    tomato.grow(42)
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    main()
