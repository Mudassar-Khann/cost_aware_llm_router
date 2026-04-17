import logging
from pathlib import Path


Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    filemode="a",
    encoding="utf-8",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
