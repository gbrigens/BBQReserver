import pytest
from sqlalchemy import func

from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

from ptbtest import ChatGenerator
from ptbtest import MessageGenerator
from ptbtest import Mockbot
from ptbtest import UserGenerator

from handler import keyboardHandler, reserve
from database import Reservation, sess


delete_reservation_parameters = [
    ["1", "Reservation was canceled.", {'id': 1234, 'first_name': 'Test', 'last_name': 'The Bot'}],
]


@pytest.mark.parametrize("test_input, expected, userdata", delete_reservation_parameters)
def test_delete_reservation(test_input, expected, userdata):
    bot = Mockbot()
    ug = UserGenerator()
    cg = ChatGenerator()
    mg = MessageGenerator(bot)
    user = ug.get_user(id=userdata['id'], first_name=userdata['first_name'], last_name=userdata['last_name'])
    chat = cg.get_chat(user=user)
    updater = Updater(bot=bot)
    reserve.userState[userdata['id']] = {'state': 'cancel', 'reservations':1}
    updater.dispatcher.add_handler(MessageHandler(Filters.text, keyboardHandler.keyboard_handler))
    updater.start_polling()
    initial_rows = sess.query(func.count(Reservation.id_)).scalar()
    update = mg.get_message(user=user, chat=chat, text=test_input)
    bot.insertUpdate(update)
    sent = bot.sent_messages
    updater.stop()
    assert sent[0]['text'] == expected
    final_rows = sess.query(func.count(Reservation.id_)).scalar()
    assert final_rows < initial_rows