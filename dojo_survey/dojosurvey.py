from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')

def dojo_survey():
    return render_template('index.html')

def result():
    return render_template('result.html')
app.run(debug=True)