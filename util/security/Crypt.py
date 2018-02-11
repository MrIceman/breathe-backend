from cryptography.fernet import Fernet


class Crypt:

    def set_key(self, key):
        self.f = Fernet(key)

    def encrypt(self, hidden_msg):
        return self.f.encrypt(hidden_msg)

    def decrypt(self, token):
        return self.f.decrypt(token).decode('utf-8')
