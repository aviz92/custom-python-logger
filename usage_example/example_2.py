import logging

from usage_example.extended_logger.extended_logger import build_extended_logger

x = build_extended_logger(
    project_name="private_python_test",
    log_level=logging.DEBUG,
)

x.xxx("x1")
x.yyy("x2")
x.debug("debug")
x.info("info")
x.warning("warning")
x.error("error")
