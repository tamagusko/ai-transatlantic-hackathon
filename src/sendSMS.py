# (c) Tiago Tamagusko 2022
# Source: https://www.twilio.com/docs/sms/quickstart/python
"""
Sends an sms using Twilio API.

Usage:
    $ sendSMS(delivery_id, client_phone)

Example:
    # send a sms to the phone 1234567890
    $ sendSMS(20220415_1, 1234567890)
"""
from __future__ import annotations

import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()  # secrets are saved on .env file
# .env: TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE


def sendSMS(delivery_id: str, phone: str):
    # authenticate with twilio
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    # gen the message
    text_to_send = f'Delivery {delivery_id} should be delivered within approximately 1 hour. \
        Are you at home to receive the order? Reply y or n to confirm delivery.'

    # send the message
    message = client.messages \
        .create(
            body=text_to_send,
            from_=os.getenv('TWILIO_PHONE'),
            to=phone,
        )
    return message.sid


# test: sendSMS('20220415_1', '+351 914557970')