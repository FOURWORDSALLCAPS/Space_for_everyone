import requests
import argparse
from environs import Env
from get_extension import get_extension
from get_picture import get_picture


def fetch_astronomy_picture_day(api_key, args):
    link_response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}&count={args.c}")
    links = []
    if link_response.ok:
        data_list_nasa = link_response.json()
        for item in data_list_nasa:
            links.append(item["url"])
    else:
        print("Error:", link_response.status_code)

    for link_number, link in enumerate(links):
        if not get_extension(link) == '':
            get_picture(link, f"images/nasa_apod_{link_number}{get_extension(link)}")


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
