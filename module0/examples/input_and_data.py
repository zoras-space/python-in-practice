"""Input, variables, conversion, calculations, and totals."""


def ft_garden_name():
    garden_name = input("Enter garden name: ")
    print("Garden: " + garden_name + "\nStatus: Growing well!")


def ft_plot_area():
    # input() produces text. int() converts that text before multiplication.
    plot_length = int(input("Enter length: "))
    plot_width = int(input("Enter width: "))
    print(f"Plot area: {plot_length * plot_width}")


def ft_harvest_total():
    harvest_weight = 0
    count = 1
    while count < 4:
        # The accumulator keeps the combined weight from earlier entries.
        harvest_weight += int(input(f"Day {count} harvest: "))
        count += 1
    print("Total harvest:", harvest_weight)


def demonstrate():
    print("=== Input and data ===")
    ft_garden_name()
    ft_plot_area()
    ft_harvest_total()


if __name__ == "__main__":
    demonstrate()
