class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def aff_plant(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main():
    plant1 = plant("Rose", 25, 30)
    plant2 = plant("Sunflower", 80, 45)
    plant3 = plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(plant1.aff_plant())
    print(plant2.aff_plant())
    print(plant3.aff_plant())


if __name__ == "__main__":
    main()
