import requests
from environs import Env
from get_extension import get_extension
from get_picture import get_picture
import argparse


def fetch_astronomy_picture_day(api_key, user_count):
    link_response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}&count={user_count.c}")
    links = []
    if link_response.status_code == 200:
        json_data = link_response.json()
        for item in json_data:
            links.append(item["url"])
    else:
        print("Error:", link_response.status_code)

    for link_number, link in enumerate(links):
        if not get_extension(link) == '':
            get_picture(link, f"images/nasa_apod_{link_number}{get_extension(link)}")


def main():
    parser = argparse.ArgumentParser(
        description='Скрипт скачивает астрономическую картину дня'
    )
    parser.add_argument('-c', default='2', help='Введите число')
    user_count = parser.parse_args()
    api_key = env('API_KEY')
    fetch_astronomy_picture_day(api_key, user_count)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    main()
