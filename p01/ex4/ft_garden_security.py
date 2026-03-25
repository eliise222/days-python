#!/usr/bin/env python3

class Plant:
    """
    Represents a plant with protected attributes and data integrity validation.
    """
    def __init__(self, name: str, height: float, age: int) -> None:
        """
        Initializes the plant instance using setters for validation.
        """
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0

        print("=== Garden Security System ===")
        self.set_height(height)
        self.set_age(age)
        print("Plant created: ", end="")
        self.show()

    def get_height(self) -> float:
        """
        Returns the protected height value.
        """
        return self._height

    def set_height(self, value: float) -> None:
        """
        Validates and sets the plant height.
        """
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(value)

    def get_age(self) -> int:
        """
        Returns the protected age value.
        """
        return self._age

    def set_age(self, value: int) -> None:
        """
        Validates and sets the plant age.
        """
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = int(value)

    def show(self) -> None:
        """
        Displays the current state of the plant.
        """
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")


def main() -> None:
    """
    Demonstrates data integrity checks for the garden security system.
    """
    rose = Plant("Rose", 15.0, 10)

    print("\nHeight updated: 25cm")
    rose.set_height(25)
    print("Age updated: 30 days\n")
    rose.set_age(30)

    rose.set_height(-5)
    rose.set_age(-1)

    print("\nCurrent state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
