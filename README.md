<div align="center">
  <a href="https://github.com/thiiagoms/links-extractor">
      <img src="./assets/img/clamp.png" alt="Logo" width="80" height="80">
  </a>
  <h3>Extract links from urls :clamp: </h3>
  <p float="left">
    <img
      src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"
      alt="Python"
    />
  </p>
</div>
Library that allows for the extraction of links from web pages

- [Dependencies :heavy_plus_sign:](#dependencies)
- [Install :package:](#install)
- [Run :runner:](#run)
- [Bonus :medal_sports:](#bonus)

## Dependencies
- Python 3.8+
- Requests
- BeautifulSoup

## Install

01 -) Clone:
```shell
$ git clone https://github.com/thiiagoms/links-extractor
```

02 -) Go to `links-extractor` directory:
```shell
$ cd links-extractor
links-extractor $
```

## Run

01 -) In your `script.py` call `Extractor` main class like:
```python
from src.services.extractor import Extractor
from src.utils.printer import Printer

urls = ['https://github.com', 'https://google.com']
extractor = Extractor()
links = extractor.extract(urls, timeout=10)

for url, extracted_links in links.items():
    Printer.message(f"Url: {url}")
    for link in extracted_links:
        Printer.success(f" { link}")
    Printer.message("###############")
```

And you should receive this output:
```text
$ python example.py

Url: https://github.com

  #start-of-content
  https://github.com/
  /signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home
  /features/actions
  /features/packages
  /features/security

###############

Url: https://google.com

  https://www.google.com/imghp?hl=pt-BR&tab=wi
  https://maps.google.com.br/maps?hl=pt-BR&tab=wl
  https://play.google.com/?hl=pt-BR&tab=w8

###############
```


## Bonus

01 -) Run tests with **pytest**:
```bash
links-extractor $ pytest
```

02 -) Run **autopep8** lint on files like:
```bash
links-extractor $  autopep8 --in-place --aggressive --aggressive src/services/extractor.py
```
p