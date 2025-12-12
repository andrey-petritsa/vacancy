from business.exceptions.exceptions import UserNotFoundException


class StubAuthorizer:
    def __init__(self):
        self.is_throw_exception = False


    def check_is_token_exists(self, token):
        if self.is_throw_exception:
            raise UserNotFoundException()