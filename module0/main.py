"""A concept-based launcher for the Module 0 examples."""

# These imports reuse the small demonstrations collected in examples/.
from examples.decisions import demonstrate as demonstrate_decisions
from examples.functions_and_output import demonstrate as demonstrate_functions
from examples.input_and_data import demonstrate as demonstrate_input
from examples.repetition import demonstrate as demonstrate_repetition
from examples.strings_and_types import demonstrate as demonstrate_strings


def show_menu():
    print("\nPython Fundamentals — Module 0")
    print("\nChoose a topic:\n")
    print("1. Functions and output")
    print("2. Input and data")
    print("3. Decisions")
    print("4. Repetition")
    print("5. Strings and type hints")
    print("0. Exit")


def main():
    choice = ""
    while choice != "0":
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            demonstrate_functions()
        elif choice == "2":
            demonstrate_input()
        elif choice == "3":
            demonstrate_decisions()
        elif choice == "4":
            demonstrate_repetition()
        elif choice == "5":
            demonstrate_strings()
        elif choice == "0":
            print("Goodbye!")
        else:
            print("Please choose a number from 0 to 5.")


if __name__ == "__main__":
    main()
