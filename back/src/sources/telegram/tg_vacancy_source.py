import uuid

from sources.telegram.tg_app import TgApp
from details.utils import loggers


class TgVacancySource:
    def __init__(self, tg_config):
        self.chat_id = None
        self.vacancy_validator = None
        self.tg_app = TgApp(tg_config)

    def get_vacancies(self):
        chat_msgs = self.tg_app.fetch_new_messages(self.chat_id)
        vacancies = [self.__to_vacancy(msg) for msg in chat_msgs if self.__is_message_valid(msg)]
        valid_vacancies = []
        for vacancy in vacancies:
            if self.vacancy_validator.is_valid(vacancy):
                valid_vacancies.append(vacancy)
            else:
                loggers.report_logger.info(f'НЕ ВАЛИДНАЯ ВАКАНСИЯ: {vacancy["text"]}')
        return valid_vacancies

    def __to_vacancy(self, msg):
        return {
            'text':msg.text,
            'timestamp':int(msg.date.timestamp()),
            'user_id':str(msg.from_user.id) if msg.from_user else "Unknown",
            'source': f'telegram:{self.chat_id}',
            'id':str(uuid.uuid4()),
        }

    def __is_message_valid(self, api_msg):
        return api_msg.text != None
