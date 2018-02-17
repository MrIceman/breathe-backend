from flask import Blueprint

board_blueprint = Blueprint('board', __name__, url_prefix='/board')

from .view import *
