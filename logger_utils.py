"""Utility module for setting up consistent logging across the application."""
import logging
from datetime import datetime

def get_logger(name):
    """Initializes and returns a logger instance with file and console handlers."""
    log_filename = f"broadcast_{datetime.now().strftime('%Y%m%d')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(name)
