# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def send_sms(message):
    account_sid = "ACb2ad4379c248cfc7652eb699c001dfbf"
    auth_token = "72b0755db80f7d535eac671fba85fabc"
    client = Client(account_sid, auth_token)

    message = client.messages.create(body=message,
                                     from_='+12706409353',
                                     to='+916387744330')
    print(message.status)
