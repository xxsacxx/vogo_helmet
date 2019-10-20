from flask import Flask
app = Flask(__name__, static_url_path='/assets', static_folder="assets")
# app.config['MONGO_DBNAME'] = 'dev'
# app.config['MONGO_AUTH_SOURCE'] = 'admin'
app.config['MONGO_URI'] = 'mongodb://root:pass123@ds255539.mlab.com:55539/heroku_3xgdc44r'
mongo = PyMongo(app=app,retryWrites=False)


from .dash import *