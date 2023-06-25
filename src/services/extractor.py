"""
extractor.py

This module contains the Extractor class, which is responsible for
extracting all links from a list of URLs asynchronously,
using concurrent execution with a timeout interval between URL requests.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from requests import get
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

try:
    from src.utils.printer import Printer
except ImportError:
    from utils.printer import Printer

class Extractor:
    """
    Class for extracting links from web pages.
    """

    def _send_request(self, url: str) -> BeautifulSoup:
        """
        Send an HTTP GET request to URL and return the BeautifulSoup object from the response.

        Args:
            url (str): The URL to send the GET request to.

        Returns:
            BeautifulSoup: The BeautifulSoup object representing the HTML response.
        """
        req = get(url,timeout=2) # default timeout to get url
        return BeautifulSoup(req.text, 'html.parser')

    def get_links(self, url: str) -> list:
        """
        Extract links from a web page.

        Args:
            url: The URL of the web page to extract links from.

        Returns:
            list: A list of extracted links.
        """
        response = self._send_request(url)
        urls = []
        for link in response.find_all('a'):
            urls.append(link.get('href'))
        return urls

    def extract(self, urls: list, timeout: int) -> list:
        """
        Extract links from multiple web pages using concurrent execution.

        Args:
            urls (list): A list of URLs to extract links from.
            timeout (int): The maximum timeout for each URL request.

        Returns:
            dict: A dictionary mapping each URL to a list of extracted links.
        """
        all_links = {}
        with ThreadPoolExecutor() as executor:
            future_to_url = {
                executor.submit(
                    self.get_links,
                    url): url for url in urls}
            for future in as_completed(
                    future_to_url, timeout=timeout):
                url = future_to_url[future]
                try:
                    links = future.result()
                    all_links[url] = links
                except HTTPError as exception:
                    Printer.error(
                        f"Error retrieving links for URL: {url}, Exception: {exception}")
        return all_links
