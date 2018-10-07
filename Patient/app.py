#!/usr/bin/env python3
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os
import requests
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Email, Length
from wtforms.fields.html5 import DateField, TimeField
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
bootstrap = Bootstrap(app)
basedir = os.path.abspath(os.path.dirname(__file__))


USER   = 'root'
PASS   = 'flaskp1o7'
HOST   = '35.189.60.247'
DBNAME = 'maps'
app.config['SECRET_KEY'] = 'xyz12143'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/maps'.format(USER,PASS,HOST,DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

# DB Models
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    dob = db.Column(db.Date)
    gender = db.Column(db.String(1))
    address = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, firstname, lastname, dob, gender, address, email):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.address = address
        self.email = email


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    description = db.Column(db.String(200))
    email = db.Column(db.String(120), unique=True)
    calendar_id = db.Column(db.String(120), unique=True)

    def __init__(self, firstname, lastname, description, email, calendar_id):
        self.firstname = firstname
        self.lastname = lastname
        self.description = description
        self.email = email
        self.calendar_id = calendar_id

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.String(50))
    doctor_id = db.Column(db.Integer)
    doctor_email = db.Column(db.String(120))
    patient_id = db.Column(db.Integer)
    patient_email = db.Column(db.String(120))
    starttime = db.Column(db.String(120))
    endtime = db.Column(db.String(120))

    def __init__(self, event_id, doctor_id, doctor_email, patient_id, patient_email, starttime, endtime):
        self.event_id = event_id
        self.doctor_id = doctor_id
        self.doctor_email = doctor_email
        self.patient_id = patient_id
        self.patient_email = patient_email
        self.starttime = starttime
        self.endtime = endtime


class PatientSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('firstname', 'lastname', 'dob', 'gender', 'address', 'email')

class DoctorSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'firstname', 'lastname', 'description', 'email', 'calendar_id')

class AppointmentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'event_id', 'doctor_id', 'doctor_email', 'patient_id', 'patient_email', 'starttime', 'endtime')

# Flask Forms
class RegisterForm(FlaskForm):
    firstname = StringField('firstname', validators=[InputRequired(message="This field cannot be left blank.")])
    lastname = StringField('lastname', validators=[InputRequired(message="This field cannot be left blank.")])
    dob = DateField('dob', format='%Y-%m-%d', validators=[InputRequired(message="This field cannot be left blank.")])
    gender = SelectField('gender', choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Non-Binary')], validators=[InputRequired(message="This field cannot be left blank.")])
    address = StringField('address', validators=[InputRequired(message="This field cannot be left blank.")])
    email = StringField('email', validators=[InputRequired(message="This field cannot be left blank.")])

class BookingForm(FlaskForm):
    day = DateField('day', format="%Y-%m-%d", validators=[InputRequired(message="This field cannot be left blank.")])
    time = TimeField('time', validators=[InputRequired(message="This field cannot be left blank.")])

# Schemas
patient_schema = PatientSchema()
doctor_schema = DoctorSchema()
appointment_schema = AppointmentSchema()
patients_schema = PatientSchema(many=True)
doctors_schema = DoctorSchema(many=True)
appointments_schema = AppointmentSchema(many=True)


# main route 
@app.route("/")
def index():
    return render_template('index.html')


# register page
@app.route("/patient/register", methods=['GET'])
def register():
    form = RegisterForm()

    return render_template('register.html', form=form)


# doctors page
@app.route("/doctors", methods=["GET"])
def doctors():
    form = BookingForm()
    url = request.url
    all_doctors = Doctor.query.all()
    result = doctors_schema.dump(all_doctors)
    doctorsr = result[0]
    print (doctorsr)
    return render_template('doctors.html', form=form, doctors=doctorsr, url = url)


@app.route("/api/patient", methods=['POST'])
def patient_reg():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    dob = request.form['dob']
    gender = request.form['gender']
    address = request.form['address']
    email = request.form['email']
    new_patient = Patient(firstname, lastname, dob, gender, address, email)

    db.session.add(new_patient)
    db.session.commit()

    return redirect(url_for('index'))


@app.route("/api/booking", methods=['POST'])
def patient_booking():
    doctor_id = request.form['doctor_id']
    doctor_email = request.form['doctor_email']
    startdate = request.form['day']
    starttime = request.form['time']
    enddate = request.form['day']
    endtime = format((datetime.strptime(starttime, '%H:%M') + timedelta(hours=1)),"%H:%M:%S")
    startdatetime = "{0}T{1}:00+10:00".format(startdate, starttime)
    enddatetime = "{0}T{1}+10:00".format(enddate, endtime)
    calendar_id = request.form['calendar_id']
    patient_id = "2"
    patient_email = "fake2@fake.org"
    event = {
      'summary': 'Appointment',
      'location': 'MAPS Office',
      'description': 'An appointment has been booked at thsi time',
      'start': {
            'dateTime': startdatetime,
            'timeZone': 'Australia/Melbourne',
        },
      'end': {
            'dateTime': enddatetime,
            'timeZone': 'Australia/Melbourne',
        },
      'attendees': [
        {'email': doctor_email},
        {'email': patient_email}
      ],
    }

    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    event_id = event.get('id')
    new_appointment = Appointment(event_id, doctor_id, doctor_email, patient_id, patient_email, starttime, endtime)

    db.session.add(new_appointment)
    db.session.commit()

    return redirect(url_for('index'))
