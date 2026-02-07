import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_APP_PASSWORD")


def send_email(post):

    msg = EmailMessage()

    msg["Subject"] = "Your Daily Founder Post"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    msg.set_content(post)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)

    print("Email sent successfully!")
