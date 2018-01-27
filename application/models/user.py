from ..core import database as db
import bcrypt
from datetime import datetime


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    tasks = db.relationship('Task', backref='author', lazy='joined')

    def __init__(self, email, password, confirmed,
                 paid=False, confirmed_on=None):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.utcnow()
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on
