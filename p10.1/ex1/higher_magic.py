from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combined(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)

    return combined


def power_amplifier(spell1: Callable, power1: int) -> Callable:

    def amplified(target: str, power: int) -> str:
        return spell1(target, power1 * power)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:

    def sequence(target: str, power: int) -> list[str]:
        lst: list[str] = []
        for spell in spells:
            lst.append(spell(target, power))
        return lst
    return sequence


def main() -> None:
    print("Testing spell combiner...")
    combo = spell_combiner(fireball, heal)
    result = combo("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    amplif = power_amplifier(fireball, 3)
    result2 = amplif("Dragon", 10)
    print(f"Power amplifier result : {result2}")

    print("\nTesting Conditional Caster...")

    def cond(target: str, power: int) -> bool:
        return power > 5

    fireb = conditional_caster(cond, fireball)
    print("Conditional Caster result:")
    print(fireb("Dragon", 10))
    print(fireb("Dragon", 2))

    print("\nTesting Spell Sequence...")
    sequence = spell_sequence([fireball, heal])
    result4 = sequence("Dragon", 10)
    for r in result4:
        print(r)


if __name__ == "__main__":
    main()
