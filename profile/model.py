from database.Database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session = db.relationship('session', backref='user', lazy='dynamic')
    email = db.Column(db.Text)
    display_name = db.Column(db.Text)
    password = db.Column(db.Text)
    country = db.Column(db.Text)
    location = db.Column(db.Text)
    age = db.Column(db.Integer)
    bio = db.Column(db.Text)
    longest_breath = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, location):
        self.location = location

    def to_dict(self, all_messages=False):
        result = {'id': self.id,
                  'location': self.location,
                  'message_count': len(list(self.messages)),
                  'created_on': self.created_on}
        if all_messages:
            result['messages'] = [msg.to_dict() for msg in self.messages]
        return result

    def to_json(self, all_messages=False):
        from flask import jsonify
        return jsonify(self.to_dict(all_messages))
