class StubVacancyParser:
    def parse_many(self, vacancies):
        return [
            {'languages': ['Python']}
        ]

    def parse_one(self, vacancy):
        return {'languages': ['Python']}

    def generate_cover_latter(self, vacancy, resume):
        return 'StubCoverLatter'