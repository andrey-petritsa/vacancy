class GenerateCoverLatterCommand:
    def __init__(self):
        self.vacancy_parser = None
        self.authorizer = None
        self.resume = None

    def execute(self, vacancy, token):
        self.authorizer.check_is_token_exists(token)
        return self.vacancy_parser.generate_cover_latter(vacancy, self.resume)