from dotenv import dotenv_values

from details.parser.deepseek.deepseek_vacancies_validator import DeepseekVacanciesValidator


class TestDeepseekVacanciesValidator:
    def test_valid_vacancy(self):
        vacancy_text = "#вакансия #python #удаленка #backend #middle\n💼 Middle / Middle+ Python/Django разработчик (B2C, проект Valta)\n\nО компании и проекте:\nValta Pet Products — e-commerce компания, развивающая B2C-направление для брендов в сфере зоотоваров. Сейчас команда полностью переписывает платформу на Django, выстраивая архитектуру заново с акцентом на стабильность, масштабируемость и высокую производительность.\n\nСтек и требования:\nPython, Django - отличное знание фреймворка, понимание его устройства\nDjango Ninja или FastAPI - опыт работы на практическом уровне\nCelery - опыт работы на практическом уровне\nPostgreSQL - на уровне оптимизации запросов\nRedis, RabbitMQ - опыт работы на практическом уровне\nJWT - авторизация/аутентификация (must have)\nDocker - будет плюсом\nВажно: понимание принципов SOLID и уверенное владение ООП.\n\nУсловия:\nВилка: 200 000 – 240 000 ₽ (по результатам собеседования)\nФормат: полная удалёнка, не приближенка\nГибкий график, важно быть на связи с 10:00 до 13:00 мск\nПриоритет на результат, а не на процессы\n\n📩 Контакты для откликов: @asyasukhanovarecr"
        vacancy = {'text': vacancy_text}
        token = dotenv_values("back/secrets/.env")['DEEPSEEK_TOKEN']
        validator = DeepseekVacanciesValidator(token)

        assert True == validator.is_valid(vacancy)

    def test_notvalid_vacancy(self):
        vacancy_text = "Привет меня зовут Андрей я программист! Ищу работу"
        vacancy = {'text': vacancy_text}
        token = dotenv_values("back/secrets/.env")['DEEPSEEK_TOKEN']
        validator = DeepseekVacanciesValidator(token)

        assert False == validator.is_valid(vacancy)