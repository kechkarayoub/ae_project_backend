from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.decorators import task
from datetime import timedelta

# @periodic_task(run_every=crontab(hour=7, minute=30, day_of_week="mon"))
@periodic_task(run_every=crontab(minute=14))
def test():
    print("gggggggggggggggggggggggggggggggg")
@task(name="multiply_two_numbers")
def test2():
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")