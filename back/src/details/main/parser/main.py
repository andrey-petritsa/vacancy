import time
import signal

from business.exceptions.exceptions import VacancyNotFoundException
from details.utils import loggers
from details.utils import command_registry
from sources.telegram import config

should_stop = False

def handle_stop(signum, frame):
    global should_stop
    should_stop = True
    loggers.logger.info("Получен Ctrl+C, останавливаюсь...")

signal.signal(signal.SIGINT, handle_stop)
signal.signal(signal.SIGTERM, handle_stop)


while not should_stop:
    config.limit = 10
    loggers.logger.info('Загружаю вакансии из источника')
    command_registry.get_vacancies_from_source_command.execute()
    loggers.logger.info('Вакансии успешно загружены')

    if should_stop:
        break

    while not should_stop:
        try:
            command_registry.parse_vacancy_command.execute()
        except VacancyNotFoundException:
            loggers.logger.info('Не найдено вакансии для парсинга. Ожидаю минуту...')
            for _ in range(60):
                if should_stop:
                    break
                time.sleep(1)
            break