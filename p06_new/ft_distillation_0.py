from alchemy import potions


def main() -> None:
    print("=== Distillation 0 ===")
    print(f"Testing strength_potion: {potions.strength_potion()}")
    print(f"Testing healing_potion: {potions.healing_potion()}\n")


if __name__ == "__main__":
    main()
