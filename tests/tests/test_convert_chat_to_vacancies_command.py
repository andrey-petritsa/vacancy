from tests.helpers.mocks.spy_message import SpyMessage
from tests.helpers.mocks.spy_vacancies_parser import SpyVacanciesParser
from tests.helpers.mocks.spy_vacancy import SpyVacancy
from vacancy.usecases.convert_chat_to_vacations_command import ConvertChatToVacanciesCommand


class TestConvertChatToVacanciesCommand():
    def setup_method(self):
        cmd = ConvertChatToVacanciesCommand()
        cmd.vacancy = SpyVacancy()
        cmd.message = SpyMessage()
        cmd.vacancies_parser = SpyVacanciesParser()

        self.cmd = cmd

    def assert_all_done(self, messages):
        for msg in messages:
            assert msg.status == 'done'

    def test_execute_saves_vacancies(self):
        self.cmd.execute()
        assert len(self.cmd.vacancy.saved) != 0

    def test_execute_change_msgs_status(self):
        self.cmd.execute()
        assert all(msg.status == 'done' for msg in self.cmd.message.saved)
