from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

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

