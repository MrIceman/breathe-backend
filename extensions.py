from database.Database import init_db
from database.DatabaseManager import DatabaseManager
from util.security.Crypt import Crypt

database_manager = DatabaseManager
crypto = Crypt()


def set_up_database(app):
    init_db(app)


def set_up_crypt(secret):
    crypto.set_key(secret)
