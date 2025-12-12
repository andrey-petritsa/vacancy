class InMemoryVacancySource:
    def __init__(self):
        self.vacancies = []

    def get_vacancies(self):
        return self.vacancies