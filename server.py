from flask import Flask, render_template

app = Flask("FHIR")

@app.route("/")
def home():
    return "Hello World"

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(port=8080, debug=True)