from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = "asdf"

@app.route('/')
def index():
    if 'num' not in session: 
        session['num'] = random.randrange(0, 101)
        num = session['num']
        print num
    
    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess():
    c = ""
    # Coudn't get this function to work (display message if guess not int)
    # if isinstance(request.form('guess'), (int, long)):
    #     session['result'] = 'Input must be a number between 1-100'
    #     c = "red"

    if session['num'] == int(request.form['guess']):
        session['result'] = 'Correct'
        c = "green"
    
    elif session['num'] < int(request.form['guess']):
        session['result'] = 'Too High!'
        c = "red"

    else:
        session['result'] = 'Too Low!'
        c = "red"

    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('num')
    session.pop('result')
    return redirect('/')

app.run(debug=True)