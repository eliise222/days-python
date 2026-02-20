class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def Garden_Maintenance(available_water, plant_alive, plant_name="tomato"):
    if not available_water:
        raise WaterError("Not enough water in the tank!")
    if not plant_alive:
        raise PlantError(f"The {plant_name} plant is wilting!")


def main():
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        Garden_Maintenance(available_water=True, plant_alive=False,
                           plant_name="tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\n")

    print("Testing WaterError...")

    try:
        Garden_Maintenance(available_water=False, plant_alive=True)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\n")

    print("Testing catching all garden errors...")
    water = False
    plant = False

    try:
        Garden_Maintenance(available_water=True, plant_alive=False,
                           plant_name="tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
        plant = True

    try:
        Garden_Maintenance(available_water=False, plant_alive=True)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
        water = True

    if water and plant:
        print("\nAll custom error types work correctly!")
    else:
        print("\nError: All custom error types not work correctly...")


if __name__ == "__main__":
    main()
