"""
This module provides decorators for handling exceptions, logging function calls, and measuring execution time.
"""

import sys
from functools import wraps
from time import perf_counter
from typing import Callable

from src.project_name.utils.exception import CustomException
from src.project_name.utils.logger import get_logger

logging = get_logger()


def exception_handler(func: Callable) -> Callable:
    """
    This function is used to handle exceptions. It wraps the function and catches any exception raised by the function.
    To be used as a decorator.

    Args:
        func: Function to be wrapped.

    Returns:
        callable: Wrapped function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise CustomException(e, sys) from e

    return wrapper


def log_handler(func: Callable) -> Callable:
    """
    This function is used to log the function name, arguments and keyword arguments before and after the function is
    executed.
    To be used as a decorator.

    Args:
        func: Function to be wrapped.

    Returns:
        callable: Wrapped function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(
            f"Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}"
        )
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' executed successfully!")
        return result

    return wrapper


def get_time(func: Callable) -> Callable:
    """
    This function is used to calculate the time taken by the function to execute.
    To be used as a decorator.

    Args:
        func: Function to be wrapped.

    Returns:
        callable: Wrapped function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        end_time = perf_counter()
        logging.info(
            f"Function '{func.__name__}' took {round(end_time - start_time, 2)} seconds to execute."
        )

    return wrapper
