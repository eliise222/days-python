from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500, default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validaterules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic\
           and self.witness_count < 3:
            raise ValueError("Telepathic contact requires \
at least 3 witnesses")
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Message received can't be 'None'")
        return self


def main() -> None:
    try:
        contact = AlienContact(
                                contact_id="AC_2024_001",
                                timestamp=datetime.fromisoformat("2024-01-15T10:\
30:00"),
                                location="Area 51, Nevada",
                                contact_type=ContactType.radio,
                                signal_strength=8.5,
                                duration_minutes=45,
                                witness_count=5,
                                message_received="Greetings from \
                                Zeta Reticuli",
                                is_verified=False
                            )
        print("Alien Contact Log Validation")
        print("=" * 40)
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'\n")
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))

        print("=" * 40)
        print("Expected validation error:")
    try:
        _ = AlienContact(
                            contact_id="AC_2024_001",
                            timestamp=datetime.fromisoformat("2024-01-15T10:\
30:00"),
                            location="Area 51, Nevada",
                            contact_type=ContactType.telepathic,
                            signal_strength=8.5,
                            duration_minutes=45,
                            witness_count=2,
                            message_received="Greetings from Zeta Reticuli",
                            is_verified=False
                        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
