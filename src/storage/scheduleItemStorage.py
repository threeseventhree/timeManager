from pathlib import Path
import json
from src.models.scheduleItem import ScheduleItem

class ScheduleItemStorage:
    def __init__(self, path: str):
        self.path = Path(path)

    def saveItems(self, scheduleItems: list[ScheduleItem]):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        data = [scheduleItem.toDict() for scheduleItem in scheduleItems]
        with open(self.path, "w") as file:
            json.dump(data, file, indent=4)
        
    def loadItems(self) -> list[ScheduleItem]:
        if not self.path.exists():
            return []
        with open(self.path, "r") as file:
            data = json.load(file)
        return [ScheduleItem.fromDict(scheduleItem) for scheduleItem in data]
