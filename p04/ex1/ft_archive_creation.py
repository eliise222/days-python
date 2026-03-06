def main():
    print("=== CYBER ARCHIVES = PRESERVATION SYSTEM ===\n")

    VERT = "\033[32m"
    RESET = "\033[0m"
    BLEU = "\033[34m"
    ROUGE = "\033[31m"

    try:
        print("Initializing new storage unit: new_discovery.txt")
        f = open("new_discovery.txt", 'w')
        print(f"{VERT}Storage unit created successfully...\n{RESET}")

        print(f"{BLEU}Inscribing preservation data...{RESET}")
        f.write("[ENTRY 001] New quantum algorithm discovered")
        f.write("\n[ENTRY 002] Efficiency increased by 347%")
        f.write("\n[ENTRY 003] Archived by Data Archivist trainee")

        f.close()

        f = open("new_discovery.txt", 'r')
        contenu = f.read()
        print(contenu)

        print(f"\n{VERT}Data inscription complete.{RESET} Storage unit {ROUGE}\
sealed{RESET}")
        f.close()
        print("Archive 'new_discovery.txt' ready for long-term preservation.")

    except OSError as e:
        f.close()
        print(f"ERROR : {e}")


if __name__ == "__main__":
    main()
