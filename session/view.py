from flask import request

from extensions import crypto
from session.model import Session
from . import session_blueprint


@session_blueprint.route('/patch', methods=['POST'])
def hello():
    payload = crypto.encrypt_auth_token(request.headers['auth'])
    email = payload['auth']
    return 'Session Blueprint Page. You entered!'


@session_blueprint.route('/create', methods=['POST'])
def _create_session():
    payload = crypto.decrypt_auth_token(request.headers['auth'])
    id = payload['userid']
    json = request.get_json()

    session = Session(**json)
    if session:
        return session.to_json()
    return 'Error'
