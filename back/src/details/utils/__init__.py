from types import SimpleNamespace
DTO = SimpleNamespace
from details.utils.console_logger import ConsoleLogger

logger = ConsoleLogger()

from types import SimpleNamespace

def to_dtos(data):
    return [SimpleNamespace(**d) for d in data]
