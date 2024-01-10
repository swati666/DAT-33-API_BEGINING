import requests
from _datetime import datetime
import time
import smtplib

sender_email = "your_email"
sender_pass = "app_password"
my_lng = 77.139679
my_lat = 28.685129


# todo- if ISS is close to my current location-- lets take -5 and +5 margin for the calculation.
def iss_close():
    iss_res = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_lng = float(iss_res.json()["iss_position"]["longitude"])
    iss_lat = float(iss_res.json()["iss_position"]["latitude"])

    if my_lng-5 <= iss_lng <= my_lng+5 and my_lat-5 <= iss_lat <= my_lat+5:
        return True


# todo- and if its currently dark
def is_dark():
    response = requests.get(url="https://api.sunrise-sunset.org/json?formatted=0&lng=77.139679&lat=28.685129")
    response.raise_for_status()
    sunrise = int(response.json()['results']["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response.json()['results']["sunset"].split("T")[1].split(":")[0])
    current = int(datetime.now().hour)

    if sunset <= current <= sunrise:
        return True


# todo- then send me an email to look up
if is_dark() and iss_close():
    pass


# todo-- BONUS run the code every 60 seconds.
loop = True
while loop:
    time.sleep(60)
    if is_dark() and iss_close():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=sender_email, password=sender_pass)
        connection.sendmail(
            to_addrs="swatiyadavcreate333@gmail.com",
            from_addr=sender_email,
            msg="subject:International space station reminder\n\nDarling.. LOOK UP INTO THE SKY."
        )


# syntax --some useful code snippet
#  param = {
#     "lng": 77.139679,
#     "lat": 28.685129
#     }
#   response = requests.get(url="https://api.sunrise-sunset.org/json?formatted=0", params=param)
