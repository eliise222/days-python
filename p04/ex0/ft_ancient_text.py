def main() -> None:

    VERT = "\033[32m"
    RESET = "\033[0m"
    ROUGE = "\033[31m"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        f = open("ancient_fragment.txt", 'r')
        print(f"{VERT}Connection established...\n{RESET}")

        contenu: str = f.read()

        print("RECOVERED DATA:")
        print(contenu)
        f.close()
        print(f"\n{VERT}Data recovery complete.{RESET} "
              f"Storage unit {ROUGE}disconnected.{RESET}")

    except FileNotFoundError:
        print(f"{ROUGE}ERROR: Storage vault not found. "
              f"Run data generator first.{RESET}")


if __name__ == "__main__":
    main()
