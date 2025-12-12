import json
import fcntl
from pathlib import Path

from business.exceptions.exceptions import VacancyNotFoundException
from details.utils import settings as s
from details.utils.matcher import Matcher
from details.utils import loggers

class FileVacancyRepository:
    def __init__(self):
        base = Path(s.path_to_database)
        base.mkdir(parents=True, exist_ok=True)
        for fname in ('unparsed_vacancies.json', 'parsed_vacancies.json', 'invalid_vacancies.json'):
            path = base / fname
            if not path.exists():
                self.__write_json_locked(path, [])

    def insert_one_unparsed(self, vacancy):
        path = Path(s.path_to_database) / 'unparsed_vacancies.json'
        self.__modify_json_locked(path, lambda v: v.append(vacancy))

    def insert_one_parsed(self, vacancy):
        path = Path(s.path_to_database) / 'parsed_vacancies.json'
        self.__modify_json_locked(path, lambda v: v.append(vacancy))
        loggers.logger.info(f'Загрузил вакансию {vacancy['id']} в хранилище спаршенных вакансий')

    def insert_many_unparsed(self, vacancies):
        path = Path(s.path_to_database) / 'unparsed_vacancies.json'
        self.__modify_json_locked(path, lambda v: v.extend(vacancies))
        loggers.logger.info(f'Загрузил {len(vacancies)} вакансий в файловое хранилище неспаршенных вакансий')

    def insert_many_parsed(self, vacancies):
        path = Path(s.path_to_database) / 'parsed_vacancies.json'
        self.__modify_json_locked(path, lambda v: v.extend(vacancies))

    def insert_many_invalid(self, vacancies):
        path = Path(s.path_to_database) / 'invalid_vacancies.json'
        self.__modify_json_locked(path, lambda v: v.extend(vacancies))

    def find_all_unparsed(self):
        return self.__read_json_locked(Path(s.path_to_database) / 'unparsed_vacancies.json')

    def find_all_parsed(self):
        return self.__read_json_locked(Path(s.path_to_database) / 'parsed_vacancies.json')

    def update_unparsed_vacancy_status(self, vacancy_id, status):
        path = Path(s.path_to_database) / 'unparsed_vacancies.json'
        def modifier(vacancies):
            for v in vacancies:
                if v['id'] == vacancy_id:
                    v['status'] = status
        self.__modify_json_locked(path, modifier)

    def update_parsed_vacancy_status(self, vacancy_id, status):
        path = Path(s.path_to_database) / 'parsed_vacancies.json'
        def modifier(vacancies):
            for v in vacancies:
                if v['id'] == vacancy_id:
                    v['status'] = status
        self.__modify_json_locked(path, modifier)

    def find_parsed_by_id(self, vacancy_id):
        return next((v for v in self.find_all_parsed() if v['id'] == vacancy_id), None)

    def find_parsed_by_search_query(self, search_query):
        return [v for v in self.find_all_parsed() if Matcher.is_matches_search_query(v, search_query)]

    def find_all_unparsed_with_status(self, status):
        return [v for v in self.find_all_unparsed() if v['status'] == status]

    def find_all_parsed_with_status(self, status):
        return [v for v in self.find_all_parsed() if v['status'] == status]

    def find_one_unparsed_for_processing(self):
        path = Path(s.path_to_database) / 'unparsed_vacancies.json'
        vacancy = None

        def modifier(vacancies):
            nonlocal vacancy
            for v in vacancies:
                if v.get("status") == 'unparsed':
                    v["status"] = "processing"
                    vacancy = v
                    break
        self.__modify_json_locked(path, modifier)
        if vacancy == None:
            raise VacancyNotFoundException('Не найдено вакансии со статусом processing')
        return vacancy

    def save_data_to_file(self, data, path):
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        self.__write_json_locked(p, data)

    def __read_json_locked(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_SH)
            data = json.load(f)
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
        return data

    def __write_json_locked(self, path, data):
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.flush()
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)

    def __modify_json_locked(self, path, modifier):
        with open(path, 'r+', encoding='utf-8', newline='\n') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            data = json.load(f)
            modifier(data)
            f.seek(0)
            f.truncate()
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.flush()
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)