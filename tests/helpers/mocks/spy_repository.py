from types import SimpleNamespace as DTO

class SpyRepository:
    def __init__(self):
        self.msgs = []

    def save_many_messages(self, messages):
        self.saved_msgs = messages

    def save_many_vacancies(self, vacancies):
        self.saved_vacancies = vacancies

    def get_latest_message_id_from_channel(self, channel_id):
        return 119188

    def get_messages_with_status(self, status):
        return self.msgs