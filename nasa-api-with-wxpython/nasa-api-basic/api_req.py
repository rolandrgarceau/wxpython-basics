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
# 
# place this in a file to be parsed?
#
# file open > write to it > extract information from it 
print(data) # for now just stdout

# extract data
# def extract_first_item(data):

item = data['collection']['items'][0]
nasa_id = item['data'][0]['nasa_id']
asset_url = 'https://images-api.nasa.gov/asset/' + nasa_id
image_request = requests.get(asset_url)
image_json = image_request.json()
image_urls = [url['href'] for url in image_json['collection']['items']]

print("New Data extraction")
print('#')
print('#')
print('#')
print(image_urls)