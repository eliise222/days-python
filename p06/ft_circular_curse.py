from alchemy.grimoire.spellbook import record_spell
from alchemy.grimoire.validator import validate_ingredients


def main():
    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    try:
        print(f'validate_ingredients("fire air"): \
{validate_ingredients("fire air")}')
    except NameError:
        print('validate_ingredients("fire air"): NameError - not imported')
    try:
        print(f'validate_ingredients("dragon scales"): \
{validate_ingredients("dragon scales")}\n')
    except NameError:
        print('validate_ingredients("dragon scales"): \
NameError - not imported\n')

    print("Testing spell recording with validation:")
    try:
        print(f'record_spell("Fireball", "fire air"): \
{record_spell("Fireball", "fire air")}')
    except NameError:
        print('record_spell("Fireball", "fire air"): NameError - not imported')
    try:
        print(f'record_spell("Dark Magic", "shadow"): \
{record_spell("Dark Magic", "shadow")}\n')
    except NameError:
        print('record_spell("Dark Magic", "shadow"): \
NameError - not imported\n')

    print("Testing late import technique:")
    try:
        print(f'record_spell("Lightning", "air"): \
{record_spell("Lightning", "air")}\n')
    except NameError:
        print('record_spell("Lightning", "air"): NameError - not imported\n')

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
