import os
import logging
from datetime import datetime
from src.project_name.constants import PROJECT_ROOT


TODAY = datetime.now().strftime('%Y-%m-%d')
LOG_FILE = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logs_path = os.path.join(PROJECT_ROOT, "logs", TODAY)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Create formatter
formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")

# Create file handler
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setFormatter(formatter)

# Create stream handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Get root logger
logger = logging.getLogger()

# Set logger level
logger.setLevel(logging.DEBUG)

# Add handlers to the logger
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)


if __name__ == '__main__':
    logging.info('Logging has started!')
