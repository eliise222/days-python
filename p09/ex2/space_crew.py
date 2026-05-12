from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1,
                                   max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validaterules(self) -> 'SpaceMission':
        is_available = 0
        experimented = 0
        non_active = 0
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        for i in self.crew:
            if i.rank == Rank.commander or i.rank == Rank.captain:
                is_available += 1
        if is_available == 0:
            raise ValueError("Mission must have at least one Commander \
or Captain")
        if self.duration_days > 365:
            for e in self.crew:
                if e.years_experience >= 5:
                    experimented += 1
            moit_equp = len(self.crew) / 2
            if not experimented >= moit_equp:
                raise ValueError("For long mission : needed 50% experienced \
crew (5+ years)")
        for e in self.crew:
            if not e.is_active:
                non_active += 1
        if non_active > 0:
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    member1 = CrewMember(
                          member_id="CM001",
                          name="Sarah Connor",
                          rank="commander",
                          age=35,
                          specialization="Mission Command",
                          years_experience=10
                        )

    member2 = CrewMember(
                          member_id="CM002",
                          name="John Smith",
                          rank="lieutenant",
                          age=28,
                          specialization="Navigation",
                          years_experience=5
                        )

    member3 = CrewMember(
                          member_id="CM003",
                          name="Alice Johnson",
                          rank="officer",
                          age=29,
                          specialization="Engineering",
                          years_experience=8
                        )

    mission_one = SpaceMission(
                                mission_id="M2024_MARS",
                                mission_name=" Mars Colony Establishment",
                                destination="Mars",
                                launch_date="2024-01-15T10:30:00",
                                duration_days=900,
                                crew=[member1, member2, member3],
                                budget_millions=2500.0
                               )

    print("Space Mission Crew Validation")
    print("=" * 40)
    print("Valid mission created:")
    print(f"Mission: {mission_one.mission_name}")
    print(f"ID: {mission_one.mission_id}")
    print(f"Destination: {mission_one.destination}")
    print(f"Duration: {mission_one.duration_days} days")
    print(f"Budget: ${mission_one.budget_millions}M")
    print(f"Crew size: {len(mission_one.crew)}")
    print("Crew members:")
    for member in mission_one.crew:
        print(f"{member.name} ({member.rank.value}) - {member.specialization}")
    print("\n")
    print("=" * 40)

    print("Expected validation error:")
    try:
        _ = SpaceMission(
                                mission_id="M2024_MARS",
                                mission_name=" Mars Colony Establishment",
                                destination="Mars",
                                launch_date="2024-01-15T10:30:00",
                                duration_days=900,
                                crew=[member2, member3],
                                budget_millions=2500.0
                              )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
