#!/usr/bin/env python3

class Plant:
    """
    Represents a plant blueprint used for mass production in the factory.
    """
    def __init__(self, name: str, height: float, age: int) -> None:
        """
        Initialize a new plant instance with its starting characteristics.
        """
        self.name: str = name
        self.height: float = float(height)
        self._age: int = age

    def show(self) -> None:
        """
        Displays the current status of the plant in a formatted string.
        """
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        """
        Increases the height of the plant to simulate growth.
        """
        self.height += 0.8

    def age(self) -> None:
        """
        Increases the chronological age of the plant.
        """
        self._age += 1


def main() -> None:
    """
    Entry point to simulate the plant factory output by creating
    multiple plants.
    """
    plant_data = [
        ("Rose", 25.0, 30),
        ("Oak", 200.0, 365),
        ("Cactus", 5.0, 90),
        ("Sunflower", 80.0, 45),
        ("Fern", 15.0, 120)
    ]

    print("=== Plant Factory Output ===")

    for name, height, age in plant_data:
        new_plant = Plant(name, height, age)
        print("Created: ", end="")
        new_plant.show()


if __name__ == "__main__":
    main()
