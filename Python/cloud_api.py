'''from flask import Flask, request, jsonify
from flask_sqlalchemy import  SQLAlchemy
from flask_marshmallow import Marshmallow'''
import mysql.connector
import os

def connect_to_database(host, database, user, password):
    try:
        conn = mysql.connector.connect(
            host=host,database=database, user=user, password=password
        )

        if conn.is_connected():
            print('Connected to Google MySQL database')
        
    except Error as e:
        print('Could not connect to Google MySQL database')
        print(e)

    finally:
        conn.close()

'''
def insert_patient():

def remove_patient():

def insert_doctor():

def remove_doctor():

def create_appointment():
    
def remove_appointment():
'''

def insert_patient():
    sql = ''