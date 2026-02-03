class Plant:
    """
    Base class representing a generic plant with common features
    like name, height, and age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize the basic attributes of a plant.
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Specialized plant type that has a color and the ability to bloom.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a flower by calling the parent setup and adding color.
        """
        super().__init__(name, height, age)
        self.color = color

    def is_flower(self) -> bool:
        """
        Identify if the plant belongs to the Flower category.
        """
        return True

    def is_vegetable(self) -> bool:
        """
        Identify if the plant belongs to the Vegetable category.
        """
        return False

    def is_tree(self) -> bool:
        """
        Identify if the plant belongs to the Tree category.
        """
        return False

    def bloom(self, flower: "Flower") -> str:
        """
        Simulate the blooming behavior based on the plant's age.
        """
        if flower.age > 8:
            return "blooming beautifully"
        else:
            return "not blooming"


class Tree(Plant):
    """
    Specialized plant type that tracks trunk diameter and produces shade.
    """
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """
        Initialize a tree with specialized trunk measurements.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def is_tree(self) -> bool:
        """
        Identify if the plant belongs to the Tree category.
        """
        return True

    def is_flower(self) -> bool:
        """
        Identify if the plant belongs to the Flower category.
        """
        return False

    def is_vegetable(self) -> bool:
        """
        Identify if the plant belongs to the Vegetable category.
        """
        return False

    def produce_shade(self, tree: "Tree") -> int:
        """
        Calculate the shade coverage based on the tree's trunk diameter.
        """
        shade = tree.trunk_diameter * 1.56
        return int(shade)


class Vegetable(Plant):
    """
    Specialized plant type grown for nutritional value and
    specific harvest seasons.
    """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        Initialize a vegetable with its harvest and
        nutritional characteristics.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def is_vegetable(self) -> bool:
        """
        Identify if the plant belongs to the Vegetable category.
        """
        return True

    def is_flower(self) -> bool:
        """
        Identify if the plant belongs to the Flower category.
        """
        return False

    def is_tree(self) -> bool:
        """
        Identify if the plant belongs to the Tree category.
        """
        return False


def main() -> None:
    """
    Entry point for demonstrating the specialized
    characteristics of different plant types.
    """
    print("=== Garden Plant Types ===\n")
    plants = [Flower("Rose", 25, 30, "red"),
              Flower("Sunflower", 80, 45, "yellow"),
              Tree("Oak", 500, 1825, 50), Tree("Maple", 120, 730, 20),
              Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C"),
              Vegetable("Carrot", 25, 90, "spring harvest", "vitamin B")]
    for plt in plants:
        if plt.is_flower():
            print(f"{plt.name} (Flower): {plt.height}cm, {plt.age} days,\
{plt.color} color")
            print(f"{plt.name} is {plt.bloom(plt)}!\n")
        elif plt.is_tree():
            print(f"{plt.name} (Tree): {plt.height}cm, {plt.age} days,\
{plt.trunk_diameter}cm diameter")
            print(f"{plt.name} provides {plt.produce_shade(plt)} square \
meters of shade\n")
        elif plt.is_vegetable():
            print(f"{plt.name} (Vegetable): {plt.height}cm, {plt.age}\
 days, {plt.harvest_season}")
            print(f"{plt.name} is rich in {plt.nutritional_value}\n")


if __name__ == "__main__":
    main()
