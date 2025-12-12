from business.usecases.change_vacancy_status_command import ChangeVacancyStatusCommand
from helpers.mocks.in_memory_vacancy_repository import InMemoryVacancyRepository
from helpers.mocks.stub_authorizer import StubAuthorizer


class TestChangeVacancyStatusCommand:
    def test_execute(self):
        cmd = ChangeVacancyStatusCommand()
        cmd.vacancy_repository = InMemoryVacancyRepository()
        cmd.vacancy_repository.parsed_vacancies = [{'id': 1}]
        cmd.authorizer = StubAuthorizer()

        cmd.execute(vacancy_id=1, status='like', token='stub')

        assert cmd.vacancy_repository.find_parsed_by_id(1)['status'] == 'like'