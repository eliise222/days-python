import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            line: str = input("Enter new coordinates as floats\
 in format 'x,y,z': ")
            parts: list[str] = line.split(',')
            if len(parts) != 3:
                print("Invalid syntax")
                continue

            for p in parts:
                try:
                    float(p)
                except ValueError:
                    val = p.strip()
                    print(f"Error on parameter '{val}': could not convert "
                          f"string to float: '{val}'")
                    raise ValueError

            return (float(parts[0]), float(parts[1]), float(parts[2]))

        except ValueError:
            continue


def calculate_distance(p1: tuple[float, float, float],
                       p2: tuple[float, float, float]) -> float:
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 +
                     (p2[2] - p1[2])**2)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")

    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_center: float = calculate_distance(pos1, (0.0, 0.0, 0.0))
    print(f"Distance to center: {dist_center:.4f}\n")

    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()

    dist_between: float = calculate_distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")


if __name__ == "__main__":
    main()
