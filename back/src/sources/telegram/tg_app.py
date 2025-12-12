import time

from pyrogram import Client
from pathlib import Path
import json
from details.utils import loggers

from details.utils import settings as s
from . import config


class TgApp:
    def __init__(self, tg_config):
        self.app = Client(name='tg_session',
                     session_string=tg_config["TG_SESSION"],
                     api_id=tg_config["TG_API_ID"],
                     api_hash=tg_config["TG_API_HASH"])
        self.app.start()
        self.__get_last_known_ids_and_maybe_init_state()

    def __get_last_known_ids_and_maybe_init_state(self):
        base = Path(s.path_to_database)
        base.mkdir(parents=True, exist_ok=True)
        self.last_known_ids_path = base / 'tg_last_known_ids.json'
        if not self.last_known_ids_path.exists():
            self.last_known_ids_path.write_text("{}", encoding="utf-8")
        content = self.last_known_ids_path.read_text(encoding="utf-8")
        self.last_known_ids = json.loads(content) if content.strip() else {}

    def fetch_new_messages(self, chat_id):
        loggers.logger.info(f"Получаю сообщения из чата {chat_id}. Последнее ид сообщения из чата {self.last_known_ids.get(chat_id)}")
        new_messages = []
        offset_id = 0
        first_run = chat_id not in self.last_known_ids.keys()

        while True:
            chunk = list(self.app.get_chat_history(chat_id=chat_id, limit=config.limit, offset_id=offset_id))
            if not chunk:
                break

            if first_run:
                new_messages.extend(chunk)
                ids = [m.id for m in chunk]
                if ids:
                    self.last_known_ids[chat_id] = max(ids)
                    self.__save_last_know_ids()
                return new_messages
            if not first_run:
                for msg in chunk:
                    if msg.id > self.last_known_ids.get(chat_id, 0):
                        new_messages.append(msg)
                    else:
                        break

                if any(msg.id <= self.last_known_ids.get(chat_id, 0) for msg in chunk):
                    break

                offset_id = chunk[-1].id - 1
            time.sleep(5)

        if new_messages:
            self.last_known_ids[chat_id] = max(m.id for m in new_messages)
            self.__save_last_know_ids()
        return new_messages

    def __save_last_know_ids(self):
        self.last_known_ids_path.write_text(json.dumps(self.last_known_ids), encoding="utf-8")
