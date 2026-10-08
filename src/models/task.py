from dataclasses import dataclass, field
from uuid import UUID, uuid4
@dataclass
class Task:
    name: str
    duration: int
    completed: bool = False
    id: UUID = field(default_factory=uuid4)
