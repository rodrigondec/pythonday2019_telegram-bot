import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token='999651935:AAGi5RcJ08qR90m8G-0xXp26q_ZC5P0-CzM')


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, eu sou o bot do Python Day 2019!")


def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='world!')


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))


if __name__ == "__main__":
    updater.start_polling()
