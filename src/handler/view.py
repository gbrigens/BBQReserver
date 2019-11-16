from datetime import datetime
from telegram import ReplyKeyboardMarkup, ParseMode

from database import sess, Reservation
from handler.base import main_menu


def view_reservations(update, context):
    reservations = sess.query(Reservation).filter(
        Reservation.user_id == update.message.chat.id,
        Reservation.is_expired != True,
        Reservation.day > datetime.now()
    ).all()
    if reservations:
        response = "You have made the following reservations:```\n"
        for res in reservations:
            response += "ID:" + str(res.id_) + " Time: " + res.day.strftime("%Y-%m-%d %H:%M") + "\n"
        response += '```'
    else:
        response = "You have not made any reservations yet"
    update.message.reply_text(
        response,
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True, one_time_keyboard=True),
        parse_mode=ParseMode.MARKDOWN
    )
    return True