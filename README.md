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
from custom_python_logger.logger import get_logger, CustomLoggerAdapter

logger: CustomLoggerAdapter = CustomLoggerAdapter(logging.getLogger(__name__))


def main():
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
    _ = get_logger(
        project_name='Logger Project Test',
        log_level=logging.DEBUG,
        extra={'user': 'test_user'}
    )

    main()
```

---

## 🤝 Contributing
If you have a helpful tool, pattern, or improvement to suggest:
Fork the repo <br>
Create a new branch <br>
Submit a pull request <br>
I welcome additions that promote clean, productive, and maintainable development. <br>

---

## 🙏 Thanks
Thanks for exploring this repository! <br>
Happy coding! <br>
