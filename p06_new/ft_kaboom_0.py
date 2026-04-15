import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing record light spell: \
{alchemy.grimoire.light_spell_record('Fantasy', 'Earth, wind and fire')}\n")


if __name__ == "__main__":
    main()
