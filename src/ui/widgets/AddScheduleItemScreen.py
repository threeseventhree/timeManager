from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Static, Label, Input, Button
from textual.containers import Container

from src.managers.scheduleManager import ScheduleManager
from src.models.scheduleItem import ScheduleItem

import re
class AddScheduleItemScreen(ModalScreen):
    CSS = """
    AddScheduleItemScreen {
        align: center middle;
        background: rgba(0, 0, 0, 0.7);
    }

    #addScheduleItemContainer {
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

    #addScheduleItemButton {
        width: 100%;
        height: 3;
        margin-top: 2;
        background: #1c2027;
        border: round #2a2f38;
        color: #f1f3f5;
    }

    #addScheduleItemButton:hover {
        background: #252a33;
        border: round #596273;
    }
    """

    def __init__(self, manager: ScheduleManager):
        super().__init__()
        self.manager = manager

    def compose(self) -> ComposeResult:
        with Container(id="addScheduleItemContainer"):
            yield Static("Add Schedule Item", id="title")

            yield Label("Name", classes="inputLabel")
            yield Input(
                placeholder="e.g. Gym",
                id="scheduleItemNameInput"
            )

            yield Label("Day of Week", classes="inputLabel")
            yield Input(
                placeholder="e.g. Monday",
                id="dayOfWeekInput"
            )

            yield Label("Start Time", classes="inputLabel")
            yield Input(
                placeholder="e.g. 9:00",
                id="startTimeInput"
            )

            yield Label("End Time", classes="inputLabel")
            yield Input(
                placeholder="e.g. 10:00",
                id="endTimeInput"
            )

            yield Button("Add Schedule Item", id="addScheduleItemButton")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id != "addScheduleItemButton":
            return
        scheduleItemName = self.query_one("#scheduleItemNameInput", Input).value.strip()
        dayOfWeek = self.query_one("#dayOfWeekInput", Input).value.strip().capitalize()
        startTime = self.query_one("#startTimeInput", Input).value.strip()
        endTime = self.query_one("#endTimeInput", Input).value.strip()
        if not scheduleItemName or dayOfWeek not in [
            "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"
        ]:
            return

        timePattern = r"^(?:[01]?\d|2[0-3]):[0-5]\d$"

        if not re.match(timePattern, startTime) or not re.match(timePattern, endTime):
            return

        scheduleItem = ScheduleItem(scheduleItemName, dayOfWeek, startTime, endTime)
        self.manager.addItem(scheduleItem)
        self.dismiss(scheduleItem)
