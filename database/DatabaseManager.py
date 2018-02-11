from contextlib import contextmanager

from .Database import init_db, get_db


class DatabaseManager:

    def __init__(self, app=None):
        if app is not None:
            init_db(app)

    def init_app(self, app):
        init_db(app)

    @contextmanager
    def get_db(self, **kwargs):
        db = get_db()
        yield db
        if 'commit' in kwargs:
            db.session.commit()
        elif 'flush' in kwargs:
            db.session.flush()
        print('Added something. Done here')
