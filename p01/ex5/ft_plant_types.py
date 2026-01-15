class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color, bloom):
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom

    def is_flower(self):
        return True

    def is_vege(self):
        return False

    def is_tree(self):
        return False


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter, produce_shade):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.produce_shade = produce_shade

    def is_tree(self):
        return True

    def is_flower(self):
        return False

    def is_vegetable(self):
        return False


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def is_vegetable(self):
        return True

    def is_flower(self):
        return False

    def is_tree(self):
        return False


def main():
    print("=== Garden Plant Types ===\n")
    plants = [Flower("Rose", 25, 30, "red", "blooming beautifully"),
              Flower("Sunflower", 80, 45, "yellow", "blooming"),
              Tree("Oak", 500, 1825, 50, 78), Tree("Maple", 120, 730, 20, 2),
              Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C"),
              Vegetable("Carrot", 25, 90, "spring harvest", "vitamin B")]
    for plt in plants:
        if plt.is_flower():
            print(f"{plt.name} (Flower): {plt.height}cm, {plt.age} days,\
{plt.color} color")
            print(f"{plt.name} is {plt.bloom}!\n")
        elif plt.is_tree():
            print(f"{plt.name} (Tree): {plt.height}cm, {plt.age} days,\
{plt.trunk_diameter}cm diameter")
            print(f"{plt.name} provides {plt.produce_shade} square \
meters of shade\n")
        elif plt.is_vegetable():
            print(f"{plt.name} (Vegetable): {plt.height}cm, {plt.age}\
 days, {plt.harvest_season}")
            print(f"{plt.name} is rich in {plt.nutritional_value}\n")


if __name__ == "__main__":
    main()
