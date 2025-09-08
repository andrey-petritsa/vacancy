import os

from behave import *
import shutil
from vacancy.usecases.convert_chat_to_vacations_command import ConvertChatToVacanciesCommand
from vacancy.usecases.repository.file_message import FileMessage
from vacancy.usecases.repository.file_vacancy import FileVacancy

use_step_matcher("re")


@when("у меня есть сохраненный чат")
def step_impl(context):
    shutil.copy('test_data/messages.jsonl', 'test_artifacts/messages.jsonl')

@when("я вызываю команду конвертации чата")
def step_impl(context):
    cmd = ConvertChatToVacanciesCommand()
    cmd.execute()


@then("вакансии конвертируются и сохраняются")
def step_impl(context):
    assert len(FileVacancy.get_all()) > 0


@then("сконвертированные сообщения переходят в статус done")
def step_impl(context):
    message = FileMessage
    assert all(msg.status == "done" for msg in message.get_all())