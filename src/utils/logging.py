"""Unified logging configuration using rich for pretty terminal output."""

from __future__ import annotations

import logging
import sys
from pathlib import Path

from rich.logging import RichHandler


def setup_logging(
    level: str = "INFO",
    log_file: Path | str | None = None,
    rich_console: bool = True,
) -> logging.Logger:
    """Set up project-wide logging.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        log_file: Optional path to a log file. Logs go there as plain text.
        rich_console: If True, use RichHandler for pretty colored output.
            If False, use standard StreamHandler.

    Returns:
        The configured root logger.
    """
    handlers: list[logging.Handler] = []

    if rich_console:
        handlers.append(
            RichHandler(
                rich_tracebacks=True,
                tracebacks_show_locals=False,
                show_time=True,
                show_path=False,
            )
        )
    else:
        stream = logging.StreamHandler(sys.stdout)
        stream.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )
        handlers.append(stream)

    if log_file is not None:
        log_file = Path(log_file)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )
        handlers.append(file_handler)

    logging.basicConfig(
        level=level.upper(),
        handlers=handlers,
        format="%(message)s",
        force=True,  # override any prior config
    )

    # Tame verbose libraries
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("filelock").setLevel(logging.WARNING)

    return logging.getLogger()


def get_logger(name: str) -> logging.Logger:
    """Get a named logger. Use module-level: `logger = get_logger(__name__)`."""
    return logging.getLogger(name)
