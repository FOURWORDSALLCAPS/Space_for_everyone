import requests
import argparse
from environs import Env
from get_extension import get_extension
from get_picture import get_picture


def fetch_earth_polychromatic_imaging(api_key, args):
    link_response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}")

    links = []
    if link_response.ok:
        data_list_nasa = link_response.json()
        for item in data_list_nasa:
            image_id = item["identifier"]
            url = f"https://api.nasa.gov/EPIC/archive/natural/{args.d}/png/epic_1b_{image_id}.png?api_key={api_key}"
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
    args = parser.parse_args()
    api_key = env('NASA_TOKEN')
    fetch_earth_polychromatic_imaging(api_key, args)


if __name__ == '__main__':
    main()
