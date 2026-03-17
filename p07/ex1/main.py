from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    dragon = CreatureCard("Fire Dragon", 5, "Epic", 5, 5)
    bolt = SpellCard("Lightning Bolt", 3, "Common", "Damage")
    crystal = ArtifactCard("Mana Crystal", 2, "Rare", 3,
                           "Permanent: +1 mana per turn")

    deck = Deck()
    deck.add_card(dragon)
    deck.add_card(bolt)
    deck.add_card(crystal)

    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}\n")

    print("Drawing and playing cards:\n")

    for _ in range(3):
        card = deck.draw_card()
        if card:
            info = card.get_card_info()
            print(f"Drew: {card.name} ({info['type']})")

            result = card.play({})

            print(f"Play result: {result}\n")

    print("Polymorphism in action: Same interface, different \
card behaviors!")


if __name__ == "__main__":
    main()
