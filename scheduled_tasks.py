from celery import shared_task
from flask import current_app
import settings
from celery.schedules import crontab
from celery_inst import celery


@celery.task
def add_2():
    current_app.logger.debug(dict(
        message="==== request add 2 ===="
    ))
    add_more_2.delay(1, 9)
    return True


@shared_task()
def add_more_2(a, b):
    current_app.logger.debug(dict(
        message="=== in shared task 2 ===="
    ))
    return a + b
