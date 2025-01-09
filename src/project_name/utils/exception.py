"""
This module provides utility functions and classes for handling exceptions and logging error details.
"""

import sys
import traceback
from typing import Any

from src.project_name.utils.logger import get_logger

logging = get_logger()


def error_message_detail(error: Any, error_detail: Any) -> str:
    """
    Get detailed error message including file name, line number, and error message.

    Args:
        error (Any): The error caught by the base Exception class.
        error_detail (Any): System level details of the error.

    Returns:
        str: Formatted error message with details:
            1. File name where the error occurred.
            2. Line number where the error occurred.
            3. Error message.
    """
    _, _, exc_traceback = error_detail.exc_info()
    frame = traceback.extract_tb(exc_traceback)[-1]
    file_name, line_number = frame.filename, frame.lineno
    error_message = f"Error occurred in script: [{file_name}], line number: [{line_number}], error message: [{str(error)}]"

    return error_message


class CustomException(Exception):
    """
    Custom exception class to raise exceptions with detailed error messages.
    """

    def __init__(self, error_message: Any, error_detail: Any):
        """
        Initialize the CustomException class.

        Args:
            error_message (Any): Error message caught by the base Exception class.
            error_detail (Any): System level details of the error.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )
        logging.error(self.error_message)

    def __str__(self) -> str:
        """
        Return the error message.

        Returns:
            str: Error message.
        """
        return self.error_message
