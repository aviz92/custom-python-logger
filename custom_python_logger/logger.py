import json
import logging
import os
import time
from logging import Logger
from pathlib import Path
from typing import Any, Callable, Optional

import yaml
from colorlog import ColoredFormatter

from custom_python_logger.consts import LOG_COLORS, CustomLoggerLevel


def json_pretty_format(
    data: Any, indent: int = 4, sort_keys: bool = True, default: Callable = None
) -> str:
    return json.dumps(data, indent=indent, sort_keys=sort_keys, default=default)


def yaml_pretty_format(
    data: Any, indent: int = 4, sort_keys: bool = False, allow_unicode=True
) -> str:
    return yaml.dump(
        data, sort_keys=sort_keys, indent=indent, allow_unicode=allow_unicode
    )


def get_project_path_by_file(markers: Optional[list[str]] = None) -> Path:
    if not markers:
        markers = ["pyproject.toml", "setup.py", ".git", "requirements.txt", ".gitignore", ".github", ".gitlab"]
    path = Path(__file__).resolve()
    for parent in path.parents:
        for marker in markers:
            if (parent / marker).exists():
                return parent
    raise RuntimeError(f'Project root with one of the markers: "{markers}" not found.')


def print_before_logger(project_name: str) -> None:
    main_string = f'Start "{project_name}" Process'

    number_of_ladder = "#" * len(f"### {main_string} ###")
    print(f"\n{number_of_ladder}")
    print(f"### {main_string} ###")
    print(f"{number_of_ladder}\n")
    time.sleep(0.3)


class CustomLoggerAdapter(logging.LoggerAdapter):
    def exception(self, msg: str, *args, **kwargs):
        logging.addLevelName(CustomLoggerLevel.EXCEPTION.value, "EXCEPTION")
        kwargs.setdefault("stacklevel", 2)
        self.log(CustomLoggerLevel.EXCEPTION.value, msg, *args, exc_info=True, **kwargs)

    def step(self, msg: str, *args, **kwargs):
        logging.addLevelName(CustomLoggerLevel.STEP.value, "STEP")
        kwargs.setdefault("stacklevel", 2)
        self.log(CustomLoggerLevel.STEP.value, msg, *args, exc_info=False, **kwargs)


def clear_existing_handlers(logger: Logger) -> None:
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)


def add_file_handler_if_specified(
    logger: Logger,
    log_file: bool,
    log_file_path: Optional[str],
    log_format: str,
) -> None:
    if log_file and log_file_path is not None:
        log_file_formatter = logging.Formatter(log_format)

        # Create directory if it doesn't exist
        log_dir = os.path.dirname(log_file_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        file_handler = logging.FileHandler(log_file_path)

        file_handler.setFormatter(log_file_formatter)
        logger.addHandler(file_handler)


def add_console_handler_if_specified(
    logger: Logger,
    console_output: bool,
    log_format: str
):
    if console_output:
        log_console_formatter = ColoredFormatter(
            "%(log_color)s " + log_format,
            log_colors=LOG_COLORS,
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_console_formatter)
        logger.addHandler(console_handler)


def configure_logging(
    log_format: str,
    utc: bool,
    log_level: int = logging.INFO,
    log_file: bool = False,
    log_file_path: Optional[str] = None,
    console_output: bool = True,
) -> None:
    """
    Configure global logging settings.

    Args:
        log_level: Logging level (default: INFO)
        log_format: Format string for log messages
        log_file: Whether to log to a file
        log_file_path: Path to log file (if None, no file logging)
        console_output: Whether to output logs to console
        utc: Whether to use UTC time for log timestamps
    """
    if utc:
        logging.Formatter.converter = time.gmtime

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    clear_existing_handlers(logger=root_logger)

    add_file_handler_if_specified(
        logger=root_logger,
        log_file=log_file,
        log_file_path=log_file_path,
        log_format=log_format,
    )

    add_console_handler_if_specified(
        logger=root_logger,
        console_output=console_output,
        log_format=log_format,
    )


def build_logger(
    project_name: str,
    extra: Optional[dict[str, Any]] = None,
    log_format: str = "%(asctime)s | %(levelname)-9s | l.%(levelno)s | %(name)s | %(filename)s:%(lineno)s | %(message)s",
    log_level: int = logging.INFO,
    log_file: bool = False,
    log_file_path: str = None,
    console_output: bool = True,
    utc: bool = False,
) -> CustomLoggerAdapter | Logger:
    """
    Get a named logger with optional extra context.

    Args:
        project_name: Name of the project
        log_level: Optional specific log level
        extra: Optional dictionary of extra context values
        log_format: Format string for log messages
        log_file: Whether to log to a file
        log_file_path: Path to log file (if None, no file logging)
        console_output: Whether to output logs to console
        utc: Whether to use UTC time for log timestamps
    Returns:
        Configured logger
    """
    if not log_file_path:
        log_file_path = f"{get_project_path_by_file()}/logs/{project_name}.log"
        log_file_path = log_file_path.lower().replace(" ", "_")

    configure_logging(
        log_level=logging.DEBUG,
        log_format=log_format,
        log_file=log_file,
        log_file_path=log_file_path,
        console_output=console_output,
        utc=utc,
    )

    logger = logging.getLogger(project_name)

    if log_level is not None:
        logger.setLevel(log_level)

    return CustomLoggerAdapter(logger, extra)


def get_logger(name: str, extra: Optional[dict] = None) -> CustomLoggerAdapter:
    return CustomLoggerAdapter(logging.getLogger(name), extra=extra)
