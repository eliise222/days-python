def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
	unit_valid = ["packets", "grams", "area"]
	if unit in unit_valid:
		print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
	else:
		print("Unknown unit type")
# ft_seed_inventory("tomato", 15, "grams")0