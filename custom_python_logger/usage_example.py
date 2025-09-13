import logging

from custom_python_logger import build_logger, get_logger


class LoggerTest:
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)

    def main(self):
        self.logger.debug("Hello World")
        self.logger.info("Hello World")
        self.logger.step("Hello World")


def main():
    logger = build_logger(
        project_name="Logger Project Test",
        log_level=logging.DEBUG,
        log_file=True,
        # extra={'user': 'test_user'}
    )

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.step("This is a step message.")
    logger.warning("This is a warning message.")

    try:
        _ = 1 / 0
    except ZeroDivisionError:
        logger.exception("This is an exception message.")

    logger.critical("This is a critical message.")

    logger_test = LoggerTest()
    logger_test.main()


if __name__ == "__main__":
    main()
