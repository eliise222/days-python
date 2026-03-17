from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        if not isinstance(effect_type, str):
            raise TypeError("Effect type must be a string.")
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        dict_play = {"card_played": self.name,
                     "mana_used": self.cost,
                     "effect": "Deal 3 damage to target"
                     }
        return dict_play

    def resolve_effect(self, target: str) -> dict:
        effect_dict = {"name": self.name,
                       "target": target,
                       "effect": self.effect_type
                       }
        return effect_dict

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info["type"] = "spell"
        card_info["effect_type"] = self.effect_type
        return card_info
