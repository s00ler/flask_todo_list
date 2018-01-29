from ..core import database as db, bcrypt
from datetime import datetime


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True, default=None)

    tasks = db.relationship('Task', backref='author', lazy='joined')

    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.utcnow()

    @classmethod
    def add(cls, email, password):
        try:
            user = cls(email=email, password=password)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception:
            db.session.rollback()
            return None
