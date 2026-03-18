from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Magical, Combatable):
    def __init__(self, name: str, cost: int, rarity: str, attack_nb: int,
                 defense_nb: int, mana_nb: int):
        super().__init__(name, cost, rarity)
        self.attack_nb = attack_nb
        self.defense_nb = defense_nb
        self.mana_nb = mana_nb
        self.life = 10

    def attack(self, target) -> dict:
        attack_dict = {'attacker': self.name,
                       'target': target,
                       'damage': self.attack_nb,
                       'combat_type': 'melee'
                       }
        return attack_dict

    def defend(self, incoming_damage: int) -> dict:
        damage = max(0, incoming_damage - self.defense_nb)
        alive = self.life > damage
        dict_def = {'defender': self.name,
                    'damage_taken': damage,
                    'damage_blocked': self.defense_nb,
                    'still_alive': alive
                    }
        return dict_def

    def get_combat_stats(self) -> dict:
        dict_combat_stats = {'attack': self.attack_nb,
                             'defense': self.defense_nb,
                             'life': self.life
                             }
        return dict_combat_stats

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = 4
        self.mana_nb -= mana_cost
        dict_cast = {'caster': self.name,
                     'spell': spell_name,
                     'targets': targets,
                     'mana_used': mana_cost}
        return dict_cast

    def channel_mana(self, amount: int) -> dict:
        self.mana_nb += amount
        dict_channel = {'channeled': amount,
                        'total_mana': self.mana_nb}
        return dict_channel

    def get_magic_stats(self) -> dict:
        return {'mana': self.mana_nb}

    def play(self, game_state: dict) -> dict:
        print(f"Playing {self.name} (Elite Card):\n")
        dict_play = {'card': self.name,
                     'type': 'Elite',
                     'status': 'Ready for combat and magic'}
        return dict_play
