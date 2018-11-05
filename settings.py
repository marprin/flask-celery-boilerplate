"""Settings file will be here, please do not
create another settings file, you better dynamicaly
update the value using environtment variable
"""

import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
dotenv_file = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_file)

TOKEN_EXPIRY = int(os.getenv('TOKEN_EXPIRY'))
SECRET_KEY = os.getenv('SECRET_KEY')
REDIS_HOST = os.getenv('REDIS_HOST')

CELERY_BROKER_URL = 'redis://{}/0'.format(REDIS_HOST)
CELERY_RESULT_BACKEND = 'redis://{}/1'.format(REDIS_HOST)
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(process)s - %(name)s - %(levelname)s - %(message)s"
        },
        "json_formatter": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(process)d %(threadName)s "
                    "%(name)s %(levelname)s %(pathname)s %(lineno)s %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z"
        }
    },
    "handlers": {
        "wsgi": {
            "class": "logging.StreamHandler",
            "stream": "ext://flask.logging.wsgi_errors_stream",
            'formatter': 'default'
        },
        "file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "default",
            "filename": "logs/debug.log",
            "maxBytes": 10485760,
            "backupCount": 5,
            "encoding": "utf8"
        }
    },
    "loggers": {
        "flask.app": {
            "handlers": ['file_handler', 'wsgi']
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ['wsgi']
    }
}