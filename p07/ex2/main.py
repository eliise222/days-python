from ex2.EliteCard import EliteCard


def main():
    print("\n=== DataDeck Ability System ===\n")

    arcane = EliteCard('Arcane Warrior', 5, "Legendary", 5, 3, 8)

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    arcane.play({})

    print("Combat phase:")
    print(f"Attack result: {arcane.attack('Enemy')}")
    print(f"Defense result: {arcane.defend(5)}")

    print("\nMagic phase:")
    print(f"Spell cast: {arcane.cast_spell('Fireball',
                                           ['Enemy 1', 'Enemy 2'])}")
    print(f"Mana channel: {arcane.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
