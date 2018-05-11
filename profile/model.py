from flask import jsonify

from database.Database import db
from extensions import crypto


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False)
    display_name = db.Column(db.Text, default='default')
    password = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, default='')
    location = db.Column(db.Text, default='false')
    age = db.Column(db.Integer, default=0)
    bio = db.Column(db.Text, default='default')
    longest_breath = db.Column(db.Integer, default=0)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    session = db.relationship('Session', backref='user', lazy='dynamic')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                self.__setattr__(key, value)
            except AttributeError:
                print('{} is an unknown Attribute'.format(key))
        if 'display_name' not in kwargs:
            self.display_name = 'Iceman {}'.format(self.id)

    def to_dict(self):
        password = crypto.decrypt(self.password)
        result = {

        }

        return result

    def to_json(self):
        return jsonify(self.to_dict())
