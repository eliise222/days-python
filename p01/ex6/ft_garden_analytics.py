class Plant():
    """
    Base class representing a generic plant with a name and height.
    """
    def __init__(self, name: str, height: int):
        """
        Initializes a generic Plant with a name and height in cm.
        """
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    """
    Represents a plant that produces flowers, inheriting from Plant.
    """
    def __init__(self, name: str, height: int, color: str) -> None:
        """
        Initializes a FloweringPlant with an additional color attribute.
        """
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    """
    Premium flower type for competitions, inheriting from FloweringPlant.
    """
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        """
        Initializes a PrizeFlower with competition prize points.
        """
        super().__init__(name, height, color)
        self.prize = prize


class Garden:
    """
    Manages a collection of plants and calculates garden-wide metrics.
    """
    total_garden = 0
    all_gardens = []

    def __init__(self, name: str) -> None:
        """
        Initializes a Garden and registers it in the global garden list.
        """
        self.name = name
        self.all_plants = []
        Garden.total_garden += 1
        self.all_gardens.append(self)

    def add_plants(self, plant: "Plant") -> None:
        """
        Adds a plant object to the current garden's collection.
        """
        self.all_plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def garden_score(self) -> int:
        """
        Calculates the total score of the garden based on plant heights.
        """
        total_height = 0
        for plt in self.all_plants:
            total_height += plt.height
        score = total_height * 1.23
        return int(score)


class GardenManager:
    """
    Orchestrates multiple gardens and provides analytical tools.
    """
    def create_garden_network(cls) -> "GardenManager":
        """
        Class method to initialize the management system.
        """
        print("=== Garden Management System Demo ===\n")
        return cls()
    create_garden_network = classmethod(create_garden_network)

    def height_valid(height: int) -> bool:
        """
        Static utility method to validate if a height value is non-negative.
        """
        if height >= 0:
            return True
    height_valid = staticmethod(height_valid)

    class GardenStats:
        """
        Nested helper class to calculate plant type distributions.
        """
        def count_plants(plants_list: list) -> tuple:
            """
            Analyzes the list of plants to categorize them by type.
            """
            plt = 0
            prize = 0
            flower = 0
            for plant in plants_list:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flower += 1
                else:
                    plt += 1
            return (plt, prize, flower, len(plants_list))
        count_plants = staticmethod(count_plants)

    def grow_plants(garden: "Garden") -> tuple:
        """
        Simulates growth for all plants in a specific garden.
        """
        add = 1
        tot_add = 0
        print(f"\n{garden.name} is helping all plants grow...")
        for plt in garden.all_plants:
            plt.height += add
            tot_add += add
            print(f"{plt.name} grew {add} cm")
        return GardenManager.GardenStats.count_plants(garden.all_plants), \
            tot_add
    grow_plants = staticmethod(grow_plants)

    def show_garden(self, garden: "Garden") -> None:
        """
        Displays a detailed status report for a specific garden.
        """
        stats, tot_add = self.grow_plants(garden)
        plnt, prz, flw, tt = stats
        print(f"\n=== {garden.name}'s Garden Report ===")
        print("Plants in garden:")
        for plt in garden.all_plants:
            print(f"- {plt.name}: {plt.height}cm", end="")
            if isinstance(plt, FloweringPlant):
                print(f", {plt.color} flowers (blooming)", end="")
            if isinstance(plt, PrizeFlower):
                print(f", Prize Points: {plt.prize}", end="")
            print()
        print(f"\nPlants added: {tt}, Total growth: {tot_add}cm")
        print(f"Plant types: {plnt} regular, {flw} flowering, {prz} prize \
flowers\n")

    def display_garden_scores(cls) -> None:
        """
        Class method to display validated scores for all gardens.
        """
        result = []
        for garden in Garden.all_gardens:
            score = garden.garden_score()
            if cls.height_valid(score):
                print("Height validation test: True")
                result.append(f"{garden.name}: {score}")
            else:
                print("Height validation test: False")
        final_str = ", ".join(result)
        print(f"Garden scores - {final_str}")
        print(f"Total gardens managed: {Garden.total_garden}\n")
    display_garden_scores = classmethod(display_garden_scores)


def main() -> None:

    """
    Main execution block to demonstrate the Garden Management System.
    """
    manager = GardenManager.create_garden_network()
    alice = Garden("Alice")
    alice.add_plants(Plant("Oak tree", 100))
    alice.add_plants(FloweringPlant("Rose", 25, "red"))
    alice.add_plants(PrizeFlower("Sunflower", 50, "Yellow", 10))
    manager.show_garden(alice)

    bob = Garden("Bob")
    bob.add_plants(Plant("Lily", 10))
    bob.add_plants(FloweringPlant("Roses", 35, "red"))
    bob.add_plants(PrizeFlower("Sunflower", 78, "Yellow", 10))
    manager.show_garden(bob)

    GardenManager.display_garden_scores()


if __name__ == "__main__":
    main()
