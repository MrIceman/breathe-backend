from .ErrorCodes import *
from flask import jsonify


def _get_json_msg(text):
    return jsonify({'Error': text})


def make_error_message(code):
    if code is AUTH_TOKEN_INVALID:
        return _get_json_msg('Authentication invalid')
    elif code is AUTH_TOKEN_MISSING:
        return _get_json_msg('Authentication missing')
