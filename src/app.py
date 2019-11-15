# import telegram
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence
from telegram import Update

import logging
from handler import base, keyboardHandler, reserve, cancel
from helper import sendNotification

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

pp = PicklePersistence(filename='bbqreserve')
updater = Updater(token='601024499:AAFTc8SZueqqSHwiTclXQafUt9hTtASNJ2c', persistence=pp, use_context=True) #976212417:AAGFR9gjY6C3l5KbIixps3mVojaFCq-sL7s
j=updater.job_queue
j.run_daily(sendNotification, interval=43200, first=300)

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', base.start)
dispatcher.add_handler(start_handler)

cancel_handler = CommandHandler('cancel', base.cancel)
dispatcher.add_handler(cancel_handler)

dispatcher.add_handler(reserve.reserve_conv_handler)
dispatcher.add_handler(cancel.cancel_reserve_conv_handler)
message_handler = MessageHandler(Filters.text, keyboardHandler.keyboard_handler)
# print(Filters.update.message)
dispatcher.add_handler(message_handler)

unknown_handler = MessageHandler(Filters.command, base.unknown)
dispatcher.add_handler(unknown_handler)

# reserve.set_month()

updater.start_polling()
updater.idle()
