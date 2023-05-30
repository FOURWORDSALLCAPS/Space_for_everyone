from os.path import splitext, splitdrive
from urllib.parse import urlparse


def get_extension(url):
    url_parse = urlparse(url)
    path = splitdrive(f'{url_parse.path}')[1]
    extension = splitext(path)[1]
    return extension
