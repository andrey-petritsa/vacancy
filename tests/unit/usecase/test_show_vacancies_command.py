from business.usecases.show_vacancies_command import ShowVacanciesCommand
from helpers.mocks.in_memory_vacancy_repository import InMemoryVacancyRepository
from helpers.mocks.stub_authorizer import StubAuthorizer


class TestShowVacanciesCommand:
    def test_execute(self):
        cmd = ShowVacanciesCommand()
        cmd.vacancy_repository = InMemoryVacancyRepository()
        cmd.vacancy_repository.parsed_vacancies = [{'languages': ['Python'], 'status': 'unseen'}]
        cmd.authorizer = StubAuthorizer()

        search_query = {'status': 'unseen', 'language': 'Python'}
        vacancies = cmd.execute(search_query, 'stub-token')

        assert len(vacancies) != 0