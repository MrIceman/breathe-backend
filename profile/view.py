from flask import request, stream_with_context, Response
from .controller import create_user, sign_in, decrypt_auth_token
from . import profile_blueprint


@profile_blueprint.route('/register', methods=['POST'])
def request_sign_up():
    data = {}
    for key, value in request.data.items():
        data[key] = str(value)

    print('Received data: {}'.format(data))
    result = create_user(**data)
    return result


@profile_blueprint.route('/test', methods=['GET'])
def test_():
    token = request.headers['auth']
    return '{}'.format(decrypt_auth_token(token))


@profile_blueprint.route('/sign_in', methods=['POST'])
def request_sign_in():
    """
    {
  "age": 0,
  "bio": "default",
  "country": "",
  "display_name": "now",
  "email": "mrtnnwsd@gmail.com",
  "id": 12,
  "location": "false",
  "password": "1"

  JWT:
  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im1ydG5ud3NkQGdtYWlsLmNvbSJ9.BxuYPD1Vpx2h3xC3k7E57slNmMob2HxiLwofv5jWXvw
}
    :return:
    """
    data = request.json
    email = data['email']
    password = data['password']
    return sign_in(email, password)
