'''
Bluest Berries: Leon Huang, Amanda Tan, Jason Chao, Nia Lam
SoftDev
P04: Makers Makin' It, Act II -- The Seequel
2025-04-21
Time Spent: [INSERT TIME HERE]
'''

import pymongo
import csv
import bcrypt

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://jasonc573:Dragonace2010@blueberry.pjtpwgq.mongodb.net/?appName=Blueberry"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

db = client['database']
user_collection = db['users']
student_data_collection = db['student_data']

def insert_student_data():
    clear_collection(student_data_collection)
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

def retrieve_student_data(data_type):
    data_list = []
    for data in student_data_collection.find({}, {"_id": 0, data_type: 1}):
        data_list.append(int(data[data_type]))
    # print(data_list)
    return data_list

def insert_user_data(username, password):
    # use bcrypt as a password hasher
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password.encode('utf-8'), salt)

    user_dict = {
        'username': username,
        # 'password': password, # plaintext password is NOT stored, only its salt and hash
        'salt': salt,
        'password_hash': hash
    }
    data_insertion = user_collection.insert_one(user_dict)

def verify_user_login(inputted_username, inputted_password):
    for user_document in user_collection.find({'username': inputted_username}, {'_id': 0, 'username': 0}):
        salt = user_document['salt']
        password_hash = user_document['password_hash']

        inputted_password_hash = bcrypt.hashpw(inputted_password.encode('utf-8'), salt)
        if password_hash == inputted_password_hash:
            print(f'Login successful for {inputted_username}!')
            return True
        else:
            print('Incorrect password.')
            return False
    print('Username not found.')
    return False

def clear_collection(collection_name):
    document_deletion = collection_name.delete_many({})
    print(f'{document_deletion.deleted_count} documents deleted from {collection_name}.')

### CLEAR COLLECTIONS -- USE WITH CAUTION ###
# clear_collection(student_data_collection)
# clear_collection(user_collection)


# insert_user_data('jason', 'chao')
# verify_user_login('jason', 'chao')
# retrieve_student_data('study_hours')
