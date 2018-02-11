from extensions import database_manager as db_manager
from board.model import Board, Message


def get_board_by_city(city, json=False, raw=False, **kwargs):
    with db_manager.get_db(commit=True) as db:
        board = db.session.query(Board).filter(Board.location.is_(city)).first()
        if board is None:
            raise Exception

    if 'with_messages' in kwargs:
        with_msg = kwargs['with_messages']

    if json:
        result = board.to_json(with_msg)
    elif raw:
        result = board
    elif json is False:
        result = board.to_dict(with_msg)

    return result


def set_board_by_city(city, json=False):
    with db_manager.get_db(commit=True) as db:
        board = Board(city)
        db.session.add(Board(city))

    return board.to_json()


def insert_message(board_name, content):
    with db_manager.get_db(commit=True) as db:
        board = db.session.query(Board).filter(Board.location.is_(board_name)).first()
        if board is None:
            print('raising an exception!')
            raise Exception
        msg = Message(content, board.id)
        db.session.add(msg)
    return msg.to_json()
