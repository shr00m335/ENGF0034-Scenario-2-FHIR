from flask import Flask, render_template, request
import json
import hashlib
import uuid
from fhir import FHIR_Api, Patient, LoincCode, Observation
from typing import Dict

app = Flask("FHIR")

users_data: Dict[str, str] = {}
with open("data.json", "r") as fp:
    users_data = json.load(fp)

api = FHIR_Api()

logged_in_users: Dict[str, Patient] = {

}

def generate_uuid() -> str:
    uid = str(uuid.uuid4())
    while uid in logged_in_users:
        uid = str(uuid.uuid4())
    return uid

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.form
    if not ("username" in data and "password" in data):
        return {"message": "Incorrect username or password"}, 400
    username = data["username"]
    password = data["password"]
    if not username in users_data:
        return {"message": "Incorrect username or password"}, 400
    password = (password + "fhirscenario2").encode()
    if users_data[username] != hashlib.sha256(password).hexdigest():
        return {"message": "Incorrect username or password"}, 400
    patient = api.get_patient_details(" ".join(username.split(" ")[:-1]), username.split(" ")[-1])
    uid = generate_uuid()
    logged_in_users[uid] = patient
    return {"token": uid}, 200

@app.route("/details", methods=["GET"])
def details():
    return render_template("details.html")

def find_observation(data, code) -> Dict[str, str]:
    return next((x.to_json() for x in data if x.code == code), None)

@app.route("/patient/data", methods=["GET"])
def get_patient_data():
    headers = request.headers
    if not "Authorization" in headers:
        return {}, 401
    token = headers["Authorization"].split(" ")[-1]
    print(token, logged_in_users)
    if not token in logged_in_users:
        return {}, 401
    data = api.get_patient_health_data(logged_in_users[token])
    return {
        "name": logged_in_users[token].full_name,
        "height": find_observation(data, LoincCode.HEIGHT),
        "weight": find_observation(data, LoincCode.WEIGHT),
        "bmi": find_observation(data, LoincCode.BODY_MASS_INDEX),
        "hr": find_observation(data, LoincCode.HEART_RATE),
        "rr": find_observation(data, LoincCode.RESPIRATORY_RATE),
        "ss": find_observation(data, LoincCode.SMOKING_STATUS),
        "temperature": find_observation(data, LoincCode.BODY_TEMPERATURE),
        "bmip": find_observation(data, LoincCode.BODY_MASS_INDEX_PER_PERCENTILE),
        "bp": find_observation(data, LoincCode.BLOOD_PRESSURE),
        }, 200

if __name__ == "__main__":
    app.run(port=8080, debug=True)