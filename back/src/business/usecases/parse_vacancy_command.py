
class ParseVacancyCommand:
    def __init__(self):
        self.vacancy_parser = None
        self.vacancy_repository = None

    def execute(self):
        unparsed_vacancy = self.vacancy_repository.find_one_unparsed_for_processing()
        parsed_vacancy = self.vacancy_parser.parse_one(unparsed_vacancy)
        parsed_vacancy['status'] = 'unseen'
        self.vacancy_repository.insert_one_parsed(parsed_vacancy)
        self.vacancy_repository.update_unparsed_vacancy_status(unparsed_vacancy['id'], 'parsed')