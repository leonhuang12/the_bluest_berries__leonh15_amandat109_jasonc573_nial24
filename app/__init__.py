'''
Bluest Berries: Leon Huang, Amanda Tan, Jason Chao, Nia Lam
SoftDev
P04: Makers Makin' It, Act II -- The Seequel
2025-04-[INSERT DAY HERE]
Time Spent: [INSERT TIME HERE]
'''

from flask import Flask, flash, render_template, request, redirect, url_for, session, flash
import pymongo
import csv

# MONGODB INITIALIZATION
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# uri = "mongodb+srv://jasonc573:Dragonace2010@blueberry.pjtpwgq.mongodb.net/?appName=Blueberry"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
# db = client['database']
# user_collection = db['users']
# student_data_collection = db['student_data']

# FLASK APP INITIALIZATION
app = Flask(__name__)

@app.route('/')
def home():
    if 'username' not in session:
        return redirect('/login')
    return render_template('index.html')

@app.route('/login')
def login():
    # if request.method == 'POST':
    #     if request.form.get('register'):
    #         return register_user()
    #     if request.form.get('login'):
    #         return login_user()
    #     # RETRIEVE USER AND PASS FROM LOGIN FORM
    #     db.insert_user_data(user, pass)
    #     else:
    #         flash('form error')
    return render_template('login.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
