class SecurePlant:
    """
    Represents a plant with encapsulated attributes and specific
    validation logic.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes the plant instance with private height and age.
        """
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self) -> int:
        """
        Returns the private height attribute.
        """
        return self.__height

    def set_age(self) -> int:
        """
        Returns the private age attribute.
        """
        return self.__age

    def get_height(self, plant: "SecurePlant") -> bool:
        """
        Validates if the provided plant's height is strictly positive.
        """
        if plant.set_height() > 0:
            return True
        else:
            return False

    def get_age(self, plant: "SecurePlant") -> bool:
        """
        Validates if the provided plant's age is strictly positive.
        """
        if plant.set_age() > 0:
            return True
        else:
            return False

    def validplants(self, plant: "SecurePlant") -> int | None:
        """
        Performs a global security check and prints alerts for invalid data.
        """
        h_valid = plant.get_height(plant)
        a_valid = plant.get_age(plant)
        if (not h_valid and not a_valid):
            print(f"Invalid operation attemped: "
                  f"height {self.set_height()} [REJECTED]")
            print(f"Invalid operation attemped: "
                  f"age {self.set_age()} [REJECTED]")
            print("Security: Negative height and age rejected")
            return
        if (not h_valid):
            print(f"\nInvalid operation attemped: "
                  f"height {self.set_height()} [REJECTED]")
            print("Security: Negative height rejected")
            return
        if (not a_valid):
            print(f"\nInvalid operation attemped: "
                  f"age {self.set_age()} [REJECTED]")
            print("Security: Negative age rejected")
            return
        else:
            return 1


def main() -> None:
    """
    Demonstrates the plant security system and data integrity checks.
    """
    print("=== Garden security ===")
    plants = [SecurePlant("Rose", 25, 30)]
    for plt in plants:
        if plt.validplants(plt) == 1:
            print(f"Plant created: {plt.name}")
            print(f"Height updated: {plt.set_height()}cm [OK]")
            print(f"Age updated: {plt.set_age()} days [OK]")
            print(f"\nCurrent plant: {plt.name} ({plt.set_height()}cm, \
{plt.set_age()} days)")


if __name__ == "__main__":
    main()
