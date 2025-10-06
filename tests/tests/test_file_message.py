from vacancy.main.app_setuper import init_directories
from vacancy.usecases.repository.file_message import FileMessage

from vacancy.utils import to_dtos


class TestFileMessage:
    def test_message(self):
        msg = FileMessage()
        msg.id = '1:telegram:@test'
        msg.text = "привет мир"
        msg.chat = 'telegram'
        msg.channel_id = "@test"
        msg.status = "pending"

        msg.save()

        msg = FileMessage.find("1:telegram:@test")
        assert msg.text == 'привет мир'

        msg.status = "done"
        msg.save()

        msg = FileMessage.find("1:telegram:@test")
        assert msg.status == 'done'

    def test_save_many(self):
        msgs = [{'id': '1:telegram:@test', 'text': '1'}, {'id': '2:telegram:@test', 'text': '2'}]
        FileMessage.save_many(to_dtos(msgs))
        assert FileMessage.find("1:telegram:@test").text == '1'
        assert FileMessage.find("2:telegram:@test").text == '2'

        msgs = [{'id': '1:telegram:@test', 'text': 'changed'}, {'id': '2:telegram:@test', 'text': '2'}]
        FileMessage.save_many(to_dtos(msgs))
        assert FileMessage.find("1:telegram:@test").text == 'changed'
        assert FileMessage.find("2:telegram:@test").text == '2'

    def test_get_latest_id_from_channel(self):
        msgs = [{'id': '2:telegram:@test', 'text': 'latest'}, {'id': '1:telegram:@test', 'text': 'oldest'}]
        FileMessage.save_many(to_dtos(msgs))

        assert FileMessage.get_latest_id_from_channel("telegram:@test") == 2
