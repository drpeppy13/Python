from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "asdf"

@app.route("/")
def index():
    if "num" not in session:
        session["num"] = 1
    else:
        session["num"] += 1
    if user in session
        session["users"].append({"name":"a new user", "favorite_number":5})
    else:
        session["users"] = [{"name":"minh", "favorite "}]
    
    return render_template("index.html", times=session["num"], myUsers=session["users"])

@app.route("/add_num")
def add_num():
    session["num"] += 1
    return redirect("/")

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")

app.run(debug=True)
