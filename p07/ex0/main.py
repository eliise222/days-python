from ex0.CreatureCard import CreatureCard


def main():
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("\n=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    print(f"{dragon.get_card_info()}\n")

    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    if dragon.is_playable(6) is True:
        print(f"Play result: {dragon.play({})}\n")

    print("Fire Dragon attacks Goblin Warrior:")
    print(f'Attack result: {dragon.attack_target("Goblin Warrior")}\n')

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}\n")
    if dragon.is_playable(3) is True:
        print(f"Play result: {dragon.play({})}\n")

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
