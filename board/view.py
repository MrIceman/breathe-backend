from flask import request

from . import board_blueprint as blueprint
from .controller import get_board_by_city, set_board_by_city, insert_message
from Exceptions import make_error_response


@blueprint.route('/get/city=<string:city>', methods=['GET', 'POST'])
def get_by_city(city):
    with_messages = False
    if 'with_messages' in request.args:
        with_messages = True

    try:
        return get_board_by_city(city, json=True, with_messages=with_messages)
    except Exception as e:
        print(e)
        return make_error_response(message='Error with loading {}'.format(city))


@blueprint.route('/set/city=<string:city>', methods=['GET', 'POST'])
def set_by_city(city):
    result = set_board_by_city(city, json=True)

    return result


@blueprint.route('/<string:board_location>/message/set/', methods=['GET'])
def set_message(board_location):
    try:
        result = insert_message(board_location, 'doom dee daa')
        return result
    except Exception as e:
        print('Exception {}'.format(e))
        return make_error_response(message='Error with creating a message at {}'.format(board_location))
