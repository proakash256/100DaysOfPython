import requests
from sms import *

MY_LOCATION = {"lat": 43.212170,
               "long": -8.691040
               }

parameters = {"latitude": MY_LOCATION["lat"],
              "longitude": MY_LOCATION["long"],
              "hourly": "weathercode"
              }

response = requests.get(url="https://api.open-meteo.com/v1/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
weathercode_data = weather_data["hourly"]["weathercode"]
will_rain = False
for condition_code in weathercode_data:
    if condition_code > 50:
        will_rain = True
if will_rain:
    send_sms()
