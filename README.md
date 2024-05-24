# auto-inspiration-generator
 This is a API that can generate inspriation text using REST api, powered by ChatGPT


1. first, create a app password using your email in this link
https://myaccount.google.com/apppasswords 
3. run
```
pip install -r requirement.txt
```
2. Create a setup.env in the root directory, contain 3 variable
```
SENDER_APP_PASSWORD=**** **** **** ****
SENDER_EMAIL=example@gmail.com
RECEIVER_EMAIL=example@gmail.com
```
3. edit subjest and boy in test.py
4. run the following to send the email 
```
python test.py
```
