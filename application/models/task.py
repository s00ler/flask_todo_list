from ..core import database as db
from datetime import datetime


class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)

    creator_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)
    done_on = db.Column(db.DateTime, nullable=True, default=None)

    def __init__(self, creator_id, description):
        self.creator_id = creator_id
        self.description = description
        self.registered_on = datetime.utcnow()

    @classmethod
    def add(cls, creator_id, description):
        try:
            task = cls(creator_id=creator_id, description=description)
            db.session.add(task)
            db.session.commit()
            return task
        except Exception:
            session.rollback()
            return None
