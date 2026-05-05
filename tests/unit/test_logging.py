"""Tests for logging setup."""

import logging
from pathlib import Path

from src.utils.logging import get_logger, setup_logging


class TestSetupLogging:
    def test_returns_root_logger(self) -> None:
        logger = setup_logging(level="INFO", rich_console=False)
        assert logger is logging.getLogger()

    def test_respects_level(self) -> None:
        setup_logging(level="WARNING", rich_console=False)
        assert logging.getLogger().level == logging.WARNING

    def test_writes_to_file(self, tmp_path: Path) -> None:
        log_file = tmp_path / "test.log"
        logger = setup_logging(level="INFO", log_file=log_file, rich_console=False)
        logger.info("hello world")
        # Force flush
        for handler in logger.handlers:
            handler.flush()
        content = log_file.read_text(encoding="utf-8")
        assert "hello world" in content


class TestGetLogger:
    def test_returns_named_logger(self) -> None:
        logger = get_logger("my.module")
        assert logger.name == "my.module"
