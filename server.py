from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = "The secret key"

@app.route("/")
def index():
    session["name"] = "Minh"
    return "created variable"

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    if email == "mnguyen@codingdojo.com":
        if password == "asdfasdf":
            return "logged in woohooo!"
        else:
            return "got the wrong password"
    else:
        return "didn't get the right email"
        
@app.route("/anotherroute")
def anotherroute():
    if "name" in session:
        print session["name"]
    else:
        session["name"] = "NOT Minh"
    return "testing"

@app.route("/clear")
def clear():
    session.clear()

app.run(debug=True)
