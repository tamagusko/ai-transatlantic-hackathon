# (c) Tiago Tamagusko 2022
"""
Sends an sms asking if the client is at home to receive the order. Expected response: yes (y) or no (n).
If the answer is yes (y), the delivery continues, if it is no (n) it generates a closest Locker request.

Usage:
    $ python path/to/systemSMS.py --id DELIVERY_ID --phone NUMBER --time WAITING_TIME_IN_SECONDS

Example:
    # send a sms to the phone number 1234567890 to confirm 20220415_1 delivery and wait for a response for 2 minutes
    $ python path/to/systemSMS.py --id 20220415_1 --phone 1234567890 --time 120
"""
from __future__ import annotations

import argparse
import time

from receiveSMS import receiveSMS
# from sendSMS import sendSMS

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

time.sleep(args.time)
if receiveSMS(args.id, args.phone):
    print('Client is at home')


# test:  sendSMS(args.id, args.phone, args.time)
