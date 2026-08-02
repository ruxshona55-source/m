# myapp/tasks.py
from celery import shared_task
import time

# Oddiy task
@shared_task
def add(x, y):
    return x + y