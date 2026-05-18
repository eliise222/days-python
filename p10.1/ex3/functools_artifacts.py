from collections.abc import Callable
from functools import singledispatch, lru_cache, partial, reduce
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    elif operation == 'add':
        return reduce(add, spells)
    elif operation == 'multiply':
        return reduce(mul, spells)
    elif operation == 'max':
        return reduce(lambda a, b: a if a > b else b, spells)
    elif operation == 'min':
        return reduce(lambda a, b: a if a < b else b, spells)
    else:
        raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_spell = partial(base_enchantment, power=50, element="Fire")
    water_spell = partial(base_enchantment, power=50, element="Water")
    earth_spell = partial(base_enchantment, power=50, element="Earth")

    return {
        "fire": fire_spell,
        "water": water_spell,
        "earth": earth_spell
           }


@lru_cache
def memoized_fibonacci(n: int) -> int:

    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def main() -> None:
    print("Testing spell reducer...")
    lst = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(lst, 'add')}")
    print(f"Product: {spell_reducer(lst, 'multiply')}")
    print(f"Max: {spell_reducer(lst, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element} hits {target} for {power}"

    spells = partial_enchanter(base_enchantment)
    print(spells["fire"](target="Dragon"))
    print(spells["water"](target="Dragon"))

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fire", "ice", "lightning"]))
    print(dispatcher(3.14))


if __name__ == "__main__":
    main()
