from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' +os.getenv('MYSQL_USER')+ ':' +os.getenv('MYSQL_PASS')+ '@' +os.getenv('MYSQL_IP')+ '/llewthenics'
db = SQLAlchemy(app)

from application import routes