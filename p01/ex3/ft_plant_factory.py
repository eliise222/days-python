class Plant:
    """
    Represents a plant blueprint used for mass production in the factory.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new plant instance with its starting characteristics.
        """
        self.name = name
        self.height = height
        self.age = age


def main() -> None:
    """
    Entry point to simulate the plant factory output by iterating
    through plant data.
    """
    print("=== Plant Factory Output ===")
    plants = [("Rose", 25, 30),
              ("Oak", 200, 365),
              ("Cactus", 5, 90),
              ("Sunflower", 80, 45),
              ("Fern", 15, 120)
              ]
    created_plants = []

    for name, height, age in plants:
        new_plant = Plant(name, height, age)
        created_plants.append(new_plant)

        print(f"Created: {new_plant.name} ({new_plant.height}cm, "
              f"{new_plant.age} days)")

    print(f"\nTotal plants created: {len(created_plants)}")


if __name__ == "__main__":
    main()
