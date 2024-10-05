# Programme to get information from the web and to familiarise myself with JSON
# Author: Andrew Beatty

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print (data['bpi']['EUR']['rate_float'])