import sys
from functools import wraps

from src.MLProjectTemplate.logger import logging
from src.MLProjectTemplate.exception import CustomException


def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise CustomException(e, sys)
    return wrapper


def log_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} executed successfully!")
        return result
    return wrapper


if __name__ == "__main__":
    @log_handler
    @exception_handler
    def division(x, y):
        return x / y

    print(division(10, 2))
    print(division(10, 0))
