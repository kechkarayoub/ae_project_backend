from backend.celery import app
from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.decorators import task
from datetime import timedelta
from backend.utils import send_email
from django.conf import settings
@app.task
def test___task():
    send_email("Test celery", "Celery work perfectly", settings.EMAIL_HOST_USER, "kechkarayoub@gmail.com")
    print('........................')