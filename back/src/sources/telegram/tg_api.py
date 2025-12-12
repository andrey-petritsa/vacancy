import asyncio

from pyrogram import utils as pyrogram_utils, raw
import details.utils as utils

class TgApi:
    def __init__(self, app):
        self.app = app

    def fetch_newer(self, message_id, channel_id):
        msgs = []
        min_id = message_id
        peer = self.app.resolve_peer(channel_id)

        while True:
            limit = 100
            res = self.app.invoke(
                raw.functions.messages.GetHistory(
                    peer=peer,
                    offset_id=0,
                    offset_date=0,
                    add_offset=0,
                    limit=limit,
                    max_id=0,
                    min_id=min_id,
                    hash=0,
                )
            )
            api_msgs = asyncio.get_event_loop().run_until_complete(
                pyrogram_utils.parse_messages(self.app, res, replies=0)
            )
            utils.logger.log(f'Получаю сообщения из {channel_id} новее чем {min_id}. Получено {len(api_msgs)}')
            if not api_msgs:
                break

            msgs.extend(api_msgs)
            min_id = max(m.id for m in msgs)
        return msgs



    def fetch_latest(self, channel_id):
        limit = 100
        peer = self.app.resolve_peer(channel_id)

        res = self.app.invoke(
            raw.functions.messages.GetHistory(
                peer=peer,
                offset_id=0,
                offset_date=0,
                add_offset=0,
                limit=limit,
                max_id=0,
                min_id=0,
                hash=0,
            )
        )

        msgs = asyncio.get_event_loop().run_until_complete(
            pyrogram_utils.parse_messages(self.app, res, replies=0)
        )

        return msgs
