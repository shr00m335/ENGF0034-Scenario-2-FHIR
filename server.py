from flask import Flask, render_template, request
import json
import hashlib
import uuid
from fhir import FHIR_Api, LoincCode

app = Flask("FHIR")

users_data = {}
with open("data.json", "r") as fp:
    users_data = json.load(fp)

api = FHIR_Api()

logged_in_users = {

}

def generate_uuid():
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
    return [x.to_json() for x in data], 200

if __name__ == "__main__":
    app.run(port=8080, debug=True)