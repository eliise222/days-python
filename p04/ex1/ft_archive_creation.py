def main() -> None:
    print("=== CYBER ARCHIVES = PRESERVATION SYSTEM ===\n")

    VERT = "\033[32m"
    RESET = "\033[0m"
    BLEU = "\033[34m"
    ROUGE = "\033[31m"

    entries: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
                         ]

    try:
        print("Initializing new storage unit: new_discovery.txt")
        f = open("new_discovery.txt", 'w')
        print(f"{VERT}Storage unit created successfully...\n{RESET}")

        print(f"{BLEU}Inscribing preservation data...{RESET}")
        for entry in entries:
            f.write(entry + "\n")
            print(f"{entry}")

        f.close()

        print(f"\n{VERT}Data inscription complete.{RESET} Storage unit {ROUGE}"
              f"sealed{RESET}")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")

    except OSError as e:
        print(f"ERROR : {e}")


if __name__ == "__main__":
    main()
