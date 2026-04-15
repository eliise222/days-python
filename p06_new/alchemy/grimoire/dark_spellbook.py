from alchemy.grimoire.dark_validator import validate_dark_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result: str = validate_dark_ingredients(ingredients)

    if "- VALID" in result:
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"
