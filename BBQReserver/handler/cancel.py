import re

from telegram import ReplyKeyboardMarkup

from handler.reserve import userState
from models.reservation import Reservation

reservations = [Reservation('00:00','12:00',4,"Caka",12)]

def cancel_reservation(update, context):
    reply_keyboard = [['1', '2', '3', 'Cancel']]
    update.message.reply_text(
        '.',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True))

def delete_reservation(update, context):
    if re.match('\d$', update.message.text) is not None:
        num = int(update.message.text)
        userState[update.message.chat.id] = {}

