from src.models.task import Task
from uuid import UUID
from src.storage.taskStorage import TaskStorage
class TaskManager():
    def __init__(self, storage: TaskStorage):
        self.storage = storage
        self.taskList = []

    def addTask(self, task: Task):
        self.taskList.append(task)
        self.save()
    def removeTask(self, id: UUID):
        task = self.getTask(id)
        if task is None:
            return False
        self.taskList.remove(task)
        self.save()
        return True

    def completeTask(self, task: Task):
        task.completed = True
        self.save()

    def getTask(self, id: UUID):
        for task in self.taskList:
            if(task.id == id): return task
        return None

    def getAllTasks(self):
        return self.taskList

    def save(self):
        self.storage.save(self.taskList)