import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john',
        'kevin', 'Liam'
                         ]
    print(f"Initial list of players: {players}")

    capitalized_all: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized_all}")

    already_capitalized: list[str] = [name for name in players
                                      if name[0].isupper()]
    print(f"New list of capitalized names only: {already_capitalized}\n")

    scores: dict[str, int] = {name: random.randint(50, 950)
                              for name in capitalized_all}
    print(f"Score dict: {scores}")

    avg: float = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)}")

    high_scores: dict[str, int] = {k: v for k, v in scores.items() if v > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
