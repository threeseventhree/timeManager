from textual.widget import Widget
from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Label, Checkbox, Button
from src.models.task import Task
from src.managers.taskManager import TaskManager

class TaskWidget(Widget):
    CSS = """
    #task {
        width: 100%;
        height: 100%;
        padding: 1;
    }

    #taskName {
        width: 100%;
        height: 3;
        content-align: left middle;
        text-style: bold;
        color: #f1f3f5;
    }

    #taskDuration {
        width: 100%;
        height: 1;
        color: #858d9a;
    }

    #taskCheckbox {
        margin-top: 2;
        color: #b8bec8;
        border: none;
    }

    #taskCheckbox:focus {
        border: none;
    }
    """
    def __init__(self, task: Task, manager: TaskManager, **kwargs):
        super().__init__(**kwargs)
        self.taskData = task
        self.manager = manager

    def compose(self) -> ComposeResult:
        with Container(id="task"):
            yield Label(
                self.taskData.name,
                id="taskName"
            )

            yield Label(
                f"Duration: {self.taskData.duration}min",
                id="taskDuration"
            )

            yield Checkbox(
                "Completed",
                self.taskData.completed,
                id="taskCheckbox"
            )

    def on_checkbox_changed(self, event: Checkbox.Changed):
        self.manager.setCompleted(self.taskData, event.value)