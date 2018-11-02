from flask import Flask
from werkzeug.contrib.cache import RedisCache
from apps.auth.views import auth
import settings


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(settings)

    app.cache = RedisCache(settings.REDIS_HOST)

    # Register blueprint here
    app.register_blueprint(auth)

    return app
