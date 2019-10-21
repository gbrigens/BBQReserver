from handler.base import cancel, unknown
from handler.cancel import cancel_reservation
from handler.reserve import reserve, choose_month, choose_day, choose_hour, userState
from handler.view import view_reservations


def keyboard_handler(update, context):
    if update.message.chat.id in userState and 'state' in userState[update.message.chat.id]:

        if userState[update.message.chat.id]['state'] == 'month':
            if choose_month(update, context):
                userState[update.message.chat.id]['state'] = 'day'
                return

        elif userState[update.message.chat.id]['state'] == 'day':
            if choose_day(update, context):
                userState[update.message.chat.id]['state'] = 'slot'
                return

        elif userState[update.message.chat.id]['state'] == 'slot':
            if choose_hour(update, context):
                userState[update.message.chat.id]['state'] = 'slot'
                cancel(update, context)
                return

    if update.message.text == '🖊 Reserve':
        reserve(update, context)
        userState[update.message.chat.id] = {}
        userState[update.message.chat.id]['state'] = 'month'
    elif update.message.text == '🗑 Cancel reservation':
        cancel_reservation(update, context)
    elif update.message.text == '📖 View reservations':
        view_reservations(update, context)
    else:
        unknown(update, context)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
