class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self):
        return self.__height

    def set_age(self):
        return self.__age

    def validplants(self):
        # if (self.set_height() < 0 and self.set_age() < 0):
        #     print(f"Invalid operation attemped: height {self.set_height()} [REJECTED]")
        #     print(f"Invalid operation attemped: age {self.set_age()} [REJECTED]")
        #     print("Security: Negative height and age rejected")
        #     return
        if (self.set_height() < 0):
            print(f"Invalid operation attemped: height {self.set_height()} [REJECTED]")
            print("Security: Negative height rejected")
            return
        elif (self.set_age() < 0):
            print(f"Invalid operation attemped: age {self.set_age()} [REJECTED]")
            print("Security: Negative age rejected")
            return
        else:
            return 1


def main():
    print("=== Garden security ===")
    plants = [plant("Rose", -25, 30)]
    for plt in plants:
        plt.validplants()
        if plt.validplants() == 1:
            print(f"Plant created: {plt.name}")
            print(f"Height updated: {plt.set_height()}cm [OK]")
            print(f"Age updated: {plt.set_age()} days [OK]")
    print(f"Current plant: {plt.name} ({plt.set_height()}cm, {plt.set_age()} days)")


if __name__ == "__main__":
    main()
