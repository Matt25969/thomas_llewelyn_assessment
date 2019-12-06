from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange, Email, EqualTo, ValidationError
from application.models import User, Workout
from flask_login import LoginManager, current_user

class LogForm(FlaskForm):
    workout = StringField('Workout: ',
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    body_part = StringField('Body Part: ',
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    sets = IntegerField('Sets: ',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=100)
        ]
    )

    reps = IntegerField('Reps:',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=100)
        ]
    )

    submit = SubmitField('Create Workout')

class UpdateWorkoutForm(FlaskForm):
    workout = StringField('Workout: ',
        validators=[
            DataRequired(),
            Length(min=2, max=60)
        ]
    ) 

    body_part = StringField('Body Part: ',
        validators=[
            DataRequired(),
            Length(min=2, max=60)
        ]
    )
    
    sets = IntegerField('Sets: ',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=100)
        ]
    )

    reps = IntegerField('Reps: ',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=100)
        ]
    )

    submit = SubmitField('Update Workout')
   

class RegistrationForm(FlaskForm):
    first_name = StringField('Name: ',
        validators=[
            DataRequired(),
            Length(min=2, max=60)
        ]
    )

    last_name = StringField('Surname: ',
        validators=[
            DataRequired(),
            Length(min=2, max=60)
        ]
    )

    email = StringField('Email: ',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password: ',
        validators=[
            DataRequired()
        ]
    )

    confirm_password = PasswordField('Confirm Password: ',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )

    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email is already in use, please try another')

class LoginForm(FlaskForm):
    email = StringField('Email: ',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password: ',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name: ',
        validators=[
            DataRequired(),
            Length(min=2, max=60)
        ]
    )

    last_name = StringField('Last Name: ',
        validators=[
            DataRequired(),
            Length(min=2, max=60)
        ]
    )

    email = StringField('Email: ',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use = Please use another')