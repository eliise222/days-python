from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str) -> None:
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("Durability must be a positive integer!")

        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        dict_play = {"card_played": self.name,
                     "mana_used": self.cost,
                     "effect": "Permanent: +1 mana per turn"
                     }
        return dict_play

    def activate_ability(self):
        ability_dict = {"artifact": self.name,
                        "ability_status": "Activated",
                        "effect_triggered": self.effect
                        }
        return ability_dict

    def get_card_info(self):
        info = super().get_card_info()

        info["type"] = "Artifact"
        info["durability"] = self.durability
        info["effect"] = self.effect
        return info
