#!/usr/bin/env python3

from requests import get
from bs4 import BeautifulSoup

class Extractor:

    def __init__(self, url: str):
        self.__url = url
    
    def _send_request(self) -> BeautifulSoup:
        reqs = get(self.__url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        return soup
    
    def cli_printer(self, response: BeautifulSoup) -> None:
        urls = []
        for link in response.find_all('a'):
            print(f"[*] Link: {link.get('href')}")

url = input(">>> URL here: ")
extractor = Extractor(url)
response = extractor._send_request()
extractor.cli_printer(response)