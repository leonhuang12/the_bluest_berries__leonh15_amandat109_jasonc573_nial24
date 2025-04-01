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
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["database"]
# print(client.list_database_names()) # printing all databases in system

# FLASK APP INITIALIZATION
app = Flask(__name__)

@app.route('/')
def home():
    return "hello"

if __name__ == "__main__":
    app.debug = True
    app.run()
