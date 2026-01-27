class Plant():
    def __init__(self, name, height, type):
        self.name = name
        self.height = height
        self.type = type

class FloweringPlant(Plant):
    def __init__(self, name, height, type, color, bloom)
        super().__init__(name, height, type)
        self.color = color
        self.bloom = bloom

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, type, color, bloom, rarity, prize):
        super().__init__(name, height, type, color, bloom)
        self.rarity = rarity
        self.prize = prize

class GardenManager:
    def __init__(self):
        self.garden = {}
    @staticmethod
    def GardenStats(garden):
       def add_garden():
           
yo = GardenManager()
GardenManager.create_garden_network(garden)


