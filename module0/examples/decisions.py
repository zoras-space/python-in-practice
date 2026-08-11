"""Comparison expressions and conditional decisions."""


def ft_plant_age():
    plant_age = int(input("Enter plant age in days: "))
    if plant_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")


def ft_water_reminder():
    days_since_wet = int(input("Days since last watering: "))
    if days_since_wet > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")


def demonstrate():
    print("=== Decisions ===")
    ft_plant_age()
    ft_water_reminder()


if __name__ == "__main__":
    demonstrate()
