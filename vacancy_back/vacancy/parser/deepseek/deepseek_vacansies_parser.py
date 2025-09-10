import json
import os

import requests
import vacancy.utils as utils


class DeepSeekVacanciesParser:
    def __init__(self):
        self.__system_promt = (
            "Ты — парсер вакансий."
            "На вход ты получаешь список текстов вакансий."
            "На выходе ты обязан вернуть строго один JSON-объект: массив объектов, "
            "где каждый объект соответствует одной вакансии из входного списка."
            "Никаких пояснений, текста, Markdown или ```json, только JSON."
            "Для каждой вакансии нужны следующие поля и только они:"
            "profession - профессия человека. Если backend программист пиши backend_programmer,"
            "если фронтенд frontend_proframmer,"
            "если фулсек fullstack_programmer"
            "languages — языки программирования вакансии (с большой буквы)."
            "salary — зарплата, с полями min и max (если не указана, вернуть 0)."
            "work_mode — режим работы: remote, office или unknown."
            "domain — предметная область проекта."
            "description — описание компании и проекта (если нету — unknown)."
            "skills — внутри него три поля: frameworks, databases, etc."
            "responsibility — обязанности по вакансии."
            "contact — контакт для связи."
            "experience_years - сколько требуется лет опыта"
        )
        self.__token = os.getenv("DEEPSEEK_TOKEN")

    def msgs_to_vacancies(self, msgs, try_count=0):
        utils.logger.log(f'Преобразую сообщения в вакансии. Кол-во сообщений {len(msgs)}')
        if try_count >= 10:
            raise Exception(f"Слишком много попыток парсинга сообщений")

        texts = [msg.text for msg in msgs]

        promt_message = {"role":"system", "content":self.__system_promt}
        vacation_message = {"role":"user", "content":("\n\n\n\n\n\n\n\n\n\n".join(texts))}

        messages = [promt_message, vacation_message]
        response = self.__get_chat_response(messages)
        response = response.json()
        text = response['choices'][0]['message']['content']

        try:
            vacations = json.loads(text)
            vacations = utils.to_dtos(vacations)
            for i in range(len(vacations)):
                vacations[i].id = msgs[i].id

            return vacations
        except json.JSONDecodeError:
            utils.logger.log(f'Deepseek вернул не json. Повторная попытка... Полученный текст\n{text}')
            return self.msgs_to_vacancies(msgs, try_count + 1)

    def __get_chat_response(self, messages):
        url = "https://api.deepseek.com/chat/completions"
        headers = {"Content-Type": "application/json","Authorization": f"Bearer {self.__token}"}

        data = {
            "model": "deepseek-chat",
            "messages":messages,
            "stream": False,
            "temperature": 0.5
        }

        response = requests.post(url, json=data, headers=headers)
        if not response.ok:
            raise Exception(response.text)

        return response

