from flask import jsonify, json

from profile.model import User
from .model import Session, SessionRound


class SessionController:

    def __init__(self, **kwargs):
        self.database_manager = kwargs['database_manager']

    """
    constructor(public readonly id: number = Date.now(),
                public globalId: number, // ID from the Backend, -1 when not initialized yet
                public date: number = Date.now(),
                public amountOfRounds: number,
                public custom: boolean,
                public rounds: Array<Rounds>,
                public notes: string,
                public inMemoryOnly: boolean = true) 

    """

    def create_session(self, **kwargs):
        with self.database_manager(commit=True) as db:
            session = Session(**kwargs)
            if session is None:
                return jsonify({'Error': 'Session could not be created'})
            db.session.add(session)
            db.session.flush()
            for session_round in kwargs['rounds']:
                data = dict(session_round)
                data.update(session_uuid=session.uuid)
                s_set = SessionRound(**data)
                db.session.add(s_set)

        return session.to_json()

    def get_sessions_by_user_id(self, user_id):
        with self.database_manager(commit=False) as db:
            user = db.session.query(User).filter(User.id.is_(user_id)).first()
            if user is None:
                return jsonify({'Error': 'User with ID {} could not be found'.format(user_id)})
            session = db.session.query(Session).filter(Session.user_id.is_(user_id)).all()
            result = [sess.to_dict() for sess in session]
            print('Result list: {}'.format(result))
        return json.dumps(result)
