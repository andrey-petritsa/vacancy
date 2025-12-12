from dotenv import dotenv_values

from details.utils.settings import path_to_secrets
from helpers.mocks.stub_vacancy_validator import StubVacancyValidator
from helpers.system_test import SystemTest
from sources.telegram.tg_vacancy_source import TgVacancySource


class TestTgVacancySource(SystemTest):
    def test_source(self):
        tg_config = dotenv_values(f"{path_to_secrets}/.tg_config.env")
        source = TgVacancySource(tg_config)
        source.vacancy_validator = StubVacancyValidator()
        source.chat_id = "@myjobit"

        vacancies = source.get_vacancies()

        assert len(vacancies) != 0