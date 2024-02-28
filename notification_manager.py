import requests
from twilio.rest import Client

account_sid = "Twilio account sid"
auth_token = "Twilio auth token"
TWILIO_NUMBER = "+Twilio Phone #"
MY_NUMBER = "Your Phone #"


class NotificationManager:
    def send_sms(self, body: str):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=body,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER,
        )
        print(message.status)
