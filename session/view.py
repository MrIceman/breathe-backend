from flask import request, jsonify

from extensions import crypto
from . import controller
from . import session_blueprint


@session_blueprint.route('/patch', methods=['POST'])
def hello():
    payload = crypto.encrypt_auth_token(request.headers['auth'])
    email = payload['auth']
    return 'Session Blueprint Page. You entered!'


@session_blueprint.route('/create', methods=['POST'])
def _create_session():
    payload = crypto.decrypt_auth_token(request.headers['Authorization'])
    user_id = payload['userid']
    json = request.get_json()
    print('Received json: {}'.format(json))
    json.update(user_id=user_id)
    session = controller.create_session(**json)
    return jsonify(session)


@session_blueprint.route('/search', methods=['GET'])
def get_by_user():
    payload = crypto.decrypt_auth_token(request.headers['Authorization'])
    userid = payload['userid']
    result = controller.get_sessions_by_user_id(userid)
    return result
