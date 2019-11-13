from handler.base import cancel, unknown
from handler.cancel import cancel_reservation, delete_reservation
from handler.reserve import reserve, choose_month, choose_day, choose_hour, userState
from handler.view import view_reservations


def keyboard_handler(bot, update):
    if update.message.chat.id in userState and 'state' in userState[update.message.chat.id]:
        if userState[update.message.chat.id]['state'] == 'month':
            if choose_month(bot, update):
                userState[update.message.chat.id]['state'] = 'day'
                return

        elif userState[update.message.chat.id]['state'] == 'day':
            if choose_day(bot, update):
                userState[update.message.chat.id]['state'] = 'slot'
                return

        elif userState[update.message.chat.id]['state'] == 'slot':
            if choose_hour(bot, update):
                userState[update.message.chat.id]['state'] = 'slot'
                cancel(bot, update)
            return

        elif userState[update.message.chat.id]['state'] == 'cancel':
            delete_reservation(bot, update)
            return

    if update.message.text == '🖊 Reserve':
        reserve(bot, update)
        userState[update.message.chat.id] = {}
        userState[update.message.chat.id]['state'] = 'month'
    elif update.message.text == '🗑 Cancel reservation':
        cancel_reservation(bot, update)
        userState[update.message.chat.id]['state'] = 'cancel'
    elif update.message.text == '📖 View reservations':
        view_reservations(bot, update)
    else:
        unknown(bot, update)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
