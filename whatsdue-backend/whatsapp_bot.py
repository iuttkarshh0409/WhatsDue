from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Twilio client with credentials from environment variables
client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

def send_whatsapp_message(text):
    """
    Send a WhatsApp message via Twilio.

    Args:
        text (str): The message body to send.

    Returns:
        tuple: (success (bool), message_sid (str or None))
    """
    try:
        message = client.messages.create(
            body=text,
            from_=os.getenv("TWILIO_WHATSAPP_NUMBER"),
            to=os.getenv("USER_WHATSAPP_NUMBER")
        )
        return True, message.sid
    except Exception as e:
        print(f"❌ Error sending WhatsApp message: {e}")
        return False, None
