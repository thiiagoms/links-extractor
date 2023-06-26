import unittest
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'src'))
sys.path.append(src_dir)

from services.extractor import Extractor

class ExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.extractor = Extractor()

    def test_extract_links(self):
        """
        Test case to verify the extraction of links.
        """
        urls = [
            'https://example.com',
            'https://google.com',
            'https://stackoverflow.com']
        links = self.extractor.extract(urls, timeout=10)
        self.assertTrue(len(links) > 0)
