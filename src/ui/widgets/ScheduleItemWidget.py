from textual.widget import Widget
from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container

from src.models.scheduleItem import ScheduleItem

def formatTime(timeString: str) -> str:
    hours, minutes = timeString.split(":")
    return f"{int(hours):02d}:{minutes}"

class ScheduleItemWidget(Widget):
    DEFAULT_CSS = """
    ScheduleItemWidget {
        width: 100%;
        height: auto;
    }
    """
    def __init__(self, scheduleItem: ScheduleItem):
        super().__init__()
        self.scheduleItem = scheduleItem

    def compose(self) -> ComposeResult:
        with Container(classes="scheduleItem"):
            yield Label(self.scheduleItem.name, classes="scheduleItemName")
            yield Label(f"{formatTime(self.scheduleItem.startTime)} – {formatTime(self.scheduleItem.endTime)}",classes="scheduleItemTime")
