import json
import os
import vacancy.utils as utils


class FileVacancy:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def save_many(cls, vacancies):
        path = cls.get_path_to_file()
        existing = {v.id: v for v in cls.get_all()}
        existing.update({v.id: v for v in vacancies})
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(json.dumps(v.__dict__, ensure_ascii=False) + "\n" for v in existing.values())

    @classmethod
    def get_all(cls):
        if not os.path.exists(cls.get_path_to_file()):
            return []
        with open(cls.get_path_to_file(), "r", encoding="utf-8") as f:
            return [cls(**json.loads(line)) for line in f]

    @classmethod
    def get_path_to_file(cls):
        return f"{utils.artifacts_path}/vacancies.jsonl"