class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def main():
    print("=== Plant Factory Output ===")
    plants = [("Rose", 25, 30), ("Oak", 200, 365), ("Cactus", 5, 90),
              ("Sunflower", 80, 45), ("Fern", 15, 120)]
    nb_plants = 0
    for plt in plants:
        print(f"Created: {plt[0]} ({plt[1]}cm, {plt[2]} days)")
        nb_plants += 1
    print("\nTotal plants created: ", nb_plants)


if __name__ == "__main__":
    main()
