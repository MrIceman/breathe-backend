from database.Database import db

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


class Board(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.Text, default='NoName')
    messages = db.relationship('Message', backref='board', lazy='dynamic')
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


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    board_id = db.Column(db.Integer, db.ForeignKey(column='board.id', name='board'))

    def __init__(self, content, board_id):
        self.content = content
        self.board_id = board_id

    def to_dict(self):
        return {'id': self.id,
                'content': self.content,
                'board': self.board.id,
                'created_on': self.created_on}

    def to_json(self):
        from flask import jsonify
        return jsonify(self.to_dict())

