import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from text_generation import generate_inspriation_text

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Set up the server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(sender_email, sender_password)
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    # Attach the body of the email to the MIME message
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Send the email
    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    load_dotenv("test.env")
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_APP_PASSWORD")
    recipient_email = os.getenv("RECEIVER_EMAIL")

    
    subject = "test subject"
    body = "test body"

    send_email(sender_email, sender_password, recipient_email, subject, body)
