import pytest

from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

from ptbtest import ChatGenerator
from ptbtest import MessageGenerator
from ptbtest import Mockbot
from ptbtest import UserGenerator

from handler import keyboardHandler


view_reservation_parameters = [
    ["📖 View reservations", "You have made the following reservations:\n1. Date:2019-12-30 Time:16:00\n", {'id': 1234, 'first_name': 'Test', 'last_name': 'The Bot'}],
]

@pytest.mark.parametrize("test_input, expected, userdata", view_reservation_parameters)
def test_view_reservation(test_input, expected, userdata):
    bot = Mockbot()
    ug = UserGenerator()
    cg = ChatGenerator()
    mg = MessageGenerator(bot)
    user = ug.get_user(id=userdata['id'], first_name=userdata['first_name'], last_name=userdata['last_name'])
    chat = cg.get_chat(user=user)
    updater = Updater(bot=bot)
    updater.dispatcher.add_handler(MessageHandler(Filters.text, keyboardHandler.keyboard_handler))
    updater.start_polling()
    update = mg.get_message(user=user, chat=chat, text=test_input)
    bot.insertUpdate(update)
    sent = bot.sent_messages
    updater.stop()
    assert sent[0]['text'] == expected