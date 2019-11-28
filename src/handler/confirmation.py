from datetime import datetime, timedelta
from telegram import ReplyKeyboardMarkup, ParseMode

from database import sess, Reservation
from handler.base import main_menu, unknown

##########################################################################
###########   Request confirmation RC-10                     #############
##########################################################################
def check_confirmation(update, context):
    now = datetime.now()
    two_hours = now + timedelta(days=2)
    reservation = sess.query(Reservation).filter(
        Reservation.day <= two_hours,
        Reservation.is_expired != True,
        Reservation.is_confirmed != True
    ).order_by(Reservation.day).first()
    if reservation:
        response = "Your reservation No `" + str(reservation.id_) + " " + reservation.day.strftime('%Y-%m-%d %H:%M') + "`"
        if update.message.text == '❌ Cancel':
            sess.delete(reservation)
            sess.commit()
            response += ' cancelled'
        elif update.message.text == '✅ Confirm':
            reservation.is_confirmed = True
            sess.commit()
            response += ' confirmed'
        update.message.reply_text(
            response,
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True, one_time_keyboard=True),
            parse_mode=ParseMode.MARKDOWN
        )
        return True
    else:
        unknown(update, context)
