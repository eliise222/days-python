class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def garden_maintenance(available_water: bool, plant_alive: bool,
                       plant_name: str = "tomato") -> None:
    if not available_water:
        raise WaterError("Not enough water in the tank!")
    if not plant_alive:
        raise PlantError(f"The {plant_name} plant is wilting!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        garden_maintenance(available_water=True, plant_alive=False)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        garden_maintenance(available_water=False, plant_alive=True)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors..")

    try:
        garden_maintenance(available_water=True, plant_alive=False)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        garden_maintenance(available_water=False, plant_alive=True)
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
