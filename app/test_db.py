# import pymongo
#
# # MONGODB INITIALIZATION
# connection = 'mongodb+srv://amandat109:NUcnFGlhEO1TdOaQ@blueberry.pjtpwgq.mongodb.net/?retryWrites=true&w=majority&appName=Blueberry'

import pymongo
import csv

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
student_data_collection = db['student_data']

with open("StudentPerformanceFactors.csv") as performance_data:
    data = csv.reader(performance_data, delimiter=',')
    next(data) # skip headers
    for row in data:
        student_data_dict = { # reordered dict info
            'study_hours': row[0],
            'sleep_hours': row[5],
            'tutoring_sessions': row[9],
            'physical_activity': row[14],
            'attendance': row[1],
            'gender': row[18],
            'previous_score': row[6],
            'score': row[19]
        }
        data_insertion = student_data_collection.insert_one(student_data_dict)


# document_deletion = user_collection.delete_many({})
# print(document_deletion.deleted_count, " documents deleted.")

# user_dict = {
#     "username": "jason",
#     "password": "chao"
# }
#
# user_insertion = user_collection.insert_one(user_dict)
# print(user_insertion.inserted_id)
# print(user_collection.find_one())
