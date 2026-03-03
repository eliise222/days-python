import math


x = (10, 20, 5)
y = (0, 0, 0)
coord_str = "3,4,0"
inval = "abc,def,ghi"


def parse(str):
    try:
        str_tup = []
        str = str.split(',')
        for i in str:
            str_tup.append(int(i))
        return tuple(str_tup)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")


def verif(x, y):
    if len(x) > 3:
        print("Error parsing coordinates : there is more than 3 coordinates.")
        return 0
    elif len(y) > 3:
        print("Error parsing coordinates : there is more than 3 coordinates.")
        return 0


def calculate(x, y):
    verif(x, y)
    distance = math.sqrt((y[0]-x[0]) ** 2 +
                         (y[1]-x[1]) ** 2 + (y[2]-x[2]) ** 2)
    return distance


def test(x, y, coord_str, inval):
    print("=== Game Coordinate System ===\n")

    print(f"Position created: {x}")
    dist = calculate(x, y)
    print(f"Distance between {y} and {x}: {dist:.2f}\n")

    print(f'Parsing coordinates : "{coord_str}"')
    parsed = parse(coord_str)
    print(f"Parsed position: {parsed}")
    distparse = calculate(parsed, y)
    print(f"Distance between {y} and {parsed}: {distparse:.2f}\n")

    print(f'Parsing invalid coordinates: "{inval}"')
    parse(inval)

    print("Unpacking demonstration:")
    px, py, pz = parsed
    print(f"Player at x={px}, y={py}, z={pz}")
    print(f"Coordinates: X={px}, Y={py}, Z={pz}")


def main():
    test(x, y, coord_str, inval)


if __name__ == "__main__":
    main()
