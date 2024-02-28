import requests
from twilio.rest import Client

account_sid = "AC2ee5b5d34eb0350c4d7620b3c44e0521"
auth_token = "a0d663846baa8ac7c1585b99cc4d4bbc"
TWILIO_NUMBER = "+18557070417"
MY_NUMBER = "+13474053316"


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
