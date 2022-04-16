# (c) Tiago Tamagusko 2022
# Source: https://github.com/sendgrid/sendgrid-python
"""
Sends an email using Sendgrid API.

Usage:
    $ sendEmail('client_email', 'delivery_id')

Example:
    # send a email to tamagusko@gmail.com to inform him that his order (20220415_1) was delivered
    $ sendEmail('tamagusko@gmail.com', '20220415_1')
"""
from __future__ import annotations

import os

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()   # secrets are saved on .env file
# .env: SENDGRID_API_KEY


def sendEmail(client_email: str, delivery_id: str, locker=None):
    # created to use the locker
    if locker is None:
        content = 'will be delivered today until 7pm.'  # default content
    else:
        # if the order is in the locker
        content = f'is available in locker {locker}.'

    message = Mail(
        from_email='tamagusko@gmail.com',
        to_emails=client_email,
        subject='Package delivery',
        html_content=f'Order {delivery_id} ' + content,
    )
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    return response.status_code, response.headers


sendEmail('tamagusko@gmail.com', '20220415_1', '55')
