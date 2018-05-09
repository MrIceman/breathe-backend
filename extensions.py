from database.DatabaseManager import DatabaseManager
from util.security.Crypt import Crypt

database_manager = DatabaseManager()
crypto = Crypt()


def set_up_database_manager(app):
    global database_manager
    database_manager.init_app(app)
    if app is not None:
        print('initialized a database manager')
    else:
        print('failed to init db manager')


def set_up_crypt(secret):
    crypto.set_key(secret)
