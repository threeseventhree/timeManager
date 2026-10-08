from dataclasses import dataclass, field
from uuid import UUID, uuid4
@dataclass
class Task:
    name: str
    duration: int
    completed: bool = False
    id: UUID = field(default_factory=uuid4)
    
    def toDict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "duration": self.duration,
            "completed": self.completed
        }

    @classmethod
    def fromDict(cls, data):
        return cls(
            id=UUID(data["id"]),
            name=data["name"],
            duration=data["duration"],
            completed=data["completed"]
        )