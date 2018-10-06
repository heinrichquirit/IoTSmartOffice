'''from flask import Flask, request, jsonify
from flask_sqlalchemy import  SQLAlchemy
from flask_marshmallow import Marshmallow'''
import flask
import mysql.connector
import os

def connect_to_database():

@app.route('/templates/pat_add_app.html')
def insert_patient() :
    date = datetime.now()
    tomorrow = (date + timedelta(days=1)).strftime("%Y-%m-%d")
    time_start = "{}T06:00:00+10:00".format(tomorrow)
    time_end   = "{}T07:00:00+10:00".format(tomorrow)
    event = {
        'name': 
        'email':
        'location': 'MAPS Hospital'
    }

def remove_patient():

#def insert_doctor():

#def remove_doctor():

#def create_appointment():
    
#def remove_appointment():

def display_patients():

def check_table_exists(table_name):