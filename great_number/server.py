from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = "asdf"

@app.route('/')
def index():
    if 'num' not in session: 
        session['num'] = random.randrange(1, 101)
        print session['num']
       
    
    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess():
    try:
        c = ""
        guess = int(request.form['guess'])
        if guess <= 100 and guess > 0:
            if guess == session['num']:
                session['result'] = "Correct!"
                c = "green"
            elif guess > session['num']:
                session['result'] = "Too high!"
                c = "red"
            elif guess < session['num']:
                session['result'] = "Too low!"
                c = "red"
    except:
        session['result'] = "Input must be a number between 1-100"
        c = "red"

    # try:
    #     guess = int(request.form['guess'])
    #     if guess == int: 

    #     # print type(request.form['guess'])

    # Coudn't get this function to work (display message if guess not int)
    # if isinstance(request.form('guess'), (int, long)):
    #     session['result'] = 'Input must be a number between 1-100'
    #     c = "red"

    # if session['num'] == int(request.form['guess']):
    #     session['result'] = 'Correct'
    #     c = "green"
    #     button = "show"
    
    # elif session['num'] < int(request.form['guess']):
    #     session['result'] = 'Too High!'
    #     c = "red"

    # elif session['num'] > int(request.form['guess']):
    #     session['result'] = 'Too Low!'
    #     c = "red"

    return render_template('index.html', c=c)

@app.route('/reset')
def reset():
    session.pop('num')
    session.pop('result')
    return redirect('/')

app.run(debug=True)