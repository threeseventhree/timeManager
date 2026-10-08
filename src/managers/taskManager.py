from src.models.task import Task
from uuid import UUID
from src.storage.taskStorage import TaskStorage
class TaskManager():
    def __init__(self, storage: TaskStorage):
        self.storage = storage
        self.taskList = self.storage.load()

    def addTask(self, task: Task):
        self.taskList.append(task)
        self.saveTasks()
    def removeTask(self, id: UUID):
        task = self.getTask(id)
        if task is None:
            return False
        self.taskList.remove(task)
        self.saveTasks()
        return True

    def setCompleted(self, task: Task, completed: bool):
        task.completed = completed
        self.saveTasks()

    def getTask(self, id: UUID):
        for task in self.taskList:
            if(task.id == id): return task
        return None

    def getAllTasks(self):
        return self.taskList

    def saveTasks(self):
        self.storage.save(self.taskList)