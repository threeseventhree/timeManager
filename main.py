from src.models.task import Task
from src.managers.taskManager import TaskManager
from src.storage.taskStorage import TaskStorage
sampleTask: Task = Task("Finish Coding the Application", 60)
from src.ui.app import TimeManagerApp

def main():
    storage = TaskStorage("data/tasks.json")
    manager = TaskManager(storage)

    manager.addTask(Task("Study Physics", 60))
    manager.addTask(Task("Work on Musicbox", 45))
    manager.addTask(Task("Practice Fusion 3D", 60))

if __name__ == "__main__":
    TimeManagerApp().run()