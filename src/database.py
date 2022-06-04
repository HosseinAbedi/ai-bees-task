import os
from pymongo import MongoClient
from pymongo.errors import AutoReconnect

MONGO_CLIENT = MongoClient(f"""mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_HOST')}/{os.getenv('MONGODB_DATABASE')}?retryWrites=true""", connect=False)

def insert_one(database_name, collection_name, document):
    db = MONGO_CLIENT[database_name]
    col = db[collection_name]
    try:
        col.insert_one(document)
    except Exception as e:
        pass
   