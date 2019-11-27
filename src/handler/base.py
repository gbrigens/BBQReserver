from telegram import ReplyKeyboardMarkup

from database import User, sess
from handler import reserve

main_menu = [['🖊 Reserve'], ['🗑 Cancel reservation'], ['📖 View reservations'], ['💬 Report violation']]

def start(update, context):
    user = User(id_=update.message.chat.id,
                telegramID=update.message.chat.username)
    check = sess.query(User).get(update.message.chat.id)
    if check is None:
        sess.add(user)
        sess.commit()
    update.message.reply_text(
        'Welcome to BBQ reserver telegram bot.\n'
        'By can book a time slot for barbecue zone in Innopolis city, Republic Tatarstan!\n\n'
        'Main features of bot:\n'
        '- view available time slots for barbecue zone;\n'
        '- a book time slot for barbecue zone;\n'
        '- cancel booking;\n'
        'Send /cancel if you want to return to the main menu(just in case)',
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))


def cancel(update, context):
    update.message.reply_text(
        'Back to the main menu we go...',
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand what you've said.")

def report(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="If you want to report about something or if you need help, please, write to @bbqadmin or call +7920000000.")
