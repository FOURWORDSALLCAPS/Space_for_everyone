import requests
from pathlib import Path


def get_picture(url, path):
    Path("images").mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)
