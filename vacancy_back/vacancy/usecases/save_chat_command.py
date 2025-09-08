from vacancy.sources.chat import Chat

from vacancy.usecases.repository.file_message import FileMessage


class SaveChatCommand:
    def __init__(self):
        self.chat = Chat()
        self.message = FileMessage

    def execute(self):
        channel_id = 'telegram:@myjobit'
        id = self.__get_last_saved_msg_id(channel_id)
        messages = self.chat.get_messages_after_message({'message_id':id, 'channel_id':channel_id})
        for msg in messages:
            msg.status = "pending"
        self.message.save_many(messages)

    def __get_last_saved_msg_id(self, channel_id):
        id = self.message.get_latest_id_from_channel(channel_id)
        if id == None:
            if channel_id == "telegram:@myjobit":
                id = 119188
        return id