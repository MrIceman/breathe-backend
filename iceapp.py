from flask import Flask, g
from ice import Ice
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
boards = Ice(app)
boards.set_configs('configs.py')

# import all database models
from profile.model import User
from session.model import Session, SessionSet

boards.initialize_extensions()

# import all blueprints
from board import board_blueprint as board_bp

boards.initialize_blueprints(board_bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
