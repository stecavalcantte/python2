#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    for data in ["25", "abc"]:
        print(f"Input data is '{data}'")
        try:
            temperature = input_temperature(data)
            print(f"Temperature is now {temperature}°C\n")
        except Exception as error:
            print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
