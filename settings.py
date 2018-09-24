"""Settings file will be here, please do not
create another settings file, you better dynamicaly
update the value using environtment variable
"""

import os


class Config:
    TOKEN_EXPIRY = int(os.getenv('TOKEN_EXPIRY'))
    SECRET_KEY = os.getenv('SECRET_KEY')


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
            },
            "logentries": {
                "class": "logentries.LogentriesHandler",
                "level": "ERROR",
                "formatter": "json_formatter",
                "token": "AAAA"

            }
        },
        "loggers": {
            "flask.app": {
                "handlers": ['file_handler', 'wsgi']
            },
            "logentries": {
                "handlers": ['logentries']
            }
        },
        "root": {
            "level": "INFO",
            "handlers": ['wsgi']
        }
    }

settings = Config