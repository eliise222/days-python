import random


def gen_player_achievements() -> set[str]:
    pool: list[str] = [
        'Crafting Genius', 'World Savior', 'Master Explorer',
        'Collector Supreme', 'Untouchable', 'Boss Slayer',
        'Strategist', 'Unstoppable', 'Speed Runner',
        'Survivor', 'Treasure Hunter', 'First Steps',
        'Sharp Mind', 'Hidden Path Finder'
    ]
    count: int = random.randint(5, 11)
    return set(random.sample(pool, count))


def main() -> None:
    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }

    print("=== Achievement Tracker System ===\n")
    for name, ach in players.items():
        print(f"Player {name}: {ach}")

    all_distinct: set[str] = set().union(*players.values())
    print(f"\nAll distinct achievements: {all_distinct}")

    common: set[str] = set(all_distinct).intersection(*players.values())
    print(f"\nCommon achievements: {common}\n")

    for name, ach in players.items():
        others: set[str] = set().union(
            *(p_ach for p_name, p_ach in players.items() if p_name != name)
        )
        print(f"Only {name} has: {ach.difference(others)}")
    print("")
    for name, ach in players.items():
        print(f"{name} is missing: {all_distinct.difference(ach)}")


if __name__ == "__main__":
    main()
