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


def fetch_astronomy_picture_day():
    link_response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}&count=30")

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
