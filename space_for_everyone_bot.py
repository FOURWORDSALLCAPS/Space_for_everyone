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
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--dir', type=str,
                        help='Каталог с фотографиями для публикации')
    group.add_argument('--photo', type=str,
                        help='Путь к фото для публикации')
    parser.add_argument('--interval', type=int, default=14400,
                        help='Интервал в секундах для публикации фотографий')
    args = parser.parse_args()

    bot_token = env('TELEGRAM_TOKEN')
    chat_id = env('TG_CHAT_ID')
    bot = telegram.Bot(token=bot_token)

    if args.photo:
        with open(args.photo, 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)
    else:
        while True:
            filenames = os.listdir(args.dir)
            photo_path = os.path.join(args.dir, random.choice(filenames))
            with open(photo_path, 'rb') as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
            time.sleep(args.interval)


if __name__ == '__main__':
    main()
