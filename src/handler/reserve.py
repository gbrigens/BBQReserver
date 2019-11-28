from calendar import monthrange
from datetime import date, datetime
from time import strptime
from math import ceil

from sqlalchemy import func
from telegram import ReplyKeyboardMarkup, ParseMode
from telegram.ext import (MessageHandler, Filters, ConversationHandler)

from database import Reservation, WaitingList, sess
from handler import base

MONTH, DAY, HOUR = range(3)

YEAR = 2019
today = date.today()
next_month = date(today.year + (today.month // 12), ((today.month % 12) + 1), 1)

##########################################################################
###########   Create reservation NR-10                       #############
##########################################################################

# get month list
def get_months(for_keyboard=False):
    months = []
    months.append(today.strftime("%B"))
    months.append(next_month.strftime("%B"))
    if for_keyboard:
        months = [[i] for i in months]
    months.append(['Cancel'])
    return months


# get days list in chosen month
def get_days(month, for_keyboard=False):
    first_day = 1
    last_day = monthrange(today.year, month)[1]
    if month == today.month:
        first_day = today.day
    if not for_keyboard:
        return list(range(first_day, last_day+1))
    total_days = last_day - first_day
    rows = ceil(total_days/7)
    days = [[] for i in range(rows)]
    n = 0
    for day in range(first_day, last_day+1):
        days[n//7].append(str(day))
        n += 1
    days.append(['Back', 'Cancel'])
    return days


# get hours slot list in chosen day
def get_hours(start=8, end=24, length=2, exclude=[], for_keyboard=False):
    hours = []
    for i in range(start, end, length):
        item = "%02d"%i + ':00'
        if item not in exclude:
            hours.append(item)
    if not for_keyboard:
        return hours
    n = ceil(len(hours)/2)
    hours = [hours[i:i+n] for i in range(0, len(hours), n)]
    hours.append(['Back', 'Cancel'])
    return hours


def reserve(update, context):
    reply_keyboard = get_months(for_keyboard=True)
    update.message.reply_text(
        'Choose the month, you want to reserve',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    )
    return MONTH


def choose_month(update, context):
    months = get_months()
    if update.message.text in months or ('month' in context.user_data and 'wrong_day' in context.user_data):
        if 'wrong_day' in context.user_data:
            month = context.user_data['month']
            del context.user_data['wrong_day']
        else:
            month = strptime(update.message.text, '%B').tm_mon
            context.user_data['month'] = month
        reply_keyboard = get_days(month=month, for_keyboard=True)
        update.message.reply_text(
            'Chosen month: `' + str(month) + '`\nChoose the day, you want to reserve',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True),
            parse_mode=ParseMode.MARKDOWN
        )
        return DAY
    if update.message.text == 'Cancel':
        if 'month' in context.user_data:
            del context.user_data['month']
        base.cancel(update, context)
        return ConversationHandler.END
    reserve(update, context)


def choose_day(update, context):
    if update.message.text.isnumeric() or ('day' in context.user_data and 'wrong_hour' in context.user_data):
        if 'wrong_hour' in context.user_data:
            day = context.user_data['day']
            del context.user_data['wrong_hour']
        else:
            day = int(update.message.text)
        days = get_days(context.user_data['month'])
        if day in days:
            context.user_data['day'] = day
            chosen_day = date(YEAR, int(context.user_data['month']), int(context.user_data['day']))
            user_reserves = sess.query(Reservation).filter(
                Reservation.user_id == update.message.chat_id,
                func.date(Reservation.day) == chosen_day,
                Reservation.is_expired != True,
            ).all()
            if user_reserves:
                update.message.reply_text(
                    'You already have the reservation on `' + chosen_day.strftime('%Y-%m-%d') + '`, you should cancel previous reservation if you want to change time',
                    parse_mode=ParseMode.MARKDOWN
                )
                choose_month(update, context)
                return DAY            
            reserves = sess.query(Reservation).filter(
                func.date(Reservation.day) == chosen_day
            ).all()
            reserved_slots = [i.slot for i in reserves]
            reply_keyboard = get_hours(exclude=reserved_slots, for_keyboard=True)
            text = "Chosen date: `" + chosen_day.strftime('%Y-%m-%d') + "`\nChoose the hour, you want to reserve."
            if reserved_slots:
                text += "\n\nThese hours are already reserved:\n```\n"
                for slot in reserved_slots:
                    text += slot + '\n'
                text += '```'
                reply_keyboard.insert(-1, ['Subscribe to waiting list'])
            update.message.reply_text(
                text, reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True),
                parse_mode=ParseMode.MARKDOWN
            )
            return HOUR
        else:
            context.user_data['wrong_day'] = True
            update.message.reply_text('Wrong date')
    if update.message.text == 'Back':
        reserve(update, context)
        return MONTH
    if update.message.text == 'Cancel':
        base.cancel(update, context)
        return ConversationHandler.END
    choose_month(update, context)
    return DAY

##########################################################################
###########   Insert Data NR-22(Found inside the function)   #############
##########################################################################
def choose_hour(update, context):
    hours = get_hours()
    if update.message.text in hours:
        splitted_time = update.message.text.split(':')
        chosen_day = datetime(YEAR, int(context.user_data['month']), int(context.user_data['day']), int(splitted_time[0]), int(splitted_time[1]), 0)
        check = sess.query(Reservation).filter_by(
            day=chosen_day,
            slot=update.message.text
        ).first()
        if check is None:
            res = Reservation(
                user_id=update.message.chat.id,
                day=chosen_day,
                slot=update.message.text
            )
            sess.add(res)
            waitinglist = sess.query(WaitingList).filter(
                WaitingList.user_id == update.message.chat.id,
                WaitingList.day == date(chosen_day.year, chosen_day.month, chosen_day.day),
            ).first()
            if waitinglist:
                sess.delete(waitinglist)
            sess.commit()

            text = 'Time `' + chosen_day.strftime("%Y-%m-%d %H:%M") + '` reserved successfully'
            update.message.reply_text(text, reply_markup=ReplyKeyboardMarkup(base.main_menu, resize_keyboard=True), parse_mode=ParseMode.MARKDOWN)
            return ConversationHandler.END
        update.message.reply_text('This hour is already reserved')
    elif update.message.text == 'Back':
        context.user_data['wrong_day'] = True
        choose_month(update, context)
        return DAY
    elif update.message.text == 'Subscribe to waiting list':
        response = subscribe_user_to_waiting_list(context, update.message.chat.id)
        update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)
        base.cancel(update, context)
        return ConversationHandler.END
    elif update.message.text == 'Cancel':
        base.cancel(update, context)
        return ConversationHandler.END
    else:
        context.user_data['wrong_hour'] = True
        update.message.reply_text('Wrong hour')
    choose_day(update, context)
    return HOUR
    


def cancel(update, context):
    update.message.reply_text("Cancelling...", reply_markup=ReplyKeyboardMarkup(base.main_menu, resize_keyboard=True))
    return ConversationHandler.END

##########################################################################
###########   Add the user to waitlist NR-21                 #############
##########################################################################

def subscribe_user_to_waiting_list(context, user_id):
    chosen_day = date(YEAR, int(context.user_data['month']), int(context.user_data['day']))
    waitinglist = sess.query(WaitingList).filter(
        WaitingList.user_id == user_id,
        WaitingList.day == chosen_day,
    ).first()
    if waitinglist:
        return  'You are already in Waiting list for `' + chosen_day.strftime("%Y-%m-%d") + '`'
    new_waitinglist = WaitingList(
        user_id=user_id,
        day=chosen_day,
    )
    sess.add(new_waitinglist)
    sess.commit()
    return  'You are added to Waiting list successfully for `' + chosen_day.strftime("%Y-%m-%d") + '`. The bot will notify you if any reservation on this day is cancelled'


#ConversationHandler to create reservations
reserve_conv_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex('^(🖊 Reserve)$'), reserve)],
    states={
        MONTH: [
            MessageHandler(Filters.text, choose_month),
        ],
        DAY: [
            MessageHandler(Filters.text, choose_day),
        ],
        HOUR: [
            MessageHandler(Filters.text,choose_hour),
        ],
    },

    fallbacks=[MessageHandler(Filters.regex('^Cancel$'), cancel)],
    name="create_reserve_conversation",
    persistent=True
)