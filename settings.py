"""Settings file will be here, please do not
create another settings file, you better dynamicaly
update the value using environtment variable
"""

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

APP_KEY = os.getenv('APP_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

TOKEN_EXPIRY = int(os.getenv('TOKEN_EXPIRY'))
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

TIMEZONE = 'UTC'

CELERY_BROKER_URL = 'redis://{}:{}/0'.format(REDIS_HOST, REDIS_PORT)
CELERY_RESULT_BACKEND = 'redis://{}:{}/1'.format(REDIS_HOST, REDIS_PORT)
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True

from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {
    'add': {
        'task': 'tasks.add',
        'schedule': crontab(hour='*/1', minute=28)
    },
    'add-2': {
        'task': 'scheduled_tasks.add_2',
        'schedule': crontab(hour='*/1', minute=28)
    }
}


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
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'ERROR',
            'formatter': 'json_formatter',
            'stream': 'ext://sys.stdout'
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
            'level': 'DEBUG',
            'propagate': False,
            "handlers": ['file_handler', 'wsgi', 'console']
        }
    },
    "root": {
        "level": "ERROR",
        "handlers": ['wsgi', 'console'],
        'propagate': False,
    }
}