import requests
from environs import Env
from get_extension import get_extension
from get_picture import get_picture
import argparse


def fetch_earth_polychromatic_imaging(api_key, user_date):
    link_response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}")

    links = []
    if link_response.status_code == 200:
        data = link_response.json()
        for item in data:
            image_id = item["identifier"]
            url = f"https://api.nasa.gov/EPIC/archive/natural/{user_date.d}/png/epic_1b_{image_id}.png?api_key={api_key}"
            links.append(url)
    else:
        print("Error:", link_response.status_code)

    for link_number, link in enumerate(links):
        if not get_extension(link) == '':
            get_picture(link, f"images/nasa_epic_{link_number}{get_extension(link)}")


def main():
    env = Env()
    env.read_env()
    parser = argparse.ArgumentParser(
        description='Скрипт скачивает полихроматическое изображение Земли'
    )
    parser.add_argument(
        '-d',
        default='2023/05/29',
        help='Введите дату формата YYYY/MM/DD')
    user_date = parser.parse_args()
    api_key = env('API_KEY')
    fetch_earth_polychromatic_imaging(api_key, user_date)


if __name__ == '__main__':
    main()
