#!/usr/bin/env python3

class Plant:
    """
    Base class representing a generic plant with an internal tracking system.
    """
    class _Stats:
        """
        Nested class to track and display execution statistics for each plant.
        """
        def __init__(self) -> None:
            self.grow_calls: int = 0
            self.age_calls: int = 0
            self.show_calls: int = 0

        def display(self) -> None:
            """
            Displays the basic collected statistics.
            """
            print(f"Stats: {self.grow_calls} grow, {self.age_calls} age, "
                  f"{self.show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        """
        Initializes a plant and its internal statistics system.
        """
        self.name: str = name
        self._height: float = float(height)
        self._age: int = age
        self._stats = self._Stats()

    @staticmethod
    def is_older_than_year(age_in_days: int) -> bool:
        """
        Checks if a given age in days is strictly older than a year.
        """
        return age_in_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        """
        Creates a default plant instance when information is missing.
        """
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        """
        Displays basic plant info and increments the show counter.
        """
        self._stats.show_calls += 1
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        """
        Increases height and increments the grow counter.
        """
        self._stats.grow_calls += 1
        self._height += 8.0

    def age(self) -> None:
        """
        Increases age and increments the age counter.
        """
        self._stats.age_calls += 1
        self._age += 20


class Flower(Plant):
    """
    Plant type that can bloom and has a specific color.
    """
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self._bloomed: bool = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self) -> None:
        """
        Triggers the blooming state of the flower.
        """
        self._bloomed = True


class Tree(Plant):
    """
    Plant type that tracks shade production statistics.
    """
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter
        self._shade_calls: int = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        """
        Simulates shade production and tracks calls.
        """
        self._shade_calls += 1
        print(f"Tree {self.name} now produces a shade of {self._height:.1f}cm "
              f"long and {self.trunk_diameter:.1f}cm wide.")


class Seed(Flower):
    """
    Specialized flower that tracks seed production after blooming.
    """
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42


def display_plant_stats(plant: Plant) -> None:
    """
    Global function to display statistics for any type of plant.
    """
    print(f"[statistics for {plant.name}]")
    plant._stats.display()
    if isinstance(plant, Tree):
        print(f"{plant._shade_calls} shade")


def main() -> None:
    """
    Demonstrates the garden analytics and advanced OOP patterns.
    """
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_plant_stats(anon)


if __name__ == "__main__":
    main()
