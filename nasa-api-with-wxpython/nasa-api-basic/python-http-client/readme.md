# Python docs on [http.client](https://docs.python.org/3/library/http.client.html)

Write your own, or use the one that is already there?  How about importing [requests] instead. There we go talking about wheels again. Spinning, spinning, spinning. [Urllib3](https://github.com/urllib3/urllib3) This one is the friendly modern [http client](https://urllib3.readthedocs.io/en/latest/)

Whats in requests that's not in http.client? Do we need something different for HTTP/2? We are testing the NASA application with importing requests and docs from nasa call out curl usage.

[Here](https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-urllib3-and-requests-modul) is a semi-stale answer.

## [Urllib3](https://github.com/urllib3/urllib3)
The answer- TA-DAAAAAAAHHHHH! Wait a second, that looks like a curl request to me.
```py

>>> import urllib3
>>> http = urllib3.PoolManager()
>>> r = http.request('GET', 'http://httpbin.org/robots.txt')
>>> r.status
200
>>> r.data
'User-agent: *\nDisallow: /deny\n'
```