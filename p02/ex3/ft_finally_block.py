def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Cannot water {plant} - invalid plant")
            else:
                print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def main():
    print("=== Gardening Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully\n")

    print("Testing with error...")
    water_plants(["tomato", None])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
