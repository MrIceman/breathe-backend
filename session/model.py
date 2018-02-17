from database.Database import db
from flask import jsonify

"""
    __tablename__ = 'taskboard'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, default='No Title')
    description = db.Column(db.Text, default='No Description')
    secret = db.Column(db.Text, default='cheese')
    public_id = db.Column(db.Text)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    last_update = db.Column(db.DateTime, server_onupdate=db.func.now())
    tasks = db.relationship('Task', backref='taskboard', lazy='dynamic')
    max_tasks = db.Column(db.Integer, default=8)
    
    """


class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    notes = db.Column(db.Text, default='')
    total_time = db.Column(db.Integer, default='')
    sessions = db.relationship('session_set', backref='session', lazy='dynamic')
    user = db.Column(db.Integer, db.ForeignKey('user.id', name='user'))

    def __init__(self, **kwargs):
        for key, value in kwargs:
            try:
                if self.__getattribute__(key) is not None:
                    self.__setattr__(key, value)
            except AttributeError:
                print('{} is an unknown Attribute'.format(key))

    def to_dict(self):
        result = {'id': self.id,
                  'created_on': self.created_on,
                  'set_amount': len(list(self.sessions)),
                  'sets': [ss.json() for ss in self.sessions],
                  }
        return result

    def to_json(self):
        return jsonify(self.to_dict())


class SessionSet(db.Model):
    __tablename__ = 'session_set'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    exhale_hold_duration = db.Column(db.Integer, default=0)
    inhale_hold_duration = db.Column(db.Integer, default=0)
    breath_in_amounts = db.Column(db.Integer, default=0)
    total_time = db.Column(db.Integer, default='')
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'))

    def __init__(self, **kwargs):
        for key, value in kwargs:
            try:
                if self.__getattribute__(key) is not None:
                    self.__setattr__(key, value)
            except AttributeError:
                print('{} is an unknown Attribute'.format(key))

    def to_dict(self):
        result = {'id': self.id,
                  'created_on': self.created_on,
                  'exhale_hold_duration': len(list(self.sessions)),
                  'inhale_hold_duration': [ss.json() for ss in self.sessions],
                  'breath_in_amounts': self.breath_in_amounts,
                  'total_time': self.total_time
                  }
        return result

    def to_json(self, ):
        return jsonify(self.to_dict())
