import requests
from requests.exceptions import HTTPError

# take the raise on exception instead of checking the response status code (s_code.py example)

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
    print ("inspecting object attributes")
    for attr, value in response.__dict__.items():
        print ("Attribute: " + str(attr or ""))
        print ("Value: " + str(value or ""))