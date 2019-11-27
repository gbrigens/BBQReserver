from datetime import datetime
from telegram import ReplyKeyboardMarkup, ParseMode
from telegram.ext import (MessageHandler, Filters, ConversationHandler)

from database import sess, Reservation, get_awaiting_users
from handler.base import cancel, main_menu

CHOOSE = 0

def choose_reservation(update, context):
    reservations = sess.query(Reservation).filter(
        Reservation.user_id == update.message.chat.id,
        Reservation.is_expired != True,
        Reservation.day > datetime.now()
    ).all()
    buttons = []
    if reservations:
        response = "Choose the reservation ID you want to cancel:\n```\n"
        for res in reservations:
            response += "ID:" + str(res.id_) + " Time: " + res.day.strftime("%Y-%m-%d %H:%M") + "\n"
            buttons.append(str(res.id_))
        response += '```'
        buttons = [buttons[i:i+5] for i in range(0, len(buttons), 5)]
    else:
        response = "You have not made any reservations yet"
    buttons.append(['Cancel'])
    update.message.reply_text(
        response,
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True),
        parse_mode=ParseMode.MARKDOWN
    )
    return CHOOSE


def delete_reservation(update, context):
    if update.message.text.isnumeric():
        num = int(update.message.text)
        x = sess.query(Reservation).filter_by(user_id=update.message.chat.id, id_=num).first()
        if x:
            sess.delete(x)
            sess.commit()
            update.message.reply_text('Reservation successfully cancelled')
            awaiting_users_list = get_awaiting_users(x.day)
            choose_reservation(update, context)
            if awaiting_users_list:
                notify_awaiting_users(context, awaiting_users_list)
            return ConversationHandler.END
    elif update.message.text == "Cancel":
        cancel(update, context)
        return ConversationHandler.END
    update.message.reply_text('Wrong reservation ID')
    choose_reservation(update, context)
    return CHOOSE

def notify_awaiting_users(context, users):
    for user in users:
        response = "One user cancelled the reservation on `" + user.day.strftime('%Y-%m-%d') + "`"
        context.bot.send_message(
            chat_id=user.user_id, 
            text=response,
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True, one_time_keyboard=True),
            parse_mode=ParseMode.MARKDOWN
        )

def cancel(update, context):
    update.message.reply_text("Back to the main menu we go...", reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
    return ConversationHandler.END


#ConversationHandler to cancel reservations
cancel_reserve_conv_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex('^(🗑 Cancel reservation)$'), choose_reservation)],
    states={
        CHOOSE: [
            MessageHandler(Filters.text, delete_reservation),
        ],
    },

    fallbacks=[MessageHandler(Filters.regex('^Cancel$'), cancel)],
    name="cancel_reserve_conversation",
    persistent=True
)