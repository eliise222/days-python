def main():

    VERT = "\033[32m"
    RESET = "\033[0m"
    ROUGE = "\033[31m"

    print("=== CYBER ARCHIVES = DATA RECOVERY SYSTEM ===\n")

    print("Accessing Storage Vault: ancient_fragment.txt")

    f = open("ancient_fragment.txt", 'r')
    print(f"{VERT}Connection established...\n{RESET}")

    contenu = f.read()

    print("RECOVERED DATA:")
    print(contenu)

    print(f"\n{VERT}Data recovery complete.{RESET} \
Storage unit {ROUGE}disconnected.{RESET}")
    f.close()


if __name__ == "__main__":
    main()
