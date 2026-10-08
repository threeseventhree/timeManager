from src.models.task import Task
from src.taskManager import TaskManager
from uuid import uuid4
sampleTask: Task = Task("Finish Coding the Application", 60)

def main():
    manager = TaskManager()
    physics = Task("Study Physics", 60)
    musicbox = Task("Work on Musicbox", 45)

    manager.addTask(physics)
    manager.addTask(musicbox)

    print(physics)
    print(musicbox)

    manager.completeTask(physics)
    print(manager.getTask(physics.id))

main()