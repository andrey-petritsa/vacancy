from business.exceptions.exceptions import UserNotFoundException


class InMemoryUserRepository:
    def __init__(self):
        self.users = []
    
    def find_by_token(self, token):
        user = next((user for user in self.users if user['token'] == token), None)
        if user == None:
            raise UserNotFoundException()
        return user
