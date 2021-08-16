# - *- coding: utf- 8 - *-
import config
import logging
import requests
import json
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

telegram_id = '644907626'
api_key_telegram = '1649437858:AAE7soGnFekNgmwIqyzKa_P7ZXXU4g-wU3Q'
api_url = 'https://wowfluence.com/version-test/api/1.1/obj/'
bubble_key = 'Bearer 33be6ff8b56d8a10d8f656a1a0108db3'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    user = update.message.from_user
    update.message.reply_text (('Привет! Добро пожаловать в бот WoWFluence. Чтобы завершить регистрацию и получать индивидуальные рекламные предложения следуйте инструкции.')+ '\n' + ('2.Нажмите /ID и скопируйте ваш ID') + '\n' + ('3.Вставьте свой ID в окне на сайте:https://wowfluence.com/version-test/test1?debug_mode=true'))
    
   
    print('ID: {} '.format(user['id']))


def id(update, context):
    user = update.message.from_user
    update.message.reply_text('{}'.format(user['id']))


def echo(update, context):

    print('{}' + update.message.text)

def error(update, context):

    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    updater = Updater("1879800208:AAHFl8jpC5bHL5zegfyMGiRv6ocGVXQxFD0", use_context=True)


    dp = updater.dispatcher

  
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ID", id))
    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

  
    updater.start_polling()

   
    updater.idle()

bot.polling(none_stop=True)

if __name__ == '__main__':
    main()

