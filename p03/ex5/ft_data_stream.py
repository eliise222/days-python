import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = ["run", "eat", "sleep", "grab",
                          "move", "climb", "swim"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while event_list:
        index: int = random.randint(0, len(event_list) - 1)
        yield event_list.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_gen = gen_event()
    for i in range(1000):
        player, action = next(event_gen)
        print(f"\nEvent {i}: Player {player} did action {action}")

    event_list: list[tuple[str, str]] = [next(event_gen) for _ in range(10)]
    print(f"\nBuilt list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"\nGot event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
