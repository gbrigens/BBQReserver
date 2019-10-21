# import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from handler import base, keyboardHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token='976212417:AAGFR9gjY6C3l5KbIixps3mVojaFCq-sL7s', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', base.start)
dispatcher.add_handler(start_handler)

cancel_handler = CommandHandler('cancel', base.cancel)
dispatcher.add_handler(cancel_handler)

message_handler = MessageHandler(Filters.text, keyboardHandler.keyboard_handler)
dispatcher.add_handler(message_handler)

unknown_handler = MessageHandler(Filters.command, base.unknown)
dispatcher.add_handler(unknown_handler)

print(dispatcher.handlers)

updater.start_polling()

