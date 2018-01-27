from flask import render_template

from .core import app, database
from .forms import LoginForm


@app.route('/')
def hello():
    return 'hello'


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
