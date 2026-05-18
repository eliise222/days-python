from collections.abc import Callable


def mage_counter() -> Callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total: int = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def factory(item_type: str) -> str:
        return f"{enchantment_type} {item_type}"
    return factory


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object:
        if key in memory:
            return memory[key]
        else:
            return "Memory not found"

    return {'store': store, 'recall': recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_a call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    echt_flame = enchantment_factory("Flaming")
    echt_frozen = enchantment_factory("Frozen")
    print(echt_flame("Sword"))
    print(echt_frozen("Shield"))

    print("\nTesting memory vault...")
    memory = memory_vault()
    memory['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {memory['recall']('secret')}")
    print(f"Recall 'unknown': {memory['recall']('unknown')}")


if __name__ == "__main__":
    main()
