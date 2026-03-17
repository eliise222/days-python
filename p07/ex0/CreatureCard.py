from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer!")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer!")

        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        dict_play = {"card_played": self.name,
                     "mana_used": self.cost,
                     "effect": "Creature summoned to battlefield"
                     }
        return dict_play

    def attack_target(self, target) -> dict:
        dict_attack = {"attacker": self.name,
                       "target": target,
                       "damage_dealt": self.attack,
                       "combat_resolved": True
                       }
        return dict_attack

    def get_card_info(self) -> dict:
        creature_dict = super().get_card_info()
        creature_dict["type"] = "Creature"
        creature_dict["attack"] = self.attack
        creature_dict["health"] = self.health
        return creature_dict
