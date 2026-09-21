#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "sensor value: " + 42
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for number in range(5):
        print(f"Testing operation {number}...")
        try:
            garden_operations(number)
            print("Operation completed successfully\n")
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
