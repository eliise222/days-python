class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class SunlightError(GardenError):
    pass


def check_plant_name(plant_name):
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")


def check_plant_water(plant_name, water_level):
    if water_level > 10:
        raise WaterError(f"Water level {water_level} is too high (max 10)\n")
    elif water_level < 1:
        raise WaterError(f"Water level {water_level} is too low (min 1)\n")


def check_plant_sunlight(plant_name, sunlight_hours):
    if sunlight_hours < 2:
        raise SunlightError(f"Sunlight hours {sunlight_hours}\
 is too low (min 2)\n")
    elif sunlight_hours > 12:
        raise SunlightError(f"Sunlight hours {sunlight_hours}\
 is too high (max 12)\n")


# def check_plant_health(plant_name, water_level, sunlight_hours):
#     if check_plant_sunlight and check_plant_water:
#         print(f"{plant_name}: healthy (water: {water_level}, sun\
# {sunlight_hours}")


class Plant():

    def __init__(self, name: str, water: int, sun: int):
        self.name = name
        self.water = water
        self.sun = sun


class Garden():
    def __init__(self):
        self.all_plants = []

    def add_plant(self, plant: "Plant"):
        check_plant_name(plant.name)
        self.all_plants.append(plant)
        print(f"Added {plant.name} successfully")

    def water_plants(self):
        try:
            print("Opening watering system")
            for plant in self.all_plants:
                if plant is None:
                    raise GardenError(f"Cannot water {plant} - invalid plant")
                else:
                    print(f"Watering {plant.name}")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, plant: Plant):
        check_plant_water(plant.name, plant.water)
        check_plant_sunlight(plant.name, plant.sun)
        print(f"{plant.name}: healthy (water: {plant.water}, sun: \
{plant.sun})")

def test_garden_management():

    print("=== Garden Management System ===\n")
    manager = Garden()
    
    plants = [Plant("tomato", 5, 8),
              Plant("lettuce", 15, 5),
              Plant(None, 5, 0)]

    print("Adding plants to garden...")
    for plt in plants:
        try:
            manager.add_plant(plt)
        except ValueError as e:
            print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    for plant in manager.all_plants:
        try:
            manager.check_health(plant)
        except (WaterError, SunlightError) as e:
            print(f"Error checking {plant.name}: {e}")

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caugh GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


def main():
    test_garden_management()


if __name__ == "__main__":
    main()


