import requests
import argparse
import datetime
from environs import Env
from get_extension import get_extension
from get_picture import get_picture


def fetch_earth_polychromatic_imaging(api_key, date):
    params = {
        'api_key': api_key,
    }
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=params)

    data_nasa = response.json() if response.ok else []
    links = [
        requests.get(f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/epic_1b_{image_data['identifier']}.png",
                     params=params).url for image_data in data_nasa]

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
