import requests
from bs4 import BeautifulSoup

class BaseParser:
    URL = 'https://upl.uz'

    def get_soup(self, url=URL):
        response = requests.get(url)
        response.raise_for_status()  # != 200
        return BeautifulSoup(response.text, 'html.parser')

