import time
from functools import wraps
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball():
    time.sleep(0.1)
    return "Fireball cast!"


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(power: int, *args, **kwargs):
            if power >= min_power:
                return func(power, *args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt \
{attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and name.replace(" ", "").isalpha():
            return True
        return False

    def cast_spell(self, spell_name: str, power: int) -> str:
        if power >= 10:
            return f"Successfully cast {spell_name} with {power} power"
        return "Insufficient power for this spell"


def main() -> None:
    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def unstable_spell() -> str:
        raise Exception("Spell unstable!")

    @retry_spell(3)
    def stable_spell() -> str:
        return "Waaaaaaagh spelled !"

    print(unstable_spell())
    print(stable_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("A1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
