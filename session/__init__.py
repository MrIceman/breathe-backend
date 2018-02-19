from flask import Blueprint, request, jsonify, ctx
from util.error import ErrorCodes, ErrorMessages

session_blueprint = Blueprint('session', __name__, url_prefix='/session')


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
