from flask import jsonify, json

from cold.model import ColdSession


class ColdController:

    def __init__(self, **kwargs):
        self.database_manager = kwargs['database_manager']

    def create_cold_session(self, **kwargs):
        with self.database_manager(commit=True) as db:
            cold_session = ColdSession(**kwargs)
            if cold_session is None:
                return jsonify({'Error': 'Cold Session could not be created'})
            db.session.add(cold_session)
        return cold_session.to_json()

    def get_cold_session_by_user_id(self, user_id):
        with self.database_manager(commit=False) as db:
            sessions = db.session.query(ColdSession).filter(ColdSession.user_id.is_(user_id)).all()
        if sessions is None:
            return jsonify({'Error': 'Sessions for User ID {} could not be found'.format(user_id)})
        result = [sess.to_dict() for sess in sessions]
        return json.dumps(result)
