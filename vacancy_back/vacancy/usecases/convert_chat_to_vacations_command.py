from vacancy.parser.deepseek.deepseek_vacansies_parser import DeepSeekVacanciesParser
from vacancy.usecases.repository.file_message import FileMessage
from vacancy.usecases.repository.file_vacancy import FileVacancy


class ConvertChatToVacanciesCommand:
    def __init__(self):
        self.vacancies_parser = DeepSeekVacanciesParser()
        self.vacancy = FileVacancy
        self.message = FileMessage

    def execute(self):
        msgs = self.message.get_only_pending_status()
        vacancies = self.vacancies_parser.msgs_to_vacancies(msgs)
        self.vacancy.save_many(vacancies)

        for msg in msgs:
            msg.status = 'done'
        self.message.save_many(msgs)