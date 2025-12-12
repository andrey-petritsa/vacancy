import json
import os
from pathlib import Path

from details.utils.pathes import get_out_dir
from details.utils.serializer import to_dict, to_dto


class FileMessage:
    def __init__(self, msg_dto):
        self.msg_dto = msg_dto

    def save(self):
        path = self.__get_path_to_file()
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        existing = {m.id: m for m in self.get_all()}
        existing[self.msg_dto.id] = self.msg_dto
        with open(path, "w", encoding="utf-8") as f:
            for m in existing.values():
                data = to_dict(m)
                f.write(json.dumps(data, ensure_ascii=False) + "\n")

    @classmethod
    def save_many(cls, msgs):
        path = cls.__get_path_to_file()
        Path(path).parent.mkdir(parents=True, exist_ok=True)

        e_msgs = {m.id: m for m in cls.get_all()}
        e_msgs.update({m.id: m for m in msgs})

        with open(path, "w", encoding="utf-8") as f:
            f.writelines(
                json.dumps(to_dict(m), ensure_ascii=False) + "\n"
                    for m in e_msgs.values()
            )

    @classmethod
    def find(cls, id):
        for msg in cls.get_all():
            if msg.id == id:
                return msg
        return None

    @classmethod
    def get_all(cls):
        path = cls.__get_path_to_file()
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            return [to_dto(json.loads(line)) for line in f]

    @classmethod
    def get_all_from_channel(cls, channel_id):
        msgs = []
        for m in cls.get_all():
            parts = m.id.split(":")
            m_channel_id = parts[1] + ":" + parts[2]
            if m_channel_id == channel_id:
                msgs.append(m)
        return msgs

    @classmethod
    def get_latest_id_from_channel(cls, channel_id):
        msgs = cls.get_all_from_channel(channel_id)
        if len(msgs) == 0:
            return None
        latest_msg = msgs[-1]
        parts = latest_msg.id.split(":")
        return int(parts[0])

    @classmethod
    def get_only_pending_status(cls):
        return [m for m in cls.get_all() if getattr(m, "status", None) == "pending"]

    def get_channel_id(self):
        parts = self.msg_dto.id.split(":")
        return parts[1] + ":" + parts[2]

    @classmethod
    def __get_path_to_file(cls):
        return f"{get_out_dir()}/messages.jsonl"