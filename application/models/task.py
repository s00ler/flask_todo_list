from ..core import database as db
from datetime import datetime


class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    description = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)
    done_on = db.Column(db.DateTime, nullable=True)

    def __init__(self, creator_id, description):
        self.creator_id = creator_id
        self.description = description
        self.registered_on = datetime.utcnow()
        self.done_on = None
