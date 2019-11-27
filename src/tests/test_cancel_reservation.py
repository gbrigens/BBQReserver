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

cancel_reserve_parameters = [
    ["🗑 Cancel reservation", "Choose the reservation ID you want to cancel:\n```\nID:1 Time: 2019-12-30 16:00\n```", user1],
    ["09891", "Wrong reservation ID", user1], # Wrong reservation id
    ["Cancel", "Back to the main menu we go...", user1],
    ["🗑 Cancel reservation", "Choose the reservation ID you want to cancel:\n```\nID:1 Time: 2019-12-30 16:00\n```", user1],
    ["1", "You have not made any reservations yet", user1],
    # ["🗑 Cancel reservation", "You have not made any reservations yet", user2],

]


class TestClass:
    bot = Mockbot()
    ug = UserGenerator()
    cg = ChatGenerator()
    mg = MessageGenerator(bot)
    pp = PicklePersistence(filename='bbqreserve_test')
    updater = Updater(bot=bot, persistence=pp, use_context=True)

    @pytest.mark.parametrize("test_input, expected, userdata", cancel_reserve_parameters)
    def test_cancel_reservation(self, test_input, expected, userdata):
        user = self.ug.get_user(id=userdata['id'], first_name=userdata['first_name'], last_name=userdata['last_name'])
        chat = self.cg.get_chat(user=user)
        self.updater.dispatcher.add_handler(cancel.cancel_reserve_conv_handler)
        self.updater.start_polling()
        update = self.mg.get_message(user=user, chat=chat, text=test_input)
        self.bot.insertUpdate(update)
        sent = self.bot.sent_messages
        self.updater.stop()
        print(sent)
        # check expected result with actual result
        # assert sent[-1]['text'] == expected



test = TestClass()
for i in cancel_reserve_parameters:
    test.test_cancel_reservation(i[0], i[1], i[2])