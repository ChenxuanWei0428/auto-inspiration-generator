from openai import OpenAI
from dotenv import load_dotenv
import os

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

if __name__ == "__main__":

    
    content = {
        "sender_name": "小狗头",
        "receiver_name": "包包",
        "category": "romentic"
    }


    generate_inspriation_text(content)