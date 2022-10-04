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
async def admin():
    admins = db.child('Admin').get()
    return {admins}

@app.get("/organisers")
async def orgs():
    orgs = db.child('Organiser').get()
    return {orgs}

@app.get("/events")
async def events():
    events = db.child('Event').get()
    return {events}

@app.get("/addadmin")
async def addadmin():
    new_admin = {
        "username": "ivan",
        "password": "password"
    }
    db.child('Admin').push(new_admin)
    return {"Status": "Admin Added"}

@app.get("/addorg")
async def addorg():
    new_org = {
        "name": "IEEE",
        "username": "ieee",
        "password": "password",
        "no_of_events": 0,
        "events": {},
    }
    db.child('Organiser').push(new_org)
    return {"Status": "Org Added"}

@app.get("/orgid")
async def orgid():
    org = 'ieee'
    res = {"status": "Organiser Not Found"}
    ids = db.child("Organiser").get().val()
    for id in ids:
        if db.child("Organiser").child(id).child("username").get().val() == org:
            res = {"status": "Organiser Found", "org_id": id}
            break
    return res

@app.get("/addevent")
async def addevent():
    org_id = '-NDYnfwREy-xTBXIDK_H'
    event = {
        'org_id': org_id,
        'name': 'Athlead',
        'date': '01/01/2022',
        'venue': 'Supari Talao',
        'max_participants': 10,
        'registered_participants': 0,
        'participants': {}
    }

    db.child("Event").push(event)

    update = db.child("Organiser").child(org_id).child("no_of_events").get().val() + 1
    db.child("Organiser").child(org_id).update({"no_of_events": update})
    
    event_ids = db.child("Event").get().val()
    for id in event_ids:
        if db.child("Event").child(id).child('org_id').get().val() == org_id:
            if db.child("Organiser").child(org_id).child("events").child().get().val() == None:
                db.child("Organiser").child(org_id).child("events").push(id)
            else:
                for added_event_id in db.child("Organiser").child(org_id).child("events").child().get().val():
                    if added_event_id != id:
                        db.child("Organiser").child(org_id).child("events").push(id)

    return {'no_of_events': 'event added'}
