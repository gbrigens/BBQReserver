import re

from datetime import date
from telegram import ReplyKeyboardMarkup
import calendar

from database import Reservation, sess

userState = {}

MONTHS = [['January', 'February', 'March'],
          ['April', 'May', 'June'],
          ['July', 'August', 'September'],
          ['October', 'November', 'December']]

DAYS = [['1', '2', '3', '4', '5', '6', '7'],
        ['8', '9', '10', '11', '12', '13', '14'],
        ['15', '16', '17', '18', '19', '20', '21'],
        ['22', '23', '24', '25', '26', '27', '28'],
        ['29', '30', '31']]

HOURS = [['08:00', '10:00', '12:00', '14:00'],
         ['16:00', '18:00', '21:00'], ]

MAX_DAYS = 31


def reserve(update, context):
    reply_keyboard = MONTHS
    update.message.reply_text(
        'Choose the month, you want to reserve.',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True))


def choose_month(update, context):
    i = 0
    while i < len(MONTHS):
        if update.message.text in MONTHS[i]:
            reply_keyboard = DAYS
            userState[update.message.chat.id]['month'] = i * 3 + MONTHS[i].index(update.message.text) + 1
            num = MAX_DAYS - calendar.monthrange(2019, userState[update.message.chat.id]['month'])[1]
            print(num)
            for j in range(num):
                reply_keyboard[4].pop()
            update.message.reply_text(
                'Choose the day, you want to reserve.',
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True))
            return True
        i += 1
    return False


def choose_day(update, context):
    if re.match('\d\d$|\d$', update.message.text) is not None:
        day = int(update.message.text)
        if 0 < day <= calendar.monthrange(2019, userState[update.message.chat.id]['month'])[1]:
            userState[update.message.chat.id]['day'] = day
            reply_keyboard = HOURS
            update.message.reply_text(
                'Choose the hour, you want to reserve.',
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True))
            reserves = sess.query(Reservation).filter_by(day=date(2019,
                                                                  int(userState[update.message.chat.id]['month']),
                                                                  int(userState[update.message.chat.id]['day'])))
            reserved = 'This hours are already reserved.\n'

            for res in reserves:
                print(res.slot, res.day)
                reserved += res.slot + '\n'
            update.message.reply_text(
                reserved)
            return True
    return False


def choose_hour(update, context):
    i = 0
    while i < len(HOURS):

        if update.message.text in HOURS[i]:
            check = sess.query(Reservation).filter_by(day=date(2019,
                                                               int(userState[update.message.chat.id]['month']),
                                                               int(userState[update.message.chat.id]['day'])),
                                                      slot=update.message.text).first()
            if check is None:
                res = Reservation(user_id=update.message.chat.id,
                                  day=date(2019,
                                           int(userState[update.message.chat.id]['month']),
                                           int(userState[update.message.chat.id]['day'])),
                                  slot=update.message.text)
                sess.add(res)
                sess.commit()
                userState[update.message.chat.id] = {}
                return True
            else:
                update.message.reply_text(
                    'This hour is already reserved.')
                return False
    return False
