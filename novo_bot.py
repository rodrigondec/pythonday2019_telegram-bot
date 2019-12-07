from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater(token="999651935:AAGi5RcJ08qR90m8G-0xXp26q_ZC5P0-CzM", use_context=True)


lista_de_usuarios = set()


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá!")


def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="World!")


def caps(update, context):
    text_caps = " ".join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def echo(update, context):
    message = updater.message
    texto = message.text
    lista_de_usuarios.add(update.message.from_user.first_name)
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    print(lista_de_usuarios)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{lista_de_usuarios}")

updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('caps', caps))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

if __name__ == "__main__":
    print('Meu bot está on!')
    updater.start_polling()