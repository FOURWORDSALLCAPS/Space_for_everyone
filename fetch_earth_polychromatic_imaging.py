import requests
import argparse
import datetime
from environs import Env
from get_extension import get_extension
from get_picture import get_picture
from urllib.parse import urlencode


def fetch_earth_polychromatic_imaging(api_key, date):
    params = {
        'api_key': api_key,
    }
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=params)
    links = []
    if response.ok:
        data_list_nasa = response.json()
        for item in data_list_nasa:
            image_id = item["identifier"]
            url = f"https://api.nasa.gov/EPIC/archive/natural/{args.d}/png/epic_1b_{image_id}.png?{urlencode(params)}"
            links.append(url)

    for link_number, link in enumerate(links):
        extension = get_extension(link)
        if extension:
            get_picture(link, f"images/nasa_epic_{link_number}{extension}")


def main():
    env = Env()
    env.read_env()
    parser = argparse.ArgumentParser(
        description='Скрипт скачивает полихроматическое изображение Земли'
    )
    parser.add_argument(
        '-d',
        default=(datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y/%m/%d'),
        help='Введите дату формата YYYY/MM/DD')
    args = parser.parse_args()
    api_key = env('NASA_TOKEN')
    fetch_earth_polychromatic_imaging(api_key, args.d)


if __name__ == '__main__':
    main()
