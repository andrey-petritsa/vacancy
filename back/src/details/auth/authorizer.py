class Authorizer:
    def __init__(self):
        self.user_repository = None

    def check_is_token_exists(self, token):
        self.user_repository.find_by_token(token)