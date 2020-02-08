from backend.celery import app
from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.decorators import task
from datetime import timedelta

@app.task
def test___task():
    print('........................')