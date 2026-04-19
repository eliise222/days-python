from ex1.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_heal(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")

    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform(factory: CreatureFactory) -> None:
    print("\nTesting Creature with transform capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    test_heal(HealingCreatureFactory())
    test_transform(TransformCreatureFactory())


if __name__ == "__main__":
    main()
