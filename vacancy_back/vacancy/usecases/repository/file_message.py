import json
import os
import vacancy.utils as utils



class FileMessage:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        path = self.__get_path_to_file()
        existing = {m.id: m for m in self.get_all()}
        existing[self.id] = self
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(json.dumps(utils.to_dict(m), ensure_ascii=False) + "\n"for m in existing.values())

    @classmethod
    def save_many(cls, msgs):
        path = cls.__get_path_to_file()
        e_msgs = {m.id: m for m in cls.get_all()}
        e_msgs.update({m.id: m for m in msgs})
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(json.dumps(utils.to_dict(m), ensure_ascii=False) + "\n"for m in e_msgs.values())

    @classmethod
    def find(cls, id):
        for msg in cls.get_all():
            if msg.id == id:
                return msg
        return None

    @classmethod
    def get_all(cls):
        if not os.path.exists(cls.__get_path_to_file()):
            return []
        with open(cls.__get_path_to_file(), "r", encoding="utf-8") as f:
            return [cls(**json.loads(line)) for line in f]

    @classmethod
    def get_all_from_channel(cls, channel_id):
        msgs = []
        for m in cls.get_all():
            if m.get_channel_id() == channel_id:
                msgs.append(m)
        return msgs

    def get_channel_id(self):
        parts = self.id.split(":")
        m_channel_id = parts[1] + ':' + parts[2]
        return m_channel_id

    @classmethod
    def get_latest_id_from_channel(cls, channel_id):
        msgs = cls.get_all_from_channel(channel_id)
        if len(msgs) == 0:
            return None

        latest_msg = msgs[0]
        parts = latest_msg.id.split(":")
        id = parts[0]
        return int(id)

    @classmethod
    def get_only_pending_status(cls):
        return [m for m in cls.get_all() if m.status == "pending"]

    @classmethod
    def __get_path_to_file(cls):
        return f"{utils.artifacts_path}/messages.jsonl"