# (c) Tiago Tamagusko 2022
"""
Sends an sms asking if the client is at home to receive the order. Expected response: yes (y) or no (n).
If the answer is yes (y), the delivery continues, if it is no (n) it generates a closest Locker request.

Usage:
    $ python path/to/sendSMS.py --id DELIVERY_ID --phone NUMBER --time WAITING_TIME_IN_SECONDS

Example:
    # send a sms to the phone number 1234567890 and wait for a response for 2 minutes
    $ python path/to/sendSMS.py --id 20220415_1 --phone 1234567890 --time 120
"""
from __future__ import annotations

import argparse
import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()  # secrets are saved on .env file


def main():
    # Parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Send sms and wait for response (y or n)',
    )
    parser.add_argument(
        '-i', '--id',
        type=str,
        required=True,
        help='Delivery id',
    )
    parser.add_argument(
        '-p', '--phone',
        type=str,
        required=True,
        help='Provide phone for shipping. Supported formats: 222333444, 222,333,444, 222-333-444, 222 333 444',
    )
    parser.add_argument(
        '-t', '--time',
        type=int,
        default=300,  # 5 minutes
        help='Time to wait for client response',
    )
    args = parser.parse_args()

    def sendSMS(delivery_id, phone, waiting_time):
        text_to_send = f'Delivery {delivery_id} should take approximately 1 hour.  \
            Are you at home to receive the order? Reply y or n in the next {waiting_time} to confirm delivery.'
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=text_to_send,
            from_=os.getenv('TWILIO_PHONE_NUMBER'),
            # SMS messages sent limited to phone numbers that have been verified with Twilio (trial version)
            to=os.getenv('CLIENT1_PHONE_NUMBER'),
        )
        print(message.sid)
        sendSMS(args.id, args.phone, args.time)

        def get_response(delivery_id, phone, waiting_time):
            account_sid = os.getenv('TWILIO_ACCOUNT_SID')
            auth_token = os.getenv('TWILIO_AUTH_TOKEN')
            client = Client(account_sid, auth_token)

            message = client.messages.list(
                to=os.getenv('CLIENT1_PHONE_NUMBER'),
                from_=os.getenv('TWILIO_PHONE_NUMBER'),
                limit=1,
            )
            print(message.sid)
            sendSMS(args.id, args.phone, args.time)


if __name__ == '__main__':
    main()
