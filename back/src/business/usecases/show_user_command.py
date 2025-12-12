class ShowUserCommand:
    def __init__(self):
        self.user_repository = None

    def execute(self, token):
        return self.user_repository.find_by_token(token)