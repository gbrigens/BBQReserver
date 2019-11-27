import sys
import datetime

sys.path.insert(1, '../')

import pytest
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.ext import PicklePersistence

from ptbtest import ChatGenerator
from ptbtest import MessageGenerator
from ptbtest import Mockbot
from ptbtest import UserGenerator

from handler import reserve, keyboardHandler, cancel
from database import Reservation, sess

user2 = {
    'id': 1333,
    'first_name': 'User2',
    'last_name': 'The Bot2'
}

create_reserve_parameters = [
    ["🖊 Reserve", "Choose the month, you want to reserve", user2, -1],
    ["December", "Chosen month: `12`\nChoose the day, you want to reserve", user2, -1],
    ["30", "Chosen date: `2019-12-30`\nChoose the hour, you want to reserve.\n\nThese hours are already reserved:\n```\n16:00\n```", user2, -1],
    ["Subscribe to waiting list", "You are added to Waiting list successfully for `2019-12-30`. The bot will notify you if any reservation on this day is cancelled", user2, -2],
]

class TestClass:
    bot = Mockbot()
    ug = UserGenerator()
    cg = ChatGenerator()
    mg = MessageGenerator(bot)
    pp = PicklePersistence(filename='bbqreserve_test')
    updater = Updater(bot=bot, persistence=pp, use_context=True)

    @pytest.mark.parametrize("test_input, expected, userdata, i", create_reserve_parameters)
    def test_create_reservation(self, test_input, expected, userdata, i):
        user = self.ug.get_user(id=userdata['id'], first_name=userdata['first_name'], last_name=userdata['last_name'])
        chat = self.cg.get_chat(user=user)
        self.updater.dispatcher.add_handler(reserve.reserve_conv_handler)
        self.updater.start_polling()
        update = self.mg.get_message(user=user, chat=chat, text=test_input)
        self.bot.insertUpdate(update)
        sent = self.bot.sent_messages
        self.updater.stop()
        # check expected result with actual result
        # print(sent)
        assert sent[i]['text'] == expected
