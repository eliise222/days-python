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


def check_plant_water(plant_name, water_level, sunlight_hours):
    if water_level > 10:
        raise WaterError(f"Water level {water_level} is too high (max 10)\n")
    elif water_level < 1:
        raise WaterError(f"Water level {water_level} is too low (min 1)\n")


def check_plant_sunlight(plant_name, water_level, sunlight_hours):
    if sunlight_hours < 2:
        raise SunlightError(f"Sunlight hours {sunlight_hours}\
 is too low (min 2)\n")
    elif sunlight_hours > 12:
        raise SunlightError(f"Sunlight hours {sunlight_hours}\
 is too high (max 12)\n")


def check_plant_health(plant_name, water_level, sunlight_hours):
    if check_plant_sunlight and check_plant_water:
        print(f"{plant_name}: healthy (water: {water_level}, sun\
{sunlight_hours}")


class Plant():
    """
    Base class representing a generic plant with a name and height.
    """
    def __init__(self, name: str, water: int, sun: int):
        self.name = name
        self.water = water
        self.sun = sun


class Garden():
    def __init__(self, name):
        self.name = name
        self.all_plants = []

    def add_plant(self, plant: "Plant"):
        self.all_plants.append(plant)
        print(f"Added {plant.name} successfully")

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


def test_garden_management():

    print("=== Garden Management System ===\n")
    garden1 = Garden('garden1')
    
    plants = [Plant("tomato", 5, 8),
              Plant("lettuce", 15, 5),
              Plant(None, 5, 0)]
    print("Adding plants to garden...")
    for plt in plants:
        try:
            check_plant_name(plt.name)
            garden1.add_plant(plt)
        except ValueError as e:
            print(f"Error adding plant: {e}")
    print("\nWatering plants...")
    for plnt in plants:
        check_plant_water(plnt.water)
        garden1.water_plants(plt)
    # for p in garden1.all_plants:
    #     print(p.name, p.sun, p.water)


test_garden_management()
