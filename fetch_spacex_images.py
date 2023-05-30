import requests
import argparse
from get_picture import get_picture


def fetch_spacex_last_launch(user_id):
    link_response = requests.get(f"https://api.spacexdata.com/v5/launches/{user_id.i}")

    json_data = link_response.json()

    links = []
    if link_response.status_code == 200:
        for item in json_data["links"]["flickr"]["original"]:
            links.append(item)
    else:
        print("Error:", link_response.status_code)

    for link_number, link in enumerate(links):
        get_picture(link, f"images/spacex_{link_number}.jpg")


def main():
    parser = argparse.ArgumentParser(
        description='Скрипт скачивает астрономическую картину дня'
    )
    parser.add_argument('-i', default='5eb87d47ffd86e000604b38a', help='Введите id запуска')
    user_id = parser.parse_args()
    fetch_spacex_last_launch(user_id)


if __name__ == '__main__':
    main()
