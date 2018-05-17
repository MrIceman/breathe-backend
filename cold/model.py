from datetime import datetime

from flask import json
from sqlalchemy.testing import db


class ColdSession(db.Model):
    __tablename__ = 'cold_session'
    uuid = db.Column(db.String, primary_key=True, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text, default='')
    duration = db.Column(db.Integer, default=0)
    type = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        self.uuid = kwargs.pop('uuid')
        self.notes = kwargs.pop('notes', '')
        self.type = kwargs.pop('type', '')
        self.user_id = kwargs.pop('user_id')

    def to_dict(self):
        return {
            'uuid': self.uuid,
            'userId': self.user_id,
            'createdOn': self.created_on,
            'duration': self.duration,
            'notes': self.notes
        }

    def to_json(self):
        return json.dumps(self.to_dict())
