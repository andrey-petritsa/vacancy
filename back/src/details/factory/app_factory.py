from pathlib import Path

from dotenv import dotenv_values

from business.usecases.change_vacancy_status_command import ChangeVacancyStatusCommand
from business.usecases.generate_cover_latter_command import GenerateCoverLatterCommand
from business.usecases.get_vacancies_from_source_command import GetVacanciesFromSourceCommand
from business.usecases.parse_vacancy_command import ParseVacancyCommand
from business.usecases.show_user_command import ShowUserCommand
from details.auth.authorizer import Authorizer
from details.file_repository.file_vacancy_repository import FileVacancyRepository
from details.file_repository.file_user_repository import FileUserRepository
from details.parser.deepseek.deepseek_vacancies_validator import DeepseekVacanciesValidator
from details.parser.deepseek.deepseek_vacansies_parser import DeepSeekVacanciesParser
from details.utils.settings import path_to_secrets
from sources.telegram.tg_vacancy_source import TgVacancySource
from business.usecases.show_vacancies_command import ShowVacanciesCommand
from details.utils import settings as s




class AppFactory:
    file_user_repository = FileUserRepository()
    file_vacancy_repository = FileVacancyRepository()
    authorizer = Authorizer()
    authorizer.user_repository = file_user_repository
    deepseek_token = dotenv_values(f"{path_to_secrets}/.env")['DEEPSEEK_TOKEN']
    deepseek_parser = DeepSeekVacanciesParser(deepseek_token)

    @classmethod
    def create_get_vacancies_from_source_command(cls):
        cmd = GetVacanciesFromSourceCommand()
        tg_config = dotenv_values(f"{path_to_secrets}/.tg_config.env")
        cmd.vacancy_source = TgVacancySource(tg_config)
        cmd.vacancy_source.chat_id = "@myjobit"
        cmd.vacancy_source.vacancy_validator = DeepseekVacanciesValidator(cls.deepseek_token)
        cmd.vacancy_repository = cls.file_vacancy_repository

        return cmd

    @classmethod
    def create_parse_vacancy_command(cls):
        cmd = ParseVacancyCommand()
        cmd.vacancy_repository = cls.file_vacancy_repository
        cmd.vacancy_parser = cls.deepseek_parser

        return cmd

    @classmethod
    def create_change_vacancy_status_command(cls):
        cmd = ChangeVacancyStatusCommand()
        cmd.vacancy_repository = cls.file_vacancy_repository
        cmd.authorizer = cls.authorizer

        return cmd

    @classmethod
    def create_show_vacancies_command(cls):
        cmd = ShowVacanciesCommand()
        cmd.vacancy_repository = cls.file_vacancy_repository
        cmd.authorizer = cls.authorizer
        return cmd

    @classmethod
    def create_show_user_command(cls):
        cmd = ShowUserCommand()
        cmd.user_repository = cls.file_user_repository
        cmd.authorizer = cls.authorizer
        return cmd

    @classmethod
    def create_generate_cover_latter_command(cls):
        cmd = GenerateCoverLatterCommand()
        cmd.vacancy_parser = cls.deepseek_parser
        cmd.resume = Path(f'{s.path_to_database}/resume.txt').read_text(encoding='utf-8')
        cmd.authorizer = cls.authorizer
        return cmd