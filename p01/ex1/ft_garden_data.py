class Plant:
    """
    Class to store a plant's name, height, and age.
    """
    def __init__(self) -> None:
        """
        Initializes the plant attributes.
        """
        self.name: str = ""
        self.height: int = 0
        self.age: int = 0

    def show(self) -> None:
        """
        Displays the plant information.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """
    Creates and displays three plants.
    """
    plant1 = Plant()
    plant1.name = "Rose"
    plant1.height = 25
    plant1.age = 30

    plant2 = Plant()
    plant2.name = "Sunflower"
    plant2.height = 80
    plant2.age = 45

    plant3 = Plant()
    plant3.name = "Cactus"
    plant3.height = 15
    plant3.age = 120

    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    main()
