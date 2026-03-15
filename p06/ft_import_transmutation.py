import alchemy
import alchemy.elements
from alchemy.potions import strength_potion
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_water, create_earth, create_fire


def main():
    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    try:
        print(f"alchemy.elements.create_fire(): \
{alchemy.elements.create_fire()}\n")
    except AttributeError:
        print("alchemy.elements.create_fire(): AttributeError - not exposed\n")

    print("Method 2 - Specific function import:")
    try:
        print(f"create_water(): {create_water()}\n")
    except NameError:
        print("create_water(): NameError - not imported\n")

    print("Method 3 - Aliased import:")
    try:
        print(f"heal(): {heal()}\n")
    except NameError:
        print("heal(): NameError - alias not found\n")

    print("Method 4 - Multiple imports:")
    try:
        print(f"create_earth(): {create_earth()}")
    except NameError:
        print("create_earth(): NameError - not imported")

    try:
        print(f"create_fire(): {create_fire()}")
    except NameError:
        print("create_fire(): NameError - not imported")

    try:
        print(f"strength_potion(): {strength_potion()}\n")
    except NameError:
        print("strength_potion(): NameError\n")

    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
