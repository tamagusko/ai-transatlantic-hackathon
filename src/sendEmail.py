# (c) Tiago Tamagusko 2022
# Source: https://github.com/sendgrid/sendgrid-python
"""
Sends an email using Twilio API.

Usage:
    $ sendSMS(delivery_id, client_phone)

Example:
    # send a sms to the phone 1234567890
    $ sendSMS(20220415_1, 1234567890)
"""
from __future__ import annotations

import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def sendEmail(client_email: str, delivery_id: str):
    message = Mail(
        from_email='tamagusko@gmail.com',
        to_emails=client_email,
        subject='Package delivery',
        html_content=f'Order {delivery_id} will be delivered today until 7pm.',
    )

    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    return print(response.status_code, response.body, response.headers)


sendEmail('tamagusko@gmail.com', '20220415_1')
