from vacancy.utils.console_logger import ConsoleLogger

artifacts_path = "artifacts"
logger = ConsoleLogger()

from types import SimpleNamespace
from typing import Any

def to_dtos(data):
    return [SimpleNamespace(**d) for d in data]

def to_dict(object):
    return {k: v for k, v in object.__dict__.items() if not k.startswith("_")}