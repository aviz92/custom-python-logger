from dotenv import load_dotenv

from custom_python_logger.consts import LOG_FORMAT_FILENAME, LOG_FORMAT_SHORTPATH
from custom_python_logger.logger import (
    CustomLoggerAdapter,
    CustomLoggerLevel,
    build_logger,
    get_logger,
    json_pretty_format,
    yaml_pretty_format,
)

load_dotenv()

__all__ = [
    "CustomLoggerAdapter",
    "CustomLoggerLevel",
    "build_logger",
    "get_logger",
    "json_pretty_format",
    "yaml_pretty_format",
    "LOG_FORMAT_SHORTPATH",
    "LOG_FORMAT_FILENAME",
]
