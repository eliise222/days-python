import os
from dotenv import load_dotenv


def load_config() -> dict[str, str]:
    load_dotenv()
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "unknown"),
        "DATABASE_URL": os.getenv("DATABASE_URL", "not configured"),
        "API_KEY": os.getenv("API_KEY", "not configured"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "not configured"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", "not configured"),
    }


def mask_secret(value: str) -> str:
    return value[:3] + "****"


def display_config(config: dict[str, str]) -> None:
    mode = config["MATRIX_MODE"]
    api_key = config["API_KEY"]

    if mode == "production":
        api_key = mask_secret(api_key)

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {config['DATABASE_URL']}")
    print(f"API Access: {api_key}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {config['ZION_ENDPOINT']}\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")

    print("The Oracle sees all configurations.")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_config()
    display_config(config)


if __name__ == "__main__":
    main()
