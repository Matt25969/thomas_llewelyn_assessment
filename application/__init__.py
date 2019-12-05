from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' +os.getenv('MYSQL_USER')+ ':' +os.getenv('MYSQL_PASS')+ '@' +os.getenv('MYSQL_IP')+ '/llewthenics'
app.config['SECRET_KEY'] = os.getenv('SECRET')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from application import routes