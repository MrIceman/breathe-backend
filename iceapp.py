from flask import Flask
from ice import Ice
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
iceapp = Ice(app)
iceapp.set_configs('configs.py')
# import all database models
from profile.model import User
from session.model import Session, SessionSet

iceapp.initialize_extensions()
# import all blueprints
from profile import profile_blueprint as profile_bp
from session import session_blueprint as session_bp

iceapp.initialize_blueprints(profile_bp, session_bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
