from src.models.task import Task
from src.managers.taskManager import TaskManager
from src.storage.taskStorage import TaskStorage
sampleTask: Task = Task("Finish Coding the Application", 60)
from src.ui.app import TimeManagerApp
from src.models.scheduleItem import ScheduleItem
from src.managers.scheduleManager import ScheduleManager
from src.storage.scheduleItemStorage import ScheduleItemStorage

school = ScheduleItem(
    name="School",
    day="Monday",
    startTime="08:00",
    endTime="14:00"
)

def main():
    storage = TaskStorage("data/tasks.json")
    # manager = TaskManager(storage)

    # manager.addTask(Task("Study Physics", 60))
    # manager.addTask(Task("Work on Musicbox", 45))
    # manager.addTask(Task("Practice Fusion 3D", 60))
    # scheduleManager = ScheduleManager(storage=ScheduleItemStorage("data/schedule.json"))
    # scheduleManager.addItem(ScheduleItem("School", "Monday", "13:00", "18:30"))
    # scheduleManager.addItem(ScheduleItem("School", "Tuesday", "9:45", "13:00"))
    # scheduleManager.addItem(ScheduleItem("School", "Wednesday", "13:30", "18:30"))
    # scheduleManager.addItem(ScheduleItem("School", "Thursday", "13:30", "18:30"))
    # scheduleManager.addItem(ScheduleItem("School", "Friday", "15:15", "18:30"))


if __name__ == "__main__":
    TimeManagerApp().run()
