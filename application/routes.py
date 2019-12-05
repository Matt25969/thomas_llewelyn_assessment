from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import User, Workout
from application.forms import LogForm, RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/log')
def log():
    workoutData = Workout.query.all()
    return render_template('log.html', title='Workout Log', logs=workoutData)

@app.route('/account')
def account():
    return render_template('account.html', title='Account')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('log'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('log'))

    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('log'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=hashed_pw)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('account'))

    return render_template('register.html', title='Register', form=form)

@app.route('/create', methods=['GET','POST'])
def create():
    form = LogForm()
    if form.validate_on_submit():
        postData = Workout(
            workout=form.workout.data,
            body_part=form.body_part.data,
            sets=form.sets.data,
            reps=form.reps.data,
            user_id=1 #change this field when adding accounts!
        )

        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('log'))
    else:
        print(form.errors)
    return render_template('create_log.html', title='Create Workout', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

