import json
import time

from details.utils import loggers
from . import promts
from .deepseek_api import DeepseekApi
from ...utils.text import short_text


class DeepSeekVacanciesParser:
    def __init__(self, token):
        self.__token = token

    def parse_one(self, vacancy, try_count=0):
        start_time = time.time()
        loggers.logger.info(f"Посылаю запрос в DeepSeek на парсинг вакансии... Текст {short_text(vacancy['text'])}")
        if try_count >= 10:
            raise Exception(f"Слишком много попыток парсинга сообщений")

        promt_message = {"role":"system", "content":promts.parse_promt}
        vacancy_message = {"role":"user", "content":(vacancy['text'])}

        messages = [promt_message, vacancy_message]
        response = DeepseekApi.get_chat_response(messages, self.__token)
        response = response.json()
        text = response['choices'][0]['message']['content']

        try:
            text = self.__fix_text(text)
            parsed_vacancy = json.loads(text)
            parsed_vacancy['id'] = vacancy['id']
            parsed_vacancy['text'] = vacancy['text']
            parsed_vacancy['timestamp'] = vacancy['timestamp']
            parsed_vacancy['source'] = vacancy['source']
            elapsed_time = time.time() - start_time
            loggers.logger.info(f'Парсинг вакансии занял {elapsed_time:.2f} секунд')
            return parsed_vacancy
        except json.JSONDecodeError:
            loggers.logger.info(f'Deepseek вернул не json. Повторная попытка... Полученный текст\n{short_text(text)}')
            return self.parse_one(vacancy, try_count + 1)

    def __fix_text(self, text):
        text = text.lower()
        return text.replace("```json", "").replace("```", "")

    def generate_cover_latter(self, vacancy, resume):
        promt_message = {"role":"system", "content":promts.generate_cover_latter_promt}
        vacancy_message = {"role":"user", "content":(vacancy['text'])}
        resume_message = {"role":"user", "content":resume}

        messages = [promt_message, vacancy_message, resume_message]
        response = DeepseekApi.get_chat_response(messages, self.__token)
        response = response.json()
        text = response['choices'][0]['message']['content']
        return text


