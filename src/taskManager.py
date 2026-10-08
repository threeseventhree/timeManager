from src.models.task import Task
from uuid import UUID
class TaskManager():
    def __init__(self):
        self.taskList = []

    def addTask(self, task: Task):
        self.taskList.append(task)
        print(f"Successfully added {task.name} task.")

    def removeTask(self, id: UUID):
        task = self.getTask(id)
        if task is None:
            return False
        self.taskList.remove(task)
        return True

    def completeTask(self, task: Task):
        task.completed = True

    def getTask(self, id: UUID):
        for task in self.taskList:
            if(task.id == id): return task
        return None

    def getAllTasks(self):
        return self.taskList