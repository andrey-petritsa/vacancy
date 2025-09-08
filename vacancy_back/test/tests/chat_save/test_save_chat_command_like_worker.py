import os

from vacancy.usecases.save_chat_command import SaveChatCommand


class TestSaveChatCommand:
    def setup_method(self):
        self.cmd = SaveChatCommand()

    def teardown_method(self):
        self.cmd.chat.tg_chat.stop()

    def test_execute(self):
        self.cmd.execute()
        saved_msgs_1 = self.cmd.message.get_all_from_channel('telegram:@myjobit')

        self.cmd.execute()
        saved_msgs_2 = self.cmd.message.get_all_from_channel('telegram:@myjobit')

        assert len(saved_msgs_1) == len(saved_msgs_2)