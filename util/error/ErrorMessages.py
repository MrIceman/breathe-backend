from .ErrorCodes import *


def _get_json_msg(text, code):
    return {'Error': {'message': text, 'code': code}}


def make_error_message(code):
    if code is AUTH_TOKEN_INVALID:
        return _get_json_msg('Authentication invalid', code)
    elif code is AUTH_TOKEN_MISSING:
        return _get_json_msg('Authentication missing', code)
    elif code is SIGN_UP_FAILED_EMAIL_EXISTS:
        return _get_json_msg('Sign Up failed. Email already exists', code)
    elif code is SIGN_UP_FAILED_USER_EXISTS:
        return _get_json_msg('Sign Up failed. User already exists', code)
    elif code is INVALID_INPUT:
        return _get_json_msg('Invalid User Input', code)
    else:
        return _get_json_msg('Unknown Error', -1)
