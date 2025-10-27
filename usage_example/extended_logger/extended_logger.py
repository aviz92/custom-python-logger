from typing import Any

from custom_python_logger import CustomLoggerAdapter, build_logger
from custom_python_logger.consts import LOG_COLORS

import logging

LOG_COLORS.update(
    {
        "XXX": "red",
        "YYY": "bold_blue",
    }
)


class ExtendedLoggerAdapter(CustomLoggerAdapter):
    def xxx(self, msg: str, *args, **kwargs) -> None:
        logger_level = 27
        logging.addLevelName(logger_level, "XXX")
        kwargs.setdefault("stacklevel", 2)
        self.log(logger_level, msg, *args, **kwargs)

    def yyy(self, msg: str, *args, **kwargs) -> None:
        logger_level = 12
        logging.addLevelName(logger_level, "YYY")
        kwargs.setdefault("stacklevel", 2)
        self.log(logger_level, msg, *args, **kwargs)


def build_extended_logger(
    project_name: str,
    extra: dict[str, Any] | None = None,
    log_format: str = "%(asctime)s | %(levelname)-9s | l.%(levelno)s | %(name)s | %(filename)s:%(lineno)s | %(message)s",  # pylint: disable=C0301
    log_level: int = logging.INFO,
    log_file: bool = False,
    log_file_path: str = None,
    console_output: bool = True,
    utc: bool = False,
) -> ExtendedLoggerAdapter:
    base_logger = build_logger(
        project_name=project_name,
        extra=extra,
        log_format=log_format,
        log_level=log_level,
        log_file=log_file,
        log_file_path=log_file_path,
        console_output=console_output,
        utc=utc,
    )
    return ExtendedLoggerAdapter(base_logger.logger, base_logger.extra)
