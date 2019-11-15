from handler.base import unknown
from handler.view import view_reservations
from handler.confirmation import check_confirmation


def keyboard_handler(update, context):
    if update.message.text == '📖 View reservations':
        view_reservations(update, context)
    elif update.message.text == '✅ Confirm' or update.message.text == '❌ Cancel':
        check_confirmation(update, context)
    else:
        unknown(update, context)
