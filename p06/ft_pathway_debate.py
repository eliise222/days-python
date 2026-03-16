import alchemy
import alchemy.transmutation
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life


def main():
    print("=== Pathway debate Mastery ===\n")

    print("Testing Absolute imports (from basic.py):")
    try:
        print(f"lead_to_gold(): {lead_to_gold()}")
    except NameError:
        print("lead_to_gold(): NameError - not imported")

    try:
        print(f"stone_to_gem(): {stone_to_gem()}\n")
    except NameError:
        print("stone_to_gem(): NameError - not imported\n")

    print("Testing Relative Imports (from advanced.py):")
    try:
        print(f"philosophers_stone(): {philosophers_stone()}")
    except NameError:
        print("philosophers_stone(): NameError - not imported")

    try:
        print(f"elixir_of_life: {elixir_of_life()}\n")
    except NameError:
        print("elixir_of_life(): NameError - not imported\n")

    print("Testing Package Access:\n")
    try:
        print(f"alchemy.transmutation.lead_to_gold(): \
{alchemy.transmutation.lead_to_gold()}")
    except AttributeError:
        print("alchemy.transmutation.lead_to_gold(): \
AttributeError - not exposed")

    try:
        print(f"alchemy.transmutation.philosophers_stone(): \
{alchemy.transmutation.philosophers_stone()}\n")
    except AttributeError:
        print("alchemy.transmutation.philosophers_stone(): \
AttributeError - not exposed\n")

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
