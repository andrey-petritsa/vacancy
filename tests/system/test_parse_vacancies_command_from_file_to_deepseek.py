from pathlib import Path

from details.factory.app_factory import AppFactory
from details.file_repository.file_vacancy_repository import FileVacancyRepository
from helpers.system_test import SystemTest
from details.utils import settings as s


class TestParseVacanciesCommandFromFileToDeepseek(SystemTest):
    def setup_method(self):
        super().setup_method()
        self.save_example_vacancy()

    def test_execute(self):
        cmd = AppFactory.create_parse_vacancy_command()
        cmd.execute()
        assert len(cmd.vacancy_repository.find_all_parsed()) != 0

    def save_example_vacancy(self):
        vacancy_text = (
            "#вакансия #python #удаленка #backend #middle\n"
            "💼 Middle / Middle+ Python/Django разработчик (B2C, проект Valta)\n\n"
            "О компании и проекте:\n"
            "Valta Pet Products — e-commerce компания, развивающая B2C-направление для брендов в сфере зоотоваров. "
            "Сейчас команда полностью переписывает платформу на Django, выстраивая архитектуру заново с акцентом на стабильность, "
            "масштабируемость и высокую производительность.\n\n"
            "Стек и требования:\n"
            "Python, Django - отличное знание фреймворка, понимание его устройства\n"
            "Django Ninja или FastAPI - опыт работы на практическом уровне\n"
            "Celery - опыт работы на практическом уровне\n"
            "PostgreSQL - на уровне оптимизации запросов\n"
            "Redis, RabbitMQ - опыт работы на практическом уровне\n"
            "JWT - авторизация/аутентификация (must have)\n"
            "Docker - будет плюсом\n"
            "Важно: понимание принципов SOLID и уверенное владение ООП.\n\n"
            "Условия:\n"
            "Вилка: 200 000 – 240 000 ₽ (по результатам собеседования)\n"
            "Формат: полная удалёнка, не приближенка\n"
            "Гибкий график, важно быть на связи с 10:00 до 13:00 мск\n"
            "Приоритет на результат, а не на процессы\n\n"
            "📩 Контакты для откликов: @asyasukhanovarecr"
        )
        vacancy = {'text': vacancy_text, 'id': '1', 'status': 'unparsed', 'timestamp': 0, 'source': 'test'}
        FileVacancyRepository().save_data_to_file([vacancy], f'{s.path_to_database}/unparsed_vacancies.json')
