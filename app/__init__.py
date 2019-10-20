from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__, static_url_path='/assets', static_folder="assets")
app.config['MONGO_DBNAME'] = 'vogohelmetsdata'
app.config['MONGO_URI'] = 'mongodb://139.59.61.212:27017'
mongo = PyMongo(app=app)


from .dash import *