from vacancy.sources.telegram.tg_chat import TgChat
from vacancy.utils import to_dtos


class Chat:
    def __init__(self):
        self.tg_chat = TgChat()

    def get_messages_after_message(self, request):
        channel_id = request['channel_id']
        message_id = request['message_id']
        parts = channel_id.split(':')

        chat_name = parts[0]
        channel_id = parts[1]

        if chat_name == 'telegram':
            messages = self.tg_chat.get_messages_after_message({'message_id':message_id, 'channel_id':channel_id})
            return to_dtos(messages)
