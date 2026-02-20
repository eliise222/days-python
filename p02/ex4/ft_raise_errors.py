def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name:
        raise ValueError("Plant name cannot be empty!\n")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)\n")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)\n")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours}\
 is too low (min 2)\n")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours}\
 is too high (max 12)\n")
    else:
        return (f"Plant '{plant_name}' is healthy!\n")


def test_plant_checker():
    print("=== Garden Plant Health Checker ===\n")

    check_name = False
    check_water = False
    check_sun = False

    print("Testing good values...")
    try:
        result = check_plant_health(plant_name="tomato", water_level=6,
                                    sunlight_hours=4)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing empty plant name...")
    try:
        check_plant_health(plant_name=None, water_level=5, sunlight_hours=6)
    except ValueError as e:
        print(f"Error: {e}")
        check_name = True

    print("Testing bad water level...")
    try:
        check_plant_health(plant_name="tomato", water_level=15,
                           sunlight_hours=5)
    except ValueError as e:
        print(f"Error: {e}")
        check_water = True

    print("Testing bad sunlight hours...")
    try:
        check_plant_health(plant_name="tomato", water_level=4,
                           sunlight_hours=0)
    except ValueError as e:
        print(f"Error: {e}")
        check_sun = True

    if check_name and check_water and check_sun:
        print("\nAll error raising tests completed!")
    else:
        print("Error: not all error tests are completed")


def main():
    test_plant_checker()


if __name__ == "__main__":
    main()
