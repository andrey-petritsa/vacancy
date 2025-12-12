class GetVacanciesFromSourceCommand:
    def __init__(self):
        self.vacancy_repository = None
        self.vacancy_source = None

    def execute(self):
        vacancies = self.vacancy_source.get_vacancies()
        for v in vacancies:
            v['status'] = 'unparsed'
        self.vacancy_repository.insert_many_unparsed(vacancies)
