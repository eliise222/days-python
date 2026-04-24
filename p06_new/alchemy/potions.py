from alchemy import elements as el
import elements


def healing_potion():
    return f"Healing potion brewerd with '{el.create_earth()}' \
and '{el.create_air()}'"


def strength_potion():
    return f"Strength potion brewerd with '{elements.create_fire()}' \
and '{elements.create_water()}'"
