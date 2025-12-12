from details.factory.app_factory import AppFactory
from helpers.system_test import SystemTest
from sources.telegram import config


class TestGetVacanciesFromTgSourceCommandToFile(SystemTest):
    def test_execute(self):
        config.limit = 1
        cmd = AppFactory.create_get_vacancies_from_source_command()
        cmd.execute()
        assert len(cmd.vacancy_repository.find_all_unparsed()) != 0