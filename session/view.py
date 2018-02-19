from flask import request

from extensions import crypto
from . import session_blueprint


@session_blueprint.route('/patch', methods=['POST'])
def hello():
    payload = crypto.get_auth_token(request.headers['auth'])
    email = payload['auth']
    return 'Session Blueprint Page. You entered!'


@session_blueprint.route('/create', methods=['POST'])
def _create_session():
    payload = crypto.get_auth_token(request.headers['auth'])
    id = payload['id']

    data = dict(request.get_json())
    data['user_id'] = id
