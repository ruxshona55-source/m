import login
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
import logging

@shared_task
def send_email_task(email, subject):
    send_mail(
        subject='welcome',
        message='Welcome to task manager',
        from_email="mohigulmarifova03@gmail.com",
        recipient_list=[email],
        fail_silently=True,
    )
login.basicConfig()




# your_app/tasks.py


logger = logging.getLogger(__name__)

@shared_task
def check_status():
    logger.info(f"✅ OK — {timezone.now()}")
    return "ok"

@shared_task
def send_daily_report():
    logger.info("📊 Hisobot yuborilmoqda...")
    return "report sent"
