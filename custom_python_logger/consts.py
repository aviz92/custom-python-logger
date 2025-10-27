from enum import Enum

LOG_COLORS = {
    "DEBUG": "white",
    "INFO": "green",
    "WARNING": "yellow",
    "STEP": "blue",
    "ERROR": "red,bold",
    "EXCEPTION": "light_red,bold",
    "CRITICAL": "red,bg_white",
    "SUCCESS": "bold_green",
    "FATAL": "red,bg_white",
    "ALERT": "bold_yellow",
    "TRACE": "bold_cyan",
}


class CustomLoggerLevel(Enum):
    EXCEPTION = 45
    STEP = 25
    SUCCESS = 26
    ALERT = 35
    TRACE = 15
