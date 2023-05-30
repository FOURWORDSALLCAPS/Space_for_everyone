import os
import random
import time
import argparse
import telegram
from telegram.ext import Updater
from environs import Env

env = Env()
env.read_env()

parser = argparse.ArgumentParser(description='Telegram-бот для публикации фотографий')
parser.add_argument('--dir', type=str, required=True,
                    help='Каталог с фотографиями для публикации')
parser.add_argument('--interval', type=int, default=3600,
                    help='Интервал в секундах для публикации фотографий')
args = parser.parse_args()

bot = telegram.Bot(token='TOKEN')
filenames = os.listdir(args.dir)

while True:
    photo_path = os.path.join(args.dir, random.choice(filenames))
    bot.send_photo(chat_id='@Space_for_everyone', photo=open(photo_path, 'rb'))
    time.sleep(args.interval)
