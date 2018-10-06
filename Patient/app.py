#!/usr/bin/env python3
import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Email, Length
from wtforms.fields.html5 import DateField
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
basedir = os.path.abspath(os.path.dirname(__file__))


USER   = 'root'
PASS   = 'flaskp1o7'
HOST   = '35.189.60.247'
DBNAME = 'maps'
app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/maps'.format(USER,PASS,HOST,DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# declaring our model, here is ORM in its full glory


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    dob = db.Column(db.Date)
    gender = db.Column(db.String(1))
    address = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    #contactnumber = db.Column(db.String(120))

    def __init__(self, firstname, lastname, dob, gender, address, email):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.address = address
        self.email = email



class PatientSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('firstname', 'lastname', 'dob', 'gender', 'address', 'email')


class RegisterForm(FlaskForm):
    firstname = StringField('firstname', validators=[InputRequired(message="This field cannot be left blank.")])
    lastname = StringField('lastname', validators=[InputRequired(message="This field cannot be left blank.")])
    dob = DateField('dob', format='%Y-%m-%d', validators=[InputRequired(message="This field cannot be left blank.")])
    gender = SelectField('gender', choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Non-Binary')], validators=[InputRequired(message="This field cannot be left blank.")])
    address = StringField('address', validators=[InputRequired(message="This field cannot be left blank.")])
    email = StringField('email', validators=[InputRequired(message="This field cannot be left blank.")])

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)


# main route 
@app.route("/")
def index():
    return render_template('index.html')


# register page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    return render_template('register.html', form=form)


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

if __name__ == "__main__":
    host = os.popen('hostname -I').read()
    app.run(host='0.0.0.0', port=80, debug=False)
