import pytest
import datetime

from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

from ptbtest import ChatGenerator
from ptbtest import MessageGenerator
from ptbtest import Mockbot
from ptbtest import UserGenerator

from handler import keyboardHandler, reserve
from database import Reservation, sess

create_reserve_parameters = [
    ["🖊 Reserve", "Choose the month, you want to reserve.", {'id': 1234, 'first_name': 'Test', 'last_name': 'The Bot'}],
]

choose_month_parameters = [
    ["December", "Choose the day, you want to reserve.", {'id': 1234, 'first_name': 'Test', 'last_name': 'The Bot'}],
]

choose_day_parameters = [
    ["30", "Choose the hour, you want to reserve.", {'id': 1234, 'first_name': 'Test', 'last_name': 'The Bot', 'month': 12}],
]

choose_slot_parameters = [
    ["Time reserved successfully.", {'user_id': 1234, 'year': 2019, 'month': 12, 'day': 30, 'hour': "16:00"}],
    # ["This hour is not available to reserve.", {'user_id': 1234, 'year': 2019, 'month': 12, 'day': 30, 'hour': "16:00"}],
]

class TestCreateReservation(object):
   
    @pytest.mark.parametrize("test_input, expected, userdata", create_reserve_parameters)
    def test_create_reservation(self, test_input, expected, userdata):
        bot = Mockbot()
        ug = UserGenerator()
        cg = ChatGenerator()
        mg = MessageGenerator(bot)
        user = ug.get_user(id=userdata['id'], first_name=userdata['first_name'], last_name=userdata['last_name'])
        chat = cg.get_chat(user=user)
        updater = Updater(bot=bot)
        reserve.set_month()
        updater.dispatcher.add_handler(MessageHandler(Filters.text, keyboardHandler.keyboard_handler))
        updater.start_polling()
        update = mg.get_message(user=user, chat=chat, text=test_input)
        bot.insertUpdate(update)
        sent = bot.sent_messages
        updater.stop()
        assert sent[0]['text'] == expected

    @pytest.mark.parametrize("test_input, expected, userdata", choose_month_parameters)
    def test_choose_month(self, test_input, expected, userdata):
        bot = Mockbot()
        ug = UserGenerator()
        cg = ChatGenerator()
        mg = MessageGenerator(bot)
        user = ug.get_user(id=userdata['id'], first_name=userdata['first_name'], last_name=userdata['last_name'])
        chat = cg.get_chat(user=user)
        updater = Updater(bot=bot)
        reserve.userState[userdata['id']] = {'state': 'month'}
        reserve.set_month()
        updater.dispatcher.add_handler(MessageHandler(Filters.text, keyboardHandler.keyboard_handler))
        updater.start_polling()
        update = mg.get_message(user=user, chat=chat, text=test_input)
        bot.insertUpdate(update)
        sent = bot.sent_messages
        updater.stop()
        assert sent[0]['text'] == expected

    @pytest.mark.parametrize("test_input, expected, userdata", choose_day_parameters)
    def test_choose_day(self, test_input, expected, userdata):
        bot = Mockbot()
        ug = UserGenerator()
        cg = ChatGenerator()
        mg = MessageGenerator(bot)
        user = ug.get_user(id=userdata['id'], first_name=userdata['first_name'], last_name=userdata['last_name'])
        chat = cg.get_chat(user=user)
        updater = Updater(bot=bot)
        reserve.userState[userdata['id']] = {'state': 'day', 'month': userdata['month']}
        updater.dispatcher.add_handler(MessageHandler(Filters.text, keyboardHandler.keyboard_handler))
        updater.start_polling()
        update = mg.get_message(user=user, chat=chat, text=test_input)
        bot.insertUpdate(update)
        sent = bot.sent_messages
        updater.stop()
        assert sent[0]['text'] == expected


    @pytest.mark.parametrize("expected, rdata", choose_slot_parameters)
    def test_choose_slot(self, expected, rdata):
        bot = Mockbot()
        ug = UserGenerator()
        cg = ChatGenerator()
        mg = MessageGenerator(bot)
        user = ug.get_user(id=rdata['user_id'])
        chat = cg.get_chat(user=user)
        updater = Updater(bot=bot)
        reserve.userState[rdata['user_id']] = {'state': 'slot', 'month': rdata['month'], 'day': rdata['day']}
        updater.dispatcher.add_handler(MessageHandler(Filters.text, keyboardHandler.keyboard_handler))
        updater.start_polling()
        update = mg.get_message(user=user, chat=chat, text=rdata['hour'])
        bot.insertUpdate(update)
        sent = bot.sent_messages
        updater.stop()
        assert sent[0]['text'] == expected
        reservation = sess.query(Reservation).filter_by(user_id=rdata['user_id']).order_by(Reservation.id_.desc()).first()
        expected_day = datetime.date(rdata['year'], rdata['month'], rdata['day'])
        assert reservation.day == expected_day