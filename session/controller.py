from flask import jsonify

from extensions import database_manager
from profile.model import User
from .model import Session, SessionSet


class SessionController():

    def __init__(self, **kwargs):
        self.array_parser = kwargs['array_parser']

    def create_session(**kwargs):
        session = Session(**kwargs)
        if session is None:
            return jsonify({'Error': 'Session could not be created'})
        with database_manager(commit=True) as db:
            session = db.session.add(session)
            db.session.flush()
            for session_set in kwargs['sessions']:
                data = dict(session_set)
                s_set = SessionSet(**data)
                s_set.session_id = session.id
                db.session.add(s_set)

        return session.to_json()

    def get_sessions_by_user_id(userid):
        with database_manager(commit=False) as db:
            user = db.session.query(User).filter(User.id.is_(userid)).first()
            if user is None:
                return jsonify({'Error': 'User with ID {} could not be found'.format(userid)})
            session = db.session.query(Session).filter(Session.user_id.is_(userid)).first()
            session_sets = session.sessions
            result = [_set.to_json() for _set in session_sets]
        return result
