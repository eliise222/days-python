from ex2.strategy import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2 import InvalidStrategyError
from ex0.factories import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i, (factory_a, strategy_a) in enumerate(opponents):
        for factory_b, strategy_b in opponents[i + 1:]:
            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()

            print("\n* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")

            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (heal, defensive)])

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame, aggressive), (heal, defensive)])

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(aqua, normal), (heal, defensive), (transform, aggressive)])


if __name__ == "__main__":
    main()
