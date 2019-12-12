# -*- coding: utf-8 -*-
"""
 Simple extraction links tool
"""
import urllib.request as url_lib
from re import findall
from sys import argv


# parse the target 
url = argv[1]
print(f"[*] connection to {url}")
# connecting to url
con_site = url_lib.urlopen(url)
print("[*] reading...")
# read html code
html_response = con_site.read().decode('utf-8')
# parsing
print("[*] parsing...")
# with regex to gel all the links
links = findall('"((http|ftp)s?://.*?)"', html_response)
# print links
print(links)
