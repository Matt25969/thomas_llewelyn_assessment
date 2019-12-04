from flask import render_template
from application import app

@app.route('/')
@app.route('/home')
def home ():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')