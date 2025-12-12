from details.file_repository.file_message import FileMessage
from details.file_repository.file_vacancy import FileVacancy


class FileRepository:
    def save_msg(self, msg):
        msg = FileMessage(msg)
        msg.save()

    def save_many_messages(self, messages):
        FileMessage.save_many(messages)

    def get_latest_message_id_from_channel(self, channel_id):
        return FileMessage.get_latest_id_from_channel(channel_id)

    def find_msg(self, msg_id):
        return FileMessage.find(msg_id)

    def get_all_msgs_from_channel(self, channel_id):
        return FileMessage.get_all_from_channel(channel_id)

    def get_all_msgs(self):
        return FileMessage.get_all()

    def save_many_vacancies(self, vacancies):
        FileVacancy.save_many(vacancies)

    def get_all_vacancies(self):
        return FileVacancy.get_all()

    def get_messages_with_status(self, status):
        return [m for m in self.get_all_msgs() if m.status == status]
