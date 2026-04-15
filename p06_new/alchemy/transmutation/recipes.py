from ..elements import create_air   # relative import
from elements import create_fire    # absolute import
from alchemy.potions import strength_potion   # absolute import


def lead_to_gold() -> str:
    return f"Recipe transmuting Lead to Gold: brew '{create_air()}' and \
'{strength_potion()}' mixed with '{create_fire()}'"
