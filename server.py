from flask import Flask, render_template, request
import json
import hashlib

app = Flask("FHIR")

users_data = {}
with open("data.json", "r") as fp:
    users_data = json.load(fp)

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
    return {"token": "123"}, 200

if __name__ == "__main__":
    app.run(port=8080, debug=True)