# Python Module requests

We are able to import requests and urllib3 from directly within ipython, but being a good environmental steward- heavy on the mental, lights out if you call me steward again- we will stay here for a moment to see how the module requests work in python.

## Examples from [Real Python](https://realpython.com/python-requests/)

### Handle Errors

A couple of scripts here to handle things as they come in with responses. Notice attribute inspection and then how we use those attributes programmatically afterword.

#### s_code.py

Simple if statement to check certain values with. then a way to investigate the response object a little better.

```py
import requests

# basic start to handling errors. se the raise-for-status next

response = requests.get('https://api.github.com')
s_code = response.status_code

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

if s_code == 200:
    print("OK")
elif s_code == 404:
    print("Not There")

# not so intuitive way to see the objects innards...
# for attr, value in response.__dict__.items():
#         print(attr, value)

#for attr, value in response.__dict__.iteritems(): # no attribute iteritems
for attr, value in response.__dict__.items():
    print ("Attribute: " + str(attr or ""))
    print ("Value: " + str(value or ""))
```

#### raise-for-status.py

If everything is running "A-OK" can we shorten the papertrail just a little? If we invoke .raise_for_status(), an `HTTPError` will be raised for *certain* status codes. 200's slide...

### Content

This is the part we are really looking to get from our server request: what did it find and give us other than the response code? If we use the `.content` we get back bytes Objects, and each element in a bytes object is a small integer in the range 0 to 255. Bytes objects are immutable sequences of single byte values. The bytes object is a b uilt in type for manipulating binary data. The bytes() function also creates a bytes object.