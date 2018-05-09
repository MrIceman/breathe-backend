from util.error.ErrorCodes import SIGN_UP_FAILED_USER_EXISTS, SIGN_UP_FAILED_EMAIL_EXISTS, INVALID_INPUT
from util.error.ErrorMessages import make_error_message
from .model import User

DISPLAY_NAME_TAKEN = 1
EMAIL_TAKEN = 2
SIGN_UP_OK = 3
SIGN_IN_OK = 4

"""
Every Controller has access to its model but is not allowed to speak to the View.
All dependencies are passed via Constructor

TODO: Testing
"""


class ProfileController:
    def __init__(self, **kwargs):
        self.database_manager = kwargs['database_manager']
        self.crypto = kwargs['crypto']

    def create_user(self, **kwargs):
        if 'password' in kwargs and 'email' in kwargs and 'display_name' in kwargs:
            status_check = self.validate_credentials(kwargs['email'], kwargs['display_name'])
            if status_check is SIGN_UP_OK:
                kwargs['password'] = self.crypto.encrypt(kwargs['password'])
                user = User(**kwargs)
                with self.database_manager.get_db(commit=True) as db:
                    db.session.add(user)
                token = self.crypto.encrypt_auth_token(id=user.id)
                return {'token': str(token, 'UTF-8')}
            elif status_check is DISPLAY_NAME_TAKEN:
                return make_error_message(SIGN_UP_FAILED_USER_EXISTS)
            elif status_check is EMAIL_TAKEN:
                return make_error_message(SIGN_UP_FAILED_EMAIL_EXISTS)
        else:
            return make_error_message(INVALID_INPUT)

    def validate_credentials(self, email, display_name):
        # checks if username already exists
        with self.database_manager.get_db(commit=False) as db:
            user = db.session.query(User).filter(User.display_name.is_(display_name)).first()
            if user is not None:
                return DISPLAY_NAME_TAKEN
            user = db.session.query(User).filter(User.email.is_(email)).first()
            if user is not None:
                return EMAIL_TAKEN

        return SIGN_UP_OK

    def validate_sign_in(self, email, password):
        with self.database_manager.get_db(commit=False) as db:
            user = db.session.query(User).filter(User.email.is_(email)).first()
        if user is None:
            return {'error': 'No account for {}'.format(email)}
        if self.crypto.decrypt(user.password) != password:
            return {'error': 'Wrong password for {}'.format(email)}
        return {'status': SIGN_IN_OK, 'id': user.id}

    def sign_in(self, email, password):
        status_check = self.validate_sign_in(email, password)
        if SIGN_IN_OK not in status_check.values():
            return status_check
        token = self.crypto.encrypt_auth_token(id=status_check['id'])
        return {'token': str(token, 'UTF-8')}

    def decrypt_auth_token(self, token):
        return self.crypto.decrypt_auth_token(token)

    def update_user(self, **kwargs):
        # if ''
        pass
