"""Deliberately trigger and handle several built-in exception types."""

from examples.colors import GREEN, GREEN_BG, PINK_BG, RED, RESET


def garden_operation(operation_number: int) -> None:
    """Run one deliberately faulty operation, or one successful operation."""
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        42 / 0
    elif operation_number == 2:
        open("not_existing_random_file.txt")
    elif operation_number == 3:
        # This intentional runtime TypeError is also a valid mypy warning.
        "Hello" + 42


def demonstrate() -> None:
    """Show that handlers can respond precisely to different failures."""
    print(f"{GREEN_BG}=== Built-in Exception Types ==={RESET}")
    for operation_number in range(5):
        print(f"{GREEN}Testing operation {operation_number}...{RESET}")
        try:
            garden_operation(operation_number)
            print("Operation completed successfully")
        except ValueError as error:
            print(f"Caught Value{RED}Error{RESET}: {PINK_BG}{error}{RESET}")
        except ZeroDivisionError as error:
            print(
                f"Caught ZeroDivision{RED}Error{RESET}: "
                f"{PINK_BG}{error}{RESET}"
            )
        except FileNotFoundError as error:
            print(
                f"Caught FileNotFound{RED}Error{RESET}: "
                f"{PINK_BG}{error}{RESET}"
            )
        except TypeError as error:
            print(f"Caught Type{RED}Error{RESET}: {PINK_BG}{error}{RESET}")

    print("All operations were attempted; handled failures did not stop "
          "the loop.")


if __name__ == "__main__":
    demonstrate()
