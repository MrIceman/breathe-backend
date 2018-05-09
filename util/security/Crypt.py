import jwt
from cryptography.fernet import Fernet

from util.error.ErrorCodes import AUTH_TOKEN_INVALID
from util.error.ErrorMessages import make_error_message


class Crypt:
    """
    Class hashes input via FERNET or JWT.
    """

    def set_key(self, key):
        self.f = Fernet(key)
        self.secret = key

    def encrypt(self, hidden_msg):
        return self.f.encrypt(bytes(hidden_msg, 'UTF-8'))

    def decrypt(self, token):
        return self.f.decrypt(token).decode('UTF-8')

    def encrypt_auth_token(self, id):
        payload = {'userid': id}
        token = jwt.encode(payload=payload, key=self.secret)
        return token

    def decrypt_auth_token(self, token):
        try:
            return jwt.decode(jwt=token, key=self.secret)
        except Exception:
            return make_error_message(AUTH_TOKEN_INVALID)
