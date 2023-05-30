import requests
from pathlib import Path
from os.path import splitext, splitdrive
from urllib.parse import urlparse
from environs import Env
from get_extension import get_extension
from get_picture import get_picture

env = Env()
env.read_env()


api_key = env('API_KEY')


def fetch_earth_polychromatic_imaging():
    link_response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}")

    links = []
    if link_response.status_code == 200:
        data = link_response.json()
        for item in data:
            image_id = item["identifier"]
            date = item["date"].split()[0].replace("-", "/")
            url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/epic_1b_{image_id}.png?api_key={api_key}"
            links.append(url)
    else:
        print("Error:", link_response.status_code)

    for link_number, link in enumerate(links):
        if not get_extension(link) == '':
            get_picture(link, f"images/nasa_epic_{link_number}{get_extension(link)}")
