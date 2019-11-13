from datetime import date
from telegram import ReplyKeyboardMarkup

from database import sess, Reservation
from handler.base import cancel


def view_reservations(bot, update):
    reservations = sess.query(Reservation).filter_by(user_id = update.message.chat.id).order_by(Reservation.day)
    response = "You have made the following reservations:\n"
    i=1
    for res in reservations:
        if res.day.month<date.today().month:
            sess.delete(res)
            continue
        elif res.day.month==date.today().month and res.day.day<date.today().day:
            sess.delete(res)
            continue
        response += str(i)+". Date:"+str(res.day)+" Time:"+str(res.slot)+"\n"
        i+=1
    if response == "You have that reservations:\n":
        response = "You don't have any reservation."
    update.message.reply_text(response)
    cancel(bot, update)