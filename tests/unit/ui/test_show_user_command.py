from business.usecases.show_user_command import ShowUserCommand
from helpers.mocks.in_memory_user_repository import InMemoryUserRepository


class TestShowUserCommand:
    def test_execute(self):
        cmd = ShowUserCommand()
        cmd.user_repository = InMemoryUserRepository()
        cmd.user_repository.users = [{'token': 'test', 'id': 'andry'}]

        user = cmd.execute(token='test')

        assert user['id'] == 'andry'