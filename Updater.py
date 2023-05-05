# - *- coding: utf- 8 - *-
import config
import logging
import requests
import json
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Define the API key for the Telegram bot
api_key_telegram = '1649437858:AAE7soGnFekNgmwIqyzKa_P7ZXXU4g-wU3Q'

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the start command for the bot
def start(update, context):
    user = update.message.from_user
    update.message.reply_text(('Привет! Добро пожаловать в бот WoWFluence. Чтобы завершить регистрацию и получать индивидуальные рекламные предложения следуйте инструкции.')+ '\n' + ('2.Нажмите /ID и скопируйте ваш ID') + '\n' + ('3.Вставьте свой ID в окне на сайте:https://wowfluence.com/version-test/test1?debug_mode=true'))
    print('ID: {} '.format(user['id']))

# Define the ID command for the bot
def id(update, context):
    user = update.message.from_user
    update.message.reply_text('{}'.format(user['id']))

# Define the echo function for the bot
def echo(update, context):
    print('{}' + update.message.text)

# Define the error handler for the bot
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Define the main function for the bot
def main():
    updater = Updater(api_key_telegram, use_context=True)
    dp = updater.dispatcher

    # Add the start, ID, and echo commands to the dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ID", id))
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Add the error handler to the dispatcher
    dp.add_error_handler(error)

    # Start polling for updates
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the program is otherwise stopped
    updater.idle()

# Run the main function when the script is executed
if __name__ == '__main__':
    main()
