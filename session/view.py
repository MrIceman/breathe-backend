from . import session_blueprint


@session_blueprint.route('/patch')
def hello():
    return 'Session Blueprint Page. You entered!'
