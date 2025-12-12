class ChangeVacancyStatusCommand:
    def __init__(self):
        self.vacancy_repository = None
        self.authorizer = None

    def execute(self, vacancy_id, status, token):
        self.authorizer.check_is_token_exists(token)
        self.vacancy_repository.update_parsed_vacancy_status(vacancy_id, status)