from extensions import database_manager, crypto
from .model import User
from flask import jsonify
from util.error.ErrorMessages import make_error_message
from util.error.ErrorCodes import SIGN_UP_FAILED_USER_EXISTS, SIGN_UP_FAILED_EMAIL_EXISTS, INVALID_INPUT

DISPLAY_NAME_TAKEN = 1
EMAIL_TAKEN = 2
SIGN_UP_OK = 3
SIGN_IN_OK = 4


def create_user(**kwargs):
    if 'password' in kwargs and 'email' in kwargs and 'display_name' in kwargs:
        status_check = validate_credentials(kwargs['email'], kwargs['display_name'])
        if status_check is SIGN_UP_OK:
            kwargs['password'] = crypto.encrypt(kwargs['password'])
            user = User(**kwargs)
            with database_manager.get_db(commit=True) as db:
                db.session.add(user)
            token = crypto.get_auth_token(id=user.id)
            return {'token': str(token, 'UTF-8')}
        elif status_check is DISPLAY_NAME_TAKEN:
            return make_error_message(SIGN_UP_FAILED_USER_EXISTS)
        elif status_check is EMAIL_TAKEN:
            return make_error_message(SIGN_UP_FAILED_EMAIL_EXISTS)
    else:
        return make_error_message(INVALID_INPUT)


def validate_credentials(email, display_name):
    # checks if username already exists
    with database_manager.get_db(commit=False) as db:
        user = db.session.query(User).filter(User.display_name.is_(display_name)).first()
        if user is not None:
            return DISPLAY_NAME_TAKEN

    with database_manager.get_db(commit=False) as db:
        user = db.session.query(User).filter(User.email.is_(email)).first()
        if user is not None:
            return EMAIL_TAKEN

    return SIGN_UP_OK


def validate_sign_in(email, password):
    with database_manager.get_db(commit=False) as db:
        user = db.session.query(User).filter(User.email.is_(email)).first()
    if user is None:
        return {'error': 'No account for {}'.format(email)}
    if crypto.decrypt(user.password) != password:
        return {'error': 'Wrong password for {}'.format(email)}
    return {'status': SIGN_IN_OK, 'id': user.id}


def sign_in(email, password):
    status_check = validate_sign_in(email, password)
    if SIGN_IN_OK not in status_check.values():
        print('Failed to login')
        return status_check
    print('Login success. Encryption starting')
    token = crypto.get_auth_token(id=status_check['id'])
    return {'token': str(token, 'UTF-8')}


def decrypt_auth_token(token):
    return crypto.decrypt_auth_token(token)


def update_user(**kwargs):
    # if ''
    pass
