from copy import deepcopy

from details.utils import DTO

def to_dict(dto):
    if isinstance(dto, DTO):
        return {
            k: to_dict(v)
            for k, v in dto.__dict__.items()
            if not k.startswith("_")
        }

    if isinstance(dto, (str, int, float, bool, type(None), list, tuple, dict, set)):
        return deepcopy(dto)

    raise TypeError(f"to_dict() принимает только DTO или примитивные типы, но получен {type(dto).__name__}")

def to_dto(data):
    if isinstance(data, dict):
        return DTO(**{k: to_dto(v) for k, v in data.items()})
    elif isinstance(data, list):
        return [to_dto(v) for v in data]
    else:
        return data