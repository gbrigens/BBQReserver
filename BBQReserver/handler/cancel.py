from telegram import ReplyKeyboardMarkup


def cancel_reservation(update, context):
    reply_keyboard = [['1', '2', '3', 'Cancel']]
    update.message.reply_text(
        '.',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True))
