# define tasks that you want celery to run

# default import as in official tutorial to prevent conflicts
from __future__ import absolute_import, unicode_literals

# import shared_task decorator
from celery import shared_task

# basic task to add 2 numbers
# assumption: x, y => numbers
@shared_task
def add(x, y):
    return x + y