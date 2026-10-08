from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label, Tabs, Tab, ContentSwitcher, Button, Static, Input
from textual.containers import Container, HorizontalScroll
from textual.screen import ModalScreen

from src.storage.taskStorage import TaskStorage
from src.managers.taskManager import TaskManager
from src.models.task import Task
from src.ui.widgets.taskWidget import TaskWidget
from src.ui.widgets.AddTaskScreen import AddTaskScreen

sampleTask: Task = Task("Finish Coding the Application", 60)
storage = TaskStorage("data/tasks.json")
manager = TaskManager(storage)
tasks = manager.taskList

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

    #addTask {
        content-align: center middle;
        color: #858d9a;
    }

    #addTask:hover {
        color: #f1f3f5;
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
        yield Tabs(
            Tab("Tasks", id="tasksScreen"),
            Tab("Schedule", id="scheduleScreen"),
            active="tasksScreen"
        )
        with ContentSwitcher(initial="tasksScreen"):
            with Container(id="tasksScreen"):
                with HorizontalScroll(id="tasksContainer"):
                    for taskData in tasks:
                        yield TaskWidget(taskData, manager, classes="taskWidget")
                    yield Button("+ Add Task", id="addTask", classes="taskWidget")
            with Container(id="scheduleScreen"):
                yield Label("Schedule coming soon...")

        yield Footer(compact=True)

    def on_tabs_tab_activated(self, event: Tabs.TabActivated):
        self.query_one(ContentSwitcher).current = event.tab.id
    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "addTask":
            self.push_screen(
                AddTaskScreen(manager),
                self.addTask # type: ignore
            ) # type: ignore
            pass
    def addTask(self, task: Task):
        tasksContainer = self.query_one("#tasksContainer")
        addTaskButton = self.query_one("#addTask")

        tasksContainer.mount(
            TaskWidget(task, manager, classes="taskWidget"),
            before=addTaskButton
        )

if __name__ == "__main__":
    TimeManagerApp().run()
