from tests.helpers.mocks.spy_message import SpyMessage
from vacancy.usecases.save_chat_command import SaveChatCommand

class TestSaveChatCommand:
    def setup_method(self):
        self.cmd = SaveChatCommand()

    def teardown_method(self):
        self.cmd.chat.tg_chat.stop()

    def test_execute(self):
        message = SpyMessage()
        self.cmd.message = message

        self.cmd.execute()

        assert len(message.saved) != 0