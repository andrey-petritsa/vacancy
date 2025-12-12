# details/utils/loggers.py
from loguru import logger as _logger
import sys
from pathlib import Path


def setup_loggers(file_path: str = "logs/app.log") -> None:
    _logger.remove()

    _logger.add(
        sys.stdout,
        level="INFO",
        format="<cyan>{time:YYYY-MM-DD HH:mm:ss.SSS}</cyan> "
               "<level>{level}</level> <magenta>{message}</magenta>",
        colorize=True,
        filter=lambda record: record["extra"].get("target") == "stdout",
    )

    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    _logger.add(
        file_path,
        level="INFO",
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} {level} {message}",
        rotation="1 day",
        retention="7 days",
        filter=lambda record: record["extra"].get("target") == "file",
    )


class StdoutLogger:
    def info(self, text: str) -> None:
        _logger.bind(target="stdout").info(text)


class FileLogger:
    def info(self, text: str) -> None:
        _logger.bind(target="file").info(text)


setup_loggers()
logger = StdoutLogger()
report_logger = FileLogger()