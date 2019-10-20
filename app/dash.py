
from flask import render_template, redirect, url_for, request, Response, send_file, jsonify
from app import app, mongo
import pymongo
import pandas as pd
# app.config['MONGO_DBNAME'] = 'vogohelmetsdata'
# app.config['MONGO_URI'] = 'mongodb://139.59.61.212:27017'
MONGO_URL= 'mongodb://139.59.61.212:27017'
#MONGO_PORT= os.environ['MONGO_PORT']
myclient = pymongo.MongoClient(MONGO_URL)
mydb = myclient['vogohelmetsdata']
@app.route('/dashboard')
def dashboard_view():
    a =  mydb.totalhelmetdata.find({})
    b = pd.DataFrame(list(a))
    c = b.groupby('updatedAt').sum()

    Total_Rides = c['totalRidesCompleted']
    Total_Hel_Ret = b['totalHelmetsReturned']
    Total_Hel_Ret = Total_Hel_Ret.tolist()
    Total_Rides = Total_Rides.tolist()
    total_rets =sum(Total_Hel_Ret)
    total_ride =sum(Total_Rides)
    total_losts = total_ride - total_rets
 
    # employee_count = mydb.totalhelmetdata.find({}).count()
    active_count = mydb.totalhelmet.find().count()
    working = mydb.totalhelmet.find().count()
    return render_template('dashboard.html', total_ride=total_ride, total_rets=total_rets, total_losts=total_losts)

