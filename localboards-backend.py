from flask import Flask, g
from boards import Boards

app = Flask(__name__)
boards = Boards(app)
boards.set_configs('configs.py')

# import all database models
from board.model import Board, Message, User

boards.initialize_extensions()

# import all blueprints
from board import board_blueprint as board_bp

boards.initialize_blueprints(board_bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
