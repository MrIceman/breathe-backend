from flask import Blueprint, jsonify

from extensions import database_manager
from session.controller import SessionController
from util.error import ErrorCodes, ErrorMessages
from util.parsing.ArrayParser import ArrayParser

session_blueprint = Blueprint('session', __name__, url_prefix='/session')
controller = SessionController(database_manager=database_manager, array_parser=ArrayParser())


@session_blueprint.before_request
def validate_header():
    if 'Authorization' not in request.headers.keys():
        return ErrorMessages.make_error_message(ErrorCodes.AUTH_TOKEN_MISSING)
    else:
        from extensions import crypto
        token = crypto.decrypt_auth_token(request.headers['Authorization'])
        print('Received token {}'.format(token))
        if 'Error' in token:
            return jsonify(token)


from .view import *
