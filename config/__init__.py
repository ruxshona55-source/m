# config/__init__.py
# Django ishga tushganda Celery ham yuklansin

from .celery import app as celery_app

__all__ = ('celery_app',)