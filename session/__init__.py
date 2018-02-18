from flask import Blueprint, request, jsonify

session_blueprint = Blueprint('session', __name__, url_prefix='/session')


@session_blueprint.before_request
def validate_header():
    # todo User authentication here
    if 'Authentication' not in request.args:
        return jsonify({'Error': 'Missing Authentication!'})


from .view import *
