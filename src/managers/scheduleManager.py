from src.models.scheduleItem import ScheduleItem
from uuid import UUID
from src.storage.scheduleItemStorage import ScheduleItemStorage
class ScheduleManager:
    def __init__(self, storage: ScheduleItemStorage):
        self.storage = storage
        self.itemList: list[ScheduleItem] = self.storage.loadItems()

    def addItem(self, item: ScheduleItem):
        self.itemList.append(item)
        self.save()

    def getItem(self, id: UUID) -> ScheduleItem | None:
        for item in self.itemList:
            if(item.id == id): return item
        return None

    def removeItem(self, id: UUID):
        item = self.getItem(id)
        if item is None: return False
        self.itemList.remove(item)
        self.save()
        return True

    def getItemsForDay(self, day: str) -> list[ScheduleItem]:
        items: list[ScheduleItem] = []
        for item in self.itemList:
            if(item.day == day): items.append(item) 
        return items
    def getAllItems(self) -> list[ScheduleItem]:
        return self.itemList

    def save(self):
        self.storage.saveItems(self.itemList)
