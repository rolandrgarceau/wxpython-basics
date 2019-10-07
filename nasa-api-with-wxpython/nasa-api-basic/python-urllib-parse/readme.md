# Before diving in

Look at `import requests`. This is what the NASA app is using.

## Python [urllib.parse](https://docs.python.org/3/library/urllib.parse.html)

The urllib.parse module defines functions that fall into two broad categories: URL parsing and URL quoting. 

## urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)

Will return a 6-item named tuple of the URL, broken into their constituent parts.

#### general structure of a URL: 

scheme://netloc/path;parameters?query#fragment

#### what happens?

Each tuple is a string, possibly empty, and the delimiters are removed- except for the leading slash in path. There are rules for the breakdown. 

```py
>>> from urllib.parse import urlparse
>>> o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
>>> o   # doctest: +NORMALIZE_WHITESPACE
ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
            params='', query='', fragment='')
>>> o.scheme
'http'
>>> o.port
80
>>> o.geturl()
'http://www.cwi.nl:80/%7Eguido/Python.html'
```

## [Urllib3](https://github.com/urllib3/urllib3)

urllib3 brings many critical features that are missing from the Python standard libraries: