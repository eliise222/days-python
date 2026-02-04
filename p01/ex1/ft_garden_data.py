class Plant:
    """
    Class to store a plant's name, height, and age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes the plant attributes.
        """
        self.name = name
        self.height = height
        self.age = age

    def aff_plant(self) -> str:
        """
        Returns the plant information as a string.
        """
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    """
    Creates and displays three plants.
    """
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(plant1.aff_plant())
    print(plant2.aff_plant())
    print(plant3.aff_plant())


if __name__ == "__main__":
    main()
