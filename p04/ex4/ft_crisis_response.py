def crisis_alert():

    ROUGE = "\033[31m"
    VERT = "\033[32m"
    RESET = "\033[0m"
    BLEU = "\033[34m"
    ORANGE = "\033[33m"

    print(f"{ORANGE}CRISIS ALERT: Attempting acces to 'lost_archives.txt'...")

    try:
        with open("lost_archive.txt", 'r') as f:
            contenu = f.read()
            print(f"{VERT}SUCCESS{RESET}: Archive recovered \
= ''", contenu, "''")
            print(f"{BLEU}STATUS{RESET}: Normal operations resumed\n")
    except FileNotFoundError:
        print(f"{ROUGE}RESPONSE{RESET}: Archive not found in storage matrix")
        print(f"{BLEU}STATUS{RESET}: Crisis handled, system stable\n")
    except PermissionError:
        print(f"{ROUGE}RESPONSE{RESET}: Security protocols deny access")
        print(f"{BLEU}STATUS{RESET}: Crisis handled, security maintained\n")

    print(f"{ORANGE}CRISIS ALERT: Attempting acces to \
'classified_vault.txt'...")

    try:
        with open("classified_vault.txt", 'r') as f:
            contenu = f.read()
            print(f"{VERT}SUCCESS{RESET}: Archive recovered = \
''", contenu, "''")
            print(f"{BLEU}STATUS{RESET}: Normal operations resumed\n")
    except FileNotFoundError:
        print(f"{ROUGE}RESPONSE{RESET}: Archive not found in storage matrix")
        print(f"{BLEU}STATUS{RESET}: Crisis handled, system stable\n")
    except PermissionError:
        print(f"{ROUGE}RESPONSE{RESET}: Security protocols deny access")
        print(f"{BLEU}STATUS{RESET}: Crisis handled, security maintained\n")

    print(f"{ORANGE}CRISIS ALERT: Attempting acces \
to 'standart_archive.txt'...")

    try:
        with open("standard_archive.txt", 'r') as f:
            contenu = f.read()
            print(f"{VERT}SUCCESS{RESET}: Archive recovered \
= ''", contenu, "''")
            print(f"{BLEU}STATUS{RESET}: Normal operations resumed\n")
    except FileNotFoundError:
        print(f"{ROUGE}RESPONSE{RESET}: Archive not found in storage matrix")
        print(f"{BLEU}STATUS{RESET}: Crisis handled, system stable\n")
    except PermissionError:
        print(f"{ROUGE}RESPONSE{RESET}: Security protocols deny access")
        print(f"{BLEU}STATUS{RESET}: Crisis handled, security maintained\n")


def main():
    print("=== CYBER ARCHIVES = CRISIS RESPONSE SYSTEM ===\n")
    crisis_alert()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
