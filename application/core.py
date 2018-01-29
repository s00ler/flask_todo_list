from flask import Flask
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt
from os.path import abspath
from flask_sqlalchemy import SQLAlchemy
from configparser import ConfigParser

config = ConfigParser()
config.read('./config.ini')

app = Flask(import_name=config['Flask']['app_name'],
            root_path=abspath(config['Flask']['app_path']))

app.config['SECRET_KEY'] = config['keys']['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = config['database']['uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

CSRFProtect(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
database = SQLAlchemy(app)
