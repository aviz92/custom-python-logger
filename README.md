# custom-python-logger
A powerful and flexible Python logger with colored output, custom log levels, and advanced configuration options. <br>
Easily integrate structured, readable, and context-rich logging into your Python projects for better debugging and monitoring.

---

## 🚀 Features
- ✅ **Colored Output**: Beautiful, readable logs in your terminal using `colorlog`.
- ✅ **Custom Log Levels**: Includes `STEP` (for process steps) and `EXCEPTION` (for exception tracking) in addition to standard levels.
- ✅ **Flexible Output**: Log to console, file, or both. Supports custom log file paths and automatic log directory creation.
- ✅ **Contextual Logging**: Add extra fields (like user, environment, etc.) to every log message.
- ✅ **UTC Support**: Optionally log timestamps in UTC for consistency across environments.
- ✅ **Pretty Formatting**: Built-in helpers for pretty-printing JSON and YAML data in logs.
- ✅ **Easy Integration**: Simple API for getting a ready-to-use logger anywhere in your codebase.

---

## 📦 Installation
```bash
pip install custom-python-logger
```

---

### 🔧 Usage
Here's a quick example of how to use `custom-python-logger` in your project:

```python
import logging
from custom_python_logger import build_logger, CustomLoggerAdapter

logger: CustomLoggerAdapter = build_logger(
    project_name='Logger Project Test',
    log_level=logging.DEBUG,
    log_file=True,
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
```

#### Advanced Usage
- Log to a file:
  ```python
  from custom_python_logger import build_logger

  logger = build_logger(project_name='MyApp', log_file=True)
  ```

- Use UTC timestamps:
  ```python
  from custom_python_logger import build_logger

  logger = build_logger(project_name='MyApp', log_file=True, utc=True)
  ```

- Add extra context:
  ```python
  from custom_python_logger import build_logger

  logger = build_logger(project_name='MyApp', log_file=True, utc=True, extra={'user': 'alice'})
  ```

- Pretty-print JSON or YAML:
  ```python
  from custom_python_logger import build_logger, json_pretty_format, yaml_pretty_format

  logger = build_logger(project_name='MyApp', utc=True, log_file=True)

  logger.info(json_pretty_format({'foo': 'bar'}))
  logger.info(yaml_pretty_format({'foo': 'bar'}))
  ```

- use an existing logger (CustomLoggerAdapter) and set a custom name:
  ```python
  from custom_python_logger import get_logger

  logger = get_logger('some-name')

logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.step("This is a step message.")
  ```

---

## 🤝 Contributing
If you have a helpful tool, pattern, or improvement to suggest:
Fork the repo <br>
Create a new branch <br>
Submit a pull request <br>
I welcome additions that promote clean, productive, and maintainable development. <br>

---

## 📄 License
MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Thanks
Thanks for exploring this repository! <br>
Happy coding! <br>
