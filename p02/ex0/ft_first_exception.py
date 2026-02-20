def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    inp = input("Testing temperature: ")
    try:
        temp = int(inp)
        if temp < 0:
            print(f"Error: '{temp}°C' is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: '{temp}°C' is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")

    except ValueError:
        print(f"Error: '{inp}' is not a valid number")


test_temperature_input()
