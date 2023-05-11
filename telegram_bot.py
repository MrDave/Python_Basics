import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


load_dotenv()


token = os.getenv('TG_TOKEN')


def wait(chat_id, text):

    time = parse(text)

    try:
        bot.create_timer(time, countdown, chat_id=chat_id)
    except TypeError:
        bot.send_message(chat_id, "Неверно задано время")

    print('Пользователь ID:{} включил таймер на {} секунд'.format(chat_id, text))


def countdown(chat_id):
    message = "Время вышло!"
    bot.send_message(chat_id, message)


bot = ptbot.Bot(token)
bot.reply_on_message(wait)
bot.run_bot()
