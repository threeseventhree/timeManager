from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Static, Label, Input, Button
from textual.containers import Container

from src.managers.taskManager import TaskManager
from src.models.task import Task

class AddTaskScreen(ModalScreen):
    CSS = """
    AddTaskScreen {
        align: center middle;
        background: rgba(0, 0, 0, 0.7);
    }

    #addTaskContainer {
        width: 60;
        height: auto;
        padding: 2 3;
        background: #15181d;
        border: round #2a2f38;
    }

    #title {
        width: 100%;
        height: 3;
        content-align: center middle;
        text-style: bold;
        color: #f1f3f5;
    }

    .inputLabel {
        margin-top: 1;
        color: #858d9a;
    }

    Input {
        width: 100%;
        height: 3;
        margin-top: 1;
        background: #0d0f12;
        border: round #2a2f38;
    }

    Input:focus {
        border: round #596273;
    }

    #addTaskButton {
        width: 100%;
        height: 3;
        margin-top: 2;
        background: #1c2027;
        border: round #2a2f38;
        color: #f1f3f5;
    }

    #addTaskButton:hover {
        background: #252a33;
        border: round #596273;
    }
    """

    def __init__(self, manager: TaskManager):
        super().__init__()
        self.manager = manager

    def compose(self) -> ComposeResult:
        with Container(id="addTaskContainer"):
            yield Static("Add Task", id="title")

            yield Label("Task Name", classes="inputLabel")
            yield Input(
                placeholder="e.g. Study Physics",
                id="taskNameInput"
            )

            yield Label("Task Duration(minutes)", classes="inputLabel")
            yield Input(
                placeholder="e.g. 60",
                id="taskDurationInput"
            )

            yield Button("Add Task", id="addTaskButton")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id != "addTaskButton":
            return
        taskName = self.query_one("#taskNameInput", Input).value
        taskDuration = self.query_one("#taskDurationInput", Input).value
        if not taskName or not taskDuration:
            return
        
        task = Task(taskName, int(taskDuration))
        self.manager.addTask(task)
        self.dismiss(task)
