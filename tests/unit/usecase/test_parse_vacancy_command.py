from business.usecases.parse_vacancy_command import ParseVacancyCommand
from helpers.mocks.in_memory_vacancy_repository import InMemoryVacancyRepository
from helpers.mocks.stub_vacancy_parser import StubVacancyParser


class TestParseVacancyCommand:
    def test_execute(self):
        cmd = ParseVacancyCommand()
        cmd.vacancy_repository = InMemoryVacancyRepository()
        cmd.vacancy_parser = StubVacancyParser()

        vacancy = {'id':'1', 'text':'Текст вакансии', 'status':'unparsed', 'timestamp':0, 'source': 'test'}
        cmd.vacancy_repository.unparsed_vacancies = [vacancy]

        cmd.execute()

        assert len(cmd.vacancy_repository.unparsed_vacancies) != 0