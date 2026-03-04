def all_print():

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}

    all_achievement = alice | bob | charlie
    len_achievement = len(all_achievement)
    common = alice & bob & charlie
    alice_unique = alice - bob
    common_alice_and_bob = alice & bob
    bob_unique = bob - alice

    rare_alice = alice - (bob | charlie)
    rare_bob = bob - (alice | charlie)
    rare_charlie = charlie - (bob | alice)
    rare = rare_alice | rare_bob | rare_charlie

    print("=== Achievement Tracker System ===\n")

    print(f"Player Alice achievement :{alice}")
    print(f"Player Bob achievement :{bob}")
    print(f"Player Charlie achievement :{charlie}\n")

    print("=== Achievement Analytics ===")

    print(f"All unique achievements : {all_achievement}")
    print(f"Total unique achievement: {len_achievement}\n")

    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {common_alice_and_bob}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


def main():
    all_print()


if __name__ == "__main__":
    main()
