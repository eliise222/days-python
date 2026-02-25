import sys


def main():
    print("=== Command Quest ===")

    total = len(sys.argv)
    if total == 1:
        print("No Arguments provided!")
        print("Program name:", sys.argv[0])
        print("Arguments received:", total)
    else:
        print("Program name:", sys.argv[0])
        print("Arguments received:", total - 1)

        nb = 1
        while nb < total:
            print("Argument", str(nb) + ":", sys.argv[nb])
            nb += 1
        print("Total arguments:", total)


if __name__ == "__main__":
    main()
