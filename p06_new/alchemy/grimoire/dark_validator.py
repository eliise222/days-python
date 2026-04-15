from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
    lst_ingredient: str = ingredients.lower()

    valid: list[str] = dark_spell_allowed_ingredients()
    for i in valid:
        if i in lst_ingredient:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
