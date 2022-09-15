from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes, CallbackContext
import rational
import spy


def hello(update: Update, context: CallbackContext):
    spy.log(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def sum_handler(update: Update, context: CallbackContext):
    spy.log(update, context)
    a = update.message.text.split()
    if a[1] == '1':
        update.message.reply_text(f'{a[2]}+{a[3]}={rational.r_sum(float(a[2]), float(a[3]))}')
    if a[1] == '2':
        update.message.reply_text(f'{a[2]}+{a[3]}={rational.r_sum(complex(a[2]), complex(a[3]))}')


def sub_handler(update: Update, context: CallbackContext):
    spy.log(update, context)
    a = update.message.text.split()
    if a[1] == '1':
        update.message.reply_text(f'{a[2]}-{a[3]}={rational.r_sub(float(a[2]), float(a[3]))}')
    if a[1] == '2':
        update.message.reply_text(f'{a[2]}-{a[3]}={rational.r_sub(complex(a[2]), complex(a[3]))}')


def mul_handler(update: Update, context: CallbackContext):
    spy.log(update, context)
    a = update.message.text.split()
    if a[1] == '1':
        update.message.reply_text(f'{a[2]}*{a[3]}={rational.r_mul(float(a[2]), float(a[3]))}')
    if a[1] == '2':
        update.message.reply_text(f'{a[2]}*{a[3]}={rational.r_mul(complex(a[2]), complex(a[3]))}')


def div_handler(update: Update, context: CallbackContext):
    spy.log(update, context)
    a = update.message.text.split()
    if a[1] == '1':
        update.message.reply_text(f'{a[2]}:{a[3]}={rational.r_div(float(a[2]), float(a[3]))}')
    if a[1] == '2':
        update.message.reply_text(f'{a[2]}:{a[3]}={rational.r_div(complex(a[2]), complex(a[3]))}')



app = Updater('5500997377:AAGMhXnVXEGZS38Sdzm2cRxXXUeSBI94ueA')
app.dispatcher.add_handler(CommandHandler("hello", hello))
app.dispatcher.add_handler(CommandHandler('sum', sum_handler))
app.dispatcher.add_handler(CommandHandler('sub', sub_handler))
app.dispatcher.add_handler(CommandHandler('mul', mul_handler))
app.dispatcher.add_handler(CommandHandler('div', div_handler))


app.start_polling()
app.idle()