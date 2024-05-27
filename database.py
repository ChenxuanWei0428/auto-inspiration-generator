from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

def db_setup():
    load_dotenv("config.env")
    uri = "mongodb+srv://"+os.environ.get("DB_USERNAME")+":"+os.environ.get("DB_PASSWORD")+"@baobao.q88cpbt.mongodb.net/?retryWrites=true&w=majority&appName=BaoBao"

    client = MongoClient(uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

def input():
    pass

if __name__ == "__main__":
    db_setup()
