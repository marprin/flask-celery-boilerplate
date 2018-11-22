from celery import shared_task
from flask import current_app
import settings
from celery.schedules import crontab
from celery_inst import celery


@celery.task
def add():
    current_app.logger.debug(dict(
        message="==== request add ===="
    ))
    add_more.delay(1, 9)
    return True


@shared_task()
def add_more(a, b):
    current_app.logger.debug(dict(
        message="=== in shared task ===="
    ))
    return a + b
