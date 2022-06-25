# default import in Celery official tutorial; to prevent conflicts
from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

# set environment variable DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basic_project.settings")

# instantiate Celery with our project (basic_project)
app = Celery('basic_project')

# add django settings module as configuration source for celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto discover all tasks in our applications
app.autodiscover_tasks()