import json

from flask import request, jsonify

from profile.model import User
from . import controller
from . import profile_blueprint


@profile_blueprint.route('/register', methods=['POST'])
def request_sign_up():
    if request.json is None:
        return jsonify({'Error': 'only JSON params allowed'})
    data = json.loads(request.json)
    print('received data: {}'.format(data))
    result = json.dumps(controller.create_user(**data))
    print(result)
    return result


@profile_blueprint.route('/test', methods=['POST'])
def test_():
    token = request.headers['Authorization']
    return '{}'.format(controller.decrypt_auth_token(token))


@profile_blueprint.route('/sign_in', methods=['POST'])
def request_sign_in():
    print('Received Request: {}'.format(request.headers))
    data = json.loads(request.json)
    print('Received {}'.format(data))
    email = data['email']
    password = data['password']
    result = json.dumps((controller.sign_in(email, password)))
    print(result)
    return result


@profile_blueprint.route('/show_by_token=<token>', methods=['GET'])
def show_user(token):
    user_id = controller.decrypt_auth_token(token)['userid']
    print('Looking Up user: {}'.format(user_id))
    user = User.query.filter(User.id.is_(user_id)).first()
    return user.to_json()
