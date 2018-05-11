from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    if app is None:
        print('No app initialized')
        raise Exception
        return  # todo catch an exception
    print('Database: initializing app')
    global db
    db.init_app(app)
    db.create_all(app=app)


def get_db():
    if db.get_app() is None:
        raise Exception('No Database initialized')
    return db
