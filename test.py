import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from openai import OpenAI


def generate_inspriation_text(content):
    load_dotenv("config.env")
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    sender_name=content["sender_name"]
    receiver_name=content["receiver_name"]
    category=content["category"]

    pre_cond_context="Use a language that match sender and receiver name, also do not include any additional message or quoation mark"
    body_prompt = "Please generate a "+category+" text from "+sender_name+" to "+receiver_name+", include both name"
    subject_prompt="Please generate a title for a "+category+" text from "+sender_name+" to "+receiver_name

    response_body = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-3.5-turbo" depending on which model you want to use
        messages=[
            {"role": "system", "content": pre_cond_context},
            {"role": "user", "content": body_prompt}
        ] 
    )

    response_subject = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-3.5-turbo" depending on which model you want to use
        messages=[
            {"role": "system", "content": pre_cond_context},
            {"role": "user", "content": subject_prompt}
        ] 
    )
    print(response_body.choices[0].message.content)
    print("-----------")
    print(response_subject.choices[0].message.content)

    subject = response_subject.choices[0].message.content
    body = response_body.choices[0].message.content
    return subject, body

def send_email(sender_email, sender_password, recipient_email, content):
    # Set up the server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(sender_email, sender_password)
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email

    #generate text
    subject, body = generate_inspriation_text(content)
    
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

    content = {
        "sender_name": "小狗头",
        "receiver_name": "包包",
        "category": "romentic"
    }

    send_email(sender_email, sender_password, recipient_email, content)
    #generate_inspriation_text(content)