from requests.auth import HTTPBasicAuth
from getpass import getpass

requests.get(
     'https://api.github.com/user',
     auth=HTTPBasicAuth('username', getpass())
)
# <Response [200]>