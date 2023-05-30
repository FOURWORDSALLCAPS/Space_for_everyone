import requests
from pathlib import Path

Path('images_spacex').mkdir(parents=True, exist_ok=True)


def get_picture(url, path):
    response = requests.get(url)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    link_response = requests.get("https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a")

    json_data = link_response.json()

    links = []
    if link_response.status_code == 200:
        for item in json_data["links"]["flickr"]["original"]:
            links.append(item)
    else:
        print("Error:", link_response.status_code)

    for link_number, link in enumerate(links):
        get_picture(link, f"images_spacex/spacex_{link_number}.jpg")
