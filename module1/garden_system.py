"""The shared garden model reached at the end of py01."""


class Plant:
    """Represent a plant and track how its public methods are used."""

    class Statistics:
        """Keep analytics closely associated with the Plant model."""

        def __init__(self) -> None:
            # Double underscores trigger name mangling and discourage outside
            # code from changing the counters directly.
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0

        def record_grow(self) -> None:
            self.__grow_calls += 1

        def record_age(self) -> None:
            self.__age_calls += 1

        def record_show(self) -> None:
            self.__show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self.__grow_calls} grow, "
                  f"{self.__age_calls} age, {self.__show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        # Every object receives its own state and Statistics instance.
        self._name = name
        self._height = 0.0
        self._age = 0
        self._statistics = self.Statistics()

        # Reusing the setters applies the same validation during construction
        # and during later updates.
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        self._statistics.record_show()
        print(f"{self._name}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")

    def grow(self, growth: float) -> None:
        # State remains on self after this method returns, so later calls to
        # show() observe the updated height.
        self.set_height(self.get_height() + growth)
        self._statistics.record_grow()

    def age(self, days: int) -> None:
        self.set_age(self.get_age() + days)
        self._statistics.record_age()

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
        else:
            print(f"{self._name}: Error, height can't be negative")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
        else:
            print(f"{self._name}: Error, age can't be negative")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    @staticmethod
    def check_age(age: int) -> bool:
        # This rule is related to Plant, but it needs no object state.
        return age > 365

    @classmethod
    def create_anonymous_plant(cls) -> "Plant":
        # cls keeps construction attached to the class instead of hard-coding
        # Plant here. This is the alternative constructor from the exercise.
        # The quotes make Plant a forward reference because the class name is
        # not available until Python finishes creating the class.
        return cls("Unknown plant", 0, 0)

    def display_statistics(self) -> None:
        self._statistics.display()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        # super() lets Plant initialize the state shared by every plant type.
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        # This override extends the inherited display instead of duplicating
        # the shared part.
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self.__shade_calls = 0

        def record_shade(self) -> None:
            self.__shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self.__shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        # Tree keeps the specialized reference used by produce_shade(), then
        # makes it the statistics object used by inherited Plant methods too.
        self._tree_statistics = self.Statistics()
        self._statistics = self._tree_statistics
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self._tree_statistics.record_shade()
        print(f"Tree {self._name} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def age(self, days: int) -> None:
        # Aging still updates the Plant state and its statistics before adding
        # the behavior specific to a Vegetable.
        super().age(days)
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, seeds: int) -> None:
        super().__init__(name, height, age, color)
        self.__seeds = seeds

    def show(self) -> None:
        # The call travels through Flower.show() and then Plant.show().
        super().show()
        if self.is_blooming:
            print(f"Seeds: {self.__seeds}")
        else:
            print("Seeds: 0")


def display_statistics(plant: Plant) -> None:
    """Display statistics through the interface shared by all plant types."""
    print(f"[statistics for {plant._name}]")
    plant.display_statistics()
