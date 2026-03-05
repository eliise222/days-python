def dashboard():

    print("=== Game Analytics Dashboard ===\n")

    players = [
            {"name": "alice", "score": 2300,
             "status": "active",
             "region": "north",
             "achievement": ["first_kill", "level_10", "boss_slayer",
                             "speed_demon", "treasure_hunter"]},
            {"name": "bob", "score": 1800,
             "status": "active",
             "region": "east",
                "achievement": ["first_kill", "level_10", "treasure_hunter"]},
            {"name": "charlie", "score": 2150,
             "status": "active",
             "region": "central",
                "achievement": ["first_kill", "level_10", "boss_slayer",
                                "alchemist", "speed_demon", "treasure_hunter",
                                "collector"]},
            {"name": "diana", "score": 2050,
             "status": "inactive",
             "region": "south",
             "achievement": ["level_10"]}
        ]

    print("=== List Comprehension Exemples ===")

    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    active_players = [p["name"] for p in players if p["status"] == "active"]
    scores_double = [p["score"] * 2 for p in players]

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_double}")
    print(f"Active players: {active_players}\n")

    print("=== Dict Comprehension Examples ===")

    plyr_scr = {p["name"]: p["score"] for p in players
                if p["status"] == "active"}

    print(f"Players score: {plyr_scr}")

    categories = {
                    "high": len([p for p in players if p["score"] > 2000]),
                    "medium": len([p for p in players if p["score"] <= 2000]),
                    "low": len([p for p in players if p["score"] <= 1800])
                }

    print(f"Score categories: {categories}")
    count_achivement = {p["name"]: len(p["achievement"])
                        for p in players if p["status"] == "active"}
    print(f"Achievement counts: {count_achivement}\n")

    print("=== Set Comprehension Examples ===")

    unique_players = {p["name"] for p in players}
    unique_achievement = {achiv for p in players for achiv in p["achievement"]}
    active_regions = {p["region"] for p in players if p["status"] == "active"}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievement}")
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players = len(players)
    tt_unique_ach = len(unique_achievement)
    average_score = sum([p["score"] for p in players]) / total_players
    top_perf = max([p["score"] for p in players])
    top_name = [p["name"] for p in players if p["score"] == top_perf][0]
    top_ach = [len(p["achievement"]) for p in players
               if p["name"] == top_name][0]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements : {tt_unique_ach}")
    print(f"Average score: {average_score}")
    print(f"Top Performer: {top_name} ({top_perf} points,\
{top_ach} achievements)")


def main():
    dashboard()


if __name__ == "__main__":
    main()
