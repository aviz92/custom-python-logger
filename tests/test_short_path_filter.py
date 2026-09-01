# pylint: disable=E1101  # LogRecord.shortpath is a dynamic attribute set by _ShortPathFilter
import logging
import os
import tempfile
from collections.abc import Generator
from unittest.mock import patch

import pytest

from custom_python_logger import build_logger
from custom_python_logger.logger import _ShortPathFilter


def _make_record(pathname: str, name: str = "custom_logger.test") -> logging.LogRecord:
    record = logging.LogRecord(
        name=name,
        level=logging.DEBUG,
        pathname=pathname,
        lineno=1,
        msg="test",
        args=(),
        exc_info=None,
    )
    record.pathname = pathname
    return record


@pytest.fixture
def temp_log_file() -> Generator[str]:  # pylint: disable=W0621
    with tempfile.NamedTemporaryFile(delete=False, suffix=".log") as f:
        yield f.name
    os.remove(f.name)


class TestShortPathFilterInit:
    def test_caches_project_name_from_env(self) -> None:
        with patch.dict(os.environ, {"PROJECT_NAME": "my_project"}):
            f = _ShortPathFilter()
        assert f._project_name == "my_project", f"Expected 'my_project', got {f._project_name}"  # pylint: disable=W0212

    def test_project_name_none_when_env_not_set(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            f = _ShortPathFilter()
        assert f._project_name is None, f"Expected None, got {f._project_name}"  # pylint: disable=W0212


class TestShortPathFilterLogic:
    def test_project_name_in_path_sets_relative_shortpath(self) -> None:
        with patch.dict(os.environ, {"PROJECT_NAME": "my_project"}):
            f = _ShortPathFilter()
        record = _make_record("/home/user/my_project/app/main.py")

        result = f.filter(record)

        assert result is True, "filter() must always return True"
        assert (
            record.shortpath == "my_project/app/main.py"
        ), (  # pylint: disable=E1101
            f"Expected 'my_project/app/main.py', got '{record.shortpath}'"  # pylint: disable=E1101
        )

    def test_project_name_not_in_path_falls_back_to_full_pathname(self) -> None:
        with patch.dict(os.environ, {"PROJECT_NAME": "my_project"}):
            f = _ShortPathFilter()
        record = _make_record("/home/user/other_project/app/main.py")

        f.filter(record)

        assert (
            record.shortpath == "/home/user/other_project/app/main.py"
        ), f"Expected full pathname, got '{record.shortpath}'"  # pylint: disable=E1101  # pylint: disable=E1101

    def test_no_project_name_env_falls_back_to_full_pathname(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            f = _ShortPathFilter()
        record = _make_record("/home/user/my_project/app/main.py")

        f.filter(record)

        assert (
            record.shortpath == "/home/user/my_project/app/main.py"
        ), f"Expected full pathname, got '{record.shortpath}'"  # pylint: disable=E1101  # pylint: disable=E1101

    def test_venv_in_path_sets_venv_relative_shortpath(self) -> None:
        with patch.dict(os.environ, {"PROJECT_NAME": "my_project"}):
            f = _ShortPathFilter()
        record = _make_record("/home/user/my_project/.venv/lib/python3.13/site-packages/urllib3/pool.py")

        f.filter(record)

        assert (
            record.shortpath == ".venv/lib/python3.13/site-packages/urllib3/pool.py"
        ), f"Expected .venv-relative path, got '{record.shortpath}'"  # pylint: disable=E1101  # pylint: disable=E1101

    def test_venv_takes_precedence_over_project_name(self) -> None:
        with patch.dict(os.environ, {"PROJECT_NAME": "my_project"}):
            f = _ShortPathFilter()
        record = _make_record("/home/user/my_project/.venv/lib/python3.13/site-packages/requests/api.py")

        f.filter(record)

        assert record.shortpath.startswith(
            ".venv/"
        ), f"Expected .venv-relative path, got '{record.shortpath}'"  # pylint: disable=E1101  # pylint: disable=E1101

    def test_filter_always_returns_true(self) -> None:
        with patch.dict(os.environ, {"PROJECT_NAME": "my_project"}):
            f = _ShortPathFilter()

        for pathname in (
            "/some/random/path.py",
            "/my_project/app.py",
            "/.venv/lib/pkg.py",
        ):
            record = _make_record(pathname)
            assert f.filter(record) is True, f"filter() returned False for '{pathname}'"

    def test_shortpath_always_set_on_record(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            f = _ShortPathFilter()
        record = _make_record("/any/path/file.py")

        f.filter(record)

        assert hasattr(record, "shortpath"), "shortpath attribute must always be set on the record"


class TestBuildLoggerFilterIntegration:
    def test_handler_has_short_path_filter_after_build(self) -> None:
        root_logger = logging.getLogger()
        build_logger(project_name="TestFilter", console_output=True)

        filter_types = [type(f) for h in root_logger.handlers for f in h.filters]
        assert _ShortPathFilter in filter_types, "Handlers must have _ShortPathFilter attached"

    def test_calling_build_logger_twice_does_not_stack_filters(self) -> None:
        build_logger(project_name="TestFilter", console_output=True)
        build_logger(project_name="TestFilter", console_output=True)

        root_logger = logging.getLogger()
        for handler in root_logger.handlers:
            short_path_filters = [f for f in handler.filters if isinstance(f, _ShortPathFilter)]
            assert (
                len(short_path_filters) == 1
            ), f"Expected exactly 1 _ShortPathFilter per handler, found {len(short_path_filters)}"

    def test_shortpath_set_on_logged_records(self, temp_log_file: str) -> None:  # pylint: disable=W0621
        with patch.dict(os.environ, {"PROJECT_NAME": "custom-python-logger"}):
            logger = build_logger(
                project_name="ShortPathTest",
                log_file=True,
                log_file_path=temp_log_file,
                console_output=False,
            )
            logger.info("shortpath test message")

        with open(temp_log_file) as f:
            content = f.read()

        assert "shortpath test message" in content, "Log message not found in file"
        assert "custom-python-logger/" in content, f"Expected project-relative path in log output, got:\n{content}"
