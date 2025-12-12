from details.utils import loggers
from details.utils.text import short_text
from . import promts
from .deepseek_api import DeepseekApi
import time



class DeepseekVacanciesValidator:
    def __init__(self, token):
        self.__token = token

    def is_valid(self, vacancy):
        loggers.logger.info(f"Посылаю запрос в DeepSeek на валидацию вакансии.. Текст {short_text(vacancy['text'])}")
        start_time = time.time()
        promt_message = {"role":"system", "content":promts.validate_vacancy_promt}
        vacancy_message = {"role":"user", "content":(vacancy['text'])}

        messages = [promt_message, vacancy_message]
        response = DeepseekApi.get_chat_response(messages, self.__token)
        response = response.json()
        text = response['choices'][0]['message']['content']
        text = text.lower()

        elapsed_time = time.time() - start_time
        loggers.logger.info(f'Валидация вакансии заняла {elapsed_time:.2f} секунд')
        return not 'notavacancy' in text
