#!/usr/bin/env python3

class Plant:
    """
    Represents a plant with attributes that change over time.
    Provides methods to display status and simulate growth behaviors.
    """
    def __init__(self) -> None:
        """
        Initializes a plant with its starting name, height, and age.
        """
        self.name: str = ""
        self.height: float = 0.0
        self._age: int = 0

    def show(self) -> None:
        """
        Formats and returns the current status information of the plant.
        """
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        """
        Simulates growth.
        """
        self.height += 0.8

    def age(self) -> None:
        """
        increases the plant's age.
        """
        self._age += 1


def main() -> None:
    """
    Main entry point to simulate a week of growth for a specific plant.
    """
    plant1 = Plant()
    plant1.name = "Rose"
    plant1.height = 25
    plant1._age = 30

    initial_height = plant1.height
    print("=== Garden Plant Growth ===")

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant1.show()
        plant1.grow()
        plant1.age()

    total_growth = plant1.height - initial_height
    print(f"Growth this week: {round(total_growth)}cm")


if __name__ == "__main__":
    main()
