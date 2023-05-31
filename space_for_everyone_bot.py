import os
import random
import time
import argparse
import telegram
from environs import Env


def main():
    env = Env()
    env.read_env()
    parser = argparse.ArgumentParser(description='Telegram-бот для публикации фотографий')
    parser.add_argument('--dir', type=str, required=True,
                        help='Каталог с фотографиями для публикации')
    parser.add_argument('--interval', type=int, default=3600,
                        help='Интервал в секундах для публикации фотографий')
    parser.add_argument('--photo', type=str, default=None,
                        help='Путь к фото для публикации')
    args = parser.parse_args()

    bot_token = env('TELEGRAM_TOKEN')
    chat_id = env('TG_CHAT_ID')
    bot = telegram.Bot(token=bot_token)
    if args.photo:
        photo_path = args.photo
    else:
        filenames = os.listdir(args.dir)
        photo_path = os.path.join(args.dir, random.choice(filenames))

    while True:
        bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
        time.sleep(args.interval)


if __name__ == '__main__':
    main()
