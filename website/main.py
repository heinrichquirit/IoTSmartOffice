import sys
sys.path.insert(0, 'IoTSmartOffice/Python/cloud_api.py')

import cloud_api
from flask import Flask, url_for, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
    title = 'Home'
    name = 'Home'
    return render_template('index.html', title=title, name=name)

@app.route('/doctor.html')
def doctor():
    title = 'Doctor'
    name = 'Doctor'
    return render_template('doctor.html', title=title, name=name)

@app.route('/clerk.html')
def clerk():
	title = 'Clerk'
	name = 'Clerk'
	return render_template('clerk.html', title=title, name=name)

@app.route('/patient.html')
def patient():
	title = 'Patient'
	name = 'Patient'
	return render_template('patient.html', title=title, name=name)

if __name__ == '__main__':
	connect_to_database()
	app.run()