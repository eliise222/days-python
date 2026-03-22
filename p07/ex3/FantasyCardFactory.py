from ex3.CardFactory import CardFactory
from ex2.EliteCard import EliteCard


class FantasyCardFactory(CardFactory):
    def get_supported_types(self):
        dict_support = {'creatures': ['dragon', 'goblin'],
                        'spells': ['fireball'],
                        'artifacts': ['mana_ring']
                        }
        return dict_support

    def create_creature(self, name_or_power):
        name_or_power = None
        if isinstance(name_or_power, str):
            name = name_or_power
            attack = 5
        elif isinstance(name_or_power, int):
            attack = name_or_power
            name = "Dragon" if attack >= 5 else "Goblin"
        else:
            name = "Generic Creature"
            attack = 1

        return EliteCard(name=name, cost=attack, rarity='Common',
                         attack_nb=attack, defense_nb=attack)

    def create_spell(self, name_or_power):
        name_or_power = None