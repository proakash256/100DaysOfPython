import requests
from datetime import datetime
import mail
import time

MY_LOCATION = {"lat": 26.449923,
               "long": 80.331871
               }


# If the ISS is close to the current position,
# and it is currently dark then send an email
# reminding to look up.

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()

    iss_position = {"lat": float(iss_data["iss_position"]["latitude"]),
                    "long": float(iss_data["iss_position"]["longitude"])
                    }
    # Your position should be within +5 or -5 degrees of the ISS position.

    is_lat_overhead = (MY_LOCATION["lat"] - 5 <= iss_position["lat"] < MY_LOCATION["lat"] + 5)
    is_long_overhead = (MY_LOCATION["long"] - 5 <= iss_position["long"] < MY_LOCATION["long"] + 5)

    if is_lat_overhead and is_long_overhead:
        return True


def is_night():
    location = {
        "lat": MY_LOCATION["lat"],
        "lng": MY_LOCATION["long"],
        "formatted": 0
    }

    time_response = requests.get(url="https://api.sunrise-sunset.org/json", params=location)
    time_response.raise_for_status()
    data = time_response.json()
    sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]
    hour_now = datetime.now().hour

    if hour_now >= sunset_hour or hour_now <= sunrise_hour:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        mail.send_email()
