# import pymongo
#
# # MONGODB INITIALIZATION
# connection = 'mongodb+srv://amandat109:NUcnFGlhEO1TdOaQ@blueberry.pjtpwgq.mongodb.net/?retryWrites=true&w=majority&appName=Blueberry'

import pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://jasonc573:Dragonace2010@blueberry.pjtpwgq.mongodb.net/?appName=Blueberry"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['database']
user_collection = db['users']

user_dict = {
    "username": "jason",
    "password": "chao"
}

user_insertion = user_collection.insert_one(user_dict)
print(user_insertion.inserted_id)
print(user_collection.find_one())
