class Plant:
    """
    Represents a plant with attributes that change over time.
    Provides methods to display status and simulate growth behaviors.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a plant with its starting name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age

    def aff_plant(self) -> str:
        """
        Formats and returns the current status information of the plant.
        """
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow_plant(self) -> str:
        """
        Simulates growth by increasing height and age,
        returning the updated status.
        """
        self.height2 = self.height + 6
        self.age2 = self.age + 6
        return f"{self.name}: {self.height2}cm, {self.age2} days old"

    def growth_plant(self) -> str:
        """
        Calculates and returns the total growth achieved during the simulation.
        """
        grow = self.height2 - self.height
        return f"Growth this week: +{grow}cm"


def main() -> None:
    """
    Main entry point to simulate a week of growth for a specific plant.
    """
    plant1 = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(plant1.aff_plant())
    print("=== Day 7 ===")
    print(plant1.grow_plant())
    print(plant1.growth_plant())


if __name__ == "__main__":
    main()
