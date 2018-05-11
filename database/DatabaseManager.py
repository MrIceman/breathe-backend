from .Database import get_db


class DatabaseManager:

    def __init__(self, **kwargs):
        self.commit = kwargs.pop('commit', True)

    def __enter__(self):
        self.db = get_db()
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.commit:
            self.db.session.commit()
