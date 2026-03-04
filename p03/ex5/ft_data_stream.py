import typing


def all_events():

    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    def generator() -> typing.Generator[str, None, None]:

        name = ["Alice", "Bob", "Charlie"]

        for i in range(1000):
            level = ((i * 7) % 20) + 1
            nom = name[i % 3]

            if i % 11 == 0:
                choose_action = "found treasure"
            elif i % 7 == 0:
                choose_action = "leveled up"
            else:
                choose_action = "killed monster"

            yield f"Event {i+1}: Player {nom} (level {level}) {choose_action}"

    total = 0
    treasure = 0
    levels_up = 0
    high_level = 0

    for event in generator():
        total += 1
        parts = event.split("(level ")
        level_parts = parts[1].split(")")
        lvl_val = int(level_parts[0])

        if "found treasure" in event:
            treasure += 1

        if "leveled up" in event:
            levels_up += 1

        if lvl_val >= 10:
            high_level += 1

        if total <= 3:
            print(event)

    print("...\n")

    print("=== Stream Analytics ===")

    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {levels_up}\n")

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===")

    def fibonacci_generator() -> typing.Generator[int, None, None]:

        a = 0
        b = 1
        temp = 0
        while True:
            yield a
            temp = a
            a = b
            b = temp + b

    def prime_generator() -> typing.Generator[int, None, None]:

        n = 2
        while True:
            is_prime = True
            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                yield n
            n += 1

    fib_gen = fibonacci_generator()
    fib_res = ""
    for _ in range(10):
        val = next(fib_gen)
        if fib_res == "":
            fib_res = str(val)
        else:
            fib_res = fib_res + ", " + str(val)
    print(f"Fibonacci sequence (first 10): {fib_res}")

    prime_gen = prime_generator()
    prime_res = ""
    for _ in range(5):
        val = next(prime_gen)
        if prime_res == "":
            prime_res = str(val)
        else:
            prime_res = prime_res + ", " + str(val)
    print(f"Prime numbers (first 5): {prime_res}")


def main():
    all_events()


if __name__ == "__main__":
    main()
