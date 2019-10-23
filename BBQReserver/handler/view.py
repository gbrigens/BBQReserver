from telegram import ReplyKeyboardMarkup

from database import sess, Reservation
from handler.base import cancel


def view_reservations(update, context):
    reservations = sess.query(Reservation).filter_by(user_id = update.message.chat.id)
    response = "You have made the following reservations:\n"
    i=1
    for res in reservations:
        response += str(i)+". Date:"+str(res.day)+" Time:"+str(res.slot)+"\n"
        i+=1
    if response == "You have that reservations:\n":
        response = "You don't have any reservation."
    update.message.reply_text(response)
    cancel(update, context)