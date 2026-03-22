from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self):
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets):
        targets = sorted(available_targets, key=lambda x: x ==
                         "Enemy Player", reverse=True)
        return targets

    def execute_turn(self, hand, battlefield):
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        available_mana = 10
        card_play = []
        total_mana_use = 0
        total_damage = 0

        for c in sorted_hand:
            remaining_mana = available_mana - total_mana_use
            if c.cost <= remaining_mana:
                card_play.append(c.name)
                total_mana_use += c.cost
                total_damage += c.attack_nb
            else:
                pass

        for d in battlefield:
            total_damage += d.attack_nb

        targets = self.prioritize_targets(["Enemy Player", "Enemy Creature"])

        dict_execut = {'strategy': self.get_strategy_name(),
                       'actions': {
                           'cards_played': card_play,
                           'mana_used': total_mana_use,
                           'targets_attacked': [targets[0]],
                           'damage_dealt': total_damage
                                  }
                       }

        return dict_execut
