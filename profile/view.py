from flask import request, stream_with_context, Response, jsonify
from .controller import create_user, sign_in, decrypt_auth_token
from . import profile_blueprint


@profile_blueprint.route('/register', methods=['POST'])
def request_sign_up():
    if request.json is None:
        return jsonify({'Error': 'only JSON params allowed'})
    data = {}
    for key, value in request.json.items():
        data[key] = str(value)

    print('Received data: {}'.format(data))
    result = create_user(**data)
    return result


@profile_blueprint.route('/test', methods=['POST'])
def test_():
    token = request.headers['Authorization']
    return '{}'.format(decrypt_auth_token(token))


@profile_blueprint.route('/sign_in', methods=['POST'])
def request_sign_in():
    """
  "age": 0,
  "bio": "default",
  "country": "",
  "display_name": "marty",
  "email": "email@mine.com",
  "id": 13,
  "location": "false",
  "password": "123"

  JWT:
  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyaWQiOiJlbWFpbEBtaW5lLmNvbSJ9.L5K_hswkVXpuoV9fPpLjVO-ILzFdytdCJgBnPbhLvVE
}
    :return:
    """
    data = request.get_json()
    email = data['email']
    password = data['password']
    return sign_in(email, password)
