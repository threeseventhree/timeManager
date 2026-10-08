from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Header, Footer, Label, Checkbox
from textual.containers import Container, HorizontalScroll
from src.storage.taskStorage import TaskStorage
from src.models.task import Task

sampleTask: Task = Task("Finish Coding the Application", 60)

storage = TaskStorage("data/tasks.json")
tasks = storage.load()

class TaskWidget(Widget):
    def __init__(self, task: Task, **kwargs):
        super().__init__(**kwargs)
        self.taskData = task

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


class TimeManagerApp(App):
    CSS = """
    Screen {
        background: #0d0f12;
    }

    HorizontalScroll {
        height: 1fr;
        padding: 2 3;
        scrollbar-size: 1 1;
    }

    .taskWidget {
        width: 32;
        height: 1fr;
        margin: 1 1;
        padding: 2;
        background: #15181d;
        border: round #2a2f38;
    }

    .taskWidget:hover {
        background: #191d23;
        border: round #596273;
    }

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

    Header {
        background: #111318;
    }

    Footer {
        background: #111318;
    }
    """

    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Header()

        with HorizontalScroll():
            for taskData in tasks:
                yield TaskWidget(taskData, classes="taskWidget")

        yield Footer(compact=True)

if __name__ == "__main__":
    TimeManagerApp().run()