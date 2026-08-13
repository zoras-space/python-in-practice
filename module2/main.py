"""A concept-based launcher for the Module 2 examples."""

from examples.catching_exceptions import demonstrate as demonstrate_catching
from examples.cleanup_with_finally import demonstrate as demonstrate_cleanup
from examples.custom_exceptions import demonstrate as demonstrate_custom
from examples.exception_types import demonstrate as demonstrate_types
from examples.raising_exceptions import demonstrate as demonstrate_raising


def show_menu() -> None:
    print("\nPython Exceptions — Module 2")
    print("\nChoose a topic:\n")
    print("1. Catching exceptions")
    print("2. Raising exceptions")
    print("3. Built-in exception types")
    print("4. Custom exceptions")
    print("5. Cleanup with finally")
    print("6. Exit")


def main() -> None:
    choice = ""
    while choice != "6":
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            demonstrate_catching()
        elif choice == "2":
            demonstrate_raising()
        elif choice == "3":
            demonstrate_types()
        elif choice == "4":
            demonstrate_custom()
        elif choice == "5":
            demonstrate_cleanup()
        elif choice == "6":
            print("Goodbye!")
        else:
            print("Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
