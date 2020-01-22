# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from django.conf import settings
# from celery.schedules import crontab
#
# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.base')
#
# app = Celery('backend')
#
# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings')
#
# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks(settings.INSTALLED_APPS)
#
# app.conf.beat_schedule = {
#     'add-every-minute-contrab': {
#         'task': 'multiply_two_numbers',
#         'schedule': crontab()
#     },
#     'add-every-5-seconds': {
#         'task': 'multiply_two_numbers',
#         'schedule': 5.0
#     },
#     'add-every-30-seconds': {
#         'task': 'multiply_two_numbers',
#         'schedule': 30.0
#     },
# }
#
# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))