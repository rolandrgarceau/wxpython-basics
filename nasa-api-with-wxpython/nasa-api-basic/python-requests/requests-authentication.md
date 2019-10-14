# Authentication with requests 

Authorization headers are used, or other custom header defined by the service. All the request functions you’ve seen to this point provide a parameter called auth, which allows you to pass your credentials.

### [GitHub’s](https://developer.github.com/v3/users/#get-the-authenticated-user) Authenticated User API

Some API's require the `auth` argument or key value pair passed with the request. When we pass our username and password in a tuple to the auth parameter, requests is applying the credentials using HTTP’s Basic access authentication scheme under the hood- the all familiar `Authorization: Basic` Basic Authentication is typically used in conjunction with HTTPS to provide confidentiality. This method may not meet bare minimum best security practices, but may pass your initial sprint requirements, see below for digest and proxy auth with http.

To make a request to the Authenticated User API, you can pass your GitHub username and password in a tuple to get():

```py
from getpass import getpass
requests.get('https://api.github.com/user', auth=('username', getpass()))
#<Response [200]>

# the next one fails because the API requires the `auth` 
requests.get('https://api.github.com/user')
# 401 response
```

```py
from requests.auth import HTTPBasicAuth
from getpass import getpass

requests.get(
     'https://api.github.com/user',
     auth=HTTPBasicAuth('username', getpass())
)
# <Response [200]>

```

###  HTTPDigestAuth and HTTPProxyAuth.


### Create our own

1. Create a subclass of AuthBase. 
2. Then implement __call__():

```py
import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))
```