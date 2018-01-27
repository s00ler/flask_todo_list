from os import path
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from .readconfig import configuration as cfg
from forms import LoginForm


app = Flask(__name__, root_path=path.abspath(
    cfg['server']['application_path']))

app.config['SECRET_KEY'] = '__TODO__: SOME COMPLICATED SECRET KEY'


CSRFProtect(app)
db = SQLAlchemy(app)


@app.route('/')
def login():
    return render_template('login.html', form=LoginForm())
