from flask import render_template
from application import app

@app.route('/')
@app.route('/about')
def home ():
    return render_template('about.html', title='About')

@app.route('/log')
def about():
    return render_template('log.html', title='Log')

@app.route('/account')
def account():
    return render_template('account.html', title='Account')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')