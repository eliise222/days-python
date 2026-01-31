class Plant():
    def __init__(self, name, height):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize):
        super().__init__(name, height, color)
        self.prize = prize


class GardenManager:
    total_garden = 0
    all_gardens = []
    def __init__(self, name):
        self.name = name
        self.all_plants = []
        GardenManager.total_garden += 1
        GardenManager.all_gardens.append(self)
    def add_plants(self, plant):
        self.all_plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")
    @classmethod
    def create_garden_network(cls):
        print(f"=== Garden Management System Demo ===\n")
    @staticmethod
    def height_valid(height):
        if height >= 0:
            return True
    def garden_score(self):
        total_height = 0
        for plt in self.all_plants:
            total_height += plt.height
        score = total_height * 1.23
        return int(score)

    class GardenStats:
       @staticmethod
       def count_plants(all_plants):
            plt = 0
            prize = 0
            flower = 0
            for plant in all_plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flower += 1
                else:
                    plt += 1
            return (plt, prize, flower, len(all_plants))
    def show_garden(self):
        add = 1
        tot_add = 0
        print(f"\n{self.name} is helping all plants grow...")
        for plt in self.all_plants:
            plt.height += add
            tot_add += add
            print(f"{plt.name} grew {add} cm")
        plnt, prz, flw, tt = self.GardenStats.count_plants(self.all_plants)
        print(f"\n=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plt in self.all_plants:
            print(f"- {plt.name}: {plt.height}cm", end="")
            if isinstance(plt, FloweringPlant):
                print(f", {plt.color} flowers (blooming)", end="")
            if isinstance(plt, PrizeFlower):
                print(f", Prize Points: {plt.prize}", end="")
            print()
        print(f"\nPlants added: {tt}, Total growth: {tot_add}cm")
        print(f"Plant types: {plnt} regular, {flw} flowering, {prz} prize flowers")
    @classmethod
    def display_garden_scores(cls):
        for garden in cls.all_gardens:
            score = garden.garden_score()
            if cls.height_valid(score):
                print(f"\nHeight validation test: True")
                print(f"Garden scores - {garden.name}: {score}")
            else:
                print(f"Height validation test: False")
        print(f"Total gardens managed: {cls.total_garden}\n")

def main():

    GardenManager.create_garden_network()
    alice = GardenManager("Alice")
    alice.add_plants(Plant("Oak tree", 100))
    alice.add_plants(FloweringPlant("Rose", 25, "red"))
    alice.add_plants(PrizeFlower("Sunflower", 50, "Yellow", 10))
    alice.show_garden()
    alice.display_garden_scores()

    bob= GardenManager("Bob")
    bob.add_plants(Plant("Lily", 10))
    bob.add_plants(FloweringPlant("Roses", 35, "red"))
    bob.add_plants(PrizeFlower("Sunflower", 78, "Yellow", 10))
    bob.show_garden()
    bob.display_garden_scores()

if __name__ == "__main__":
    main()
