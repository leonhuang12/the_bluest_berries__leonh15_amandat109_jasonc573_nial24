'''
Bluest Berries: Leon Huang, Amanda Tan, Jason Chao, Nia Lam
SoftDev
P04: Makers Makin' It, Act II -- The Seequel
2025-04-21
Time Spent: [INSERT TIME HERE]
'''

from flask import Flask, flash, render_template, request, redirect, url_for, session, flash
from db import *
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

# db.insert_user_data(user, pass)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"log me in plss: {username}, {password}")
        
        if 'login' in request.form:
            user = user_collection.find_one({'username': username})
            if user and verify_user_login(username, password):
                session['username'] = username
                flash('Login successful.')
                return redirect('/')
            else:
                flash('Invalid username or password.')

        elif 'register' in request.form:
            confirm_pass = request.form.get('confirm_pass')
            print(f"reg: {username}, {password}, {confirm_pass}")

            if password != confirm_pass:
                flash('Passwords do not match.')
            else:
                existing_user = user_collection.find_one({'username': username})
                if existing_user:
                    flash('Username already exists.')
                else:
                    insert_user_data(username, password)
                    print(f"new user: {username}")
                    flash('Registration successful.')

    return render_template('login.html')



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
