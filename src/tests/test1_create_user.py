import pytest

from telegram.ext import CommandHandler
from telegram.ext import Updater

from ptbtest import ChatGenerator
from ptbtest import MessageGenerator
from ptbtest import Mockbot
from ptbtest import UserGenerator

from handler import base
from database import User, sess


create_user_parameters = [
    ["start", "/start", {'id': 1234, 'first_name': 'Test', 'last_name': 'The Bot', 'telegramID': 'TestThe Bot'},],
]

@pytest.mark.parametrize("command, test_input, expected_user", create_user_parameters)
def test_create_user(command, test_input, expected_user):
    bot = Mockbot()
    ug = UserGenerator()
    cg = ChatGenerator()
    mg = MessageGenerator(bot)
    user = ug.get_user(id=expected_user['id'], first_name=expected_user['first_name'], last_name=expected_user['last_name'])
    chat = cg.get_chat(user=user)
    updater = Updater(bot=bot)
    updater.dispatcher.add_handler(CommandHandler(command, base.start))
    updater.start_polling()
    update = mg.get_message(user=user, chat=chat, text=test_input)
    bot.insertUpdate(update)
    updater.stop()
    user = sess.query(User).get(expected_user['id'])
    assert user.id_ == expected_user['id']