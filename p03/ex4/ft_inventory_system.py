import sys


def all_calculate() -> None:
    inventory: dict[str, int] = dict()
    total: int = 0
    qty_max: int = 0
    name_max: str = ''
    qty_min: int | None = None
    name_min: str = ''

    print("=== Inventory System Analysis ===")

    for element in sys.argv[1:]:
        if ':' not in element:
            print(f"Error - invalid parameter '{element}'")
            continue

        parts: list[str] = element.split(':')
        name: str = parts[0]

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            quantity: int = int(parts[1])
            inventory.update({name: quantity})
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for name, qty in inventory.items():
        percent: float = (qty / total) * 100
        print(f"Item {name} represents {percent:.1f}%")

    for name, qty in inventory.items():
        if qty > qty_max:
            qty_max = qty
            name_max = name
        if qty_min is None or qty < qty_min:
            qty_min = qty
            name_min = name

    if inventory:
        print(f"Item most abundant: {name_max} with quantity {qty_max}")
        print(f"Item least abundant: {name_min} with quantity {qty_min}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    all_calculate()


if __name__ == "__main__":
    main()
