from fastapi import FastAPI
import pyrebase

app = FastAPI()

config = {
    "apiKey": "AIzaSyB5EbXk0JzzOjUbno3P3bccZdw5MRpSeVY",
    "authDomain": "counterlogic-b88eb.firebaseapp.com",
    "databaseURL": "https://counterlogic-b88eb-default-rtdb.firebaseio.com/",
    "projectId": "counterlogic-b88eb",
    "storageBucket": "counterlogic-b88eb.appspot.com",
    "messagingSenderId": "1048060140196",
    "appId": "1:1048060140196:web:d2f9804086a2066044a431",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()

@app.get("/")
async def root():
    return {"message": "root page"}

@app.get("/admins")
async def root():
    admins = db.child('Admin').get()
    return {admins}

@app.get("/organisers")
async def root():
    orgs = db.child('Organiser').get()
    return {orgs}

@app.get("/events")
async def root():
    events = db.child('Event').get()
    return {events}