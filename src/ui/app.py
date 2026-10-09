# Textual
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label, Tabs, Tab, ContentSwitcher, Button, Static, Input, Collapsible
from textual.containers import Container, HorizontalScroll, Vertical
# Widgets
from src.ui.widgets.taskWidget import TaskWidget
from src.ui.widgets.AddTaskScreen import AddTaskScreen
from src.ui.widgets.ScheduleItemWidget import ScheduleItemWidget
# Managers
from src.managers.taskManager import TaskManager
from src.managers.scheduleManager import ScheduleManager
# Storage
from src.storage.scheduleItemStorage import ScheduleItemStorage
from src.storage.taskStorage import TaskStorage
# Models
from src.models.task import Task
# Misc
from datetime import datetime
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
def timeToMinutes(timeString: str) -> int:
    hours, minutes = timeString.split(":")
    return int(hours) * 60 + int(minutes)

taskManager = TaskManager(TaskStorage("data/tasks.json"))
scheduleManager = ScheduleManager(ScheduleItemStorage("data/schedule.json"))
tasks = taskManager.taskList
scheduleItems = scheduleManager.itemList

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

        #scheduleScreen {
        height: 1fr;
        padding: 1 3;
    }

    #scheduleContainer {
        width: 100%;
        height: 1fr;
        overflow-y: auto;
    }

    Collapsible {
        width: 100%;
        margin-bottom: 1;
        background: #15181d;
        border: round #2a2f38;
    }

    Collapsible > Contents {
        padding: 1 2;
    }

    .scheduleItem {
        width: 100%;
        height: auto;
        padding: 1 2;
        margin-bottom: 1;
        background: #191d23;
        border-left: thick #596273;
    }

    .scheduleItemName {
        color: #f1f3f5;
        text-style: bold;
    }

    .scheduleItemTime {
        color: #858d9a;
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
            Tab("Tasks", id="tasksTab"),
            Tab("Schedule", id="scheduleTab"),
            active="tasksTab"
        )
        with ContentSwitcher(initial="tasksScreen"):
            with Container(id="tasksScreen"):
                with HorizontalScroll(id="tasksContainer"):
                    for taskData in tasks:
                        yield TaskWidget(taskData, taskManager, classes="taskWidget")
                    yield Button("+ Add Task", id="addTask", classes="taskWidget")
            with Container(id="scheduleScreen"):
                with Vertical(id="scheduleContainer"):
                    today = DAYS[datetime.now().weekday()]
                    for day in DAYS:
                        dayItems = sorted(
                            (item for item in scheduleItems if item.day == day),
                            key=lambda item: timeToMinutes(item.startTime)
                        )
                        with Collapsible(title=day, collapsed=(day != today)):
                            if dayItems:
                                for scheduleItem in dayItems:
                                    yield ScheduleItemWidget(scheduleItem)
                            else:
                                yield Label("No schedule items yet")
            
        yield Footer(compact=True)

    def on_tabs_tab_activated(self, event: Tabs.TabActivated):
        screenMap = {
            "tasksTab": "tasksScreen",
            "scheduleTab": "scheduleScreen"
        }
    
        self.query_one(ContentSwitcher).current = screenMap[event.tab.id]
    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "addTask":
            self.push_screen(
                AddTaskScreen(taskManager),
                self.addTask # type: ignore
            ) # type: ignore
            pass
    def addTask(self, task: Task):
        tasksContainer = self.query_one("#tasksContainer")
        addTaskButton = self.query_one("#addTask")

        tasksContainer.mount(
            TaskWidget(task, taskManager, classes="taskWidget"),
            before=addTaskButton
        )

if __name__ == "__main__":
    TimeManagerApp().run()
