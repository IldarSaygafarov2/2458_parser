import requests
from bs4 import BeautifulSoup

class BaseParser:
    URL = 'https://upl.uz'

    def __init__(self):
        print('base parser working')

    def get_soup(self, url=URL):
        response = requests.get(url)
        response.raise_for_status()  # != 200
        return BeautifulSoup(response.text, 'html.parser')

