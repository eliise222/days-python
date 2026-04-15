from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    lst_ingredient = ingredients.lower()

    valid = light_spell_allowed_ingredients()
    for i in valid:
        if i in lst_ingredient:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
