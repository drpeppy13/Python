from flask import Flask, render_template, redirect
app = Flask(__name__)
app.secret_key = "8888"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninja")
def ninjas():
    return render_template("everyone.html")

@app.route("/ninja/<color>")
def word(color):
    if color == "blue":
        return render_template("blue.html")
    elif color == "red":
        return render_template("red.html")
    elif color == "orange":
        return render_template("orange.html")
    elif color == "purple":
        return render_template("purple.html")
    else:
        print "Not April"
        return render_template("april.html")

# @app.route("/ninja/blue")
# def blue():
#     return render_template("blue.html")
# @app.route("/ninja/red")
# def red():
#     return render_template("red.html")
# @app.route("/ninja/orange")
# def orange():
#     return render_template("orange.html")
# @app.route("/ninja/purple")
# def purple():
#     return render_template("purple.html")   
# @app.route("/ninja/<whatever>/") 
# def april(whatever):
#     print whatever
#     return render_template("april.html")

app.run(debug=True)
