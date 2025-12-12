from details.utils.matcher import Matcher


class InMemoryVacancyRepository:
    def __init__(self):
        self.unparsed_vacancies = []
        self.parsed_vacancies = []
        self.invalid_vacancies = []

    def find_all_unparsed(self):
        return self.unparsed_vacancies

    def find_all_parsed(self):
        return self.parsed_vacancies

    def find_parsed_by_search_query(self, search_query):
        return [vacancy for vacancy in self.parsed_vacancies if Matcher.is_matches_search_query(vacancy, search_query)]

    def insert_many_parsed(self, vacancies):
        self.parsed_vacancies.extend(vacancies)

    def insert_many_unparsed(self, vacancies):
        self.unparsed_vacancies.extend(vacancies)

    def insert_many_invalid(self, vacancies):
        self.invalid_vacancies.extend(vacancies)

    def insert_one_parsed(self, vacancy):
        self.parsed_vacancies.append(vacancy)
        
    def update_unparsed_vacancy_status(self, vacancy_id, status):
        for vacancy in self.unparsed_vacancies:
            if vacancy['id'] == vacancy_id:
                vacancy['status'] = status

    def update_parsed_vacancy_status(self, vacancy_id, status):
        for vacancy in self.parsed_vacancies:
            if vacancy['id'] == vacancy_id:
                vacancy['status'] = status
                
    def find_all_unparsed_with_status(self, status):
        return [vacancy for vacancy in self.unparsed_vacancies if vacancy['status'] == status]


    def find_parsed_by_id(self, vacancy_id):
        for vacancy in self.parsed_vacancies:
            if vacancy['id'] == vacancy_id:
                return vacancy
        return None

    def find_one_unparsed_for_processing(self):
        for vacancy in self.unparsed_vacancies:
            if vacancy['status'] == 'unparsed':
                vacancy['status'] = 'processing'
                return vacancy
        return None
