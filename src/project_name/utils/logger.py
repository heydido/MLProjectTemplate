"""
This module provides a utility function to set up and configure a logger for the project.
"""

import logging
import os
from datetime import datetime
from typing import Optional

from src.project_name.constants import PROJECT_ROOT


def get_logger(name: Optional[str] = "root") -> logging.Logger:
    """
    Sets up and returns a logger with the specified name. If no name is provided, the root logger is used.

    Args:
        name (Optional[str]): The name of the logger. Defaults to "root".

    Returns:
        logging.Logger: Configured logger instance.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logs_path = os.path.join(PROJECT_ROOT, "logs", today)
    os.makedirs(logs_path, exist_ok=True)

    log_file_path = os.path.join(logs_path, log_file)

    # Create formatter
    formatter = logging.Formatter(
        "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
    )

    # Create file handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(formatter)

    # Create stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Get logger by name
    logger = logging.getLogger(name)

    # Set logger level
    logger.setLevel(logging.DEBUG)

    # Add handlers to the logger
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger
