from database.DatabaseManager import DatabaseManager
from util.security.Crypt import Crypt

database_manager = DatabaseManager()
crypto = Crypt('')


def set_up_database_manager(app):
    global database_manager
    database_manager.init_app(app)
    print('Setting database_manager!')
    if app is None:
        print('App is none')
    else:
        print('App is not none')


def set_up_crypt_tool(key):
    crypto.set_key(key)
