from vacancy.sources.telegram.tg_chat import TgChat


class TestTgChat:
    def setup_method(self):
        self.tg_chat = TgChat()
        self.channel_id = '@myjobit'

    def teardown_method(self):
        self.tg_chat.stop()

    def test_get_messages_after_message(self):
        request = {'channel_id': self.channel_id,'message_id': 119188}
        msgs = self.tg_chat.get_messages_after_message(request)
        assert len(msgs) != 0

    def test_get_recent_messages(self):
        amount = 100
        msgs = self.tg_chat.get_recent_messages(self.channel_id, amount)
        assert len(msgs) != 0