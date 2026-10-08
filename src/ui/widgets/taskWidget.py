from textual.widget import Widget
from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Label, Checkbox, Static
from src.models.task import Task
from src.managers.taskManager import TaskManager

class TaskWidget(Widget):
    DEFAULT_CSS = """
    #task {
        width: 100%;
        height: 100%;
        padding: 1;
    }

    #taskHeader {
        width: 100%;
        height: 3;
    }

    #taskName {
        width: 1fr;
        height: 3;
        content-align: left middle;
        text-style: bold;
        color: #f1f3f5;
    }

    #deleteTask {
        width: 3;
        height: 3;
        content-align: center middle;
        color: #596273;
        background: transparent;
    }

    #deleteTask:hover {
        color: #f1f3f5;
        background: #2a2f38;
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
        background: transparent;
    }

    #taskCheckbox:focus {
        border: none;
        background: transparent;
    }
    """
    def __init__(self, task: Task, manager: TaskManager, **kwargs):
        super().__init__(**kwargs)
        self.taskData = task
        self.manager = manager

    def compose(self) -> ComposeResult:
        with Container(id="task"):
            with Horizontal(id="taskHeader"):
                yield Label(self.taskData.name, id="taskName")
                yield Label("×", id="deleteTask")

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
        self.screen.set_focus(None)

    def on_click(self, event):
        if event.widget.id != "deleteTask":
            return
    
        self.manager.removeTask(self.taskData.id)
        self.remove()
