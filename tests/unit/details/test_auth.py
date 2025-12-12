import pytest

from business.exceptions.exceptions import UserNotFoundException
from details.auth.authorizer import Authorizer
from helpers.mocks.in_memory_user_repository import InMemoryUserRepository


class TestAuth:
    def test_auth(self):
        auth = Authorizer()
        auth.user_repository = InMemoryUserRepository()
        auth.user_repository.users = [{'token': 'test123'}]

        with pytest.raises(UserNotFoundException):
            auth.check_is_token_exists('test456')
