from cryptography.fernet import Fernet
import jwt


class Crypt:

    def set_key(self, key):
        self.f = Fernet(key)
        self.secret = key

    def encrypt(self, hidden_msg):
        return self.f.encrypt(bytes(hidden_msg, 'UTF-8'))

    def decrypt(self, token):
        return self.f.decrypt(token).decode('utf-8')

    def get_auth_token(self, email):
        payload = {'email': email}
        token = jwt.encode(payload=payload, key=self.secret)
        return token

    def decrypt_auth_token(self, token):
        try:
            return jwt.decode(jwt=token, key=self.secret)
        except Exception:
            return 'Wrong Authentification!'
