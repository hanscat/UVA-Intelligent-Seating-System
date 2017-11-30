from __future__ import absolute_import, unicode_literals
from celery import shared_task, Celery
import time

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@shared_task
def receive(x, y):
    while(1):
        print("!!!!!!!!!!!!!!!!!!!!")
        time.sleep(3)
    return x + y
