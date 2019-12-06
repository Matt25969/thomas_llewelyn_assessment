from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import User, Workout
from application.forms import LogForm, RegistrationForm, LoginForm, UpdateAccountForm, UpdateWorkoutForm
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/')
@app.route('/about')
def about():
    if current_user.is_authenticated:
        return redirect(url_for('log'))
    return render_template('about.html', title='About')

@app.route('/log', methods=['GET', 'POST'])
@login_required
def log():
    workoutData = Workout.query.filter_by(user_id=current_user.id).all()
    return render_template('log.html', title='Workout Log', workouts=workoutData)

@app.route('/account')
@login_required
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
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

@app.route('/create', methods=['GET','POST'])
@login_required
def create():
    form = LogForm()
    if form.validate_on_submit():
        postData = Workout(
            workout=form.workout.data,
            body_part=form.body_part.data,
            sets=form.sets.data,
            reps=form.reps.data,
            user_id=current_user.id
        )

        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('log'))
    else:
        print(form.errors)
    return render_template('create_log.html', title='Create Workout', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/update_account', methods=['GET', 'POST'])
@login_required
def update_account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('update_account.html', title='Update Details', form=form)

@app.route('/delete_workout/<int:id>', methods=['GET','POST'])
@login_required
def delete_workout(id):
    workout = Workout.query.get(id)
    try:
        db.session.delete(workout)
        db.session.commit()
        return redirect(url_for('log'))
    except:
        return "Try again"

@app.route('/delete_account', methods=['GET', 'POST'])
@login_required
def delete_account():
    user = User.query.get(current_user.id)
    logs = Workout.query.filter_by(user_id=current_user.id).all()
    print(logs)
    for log in logs:
        db.session.delete(log)
        db.session.commit()
    try:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('register'))
    except:
        return redirect(url_for('account'))
    


@app.route('/update_workout/<int:id>', methods=['GET','POST'])
@login_required
def update_workout(id):
    query = Workout.query.get(id)
    if query:
        print(query)
        form = UpdateWorkoutForm(formdata=request.form, obj=query)
        if form.validate_on_submit():
            query.body_part = form.body_part.data
            query.workout = form.workout.data
            query.sets = form.sets.data
            query.reps = form.reps.data
            db.session.commit()
            return redirect(url_for('log')) 
        return render_template('update_workout.html', title='Update Workout', form=form)
  
    

  