from enum import Enum

LOG_COLORS = {
    "DEBUG": "white",
    "INFO": "green",
    "WARNING": "yellow",
    "STEP": "blue",
    "ERROR": "red,bold",
    "EXCEPTION": "light_red,bold",
    "CRITICAL": "red,bg_white",
}


class CustomLoggerLevel(Enum):
    EXCEPTION = 45
    STEP = 25
