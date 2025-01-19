"""
This module provides utility functions to set up and configure a logger for the project.
"""

import json
import logging.config
import logging.handlers
import os
from datetime import datetime
from pathlib import Path

from src.project_name.constants import PROJECT_ROOT


def setup_logging():
    """
    Sets up logging configuration from a JSON file and creates log directories and files.

    This function reads the logging configuration from 'config/logging.json', sets up the log file path
    based on the current date and time, and configures the logging system using the loaded configuration.
    """

    # Load logging configuration from the JSON file
    config_file = Path(PROJECT_ROOT / "config/logging.json")
    with open(str(config_file)) as f_in:
        config = json.load(f_in)

    # Setup log file name based on the current date and time
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    # Create log directories if they don't exist
    logs_path = os.path.join(PROJECT_ROOT, "logs", today)
    os.makedirs(logs_path, exist_ok=True)

    # Update log file path in the configuration
    log_file_path = os.path.join(logs_path, log_file)
    config["handlers"]["file"]["filename"] = log_file_path

    logging.config.dictConfig(config)


def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger with the specified name after setting up the logging configuration.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: Configured logger instance.
    """
    setup_logging()
    return logging.getLogger(name)
