from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    os.getenv("TWILIO_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

message = client.messages.create(
    body="WhatsDue says hello! ✅.....Test Case run Successful!",
    from_=os.getenv("TWILIO_WHATSAPP_NUMBER"),
    to=os.getenv("USER_WHATSAPP_NUMBER")
)

print("✅ Message SID:", message.sid)
