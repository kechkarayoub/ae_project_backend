from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.decorators import task
from datetime import timedelta

@shared_task
def test_task():
    print('........................')