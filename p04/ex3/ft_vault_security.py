def main() -> None:
    RESET = "\033[0m"
    ORANGE = "\033[33m"
    VERT = "\033[32m"
    ROUGE = "\033[31m"
    BLEU = "\033[34m"

    print("=== CYBER ARCHIVES = VAULT SECURITY SYSTEM ===\n")

    print(f"{ORANGE}Initiating secure vault access...{RESET}")
    print("Vault connection established with failsafe protocols\n")

    print(f"{BLEU}SECURE EXTRACTION:{RESET}")
    try:
        with open("classified_data.txt", 'r') as f:
            contenu = f.read()
            print(contenu)

    except FileNotFoundError:
        with open("classified_data.txt", 'w') as f:

            f.write("[CLASSIFIED] Quantum encryption keys recovered")
            f.write("\n[CLASSIFIED] Archive integrity: 100%")

        with open("classified_data.txt", 'r') as f:
            contenu = f.read()
            print(contenu)

    except Exception as e:
        print(f"{ROUGE}[ERROR] An error was found : {e}{RESET}")

    print(f"\n{BLEU}SECURE PRESERVATION:{RESET}")
    try:
        with open("security_protocols.txt", 'w') as f:
            message = "[CLASSIFIED] New security protocols archived"
            f.write(message)
            print(message)

    except Exception as e:
        print(f"{ROUGE}[ERROR] An error was found : {e}{RESET}")

    print(f"{ORANGE}Vault automatically sealed upon completion\n{RESET}")

    print(f"{VERT}All vault operations completed with maximum "
          f"security.{RESET}")


if __name__ == "__main__":
    main()
