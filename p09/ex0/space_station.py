from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200, default=None)


def main() -> None:
    station = SpaceStation(
                            station_id="ISS001",
                            name="International Space Station",
                            crew_size=6,
                            power_level=85.5,
                            oxygen_level=92.3,
                            last_maintenance="2024-01-15T10:30:00"
                          )

    print("Space Station Data Validation")
    print("=" * 40)
    print("Valid station created")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    if station.is_operational:
        print("Status: Operational")

    print("=" * 40)
    print("Expected validation error:")
    try:
        SpaceStation(
                        station_id="ISS001",
                        name="International Space Station",
                        crew_size=50,
                        power_level=85.5,
                        oxygen_level=92.3,
                        last_maintenance="2024-01-15T10:30:00"
                    )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
