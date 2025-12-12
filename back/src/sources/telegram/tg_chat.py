import os

from pyrogram import Client
from details.utils import DTO
from sources.telegram.tg_api import TgApi


class TgChat:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.app = Client(name='tg_session', session_string=os.getenv("TG_SESSION"), api_id=os.getenv("TG_API_ID"), api_hash=os.getenv("TG_API_HASH"))
        self.app.start()
        self.tg_api = TgApi(self.app)

    def get_messages_newer_then(self, message_id):
        msgs = []
        api_msgs = self.tg_api.fetch_newer(message_id=message_id, channel_id=self.channel_id)
        for api_msg in api_msgs:
            msg = self.__convert_to_msg(api_msg)
            msgs.append(msg)
        return msgs

    def __convert_to_msg(self, msg):
        return DTO(
            id=f'{msg.id}:telegram:{self.channel_id}',
            user=DTO(
                name=msg.from_user.first_name if msg.from_user else "Unknown",
                id=str(msg.from_user.id) if msg.from_user else "Unknown"
            ),
            text=msg.text,
            date=int(msg.date.timestamp()),
            channel_id=self.channel_id
        )

    def __is_message_valid(self, api_msg):
        return api_msg.text != None

    def stop(self):
        self.app.stop()
