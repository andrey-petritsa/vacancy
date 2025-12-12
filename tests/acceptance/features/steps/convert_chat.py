from behave import *

from helpers.mocks.spy_repository import SpyRepository
from business.usecases.convert_chat_to_vacations_command import ConvertChatToVacanciesCommand
from details.utils import DTO


@step("у меня есть сохраненный чат")
def step_impl(context):
    rep = SpyRepository()
    rep.msgs = [
        DTO(id='1', text='текст вакансии')
    ]
    context.rep = rep


@step("я вызываю команду конвертации чата")
def step_impl(context):
    cmd = ConvertChatToVacanciesCommand()
    cmd.repository = context.rep
    cmd.execute()


@step("вакансии конвертируются и сохраняются")
def step_impl(context):
    assert len(context.rep.saved_msgs) > 0


@step("сконвертированные сообщения переходят в статус done")
def step_impl(context):
    messages = context.rep.saved_msgs
    assert all(msg.status == "done" for msg in messages)
