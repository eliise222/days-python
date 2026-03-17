import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    def __init__(self):
        self.deck = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        first_count = len(self.deck)
        self.deck = [c for c in self.deck if c.name != card_name]
        return len(self.deck) < first_count

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        if len(self.deck) > 0:
            new_card = self.deck.pop()
            return new_card
        return None

    def get_deck_stats(self) -> dict:
        total_count = len(self.deck)
        deck_fin = {
                    "total_cards": len(self.deck),
                    "creatures": 0,
                    "spells": 0,
                    "artifacts": 0,
                    "avg_cost": 0.0
                    }

        if deck_fin["total_cards"] == 0:
            return deck_fin
        total_cost = 0
        for card in self.deck:
            total_cost += card.cost
            if isinstance(card, CreatureCard):
                deck_fin["creatures"] += 1
            elif isinstance(card, SpellCard):
                deck_fin["spells"] += 1
            elif isinstance(card, ArtifactCard):
                deck_fin["artifacts"] += 1
        avg = total_cost / total_count
        deck_fin["avg_cost"] = round(avg, 1)
        return deck_fin
