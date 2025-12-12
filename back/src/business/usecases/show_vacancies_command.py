class ShowVacanciesCommand:
    def __init__(self):
        self.vacancy_repository = None
        self.authorizer = None

    def execute(self, search_query, token):
        self.authorizer.check_is_token_exists(token)
        return self.vacancy_repository.find_parsed_by_search_query(search_query)