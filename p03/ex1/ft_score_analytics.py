import sys


def main() -> None:
    if len(sys.argv) == 1:
        print("Player Score Analytics")
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2>")
        return

    print("=== Player Score Analytics ===")

    scores: list[int] = []

    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2>")
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")

    total_score: int = sum(scores)
    print(f"Total score: {total_score}")

    avg_score: float = total_score / len(scores)
    print(f"Average score: {avg_score}")

    high_score: int = max(scores)
    print(f"High score: {high_score}")

    low_score: int = min(scores)
    print(f"Low score: {low_score}")

    print(f"Score range: {high_score - low_score}\n")


if __name__ == "__main__":
    main()
