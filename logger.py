import logging
from pathlib import Path


def get_logger() -> logging.Logger:

    Path("logs").mkdir(exist_ok=True)


    logger = logging.getLogger("app")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)


    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )


    file_handler = logging.FileHandler(
        "logs/app.log",
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


    logger.propagate = False

    return logger
