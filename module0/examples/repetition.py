"""Compare iterative and recursive counting."""


def ft_count_harvest_iterative():
    days_till_harvest = int(input("Days until harvest: "))
    # range() excludes its stop value, so + 1 includes the final day.
    for i in range(1, days_till_harvest + 1):
        print(f"Day {i}")
    print("Harvest time!")


def count_helper(day, num):
    # A recursive function needs a base case so calls eventually stop.
    if day == num + 1:
        print("Harvest time!")
        return
    print(f"Day {day}")
    count_helper(day + 1, num)


def ft_count_harvest_recursive():
    remain_days = int(input("Days until harvest: "))
    day = 1
    count_helper(day, remain_days)


def demonstrate():
    print("=== Iterative counting ===")
    ft_count_harvest_iterative()
    print("=== Recursive counting ===")
    ft_count_harvest_recursive()


if __name__ == "__main__":
    demonstrate()
