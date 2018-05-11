from flask import request, jsonify, json
from . import controller
from . import profile_blueprint


@profile_blueprint.route('/register', methods=['POST'])
def request_sign_up():
    if request.json is None:
        return jsonify({'Error': 'only JSON params allowed'})
    data = request.json
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
    data = json.loads(request.json)
    email = data['email']
    password = data['password']
    result = json.dumps((controller.sign_in(email, password)))
    print(result)
    return result
