from behave import given, when, then

from vacancy.usecases.repository.file_message import FileMessage
from vacancy.usecases.save_chat_command import SaveChatCommand


@given('у меня есть ид канала {channel_id}')
def step_impl(context, channel_id):
    context.channel_id = channel_id

@when('я вызываю команду сохранения чата')
def step_impl(context):
    cmd = SaveChatCommand()
    cmd.execute()

@then('сообщения сохраняются')
def step_impl(context):
    messages = FileMessage.get_all_from_channel(context.channel_id)
    assert len(messages) > 0


