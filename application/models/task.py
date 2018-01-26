from datetime import datetime

from server import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300))
    active = db.Column(db.Boolean, default=True, nullable=False)
    create_time = db.Column(db.String(16), default=datetime.utcnow(
    ).strftime('%Y.%m.%d %H:%M'), nullable=False)

    def __repr__(self):
        return f'Task {self.id}'
