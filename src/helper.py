from telegram.ext import Updater
from datetime import datetime, timedelta
from telegram import ReplyKeyboardMarkup, ParseMode
from telegram.ext import CallbackContext
from database import sess, Reservation
from handler.base import cancel


def sendNotification(context: CallbackContext):
    now = datetime.now()
    period = now + timedelta(hours=24) #should be hours
    reservations = sess.query(Reservation).filter(
        Reservation.day <= period,
        Reservation.is_expired != True,
        Reservation.is_confirmed != True
    ).order_by(Reservation.day).all()

    if reservations:
        keyboard = [['✅ Confirm', '❌ Cancel']]
        for reservation in reservations:
            response = "Your have a reservation `" + str(reservation.id_) + "` at " + reservation.day.strftime('%H:%M') + " on " + reservation.day.strftime('%Y-%m-%d') + "` for the BBQZone. Confirm your reservation"
            context.bot.send_message(
                chat_id=reservation.user_id, 
                text=response,
                reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True),
                parse_mode=ParseMode.MARKDOWN
            )

