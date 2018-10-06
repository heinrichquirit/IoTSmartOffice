from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import flask
import mysql.connector
import os

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError
    flags = None

current_time = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)
CAL = build('calendar', 'v3', http=creds.authorize(Http()))

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