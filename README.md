![PyPI version](https://img.shields.io/pypi/v/custom-python-logger)
![Python](https://img.shields.io/badge/python->=3.12-blue)
![Development Status](https://img.shields.io/badge/status-stable-green)
![Maintenance](https://img.shields.io/maintenance/yes/2026)
![PyPI](https://img.shields.io/pypi/dm/custom-python-logger)
![License](https://img.shields.io/pypi/l/custom-python-logger)

---

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
- ✅ **Short Path Display**: Automatically trims log file paths to project-relative or `.venv`-relative format for cleaner output.
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

- Use an existing logger with a custom name:
  ```python
  from custom_python_logger import get_logger

  logger = get_logger('some-name')

  logger.debug("This is a debug message.")
  logger.info("This is an info message.")
  logger.step("This is a step message.")
  ```

- Use a custom log format:
  ```python
  from custom_python_logger import build_logger, LOG_FORMAT_FILENAME, LOG_FORMAT_SHORTPATH

  # Default — shows project-relative or .venv-relative path:
  # 2026-05-18 | INFO      | l.20 | my_app | my_project/app/main.py:42 | message
  logger = build_logger(project_name='MyApp', log_format=LOG_FORMAT_SHORTPATH)

  # Classic — shows filename only (no path):
  # 2026-05-18 | INFO      | l.20 | my_app | main.py:42 | message
  logger = build_logger(project_name='MyApp', log_format=LOG_FORMAT_FILENAME)
  ```

---

## 🗂️ Short Path Display

By default, `build_logger` uses `LOG_FORMAT_SHORTPATH`, which trims the file path in every log line:

| Path type | Raw `record.pathname` | Displayed as |
|---|---|---|
| Project file | `/home/user/my_project/app/main.py` | `my_project/app/main.py` |
| Dependency in `.venv` | `/home/user/my_project/.venv/lib/python3.13/site-packages/urllib3/pool.py` | `.venv/lib/python3.13/site-packages/urllib3/pool.py` |
| Unrecognised path | `/tmp/some_script.py` | `/tmp/some_script.py` (full path) |

### Setting your project name

The short-path logic uses the `PROJECT_NAME` environment variable to identify your project root.
Set it in your `.env` file (loaded automatically on import) or export it before running:

```bash
# .env
PROJECT_NAME=my_project
```

```bash
# or inline
PROJECT_NAME=my_project python main.py
```

> **Note:** `custom-python-logger` calls `load_dotenv()` on import, which reads your `.env` file automatically.
> If you set `PROJECT_NAME` programmatically, do so **before** importing `custom_python_logger` to ensure it takes effect.

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
