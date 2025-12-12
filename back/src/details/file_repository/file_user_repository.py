import json
from pathlib import Path
import fcntl

from business.exceptions.exceptions import UserNotFoundException
from details.utils import settings as s


class FileUserRepository:
    def __init__(self):
        path = self.__get_users_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            with open(path, 'w+', encoding='utf-8') as f:
                fcntl.flock(f.fileno(), fcntl.LOCK_EX)
                f.write('[]')
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)

    def find_all(self):
        path = self.__get_users_path()
        with open(path, 'r', encoding='utf-8') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            content = f.read()
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
        return json.loads(content or '[]')

    def find_by_token(self, token):
        user = next((u for u in self.find_all() if u.get('token') == token), None)
        if user == None:
            raise UserNotFoundException(f'Пользователь с токеном {token} не найден')
        return user

    def __get_users_path(self):
        return Path(f"{s.path_to_database}/users.json")
