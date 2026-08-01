"""
Application logger.
"""

import logging


def create_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s - %(message)s"
    )

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    logger.addHandler(console)

    return logger