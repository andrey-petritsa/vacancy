from behave import step

from helpers.mocks.spy_repository import SpyRepository
from business.usecases.save_chat_command import SaveNewMessagesCommand


@step('у меня есть ид канала {channel_id}')
def step_impl(context, channel_id):
    context.channel_id = channel_id


@step('я вызываю команду сохранения чата')
def step_impl(context):
    rep = SpyRepository()
    cmd = SaveNewMessagesCommand()
    cmd.repository = rep
    context.rep = rep

    cmd.execute()


@step('сообщения сохраняются')
def step_impl(context):
    assert len(context.rep.saved_msgs) > 0
