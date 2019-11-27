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

user1 = {
    'id': 1234,
    'first_name': 'Test',
    'last_name': 'The Bot'
}
user2 = {
    'id': 1235,
    'first_name': 'Test2',
    'last_name': 'The Bot'
}
user3 = {
    'id': 1236,
    'first_name': 'Test3',
    'last_name': 'The Bot'
}
user4 = {
    'id': 1237,
    'first_name': 'Test4',
    'last_name': 'The Bot'
}

create_reserve_parameters = [
    ["🖊 Reserve", "Choose the month, you want to reserve", user1, 0],
    ["December", "Chosen month: `12`\nChoose the day, you want to reserve", user1, 0],
    ["30", "Chosen date: `2019-12-30`\nChoose the hour, you want to reserve.", user1, 0],
    ["16:00", "Time `2019-12-30 16:00` reserved successfully", user1, 0],
    ["🖊 Reserve", "Choose the month, you want to reserve", user2, 0],
    ["Wrongmonth", "Choose the month, you want to reserve", user2, 0], # Wrong month
    ["Cancel", "Back to the main menu we go...", user2, 0],
    ["🖊 Reserve", "Choose the month, you want to reserve", user3, 0],
    ["December", "Chosen month: `12`\nChoose the day, you want to reserve", user3, 0],
    ["33", "Chosen month: `12`\nChoose the day, you want to reserve", user3, 0], # wrong day
    ["Cancel", "Back to the main menu we go...", user3, 0],
    ["🖊 Reserve", "Choose the month, you want to reserve", user4, 1],
    ["December", "Chosen month: `12`\nChoose the day, you want to reserve", user4, 0],
    ["31", "Chosen date: `2019-12-31`\nChoose the hour, you want to reserve.", user4, 0],
    ["99:00", "Chosen date: `2019-12-31`\nChoose the hour, you want to reserve.", user4, 0], # Wrong hour
]

class TestClass:
    bot = Mockbot()
    ug = UserGenerator()
    cg = ChatGenerator()
    mg = MessageGenerator(bot)
    pp = PicklePersistence(filename='bbqreserve_test')
    updater = Updater(bot=bot, persistence=pp, use_context=True)

    @pytest.mark.parametrize("test_input, expected, userdata, delme", create_reserve_parameters)
    def test_create_reservation(self, test_input, expected, userdata, delme):
        user = self.ug.get_user(id=userdata['id'], first_name=userdata['first_name'], last_name=userdata['last_name'])
        chat = self.cg.get_chat(user=user)
        self.updater.dispatcher.add_handler(reserve.reserve_conv_handler)
        self.updater.start_polling()
        update = self.mg.get_message(user=user, chat=chat, text=test_input)
        self.bot.insertUpdate(update)
        sent = self.bot.sent_messages
        self.updater.stop()
        if delme:
            import os
            os.remove("bbqreserve_test")
        # check expected result with actual result
        assert sent[-1]['text'] == expected
