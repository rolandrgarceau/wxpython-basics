# simple_api_request.py
 
import requests
 
from urllib.parse import urlencode, quote_plus
 
# urllib.parse offers the ability to deconstruct full urls with .parse()
base_url = 'https://images-api.nasa.gov/search'
search_term = 'apollo 11'
desc = 'moon landing'
media = 'image'
query = {'q': search_term, 'description': desc, 'media_type': media}
full_url = base_url + '?' + urlencode(query, quote_via=quote_plus)
 
r = requests.get(full_url)
data = r.json()
print(data)