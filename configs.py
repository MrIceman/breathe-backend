import os

basedir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "database.db")
DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///" + basedir
SECRET_KEY = 'secret!'
CRYPT_KEY = '6PZWMMmUaV-XF3D5fX3up-auaH9JnQND3xSI__f0iz8='
