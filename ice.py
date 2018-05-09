from extensions import set_up_database_manager, set_up_crypt


class Ice:

    def __init__(self, app):
        self.app = app
        self.db_manager = None

    def set_configs(self, config_path):
        self.app.config.from_pyfile(config_path)

    def initialize_extensions(self):
        with self.app.app_context():
            set_up_database_manager(self.app)

        set_up_crypt(self.app.config['CRYPT_KEY'])

    def initialize_blueprints(self, *args):
        for bp in args:
            self.app.register_blueprint(bp)
