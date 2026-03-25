def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    inp = "25"
    print(f"Input data is '{inp}'")
    try:
        temp = input_temperature(inp)
        print(f"Temperature is now {temp}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    inp = "abc"
    print(f"Input data is '{inp}'")
    try:
        temp = input_temperature(inp)
        print(f"Temperature is now {temp}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
