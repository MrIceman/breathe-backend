from datetime import datetime
from flask import jsonify, json

from database.Database import db


class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text, default='')
    sessions = db.relationship('SessionRound', backref='session', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        self.notes = kwargs.pop('notes', '')
        self.user_id = kwargs.pop('user_id')

    def to_dict(self):
        result = {'id': self.id,
                  'userId': self.user_id,
                  'created_on': self.created_on,
                  'amountOfRounds': len(list(self.sessions)),
                  'rounds': [ss.to_dict() for ss in self.sessions],
                  'notes': self.notes
                  }
        return result

    def to_json(self):
        print('-' * 5)
        print('Session DICT: {}'.format(self.to_dict()))
        json_result = json.dumps(self.to_dict())
        print('Session JSON: {}'.format(json_result))
        print('-' * 5)
        return json_result


class SessionRound(db.Model):
    __tablename__ = 'session_round'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    round_order = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    retention_time = db.Column(db.Integer, default=0)
    inhale_hold_duration = db.Column(db.Integer, default=0)
    breathes = db.Column(db.Integer, default=0)
    total_time = db.Column(db.Integer, default=0)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'))

    def __init__(self, **kwargs):
        print('Trying to initialize a session round with {}'.format(kwargs))
        self.round_order = kwargs.pop('round_order')
        self.breathes = kwargs.pop('breathes')
        self.retention_time = kwargs.pop('retention_time')
        self.session_id = kwargs.pop('session_id')

        # for key, value in kwargs.items()
        #     try:
        #         self.__setattr__(key, value)
        #     except AttributeError:
        #         print('{} is an unknown Attribute'.format(key))

    def to_dict(self):
        result = {"id": self.id,
                  'createdOn': self.created_on,
                  'retentionTime': self.retention_time,
                  'inhaleHoldDuration': self.inhale_hold_duration,
                  'breathes': self.breathes,
                  'totalTime': self.total_time
                  }
        return result

    def to_json(self):
        return json.dumps(self.to_dict())
