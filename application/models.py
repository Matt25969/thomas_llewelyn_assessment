from application import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

class Workout(db.Model):
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	workout = db.Column(db.String(100), nullable=False)
	sets = db.Column(db.Integer, nullable=False)
	reps = db.Column(db.Integer, nullable=False)
	body_part = db.Column(db.String(100), nullable=False)

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return ''.join([
			'Date Posted: ', self.date_posted, '\r\n',
			'Workout: ', self.body_part,' - ', self.workout, '\r\n',
			'Sets: ', self.sets, '\r\n',
			'Reps: ', self.reps, '\r\n',
			'User: ', self.user_id
		])
			
			
	
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(60), nullable=False)
	last_name = db.Column(db.String(60), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	password = db.Column(db.String(50), nullable=False)
	
	log = db.relationship('Workout', backref='author', lazy=True)

	def __repr__(self):
		return ''.join([
			'User ID: ', str(self.id), '\r\n',
			'Name: ', self.first_name, ' ', self.last_name, '\r\n',
			'Email: ', self.email
		])