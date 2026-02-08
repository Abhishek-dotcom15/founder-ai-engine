import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
from linkedin_oneclick import create_linkedin_button

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_APP_PASSWORD")


def send_email(post):

    msg = EmailMessage()

    msg["Subject"] = "Your Founder Post is Ready"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    # Create LinkedIn button
    button_html = create_linkedin_button(post)

    # Clean, high-authority email layout (NO IMAGE)
    html_content = f"""
    <html>
        <body style="font-family:Arial; max-width:700px; margin:auto;">

            <h2>Your Founder Post is Ready</h2>

            <div style="
                background:#f4f6f8;
                padding:22px;
                border-radius:10px;
                white-space:pre-wrap;
                font-size:16px;
                line-height:1.6;
            ">
            {post}
            </div>

            {button_html}

            <p style="margin-top:30px; color:gray; font-size:13px;">
            Founder AI Engine • Brillinity
            </p>

        </body>
    </html>
    """

    msg.add_alternative(html_content, subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)

    print("Email sent successfully!")
