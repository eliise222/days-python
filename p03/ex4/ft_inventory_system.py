import sys


def all_calculate():
    inventory = dict()
    moderate = dict()
    scarce = dict()
    restock = ""
    name_str = ""
    value_str = ""
    total = 0
    qty_max = 0
    name_max = ''
    qty_min = None
    name_min = ''

    print("=== Inventory System Analysis ===")

    for element in sys.argv[1:]:
        parts = element.split(':')
        name = parts[0]
        quantity = int(parts[1])
        inventory.update({name: quantity})

    for count in inventory.values():
        total = total + count

    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}\n")

    print("=== Current Inventory ===")

    for name, qty in inventory.items():
        percent = (qty / total) * 100
        print(f"{name}: {qty} units ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")

    for name, qty in inventory.items():
        if qty > qty_max:
            qty_max = qty
            name_max = name
        if qty_min is None or qty < qty_min:
            qty_min = qty
            name_min = name
    print(f"Most abundant: {name_max} ({qty_max} units)")
    print(f"Least abundant: {name_min} ({qty_min} units)\n")

    print("=== Item Categories ===")

    for sort_name, sort_qty in inventory.items():
        if sort_qty >= 5:
            moderate.update({sort_name: sort_qty})
        else:
            scarce.update({sort_name: sort_qty})
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}\n")

    print("=== Management Suggestion ===")

    for name, qty in inventory.items():
        if qty == qty_min:
            if restock == "":
                restock = name
            else:
                restock = restock + ", " + name
    print(f"Restock needed: {restock}\n")

    print("=== Dictionary Properties Demo ===")

    for name in inventory.keys():
        if name_str == "":
            name_str = name
        else:
            name_str = name_str + ", " + name
    for value in inventory.values():
        if value_str == "":
            value_str = str(value)
        else:
            value_str = value_str + ", " + str(value)

    print(f"Dictionary keys: {name_str}")
    print(f"Dictionary values: {value_str}")
    print(f"Sample lookup - 'sword' in inventory: \
{inventory.get('sword') is not None}")


def main():
    all_calculate()


if __name__ == "__main__":
    main()
