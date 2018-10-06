'''from flask import Flask, request, jsonify
from flask_sqlalchemy import  SQLAlchemy
from flask_marshmallow import Marshmallow'''
import flask
import mysql.connector
import os

app = flask.Flask(__name__)
app.config['DEBUG'] = True

def connect_to_database():
    try:
        # Fix, maybe login details for database is incorrect
        host = '35.189.38.227'
        database = 'iotsmartoffice'
        user = 'heinrich'
        password = 'root'
        print('Attempting to connect to host ({}), database ({}), user ({}) Google Cloud SQL Database...'.format(host, database, user))
        global conn 
        conn = mysql.connector.connect(
            host=host, database=database, user=user, password=password
        )

        patient_table_query = '''create table PATIENT if not exists
                (
                    patient_id varchar(4) not null,
                    doctor_id varchar(4) not null,
                    first_name varchar(30),
                    last_name varchar(30),
                    age int,
                    weight decimal,
                    gender char,
                    contact varchar(20),
                    disease varchar(50),
                    primary key (patient_id),
                    foreign key (doctor_id) references doctor(doctor_id)
                );'''

        doctor_table_query = '''create table DOCTOR if not exists
                (
                    doctor_id varchar(4) not null,
                    first_name varchar(30),
                    last_name varchar(30),
                    department varchar(20),
                    primary key (doctor_id)
                );'''

        if conn.is_connected():
            print('Connected to Google MySQL database')

            global cur 
            cur = conn.cursor()
            cur.execute('use iotsmartoffice')
            if check_table_exists('PATIENT'):
                cur.execute(patient_table_query)
                print('PATIENT table has been created.')
            if check_table_exists('DOCTOR'):
                cur.execute(doctor_table_query)
                print('DOCTOR table has been created.')
        
    except:
        print('Could not connect to Google MySQL database')

    finally:
       conn.close()

app.route('/templates')
def insert_patient(
                    id, first_name, last_name, age, 
                    weight, gender, contact, disease, doctor_id):
    query = '''insert into table PATIENT values 
                (
                    0001, heinrich, quirit, 23, 
                    73.0, M, 12345, Flu, 0002
                );'''
    cur.execute(query)

#def remove_patient():

#def insert_doctor():

#def remove_doctor():

#def create_appointment():
    
#def remove_appointment():

def display_patients():
    cur.execute('select * from patient')

def check_table_exists(table_name):
    query = '''show tables like "table_name"'''
    cur.execute(query)
    result = cur.fetchone()
    if result:
        return True
    
    return False