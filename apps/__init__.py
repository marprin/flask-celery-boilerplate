from flask import Flask
from apps.auth.views import auth


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    if config is None:
        app.config.from_pyfile('settings.py', silent=True)
    else:
        app.config.from_mapping(config)

    # Register blueprint here
    app.register_blueprint(auth)

    return app
