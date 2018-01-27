from flask import Flask
from flask_wtf import CSRFProtect
from os.path import abspath, curdir
from flask_sqlalchemy import SQLAlchemy
from configparser import ConfigParser

config = ConfigParser()
config.read('./config.ini')

app = Flask(import_name=config['Flask']['app_name'],
            root_path=abspath(config['Flask']['app_path']))

app.config['SECRET_KEY'] = '__TODO__: SO SECRET MUCH KEY'

CSRFProtect(app)

database = SQLAlchemy()
