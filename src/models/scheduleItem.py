from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class ScheduleItem:
    name: str
    day: str
    startTime: str
    endTime: str
    id: UUID = field(default_factory=uuid4)

    def toDict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "day": self.day,
            "startTime": self.startTime,
            "endTime": self.endTime,
        }

    @classmethod
    def fromDict(cls, data):
        return cls(
            id=UUID(data["id"]),
            name=data["name"],
            day=data["day"],
            startTime=data["startTime"],
            endTime=data["endTime"]
        )
