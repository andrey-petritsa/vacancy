import os
from datetime import datetime, timedelta

from pyrogram import Client

import vacancy.utils as utils
from secrets import secrets


class TgChat:
    def __init__(self):
        self.limit = 1000
        path_to_session = 'secrets/my_account'
        abs = os.path.abspath(path_to_session)
        self.app = Client(abs, api_id=secrets.tg_api_id, api_hash=secrets.tg_api_hash)
        self.app.start()

    def get_recent_messages(self, channel_id, amount):
        utils.logger.log(f'Получаю последние {amount} сообщений из {channel_id}')
        msgs = []

        api_msgs = self.app.get_chat_history(chat_id=channel_id, limit=amount)

        for api_msg in api_msgs:
            if self.__is_message_valid(api_msg):
                msgs.append(self.__convert_to_msg(api_msg, channel_id))
            else:
                utils.logger.log('Сообщение пришло без text')

        return msgs

    def get_messages_after_message(self, request):
        msgs = []
        offset_id = 0
        message_id_to_stop = request['message_id']

        while True:
            utils.logger.log(
                f'Получаю сообщение новее чем {request["message_id"]}'
                f' из {request["channel_id"]}.'
            )

            api_msgs = self.app.get_chat_history(
                chat_id=request['channel_id'],
                limit=self.limit,
                offset_id=offset_id
            )

            if not api_msgs:
                break

            for api_msg in api_msgs:
                msg = self.__convert_to_msg(api_msg, request['channel_id'])
                if api_msg.id == message_id_to_stop:
                    utils.logger.log(f"Получено {len(msgs)} сообщений из {request['channel_id']}")
                    return msgs
                msgs.append(msg)

            offset_id = msgs[-1]['id']
        return msgs

    def __convert_to_msg(self, msg, channel_id):
        return {
            'id':f'{msg.id}:telegram:{channel_id}',
            'user':{
                'name':msg.from_user.first_name if msg.from_user else "Unknown",
                'id':str(msg.from_user.id) if msg.from_user else "Unknown",

            },
            'text':msg.text,
            'date':int(msg.date.timestamp()),
            'channel_id':channel_id
        }

    def __get_past_date(self, days):
        month_ago = datetime.utcnow() - timedelta(days=days)
        timestamp = int(month_ago.timestamp())
        date = datetime.utcfromtimestamp(timestamp)
        return date

    def __is_message_valid(self, api_msg):
        return api_msg.text != None

    def stop(self):
        self.app.stop()
