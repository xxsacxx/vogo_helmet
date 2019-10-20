from app import app, mongo

@app.route('/dashboard')
@login_required
def dashboard_view():
    employee_count = mongo.db.Employee.find().count()
    active_count = mongo.db.Employee.find({"status": "Active"}).count()
    working = mongo.db.Employee.find({"emp": "working"}).count()
    return render_template('dashboard.html', count=employee_count, active=active_count, working=working)
