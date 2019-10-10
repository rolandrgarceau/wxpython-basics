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