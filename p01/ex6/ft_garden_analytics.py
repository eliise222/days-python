class Plant():
    def __init__(self, name, height, type):
        self.name = name
        self.height = height
        self.type = type


class FloweringPlant(Plant):
    def __init__(self, name, height, type, color, bloom):
        super().__init__(name, height, type)
        self.color = color
        self.bloom = bloom


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, type, color, bloom, rarity, prize):
        super().__init__(name, height, type, color, bloom)
        self.rarity = rarity
        self.prize = prize


class Garden:
    def __init__(self, name):
        self.name = name
        self.all_plants = []
    # @staticmethod
    # class GardenStats(garden):
    #    def add_garden():
    
# yo = GardenManager()
# GardenManager.create_garden_network(garden)


def main():

    rose = Plant("rose", 12, "tree")
    print(rose.name)
    print(rose.height)
    print(rose.type)
    rose.height += 3
    print(rose.height)
    abc = PrizeFlower("bob", 25, "abc", "red", "bloom", 36, 24)
    print(f"cette plante s'appelle {abc.name}")

if __name__ == "__main__":
    main()
