import requests
import argparse
from get_picture import get_picture


def fetch_spacex_last_launch(identifier):
    link_response = requests.get(f"https://api.spacexdata.com/v5/launches/{identifier}")
    data_spacex = link_response.json()

    links = [image_data for image_data in data_spacex["links"]["flickr"]["original"]] if link_response.ok else []

    for link_number, link in enumerate(links):
        get_picture(link, f"images/spacex_{link_number}.jpg")


def main():
    parser = argparse.ArgumentParser(
        description='Скрипт скачивает фотографии запуска SapceX'
    )
    parser.add_argument('-i', default='5eb87d47ffd86e000604b38a', help='Введите id запуска')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.i)


if __name__ == '__main__':
    main()
