from flask import Flask
from apps.auth.views import auth
from settings import settings


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(settings)

    # Register blueprint here
    app.register_blueprint(auth)

    return app
