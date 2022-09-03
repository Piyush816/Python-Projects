from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

from os import getenv
# for execessing the token
from dotenv import load_dotenv


import response as res


if __name__ == "__main__":
    # loading env file
    load_dotenv("./.env")

    updater = Updater(token=getenv("TOKEN"), use_context=True)

    dis = updater.dispatcher

    dis.add_handler(CommandHandler("start", res.start_command))
    dis.add_handler(CommandHandler("help", res.help_command))
    dis.add_handler(MessageHandler(Filters.text, res.message_handler))

    updater.start_polling()
    updater.idle()
