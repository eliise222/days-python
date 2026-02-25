import sys


def main():
    print("=== Player Score Analytics ===")
    total = len(sys.argv)
    score = []
    if total == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return
    nb = 1
    while nb < total:
        try:
            sys.argv[nb]
            score = score + [int(sys.argv[nb])]
        except ValueError:
            pass
        nb += 1

    total_players = len(score)
    if len(score) > 0:
        print("Scores processed:", score)
        print("Total players:", total_players)
        total_score = sum(score)
        print("Total score:", total_score)
        moy_score = total_score / total_players
        print("Average score:", moy_score)
        high_score = max(score)
        print("High score:", high_score)
        min_score = min(score)
        print("Low score:", min_score)
        score_range = high_score - min_score
        print("Score range:", score_range)
    else:
        return


if __name__ == "__main__":
    main()
