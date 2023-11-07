import logging
import os
from logging.handlers import RotatingFileHandler

import click
from rich.logging import RichHandler


class RemoveColorFilter(logging.Filter):
    """
    A custom logging filter to remove color codes from log messages.

    This filter is designed to be used with the Python logging package. It removes
    color codes from log messages to ensure that log entries are displayed in a
    color-free format, making them more suitable for log files and Rich-text console.

    Note:
    - To use this filter, you should attach it to a logger by calling
    `logger.addFilter(RemoveColorFilter())`.
    - It is especially useful when combined with loggers that use color-coded output
    formatting. In this case, the Flask logger by default.
    """

    def filter(self, record: logging.LogRecord):
        """
        Filters log records by removing color codes from log messages.

        This method processes the log record by removing color codes from the log
        message, if any are present. The filtered log record is then passed along
        the logging chain for further processing and output.

        Args:
            record (logging.LogRecord): The log record to be filtered.

        Returns:
            bool: Always returns True, indicating that the log record is accepted.
        """

        if record and record.msg and isinstance(record.msg, str):
            record.msg = click.unstyle(record.msg)
        return True


def setup_logging_system():
    """
    Configures the logging system for the application.

    This function sets up the logging system for the API, allowing log messages
    to be recorded to a log file and displayed on the console.
    """
    log_folder = "log"

    if not os.path.exists(log_folder):
        os.mkdir(log_folder)

    # log format
    formatter = logging.Formatter(
        fmt="[%(asctime)s] %(levelname)s\t%(module)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    max_log_size = 2 * (1024**2)
    debug_log_path = os.path.join(log_folder, "debug.log")
    exception_log_path = os.path.join(log_folder, "exception.log")

    remove_color_filter = RemoveColorFilter()

    console_handler = RichHandler(level=logging.DEBUG)
    console_handler.setFormatter(formatter)
    console_handler.addFilter(remove_color_filter)

    debug_handler = RotatingFileHandler(
        debug_log_path, maxBytes=max_log_size, backupCount=5
    )
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)
    debug_handler.addFilter(remove_color_filter)

    exception_handler = RotatingFileHandler(
        exception_log_path, maxBytes=max_log_size, backupCount=5
    )
    exception_handler.setLevel(logging.ERROR)
    exception_handler.setFormatter(formatter)
    exception_handler.addFilter(remove_color_filter)

    root_logger = logging.getLogger()

    root_logger.addHandler(console_handler)
    root_logger.addHandler(debug_handler)
    root_logger.addHandler(exception_handler)
