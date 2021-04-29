<center>
   <h1>Link extractor</h1>
</center>
<br>
<img src="img/clamp.png" alt="Extract links" style="height: 100px; width:100px; display: block; margin-left: auto; margin-right: auto; width: auto"/>
<br>

<h3> Extract all links from websites</h3>

## => run with pipenv :snake:
```bash
$ pipenv install
$ pipenv shell
$ python extractor.py
```
## => run with docker :whale:
```docker
$ docker build -t extractor .
$ docker run -i -t extractor
```

## and then, input the site url, for example:
```bash
>>> URL here: https://github.com
```
