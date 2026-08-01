import login
from celery import shared_task
from django.core.mail import send_mail


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

