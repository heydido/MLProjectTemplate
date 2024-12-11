import sys
from functools import wraps

from src.project_name.logger import logging
from src.project_name.exception import CustomException


def exception_handler(func: callable) -> callable:
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
            raise CustomException(e, sys)
    return wrapper


def log_handler(func: callable) -> callable:
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
        logging.info(f"Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' executed successfully!")
        return result
    return wrapper


if __name__ == "__main__":
    @log_handler
    @exception_handler
    def division(x, y):
        return x / y

    print(division(10, 2))
    print(division(10, 0))
