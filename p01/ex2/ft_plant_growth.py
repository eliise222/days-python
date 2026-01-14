class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def aff_plant(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow_plant(self):
        self.height2 = self.height + 6
        self.age2 = self.age + 6
        return f"{self.name}: {self.height2}cm, {self.age2} days old"

    def growth_plant(self):
        grow = self.height2 - self.height
        return f"Growth this week: +{grow}cm"


def main():
    plant1 = plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(plant1.aff_plant())
    print("=== Day 7 ===")
    print(plant1.grow_plant())
    print(plant1.growth_plant())


if __name__ == "__main__":
    main()
