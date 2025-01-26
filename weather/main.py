import requests
import json
import os
city = input("enter the name of the city\n")
url= f"https://api.weatherapi.com/v1/current.json?key=119338b2f2da432bb14170256252601&q={city}"
r= requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
os.system(f"say 'The current weather in {city} is {w} degrees'")