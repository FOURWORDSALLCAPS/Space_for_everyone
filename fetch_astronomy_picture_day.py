import requests
import argparse
from environs import Env
from get_extension import get_extension
from get_picture import get_picture


def fetch_astronomy_picture_day(api_key, args):
    link_response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}&count={args.c}")
    links = [item["url"] for item in link_response.json()] if link_response.ok else []

    for link_number, link in enumerate(links):
        extension = get_extension(link)
        if extension:
            get_picture(link, f"images/nasa_apod_{link_number}{extension}")


def main():
    env = Env()
    env.read_env()
    parser = argparse.ArgumentParser(
        description='Скрипт скачивает астрономическую картину дня'
    )
    parser.add_argument('-c', default='2', help='Введите количество картинок')
    args = parser.parse_args()
    api_key = env('NASA_TOKEN')
    fetch_astronomy_picture_day(api_key, args)


if __name__ == '__main__':
    main()
