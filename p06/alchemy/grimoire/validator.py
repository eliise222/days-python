def validate_ingredients(ingredients: str) -> str:
    lst_ingredient = ingredients.split(" ")
    valid = ["fire", "water", "earth", "air"]
    for i in lst_ingredient:
        if i not in valid:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
