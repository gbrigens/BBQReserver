import re

from telegram import ReplyKeyboardMarkup

from database import sess, Reservation
from handler.base import cancel
from handler.reserve import userState


def cancel_reservation(update, context):
    reservations = sess.query(Reservation).filter_by(user_id=update.message.chat.id)
    response = "Choose the number of reservation you want to cancel:\n"
    i = 1
    buttons = []
    for res in reservations:
        response += str(i) + ". Date:" + str(res.day) + " Time:" + str(res.slot) + "\n"
        buttons.append(str(i))
        i += 1
    userState[update.message.chat.id] = {}
    userState[update.message.chat.id]['reservations'] = i-1
    if response == "Choose the number of reservation you want to cancel:\n":
        response = "You don't have reservations."
    update.message.reply_text(
        response,
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True))


def delete_reservation(update, context):
    if re.match('\d$', update.message.text) is not None:
        num = int(update.message.text)
        if num > userState[update.message.chat.id]['reservations']:
            return False
        x =sess.query(Reservation).filter_by(user_id=update.message.chat.id)[num-1]
        sess.delete(x)
        userState[update.message.chat.id] = {}
        update.message.reply_text(
            'Reservation was canceled.')
        cancel(update, context)
    elif update.message.text == "Cancel":
        cancel(update, context)
