from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater(token='999651935:AAGi5RcJ08qR90m8G-0xXp26q_ZC5P0-CzM', use_context=True)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Oi, sou o bot do Python Day 2019!')


def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='world!')


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.dispatcher.add_handler(CommandHandler('caps', caps))


if __name__ == "__main__":
    print('Meu bot esta rodando!')
    updater.start_polling()
