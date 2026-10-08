from src.models.task import Task
from src.managers.taskManager import TaskManager
from src.storage.taskStorage import TaskStorage
sampleTask: Task = Task("Finish Coding the Application", 60)

def main():
    storage = TaskStorage("data/tasks.json")
    manager = TaskManager(storage)
    manager.taskList = storage.load()
    print(manager.taskList)

main()