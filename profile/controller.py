from extensions import database_manager, crypto
from .model import User
from flask import jsonify

DISPLAY_NAME_TAKEN = 1
SIGN_UP_OK = 2
SIGN_IN_OK = 3


def create_user(**kwargs):
    if 'password' in kwargs and 'email' in kwargs and 'display_name' in kwargs:
        status_check = validate_displayname(kwargs['email'], kwargs['display_name'])
        if status_check is SIGN_UP_OK:
            kwargs['password'] = crypto.encrypt(kwargs['password'])
            print('Encrypted password is: {}'.format(kwargs['password']))
            user = User(**kwargs)
            with database_manager.get_db(commit=True) as db:
                db.session.add(user)
            return user.to_json()
        elif status_check is DISPLAY_NAME_TAKEN:
            return jsonify({'error': 'username is already taken'})
    else:
        return jsonify({'error': 'invalid input'})


def validate_displayname(email, display_name):
    # validate user input
    with database_manager.get_db(commit=False) as db:
        print('Querying ' + display_name)
        user = db.session.query(User).filter(User.display_name.is_(display_name)).first()
        if user is not None:
            return DISPLAY_NAME_TAKEN
    return SIGN_UP_OK


def validate_sign_in(email, password):
    with database_manager.get_db(commit=False) as db:
        user = db.session.query(User).filter(User.email.is_(email)).first()
    if user is None:
        return {'error': 'No account for {}'.format(email)}
    if crypto.decrypt(user.password) is not password:
        return {'error': 'Wrong password for {}'.format(email)}
    return {'status': SIGN_IN_OK, 'data': user.id}


def sign_in(email, password):
    status_check = validate_sign_in(email, password)
    if SIGN_IN_OK not in status_check.values():
        return status_check
    return jsonify(crypto.get_auth_token(id=status_check['data']))


def decrypt_auth_token(token):
    return {'Payload': crypto.decrypt_auth_token(token)}


def update_user(**kwargs):
    # if ''
    pass
