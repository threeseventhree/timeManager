import json
from pathlib import Path
from src.models.task import Task

class TaskStorage:
    def __init__(self, path: str):
        self.path = Path(path)

    def save(self, tasks: list[Task]):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        data = [task.toDict() for task in tasks]
        with open(self.path, "w") as file:
            json.dump(data, file, indent=4)

    def load(self) -> list[Task]:
        if not self.path.exists():
            return []
        with open(self.path, "r") as file:
            data = json.load(file)
        return [Task.fromDict(task) for task in data]