# import telegram
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update

import logging
from handler import base, keyboardHandler, reserve

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token='976212417:AAGFR9gjY6C3l5KbIixps3mVojaFCq-sL7s')
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', base.start)
dispatcher.add_handler(start_handler)

cancel_handler = CommandHandler('cancel', base.cancel)
dispatcher.add_handler(cancel_handler)

message_handler = MessageHandler(Filters.text, keyboardHandler.keyboard_handler)
# print(Filters.update.message)
dispatcher.add_handler(message_handler)

unknown_handler = MessageHandler(Filters.command, base.unknown)
dispatcher.add_handler(unknown_handler)

reserve.set_month()

updater.start_polling()