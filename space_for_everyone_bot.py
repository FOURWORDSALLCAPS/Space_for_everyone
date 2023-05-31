import os
import random
import time
import argparse
import telegram
from environs import Env


def main():
    parser = argparse.ArgumentParser(description='Telegram-бот для публикации фотографий')
    parser.add_argument('--dir', type=str, required=True,
                        help='Каталог с фотографиями для публикации')
    parser.add_argument('--interval', type=int, default=3600,
                        help='Интервал в секундах для публикации фотографий')
    args = parser.parse_args()
    bot_token = env('BOT_TOKEN')
    chat_id = env('CHAT_ID')
    bot = telegram.Bot(token=bot_token)
    filenames = os.listdir(args.dir)

    while True:
        photo_path = os.path.join(args.dir, random.choice(filenames))
        bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
        time.sleep(args.interval)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    main()
