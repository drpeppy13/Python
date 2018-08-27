from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "asdf"

@app.route("/")
def index():
    if "num" not in session:
        session["num"] = 1
    else:
        session["num"] += 1
    # if "users" in session:
    #     session["users"].append({"name":"a new user", "favorite_number":5})
    # else:
    #     session["users"] = [{"name":"minh", "favorite_number":10}]
    
    return render_template("index.html", num=session["num"], users=session["users"])

@app.route("/add_num", methods=["POST"])
def add_num():
    session["num"] += 2
    return redirect("/")

@app.route("/clear", methods=["POST"])
def clear():
    session.clear()
    return redirect("/")

app.run(debug=True)
