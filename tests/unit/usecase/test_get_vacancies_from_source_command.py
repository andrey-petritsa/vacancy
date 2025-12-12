from helpers.mocks.in_memory_vacancy_repository import InMemoryVacancyRepository
from helpers.mocks.in_memory_vacancy_source import InMemoryVacancySource
from business.usecases.get_vacancies_from_source_command import GetVacanciesFromSourceCommand


class TestGetVacanciesFromSourceCommand:
    def test_execute(self):
        cmd = GetVacanciesFromSourceCommand()
        cmd.vacancy_source = InMemoryVacancySource()
        cmd.vacancy_repository = InMemoryVacancyRepository()

        cmd.vacancy_source.vacancies = [{'text': 'Текст вакансии'}]

        cmd.execute()

        assert len(cmd.vacancy_repository.unparsed_vacancies) > 0
