def ft_count_harvest_recursive() -> None:
    total_days = int(input("Days until harvest: "))

    def count(current: int) -> None:
        if current > total_days:
            print("Harvest time!")
            return
        print(f"Day {current}")
        count(current + 1)
    count(1)


# ft_count_harvest_recursive()
