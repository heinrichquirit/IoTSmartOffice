from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import os

app = Flask(__name__)

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])

@app.route('/')
def index():
    title = 'Home'
    name = 'Home'
    return render_template('index.html', title=title, name=name)

@app.route('/index.html')
def home():
    title = 'Home'
    name = 'Home'
    return render_template('index.html', title=title, name=name)

@app.route('/doctor.html')
def doctor():
    title = 'Doctor'
    name = 'Doctor'
    return render_template('doctor.html', title=title, name=name)

@app.route('/doc_view_pats.html')
def doc_view_pats():
	title = 'View Patients'
	name = 'View Patients'
	return render_template('doc_view_pats.html', title=title, name=name)

@app.route('/doc_add_avail.html')
def doc_add_avail():
	title = 'Add Availability'
	name = 'Add Availability'
	return render_template('doc_add_avail.html', title=title, name=name)

@app.route('/clerk.html')
def clerk():
	title = 'Clerk'
	name = 'Clerk'
	return render_template('clerk.html', title=title, name=name)

@app.route('/clerk_view_app.html')
def clerk_view_app():
	title = 'View all appointments'
	name = 'View all appointments'
	return render_template('clerk_view_app.html', title=title, name=name)

@app.route('/clerk_add_app.html')
def clerk_add_app():
	title = 'Add appointment'
	name = 'Add appointment'
	return render_template('clerk_add_app.html', title=title, name=name)

@app.route('/clerk_cancel_app.html')
def clerk_cancel_app():
	title = 'Cancel appointment'
	name = 'Cancel appointment'
	return render_template('clerk_cancel_app.html', title=title, name=name)

@app.route('/patient.html')
def patient():
	title = 'Patient'
	name = 'Patient'
	return render_template('patient.html', title=title, name=name)

@app.route("/pat_register.html", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print ("form.errors")
    if request.method == 'POST':
        name=request.form['name']
        password=request.form['password']
        email=request.form['email']
        print (name, " ", email, " ", password)
 
        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('pat_register.html', form=form)

@app.route('/pat_add_app.html')
def pat_add_app():
	title = 'Make Appointment'
	name = 'Make Appointment'
	return render_template('pat_add_app.html', title=title, name=name)

@app.route('/pat_cancel_app.html')
def pat_cancel_app():
	title = 'Cancel Appointment'
	name = 'Cancel Appointment'
	return render_template('pat_cancel_app.html', title=title, name=name)

if __name__ == "__main__":
	host = os.popen('hostname -I').read()
	app.run(host=host, port=80, debug=False)
