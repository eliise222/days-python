import sys


def main():

    ROUGE = "\033[31m"
    VERT = "\033[32m"
    RESET = "\033[0m"
    BLEU = "\033[34m"

    print("=== CYBER ARCHIVES = COMMUNICATION SYSTEM ===\n")
    try:
        arch_id = input("Input Stream active. Enter archivist ID: ")
        status = input("\nInput Stream active. Enter status report: ")
        sys.stdout.write(f"\n{BLEU}[STANDARD]{RESET} Archive status from \
{arch_id}: {status}")
        sys.stderr.write(f"\n{ROUGE}[ALERT]{RESET} System diagnostic: \
Communication channels verified")
        sys.stdout.write(f"\n{BLEU}[STANDARD]{RESET} Data transmission \
complete\n")
    except OSError as e:
        sys.stderr.write(f"\n{ROUGE}[ERROR]{RESET} An Error was found: {e}")
    except PermissionError as e:
        sys.stderr.write(f"\n{ROUGE}[PERMISSION ERROR]{RESET} Error {e}")
    except Exception as e:
        sys.stderr.write(f"\n{ROUGE}[ERROR]{RESET} An error was found: {e}")

    print(f"\n{VERT}Three-channel communication test successful.{RESET}")


if __name__ == "__main__":
    main()
