'''
Bluest Berries: Leon Huang, Amanda Tan, Jason Chao, Nia Lam
SoftDev
P04: Makers Makin' It, Act II -- The Seequel
2025-04-[INSERT DAY HERE]
Time Spent: [INSERT TIME HERE]
'''

from flask import Flask, flash, render_template, request, redirect, url_for, session, flash
import pymongo

# MONGODB INITIALIZATION
connection = 'mongodb+srv://amandat109:NUcnFGlhEO1TdOaQ@blueberry.pjtpwgq.mongodb.net/?retryWrites=true&w=majority&appName=Blueberry'
client = pymongo.MongoClient(connection)
db = client['database']
user_collection = db['users']
# print(client.list_database_names()) # printing all databases in system

# FLASK APP INITIALIZATION
app = Flask(__name__)

@app.route('/')
def home():
    # if 'username' not in session:
    #     return redirect('/login')
    # if request.method == 'POST':
    # return "hello"
    return render_template('index.html')

@app.route('/login')
def login():
    # if request.method == 'POST':
    #     if request.form.get('register'):
    #         return register_user()
    #     if request.form.get('login'):
    #         return login_user()
    #     else:
    #         flash('form error')
    # user_dict = {
    #     'username': '',
    #     'password': '',
    # }
    # insert_user_data = user_collection.insert_one(user_dict)
    return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
