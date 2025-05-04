# Custom Logger
A Python logger with colored output and additional log levels. <br> 
The logger supports custom log levels like `STEP` and `EXCEPTION` and can be easily integrated into your Python projects.

## Installation
You can install the package using pip:
```bash
pip install custom-python-logger
```

## Usage
```python
import logging
from custom_python_logger.logger import get_logger

def main():
    logger = get_logger(
        project_name='Logger Project Test',
        log_level=logging.DEBUG,
        extra={'user': 'test_user'}
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


if __name__ == '__main__':
    main()
```
