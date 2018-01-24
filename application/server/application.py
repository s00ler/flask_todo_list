from flask import Flask, url_for, render_template
from os import path
from configreader import configuration as cfg
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, root_path=cfg['server']['application_path'])

app.config['SQLALCHEMY_DATABASE_URI'] = cfg['server']['database_path']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.root_path


@app.route('/')
def hello():
    return 'hello!'


@app.route('/login')
def login():
    return app.send_static_file()


app.run()
