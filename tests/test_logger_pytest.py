import datetime
import logging
import os
import tempfile
import time

import pytest

from custom_python_logger import CustomLoggerAdapter, build_logger, json_pretty_format, yaml_pretty_format


@pytest.fixture
def temp_log_file():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        yield f.name
    os.remove(f.name)


def test_logger_creation():
    logger = build_logger(project_name="PytestTest")
    assert logger is not None
    assert isinstance(logger, CustomLoggerAdapter)
    assert hasattr(logger, "step")
    assert hasattr(logger, "exception")


def test_step_log(caplog):
    logger = build_logger(project_name="PytestTest", console_output=False)
    if not isinstance(logger, CustomLoggerAdapter):
        raise AssertionError("Logger is not a CustomLoggerAdapter")
    # Attach caplog.handler
    logging.getLogger().addHandler(caplog.handler)
    with caplog.at_level(logging.INFO):
        logger.step("Step message")
    assert any("Step message" in m for m in caplog.messages)
    assert any("STEP" in r.levelname for r in caplog.records)


def test_step_log_2(caplog):
    logger = build_logger(project_name="TestProject", console_output=False)
    if not isinstance(logger, CustomLoggerAdapter):
        raise AssertionError("Logger is not a CustomLoggerAdapter")
    logging.getLogger().addHandler(caplog.handler)
    with caplog.at_level(logging.INFO):
        logger.step("Testing step log")
    assert any("Testing step log" in m for m in caplog.messages)
    assert any("STEP" in r.levelname for r in caplog.records)


def test_exception_log(caplog):
    logger = build_logger(project_name="PytestTest", console_output=False)
    logging.getLogger().addHandler(caplog.handler)
    with caplog.at_level(logging.ERROR):
        try:
            raise RuntimeError("fail")
        except RuntimeError:
            logger.exception("Exception message")
    assert any("Exception message" in m for m in caplog.messages)
    assert any("EXCEPTION" in r.levelname for r in caplog.records)


def test_exception_log_2(caplog):
    logger = build_logger(project_name="TestProject", console_output=False)
    logging.getLogger().addHandler(caplog.handler)
    with caplog.at_level(logging.ERROR):
        try:
            raise ValueError("Test exception")
        except ValueError as e:
            logger.exception(f"Exception occurred: {e}")
    assert any("Exception occurred: Test exception" in m for m in caplog.messages)
    assert any("EXCEPTION" in r.levelname for r in caplog.records)


def test_log_to_file(temp_log_file):  # pylint: disable=W0621
    logger = build_logger(project_name="FileTest", log_file=True, log_file_path=temp_log_file)
    logger.info("File log message")
    time.sleep(0.1)
    with open(temp_log_file) as f:
        content = f.read()
    assert "File log message" in content


def test_utc_logging(temp_log_file):  # pylint: disable=W0621
    logger = build_logger(project_name="UTCTest", log_file=True, log_file_path=temp_log_file, utc=True)
    logger.info("UTC log message")
    time.sleep(0.1)
    with open(temp_log_file) as f:
        content = f.read()
    assert "UTC log message" in content
    # Check for a year in UTC (should be close to now)
    now_utc = datetime.datetime.now(tz=datetime.UTC).strftime("%Y")
    assert now_utc in content


def test_extra_context(caplog):
    logger = build_logger(project_name="ExtraTest", extra={"user": "pytest"}, console_output=False)
    logging.getLogger().addHandler(caplog.handler)
    with caplog.at_level(logging.INFO):
        logger.info("With extra")
    assert any("With extra" in m for m in caplog.messages)
    # The extra field is not in the default format, but test that logger works with extra


def test_json_pretty_format():
    data = {"a": 1, "b": 2}
    result = json_pretty_format(data)
    assert "{" in result and "a" in result and "b" in result


def test_yaml_pretty_format():
    data = {"a": 1, "b": 2}
    result = yaml_pretty_format(data)
    assert "a:" in result and "b:" in result
