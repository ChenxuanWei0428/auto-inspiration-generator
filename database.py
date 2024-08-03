from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

def db_setup():
    load_dotenv("config.env")
    uri = "mongodb+srv://"+os.environ.get("DB_USERNAME")+":"+os.environ.get("DB_PASSWORD")+"@baobao.q88cpbt.mongodb.net/?retryWrites=true&w=majority&appName=BaoBao"

    client = MongoClient(uri)

    return client
   

def record_output(string):
    client = db_setup()
    context = {"output": string}
    client.output.text.insert_one(context)
    pass

if __name__ == "__main__":
    client = db_setup()
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
