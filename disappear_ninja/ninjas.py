from flask import Flask, render_template, redirect
app = Flask(__name__)
app.secret_key = "8888"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninja")
def ninjas():
    return render_template("everyone.html")

app.run(debug=True)
