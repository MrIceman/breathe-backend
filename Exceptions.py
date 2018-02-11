from flask import jsonify


def make_error_response(message):
    return jsonify({'error': message})
